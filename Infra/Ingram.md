<h2><b>Download and install ingram</b></h2>

	git clone https://github.com/jorhelp/Ingram.git && cd Ingram

	pip install virtualenv
	
	python -m virtualenv venv
	
	source venv/bin/activate
	
	pip install -r requirements.txt

Google Country's network range

	https://lite.ip2location.com/ip-address-ranges-by-country?lang=en_US

------------------------------------------

<h1><b>Masscan</b></h1>

Save range of targets in targets1.txt

10.10.10.10/8

	sudo masscan -p80,8000,8008 -iL targets1.txt -oL test1 --rate 8000
	
	sudo masscan -p80 --range 192.168.153.0/24 -oL test1 --rate 8000

OR

<h1><b>run_ingram.py</b></h1>

In the root directory of https://github.com/jorhelp/Ingram.git

	python run_ingram.py

	nano targets2
	
	10.10.10.0/24

	python run_ingram.py -i targets2.txt -o results

Once done, usually 1 target takes around 5 - 10 mins

	cd results

<h1><b>!!! Always rm -rf results/ for new scan !!!</b></h1>
