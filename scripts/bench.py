#!/usr/bin/env python3
"""Kingdom-analysis benchmark tooling.

  bench.py check [CASE...]          validate case.json files and card names
  bench.py render CASE              print the blind kingdom brief for a case
  bench.py list                     one line per case
  bench.py sandbox [--agents PATH] [--rev REV] DIR CASE...
                                    build a blind workspace: dominion-agents'
                                    context, skills and data (working tree, or
                                    REV via git archive), plus
                                    kingdoms/<case>.md briefs

Card text comes from dominion-engine (DOMINION_ENGINE, default
~/projects/dominion-engine). dominion-agents defaults to DOMINION_AGENTS or
~/projects/dominion-agents.
"""
import glob
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "cases"
AGENTS = Path(os.environ.get("DOMINION_AGENTS", Path.home() / "projects/dominion-agents"))
AGENT_FILES = ("AGENTS.md", "context", "skills", "data")
ENGINE = Path(os.environ.get("DOMINION_ENGINE", Path.home() / "projects/dominion-engine"))

SOURCE_TYPES = {"designed-tournament", "blog-analysis", "annotated-game", "reddit-kotw",
                "commentated-match", "podcast", "forum"}
QUALITY = {"A", "B", "C"}
BASIC = {"Copper", "Silver", "Gold", "Estate", "Duchy", "Province", "Curse"}


def load_cards():
    by_name, by_pile = {}, {}
    files = sorted(glob.glob(str(ENGINE / "data/cards/*.json")))
    if not files:
        return None, None
    for f in files:
        for c in json.load(open(f)):
            by_name.setdefault(c["name"].lower(), c)
            if c.get("pile"):
                by_pile.setdefault(c["pile"].lower(), []).append(c)
    return by_name, by_pile


def resolve(name, by_name, by_pile):
    """Cards for a pile spec such as 'Smithy', 'Catapult/Rocks', 'Castles', 'Augurs'."""
    key = name.lower()
    head = key.split("/")[0].strip()
    for k in (key, head):
        if k in by_pile:
            # Split piles list only the lower half under the pile name; the top
            # card carries the pile's name itself.
            top = [by_name[k]] if k in by_name else []
            return top + [c for c in by_pile[k] if c not in top]
    if key in by_name:
        return [by_name[key]]
    if "/" in key:
        parts = [by_name.get(p.strip()) for p in key.split("/")]
        if all(parts):
            return parts
    return None


def cost(c):
    k = c.get("cost") or {}
    parts = []
    if "coins" in k:
        parts.append(f"${k['coins']}")
    if k.get("potions"):
        parts.append("Potion")
    if k.get("debt"):
        parts.append(f"{k['debt']}D")
    return "+".join(parts) or "-"


def card_md(c):
    text = c.get("text", "").strip()
    if not text:
        # Basic cards such as Platinum, Colony and Potion have no text in the data.
        parts = []
        if c.get("coins"):
            parts.append(f"${c['coins']}")
        if c.get("potions"):
            parts.append("+1 Potion")
        if c.get("vp"):
            parts.append(f"{c['vp']} VP")
        text = ", ".join(parts)
    return f"## {c['name']} ({cost(c)}) [{' - '.join(c['types'])}]\n{text}\n"


def case_dirs(ids):
    if ids:
        return [CASES / i for i in ids]
    return sorted(p for p in CASES.iterdir() if p.is_dir())


def kingdom_names(k):
    names = list(k.get("cards", [])) + list(k.get("landscapes", []))
    names += list(k.get("traits", {}).keys())
    if k.get("bane"):
        names.append(k["bane"])
    names += list(k.get("extra_cards", []))
    return names


GROUP_TYPES = {"Ruins": "Ruins", "Loot": "Loot", "Boon": "Boon", "Hex": "Hex",
               "Reward": "Reward", "Prize": "Prize", "Fate": "Boon", "Doom": "Hex"}


