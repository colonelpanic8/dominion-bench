#!/usr/bin/env bash
# player.sh M GAME ROLE SEAT: play one seat of $M/$GAME.json to the end.
# ROLE: plain (no guidance), guided (dominion-agents), target (dominion-agents + a given target deck).
set -u
M="$1"; game="$2"; role="$3"; seat="$4"
url="http://127.0.0.1:$(cat "$M/port")/mcp"
g=$(jq -r .game_id "$M/$game.json")
token=$(jq -r --argjson s "$seat" '.seats[]|select(.seat==$s)|.token' "$M/$game.json")
dir="$M/sb/$game-$role"; out="$M/out/$game-$role"; mkdir -p "$out"
cd "$dir" || exit 1
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1
cat > "$out/mcp.json" <<JSON
{"mcpServers": {"dominion": {"type": "http", "url": "$url"}}}
JSON
mcp="mcp__dominion__join_game mcp__dominion__view mcp__dominion__wait_for_decision mcp__dominion__answer mcp__dominion__card"
tools="Read,Glob,Grep,Write,Edit"; allowed=(Read Glob Grep)
if [ "$role" != plain ]; then tools="$tools,Skill"; allowed+=(Skill); fi
common=(--model claude-opus-5-5 --effort high --tools "$tools"
  --mcp-config "$out/mcp.json" --strict-mcp-config --no-chrome
  --allowedTools "${allowed[@]}" "Write(./notes.md)" "Edit(./notes.md)" $mcp
  --disallowedTools "mcp__dominion__create_game" "mcp__dominion__list_games"
  --setting-sources project --output-format stream-json --verbose)

head="You are playing a 2-player game of Dominion against another player, on the \`dominion\` MCP server. Your seat is P$((seat + 1)) of game $g; your seat token is $token. Play to win."
loop="Call join_game with game_id \"$g\" and your token. Then loop until the game is over: call wait_for_decision with timeout_ms 600000. When you have a decision, answer it with \`answer\` (the decision's id and the indices of the options you choose). A wait that returns with no decision means the opponent is still thinking: wait again."
reason="For the game log: before each answer that buys or gains a card, including a gain from a card such as Workshop, write one line, \`REASON T<turn> <card>: <why this card, now>\`, in a sentence or two. Write it as text in your reply, not only in your thinking: the log is built from reply text. When you end a turn with a buy unused, write \`REASON T<turn> nothing: <why>\`."
if [ "$role" != plain ]; then
  reason="For the game log: play-turn has you write a check before every buy or gain. Still write that check in full. After it, and before the answer, add one line that sums it up: \`REASON T<turn> <card>: <why this card, now>\`. Write the check and the line as text in your reply, not only in your thinking: the log is built from reply text. Do the same for a gain from a card such as Workshop. When you end a turn with a buy unused, write \`REASON T<turn> nothing: <why>\`. The line is added to the check and never replaces it."
fi
last="The game also ends after 50 turns each. Never stop before the game is over (the view says RESULT and the game is not running).

When the game is over, reply with the RESULT line, your final deck, the plan you made, and three lines on how it worked."
names="The game already exists, so don't create one. This server's tools are join_game, wait_for_decision, answer, view and card. Use these names where the skills name others (\`state\` is view, \`wait\` is wait_for_decision, \`step\` is answer)."

case "$role" in
plain) prompt="$head

1. The kingdom and its card text are in kingdoms/. Decide on your plan before playing. You may keep notes in notes.md (the only file you can write).
2. $loop
3. $reason
4. $last" ;;
guided) prompt="$head

1. Play the whole game with the play-game skill and this repository's context: kingdom-analysis makes the plan (the kingdom and its card text are in kingdoms/), play-turn makes the decisions. Keep the plan in notes.md (the only file you can write), and rewrite it there whenever the skill has you review it.
2. $names $loop
3. $reason
4. $last" ;;
target) prompt="$head

1. The plan is already decided, so don't run kingdom-analysis. Build a Village/Smithy/Bridge engine and win with one turn that draws the deck and plays every Bridge. The deck to build is exactly this: 6 Bridges, 10 Villages, 4 Smithies, 3 Markets, 1 Workshop, 1 Chapel and 3 Coppers. Nothing else belongs in it: the Estates and the other Coppers get trashed, there is no other Treasure and no Festival, and no Victory card until the turn that wins. Write that to notes.md (the only file you can write) as your plan. The order in which you get there is yours to work out.
2. Play the whole game with the play-game skill and this repository's context; play-turn makes the decisions.
3. $names $loop
4. $reason
5. $last" ;;
esac

log="$out/session.jsonl"
claude -p "$prompt" "${common[@]}" > "$log" 2> "$out/err.log"
sid=$(head -1 "$log" | jq -r .session_id)
for i in 1 2 3 4 5 6; do
  running=$(python3 -I "$M/scripts/mcp.py" "$url" list_games '{}' | jq -r --arg g "$g" '.games[] | select(.game_id==$g) | .running')
  [ "$running" = "true" ] || break
  echo "resume $i" >> "$out/resumes.log"
  claude -p "The game isn't over yet. Re-read notes.md, then keep playing: wait_for_decision, then answer, until the RESULT line appears. Keep writing the REASON line, as reply text, before each buy or gain." --resume "$sid" "${common[@]}" >> "$log" 2>> "$out/err.log"
done
echo "$game-$role done"
