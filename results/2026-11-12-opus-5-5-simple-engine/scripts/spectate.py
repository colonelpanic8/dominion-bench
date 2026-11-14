"""spectate.py URL GAME_JSON ROLES_JSON OUT.md: follow a game through both seats' views and write a replay."""
import json, sys, time
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from mcp import call

url, game_file, roles, out = sys.argv[1], sys.argv[2], json.loads(sys.argv[3]), sys.argv[4]
game = json.load(open(game_file))
seats = sorted(game["seats"], key=lambda s: s["seat"])
names = [s["name"] for s in seats]
label = {n: f"{n} ({roles[n]})" for n in names}
entries = {}   # seq -> (seat that saw it, entry)
hands = {}     # (turn, player) -> (hand, score line)
result = None

def view(tok):
    r = call(url, "view", {"token": tok, "format": "json"})
    return r.get("structuredContent") or json.loads(r["content"][0]["text"])

def cards(z):
    k = (z or {}).get("known", {})
    return ", ".join(f"{n} {c}" if n > 1 else c for c, n in sorted(k.items(), key=lambda x: x[0])) or "nothing"
    
def write():
    lines = [f"# Replay: game {game['game_id']}", "",
             f"Seat 1: {label[names[0]]}. Seat 2: {label[names[1]]}.", ""]
    turn_of = {}
    for seq in sorted(entries):
        seat, e = entries[seq]
        t = e["text"]
        if " starts turn " in t:
            who, n = t.split(" starts turn ")
            key = (int(n.split()[0]), who)
            lines += ["", f"## Turn {n.split()[0]}: {label.get(who, who)}"]
            if key in hands:
                h, score = hands[key]
                lines += [f"*{score}*", "", f"Hand: {h}", ""]
            continue
        lines.append(f"- {t}")
    if result:
        lines += ["", "## Result", ""] + [f"{p['rank']}. {label.get(p['name'], p['name'])}: {p['vp']} VP, {p['turns']} turns" for p in sorted(result['players'], key=lambda p: p['rank'])] + [f"", f"Ended: {result.get('reason')}"]
    open(out, "w").write("\n".join(lines) + "\n")

while True:
    try:
        for i, s in enumerate(seats):
            v = view(s["token"])
            for e in v.get("sinceLastDecision", []):
                seq = e["seq"]
                # Prefer the acting seat's own entry: it names its own cards.
                if seq not in entries or e.get("player") == i:
                    entries[seq] = (i, e)
            t = v.get("turn", {})
            if t.get("yourTurn") and not (v["you"].get("inPlay") or {}).get("known") and not t.get("coins"):
                key = (t.get("number"), names[i])
                if key not in hands:
                    you, opp = v["you"], v["opponents"][0]
                    hands[key] = (cards(you["hand"]), f"Score {names[i]} {you.get('vp')} – {opp['name']} {opp.get('vp')}")
            if not v["game"]["running"]:
                result = v["game"].get("result")
        write()
        if result:
            break
    except Exception as ex:
        print("poll error:", ex, file=sys.stderr)
    time.sleep(0.7)
print("replay done", out)