def related(cards, by_name, seen):
    """Non-Supply cards the given cards bring in: named ones (Heirlooms, Spoils,
    Horse...) and whole groups (Ruins, Loot, Boons, Hexes, Rewards, Prizes),
    followed transitively (Hexes name States)."""
    out = []
    skip = {"Event", "Randomizer", "Trait", "Way", "Landmark", "Project", "Ally", "Prophecy"}
    pool = [c for c in by_name.values() if not c.get("kingdom") and c["name"] not in BASIC
            and not skip.intersection(c["types"])]
    todo = list(cards)
    while todo:
        text = "\n".join(c.get("text", "") for c in todo)
        types = {t for c in todo for t in c["types"]}
        groups = {g for word, g in GROUP_TYPES.items()
                  if word in types or re.search(r"\b" + word + r"(s|es)?\b", text)}
        todo = []
        for c in pool:
            if c["name"] in seen:
                continue
            named = re.search(r"\b" + re.escape(c["name"]) + r"s?\b", text)
            if named or groups.intersection(c["types"]):
                out.append(c)
                todo.append(c)
                seen.add(c["name"])
    return out


def render(case_dir, by_name, by_pile):
    meta = json.load(open(case_dir / "case.json"))
    k = meta["kingdom"]
    lines = ["# Kingdom", ""]
    lines.append("Kingdom piles: " + ", ".join(k["cards"]))
    if k.get("bane"):
        lines.append(f"Young Witch Bane pile: {k['bane']}")
    if k.get("landscapes"):
        lines.append("Landscapes: " + ", ".join(k["landscapes"]))
    for trait, pile in k.get("traits", {}).items():
        lines.append(f"Trait: {trait} on the {pile} pile")
    yn = {True: "yes", False: "no", None: "unknown"}
    lines.append(f"Colonies/Platinum: {yn[k.get('colonies')]}. Shelters: {yn[k.get('shelters')]}.")
    lines.append(f"Players: {k.get('players', 2)}.")
    if k.get("setup_notes"):
        lines.append(k["setup_notes"])
    lines += ["", "# Card text", ""]
    shown, seen = [], set()
    for n in kingdom_names(k):
        cs = resolve(n, by_name, by_pile) if by_name else None
        if not cs:
            lines.append(f"## {n}\n(text not available)\n")
            continue
        for c in cs:
            if c["name"] not in seen:
                seen.add(c["name"])
                shown.append(c)
                lines.append(card_md(c))
    extras = []
    if k.get("colonies"):
        extras += ["Platinum", "Colony"]
    if k.get("shelters"):
        extras += ["Hovel", "Necropolis", "Overgrown Estate"]
    if any(c.get("cost", {}).get("potions") for c in shown):
        extras.append("Potion")
    extra_cards = [by_name[e.lower()] for e in extras if by_name and e.lower() in by_name and e not in seen]
    seen.update(c["name"] for c in extra_cards)
    extra_cards += related(shown, by_name, seen) if by_name else []
    if extra_cards:
        lines += ["# Related cards outside the Kingdom", ""]
        lines += [card_md(c) for c in extra_cards]
    return "\n".join(lines).rstrip() + "\n"


