default: check

fmt:
    alejandra -q .

fmt-check:
    alejandra -q --check .

# Validate cases against the pinned dominion-engine card data.
lint:
    DOMINION_ENGINE="${DOMINION_ENGINE:-$DOMINION_ENGINE_PINNED}" python3 -I scripts/bench.py check

check: fmt-check lint

list:
    python3 -I scripts/bench.py list

render case:
    DOMINION_ENGINE="${DOMINION_ENGINE:-$DOMINION_ENGINE_PINNED}" python3 -I scripts/bench.py render {{case}}

# just sandbox [--agents PATH] [--rev REV] DIR CASE...
sandbox +args:
    DOMINION_ENGINE="${DOMINION_ENGINE:-$DOMINION_ENGINE_PINNED}" python3 -I scripts/bench.py sandbox {{args}}
