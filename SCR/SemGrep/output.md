> **Dependencies**
>
> <https://semgrep.dev/docs/getting-started/quickstart>
>
> Install python
>
> <https://www.python.org/downloads/>
>
> Install git
>
> <https://git-scm.com/install/windows>
>
> Add both to PATH
>
> **Setting up**
>
> Browse to target folder
>
> Set environment configs
>
> powershell
>
> \$env:PYTHONUTF8="1"
>
> \$env:PYTHONIOENCODING="utf-8"
>
> \$env:SEMGREP_REPO_URL="https://local-scan/\<Target Folder\>"
>
> \$env:SEMGREP_REPO_URL="https://local-scan/MAVIS2-SCR"
>
> Configure git identity
>
> git init
>
> git add .
>
> git commit -m "initial commit"
>
> git config --global user.name "Admin"
>
> git config --global user.email "admin@local"
>
> **Start scanning**
>
> **Local scanning (Best used for SCR)**
>
> Git not required but output sucks
>
> Full Scan (Will take a long while)
>
> semgrep scan --config p/owasp-top-ten --config p/secrets --config
> p/security-audit --config p/default --json --output results.json
>
> Full security baseline        
>
> semgrep scan --config p/owasp-top-ten --json --output results.json
>
> Secrets detection        
>
> semgrep scan --config p/secrets --json --output results.json
>
> Security audit rulesSecurity audit rules --json --output results.json
>
> semgrep scan --config p/security-audit --json --output results.json
>
> Basic scanning only
>
> semgrep scan --config=auto--json --output results.json
>
> <img src="media/image1.png" style="width:6.26806in;height:1.90903in" />
>
> Convert json output to html so nicer to read
>
> Create python script
>
> \<\<json_to_html.py\>\>
>
> import json, html
>
> from pathlib import Path
>
> p = Path("results.json")
>
> data = json.loads(p.read_text(encoding="utf-8"))
>
> results = data.get("results", \[\])
>
> errors = data.get("errors", \[\])
>
> stats = data.get("stats", {})
>
> def esc(s):
>
> return html.escape("" if s is None else str(s))
>
> rows = \[\]
>
> for r in results:
>
> check_id = r.get("check_id")
>
> path = r.get("path")
>
> start = r.get("start", {})
>
> end = r.get("end", {})
>
> extra = r.get("extra", {})
>
> msg = extra.get("message")
>
> sev = extra.get("severity")
>
> line = start.get("line")
>
> col = start.get("col")
>
> \# Best-effort code snippet
>
> snippet = ""
>
> try:
>
> lines = Path(path).read_text(encoding="utf-8",
> errors="replace").splitlines()
>
> if isinstance(line, int) and 1 \<= line \<= len(lines):
>
> lo = max(1, line - 2)
>
> hi = min(len(lines), line + 2)
>
> snippet = "\n".join(f"{i:\>5}: {lines\[i-1\]}" for i in range(lo, hi +
> 1))
>
> except Exception:
>
> snippet = ""
>
> rows.append(f"""
>
> \<tr\>
>
> \<td\>{esc(sev)}\</td\>
>
> \<td\>{esc(check_id)}\</td\>
>
> \<td\>{esc(path)}\</td\>
>
> \<td\>{esc(line)}:{esc(col)}\</td\>
>
> \<td\>{esc(msg)}\</td\>
>
> \<td\>\<pre\>{esc(snippet)}\</pre\>\</td\>
>
> \</tr\>
>
> """)
>
> err_html = "".join(
>
> f"\<li\>\<b\>{esc(e.get('type'))}\</b\>:
> {esc(e.get('message'))}\</li\>" for e in errors
>
> )
>
> out = f"""\<!doctype html\>
>
> \<html\>
>
> \<head\>
>
> \<meta charset="utf-8"/\>
>
> \<title\>Semgrep Report\</title\>
>
> \<style\>
>
> body {{ font-family: Arial, sans-serif; margin: 20px; }}
>
> table {{ border-collapse: collapse; width: 100%; }}
>
> th, td {{ border: 1px solid \#ddd; padding: 8px; vertical-align: top;
> }}
>
> th {{ background: \#f5f5f5; text-align: left; }}
>
> pre {{ white-space: pre-wrap; margin: 0; }}
>
> .meta {{ margin-bottom: 16px; }}
>
> \</style\>
>
> \</head\>
>
> \<body\>
>
> \<h1\>Semgrep Report\</h1\>
>
> \<div class="meta"\>
>
> \<div\>\<b\>Findings:\</b\> {len(results)}\</div\>
>
> \<div\>\<b\>Errors:\</b\> {len(errors)}\</div\>
>
> \<div\>\<b\>Stats:\</b\> {esc(stats)}\</div\>
>
> \</div\>
>
> \<h2\>Findings\</h2\>
>
> \<table\>
>
> \<thead\>
>
> \<tr\>
>
> \<th\>Severity\</th\>
>
> \<th\>Rule\</th\>
>
> \<th\>File\</th\>
>
> \<th\>Location\</th\>
>
> \<th\>Message\</th\>
>
> \<th\>Context\</th\>
>
> \</tr\>
>
> \</thead\>
>
> \<tbody\>
>
> {''.join(rows) if rows else '\<tr\>\<td colspan="6"\>No
> findings\</td\>\</tr\>'}
>
> \</tbody\>
>
> \</table\>
>
> \<h2\>Scan Errors\</h2\>
>
> \<ul\>
>
> {err_html if err_html else '\<li\>None\</li\>'}
>
> \</ul\>
>
> \</body\>
>
> \</html\>
>
> """
>
> Path("report.html").write_text(out, encoding="utf-8")
>
> print("Wrote report.html")
>
> python json_to_html.py
>
> <img src="media/image2.png" style="width:4.03125in;height:2.51042in" />
>
> **Remote scanning (Mostly for Devs)**
>
> Requires files to be uploaded to git
>
> Requries github account
>
> semgrep login
>
> Copy link to browser and click activate
>
> semgrep ci
>
> <img src="media/image3.png" style="width:6.26806in;height:2.71875in" />
>
> Results
>
> <img src="media/image4.png" style="width:4.20833in;height:0.82292in" />
>
> Copy the findings URL
>
> Browse to Projects \> Project Name \> Code findings
>
> <img src="media/image5.png" style="width:5in;height:2.82292in" />
>
> s
