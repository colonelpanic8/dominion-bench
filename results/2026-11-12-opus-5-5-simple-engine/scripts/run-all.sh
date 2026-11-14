#!/usr/bin/env bash
# run-all.sh M: both games, each with a spectator and two players.
M="$1"; url="http://127.0.0.1:$(cat "$M/port")/mcp"
for game in guided target; do
  case $game in guided) second="Opus 5.5, dominion-agents eb8da29";; target) second="Opus 5.5, dominion-agents eb8da29, target deck given";; esac
  name=$(jq -r '.seats[1].name' "$M/$game.json")
  python3 -I "$M/scripts/spectate.py" "$url" "$M/$game.json" "{\"Opus\":\"Opus 5.5, no guidance\",\"$name\":\"$second\"}" "$M/replay/$game.md" 2> "$M/replay/$game.err" &
  "$M/scripts/player.sh" "$M" "$game" plain 0 &
  "$M/scripts/player.sh" "$M" "$game" "$game" 1 &
done
wait
echo ALL DONE