def check(ids):
    by_name, by_pile = load_cards()
    if by_name is None:
        print(f"warning: no card data under {ENGINE}; skipping card-name checks", file=sys.stderr)
    fail = 0

    def err(case, msg):
        nonlocal fail
        print(f"error: {case}: {msg}", file=sys.stderr)
        fail = 1

    for d in case_dirs(ids):
        cid = d.name
        try:
            meta = json.load(open(d / "case.json"))
        except Exception as e:
            err(cid, f"case.json: {e}")
            continue
        if meta.get("id") != cid:
            err(cid, "id must equal the directory name")
        for f in ("title", "source_type", "date", "sources", "quality", "kingdom"):
            if f not in meta:
                err(cid, f"missing {f}")
        if meta.get("source_type") not in SOURCE_TYPES:
            err(cid, f"source_type must be one of {sorted(SOURCE_TYPES)}")
        if meta.get("quality") not in QUALITY:
            err(cid, "quality must be A, B or C")
        if not re.fullmatch(r"\d{4}(-\d{2}(-\d{2})?)?", str(meta.get("date", ""))):
            err(cid, "date must be YYYY, YYYY-MM or YYYY-MM-DD")
        if not meta.get("sources") or not all(s.get("url") for s in meta.get("sources", [])):
            err(cid, "sources must be a non-empty list with urls")
        k = meta.get("kingdom", {})
        if not k.get("cards"):
            err(cid, "kingdom.cards is empty")
        elif len(k["cards"]) != 10 and not k.get("card_count_note"):
            err(cid, f"{len(k['cards'])} kingdom piles; add kingdom.card_count_note to explain")
        for f in ("colonies", "shelters"):
            if k.get(f) not in (True, False, None):
                err(cid, f"kingdom.{f} must be true, false or null")
        if by_name:
            for n in kingdom_names(k):
                if not resolve(n, by_name, by_pile):
                    err(cid, f"unknown card or pile '{n}'")
        key = d / "key.md"
        if not key.exists():
            err(cid, "key.md missing")
        else:
            body = key.read_text()
            if not re.search(r"^- \*\*R\d+\*\*", body, re.M):
                err(cid, "key.md has no rubric items (- **R1** ...)")
            for h in ("## Sources", "## Expert summary", "## Rubric"):
                if h not in body:
                    err(cid, f"key.md missing section '{h}'")
    return fail


def sandbox(dest, ids, agents=AGENTS, rev=None):
    dest = Path(dest)
    if dest.exists() and any(dest.iterdir()):
        sys.exit(f"{dest} exists and is not empty")
    dest.mkdir(parents=True, exist_ok=True)
    agents = Path(agents)
    if rev:
        present = [n for n in AGENT_FILES if subprocess.run(
            ["git", "-C", agents, "cat-file", "-e", f"{rev}:{n}"], capture_output=True).returncode == 0]
        archive = subprocess.run(["git", "-C", agents, "archive", rev, *present],
                                 check=True, capture_output=True).stdout
        subprocess.run(["tar", "-x", "-C", dest], input=archive, check=True)
    else:
        for name in AGENT_FILES:
            src = agents / name
            if src.is_dir():
                shutil.copytree(src, dest / name)
            elif src.exists():
                shutil.copy(src, dest / name)
    if not (dest / "AGENTS.md").exists():
        sys.exit(f"no AGENTS.md copied from {agents}" + (f" at {rev}" if rev else ""))
    os.symlink("AGENTS.md", dest / "CLAUDE.md")
    for link in (".claude", ".agents"):
        (dest / link).mkdir()
        os.symlink("../skills", dest / link / "skills")
    by_name, by_pile = load_cards()
    (dest / "kingdoms").mkdir()
    for d in case_dirs(ids):
        (dest / "kingdoms" / f"{d.name}.md").write_text(render(d, by_name, by_pile))
    print(dest)


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    cmd, rest = args[0], args[1:]
    if cmd == "check":
        sys.exit(check(rest))
    if cmd == "render" and len(rest) == 1:
        by_name, by_pile = load_cards()
        sys.stdout.write(render(CASES / rest[0], by_name, by_pile))
        return
    if cmd == "list":
        for d in case_dirs([]):
            m = json.load(open(d / "case.json"))
            print(f"{d.name}\t{m['quality']}\t{m['date']}\t{m['title']}")
        return
    if cmd == "sandbox":
        opts = {}
        while rest and rest[0] in ("--agents", "--rev") and len(rest) > 1:
            opts[rest[0][2:]] = rest[1]
            rest = rest[2:]
        if len(rest) >= 2:
            sandbox(rest[0], rest[1:], **opts)
            return
    sys.exit(__doc__)


if __name__ == "__main__":
    main()
