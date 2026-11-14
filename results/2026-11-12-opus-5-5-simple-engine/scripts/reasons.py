"""reasons.py REPLAY.md OUT.md NAME=SESSION.jsonl...: add each player's stated reason under every gain.

Players are asked to write `REASON T<turn> <card>: <why>` before a buy or
gain, and `REASON T<turn> nothing: <why>` when they pass a buy. Where a
player wrote no such line, the reason is what it wrote or thought just
before the answer that made the gain, and is marked as such.
"""
import json, re, sys
from collections import defaultdict

replay, out = sys.argv[1], sys.argv[2]
pat = re.compile(r"REASON\s+T(\d+)\s+([^:\n]+?):\s*(.+)")
clean = lambda s: re.sub(r"\s+", " ", s).strip(" `*")


def load(name, path):
    """Returns (pass reasons by turn, one (card, source, reason) per gain in game order)."""
    passed = defaultdict(list)
    gains = {}                   # seq -> (card, source, reason)
    stated, notes, turn = [], [], None
    for line in open(path, errors="replace"):
        try:
            o = json.loads(line)
        except ValueError:
            continue
        content = o.get("message", {}).get("content", [])
        if not isinstance(content, list):
            continue
        for b in content:
            kind = b.get("type")
            if o.get("type") == "assistant" and kind in ("text", "thinking"):
                text = b.get(kind) or ""
                for m in pat.finditer(text):
                    card = clean(m.group(2)).lower()
                    if card.startswith("nothing"):
                        passed[int(m.group(1))].append(clean(m.group(3)))
                    else:
                        stated.append((card, clean(m.group(3))))
                rest = clean(pat.sub("", text))
                if rest:
                    notes.append(("reply" if kind == "text" else "thinking", rest))
            elif kind == "tool_result":
                c = b.get("content")
                if isinstance(c, list):
                    c = "".join(x.get("text", "") for x in c if isinstance(x, dict))
                try:
                    view = json.loads(c)
                except (TypeError, ValueError):
                    continue
                if not isinstance(view, dict):
                    continue
                for e in view.get("sinceLastDecision") or []:
                    if e.get("type") != "gained" or not e.get("text", "").startswith(name + " ") or e["seq"] in gains:
                        continue
                    card = e.get("card", "")
                    hit = next((r for r in stated if r[0] == card.lower()), None)
                    if hit:
                        stated.remove(hit)
                        gains[e["seq"]] = (card, "stated", hit[1])
                        continue
                    near = [n for n in notes if card.lower() in n[1].lower()]
                    gains[e["seq"]] = (card, *near[-1]) if near else (card, None, None)
                t = view.get("turn") or {}
                now = (t.get("number"), t.get("yourTurn"))
                if now != turn:
                    turn = now
                    if t.get("yourTurn"):
                        stated, notes = [], []
    return passed, [gains[s] for s in sorted(gains)]


players = {}
for arg in sys.argv[3:]:
    name, path = arg.split("=", 1)
    players[name] = load(name, path)

lines, turn, who = [], None, None
count = defaultdict(int)
nth = defaultdict(int)


def passes():
    if who in players:
        for r in players[who][0].pop(turn, []):
            lines.append(f"- {who} passes a buy")
            lines.append(f"  - Reason: {r}")


for line in open(replay).read().splitlines():
    m = re.match(r"## Turn (\d+): (\S+)", line)
    if m or line.startswith("## Result"):
        passes()
        if lines and lines[-1] != "":
            lines.append("")
        turn, who = (int(m.group(1)), m.group(2)) if m else (None, None)
    lines.append(line)
    g = re.match(r"- (\S+) gains (?:an? )?(.+)$", line)
    if g and g.group(1) in players:
        name, card = g.group(1), g.group(2).strip()
        seen = players[name][1]
        k = nth[name]
        nth[name] += 1
        got = seen[k] if k < len(seen) and seen[k][0] == card else (card, None, None)
        _, src, text = got
        if src is None:
            count["none"] += 1
            lines.append("  - Reason: none given")
            continue
        count[src] += 1
        if len(text) > 600:
            text = text[:600].rsplit(" ", 1)[0] + " …"
        label = "Reason" if src == "stated" else f"Reason (from the player's {src} before the move)"
        lines.append(f"  - {label}: {text}")
open(out, "w").write("\n".join(lines) + "\n")
print(dict(count))
