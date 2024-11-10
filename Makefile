.DEFAULT_GOAL := up

venv:
	@python3 -m venv .venv

pip:
	@pip install -r requirements.txt

dbcreate:
	@python3 setup.py

up:
	@python3 app.py
