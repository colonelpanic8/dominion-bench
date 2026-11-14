"""Minimal MCP (streamable HTTP) client: mcp.py URL TOOL JSON_ARGS -> prints the result JSON."""
import json, sys, urllib.request

def post(url, body, session=None):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept", "application/json, text/event-stream")
    if session:
        req.add_header("Mcp-Session-Id", session)
    with urllib.request.urlopen(req, timeout=60) as r:
        sid = r.headers.get("Mcp-Session-Id")
        raw = r.read().decode()
    if not raw.strip():
        return sid, None
    if raw.lstrip().startswith("{"):
        return sid, json.loads(raw)
    msgs = [json.loads(l[5:]) for l in raw.splitlines() if l.startswith("data:") and l[5:].strip()]
    return sid, (msgs[-1] if msgs else None)

def call(url, tool, args):
    sid, _ = post(url, {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
        "protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "bench", "version": "0"}}})
    post(url, {"jsonrpc": "2.0", "method": "notifications/initialized"}, sid)
    _, res = post(url, {"jsonrpc": "2.0", "id": 2, "method": "tools/call",
                        "params": {"name": tool, "arguments": args}}, sid)
    return res["result"]

if __name__ == "__main__":
    r = call(sys.argv[1], sys.argv[2], json.loads(sys.argv[3]))
    print(json.dumps(r.get("structuredContent") or {"text": "\n".join(c.get("text", "") for c in r.get("content", []))}))
