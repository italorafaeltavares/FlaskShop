.DEFAULT_GOAL := up

venv:
	@python3 -m venv .venv
	@source .venv/bin/activate

pip:
	@pip install -r requirements.txt

dbcreate:
	@python3 setup.py

up:
	@python3 app.py

full: venv pip dbcreate up
