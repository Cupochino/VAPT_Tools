<h1>Dependencies</h1>

    https://semgrep.dev/docs/getting-started/quickstart

Install python

    https://www.python.org/downloads/

Install git

    https://git-scm.com/install/windows

Add both to PATH

<h1>Setting up</h1>

cd to target folder

Set environment configs

    powershell
    
    $env:PYTHONUTF8="1"
    
    $env:PYTHONIOENCODING="utf-8"
    
    $env:SEMGREP_REPO_URL="https://local-scan/<Target Folder>"

Configure git identity

    git init
    
    git add .
    
    git commit -m "initial commit"
    
    git config --global user.name "Admin"
    
    git config --global user.email "admin@local"

<h1>Start scanning</h1>

<h2>Local scanning (Best used for SCR)</h2>

Git not required but output sucks

Full Scan (Will take a long while)

    semgrep scan --config p/owasp-top-ten --config p/secrets --config p/security-audit --config p/default --json --output results.json

Full security baseline        

    semgrep scan --config p/owasp-top-ten --json --output results.json

Secrets detection        

    semgrep scan --config p/secrets --json --output results.json

Security audit rulesSecurity audit rules --json --output results.json

    semgrep scan --config p/security-audit --json --output results.json

Basic scanning only

    semgrep scan --config=auto--json --output results.json

<img width="939" height="286" alt="image" src="https://github.com/user-attachments/assets/59d944c7-8aea-486a-97e5-680a9b425052" />

Convert json output to html so nicer to read

Create python script

    python json_to_html.py

<img width="387" height="241" alt="image" src="https://github.com/user-attachments/assets/d3dee23e-440b-4f45-8894-129a1f4416bb" />

<h2>Remote scanning (Mostly for Devs)</h2>

Requires files to be uploaded to git

Requries github account

    semgrep login

Copy link to browser and click activate

    semgrep ci

Results

<img width="404" height="79" alt="image" src="https://github.com/user-attachments/assets/45a1a388-9fc4-46be-b01d-1ce1e1156902" />

Copy the findings URL

Browse to Projects > Project Name > Code findings

<img width="470" height="150" alt="image" src="https://github.com/user-attachments/assets/1973171c-18a9-4019-869b-ed3cae70d771" />
