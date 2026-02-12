import json, html
from pathlib import Path

p = Path("results.json")
data = json.loads(p.read_text(encoding="utf-8"))

results = data.get("results", [])
errors = data.get("errors", [])
stats = data.get("stats", {})

def esc(s): 
    return html.escape("" if s is None else str(s))

rows = []
for r in results:
    check_id = r.get("check_id")
    path = r.get("path")
    start = r.get("start", {})
    end = r.get("end", {})
    extra = r.get("extra", {})
    msg = extra.get("message")
    sev = extra.get("severity")
    line = start.get("line")
    col = start.get("col")

    # Best-effort code snippet
    snippet = ""
    try:
        lines = Path(path).read_text(encoding="utf-8", errors="replace").splitlines()
        if isinstance(line, int) and 1 <= line <= len(lines):
            lo = max(1, line - 2)
            hi = min(len(lines), line + 2)
            snippet = "\n".join(f"{i:>5}: {lines[i-1]}" for i in range(lo, hi + 1))
    except Exception:
        snippet = ""

    rows.append(f"""
      <tr>
        <td>{esc(sev)}</td>
        <td>{esc(check_id)}</td>
        <td>{esc(path)}</td>
        <td>{esc(line)}:{esc(col)}</td>
        <td>{esc(msg)}</td>
        <td><pre>{esc(snippet)}</pre></td>
      </tr>
    """)

err_html = "".join(
    f"<li><b>{esc(e.get('type'))}</b>: {esc(e.get('message'))}</li>" for e in errors
)

out = f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>Semgrep Report</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 20px; }}
    table {{ border-collapse: collapse; width: 100%; }}
    th, td {{ border: 1px solid #ddd; padding: 8px; vertical-align: top; }}
    th {{ background: #f5f5f5; text-align: left; }}
    pre {{ white-space: pre-wrap; margin: 0; }}
    .meta {{ margin-bottom: 16px; }}
  </style>
</head>
<body>
  <h1>Semgrep Report</h1>
  <div class="meta">
    <div><b>Findings:</b> {len(results)}</div>
    <div><b>Errors:</b> {len(errors)}</div>
    <div><b>Stats:</b> {esc(stats)}</div>
  </div>

  <h2>Findings</h2>
  <table>
    <thead>
      <tr>
        <th>Severity</th>
        <th>Rule</th>
        <th>File</th>
        <th>Location</th>
        <th>Message</th>
        <th>Context</th>
      </tr>
    </thead>
    <tbody>
      {''.join(rows) if rows else '<tr><td colspan="6">No findings</td></tr>'}
    </tbody>
  </table>

  <h2>Scan Errors</h2>
  <ul>
    {err_html if err_html else '<li>None</li>'}
  </ul>
</body>
</html>
"""

Path("report.html").write_text(out, encoding="utf-8")
print("Wrote report.html")
