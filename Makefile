all: black flake8 isort mypy test

black:
	black .

flake8:
	flake8 .

isort:
	isort .

mypy:
	mypy .

test:
	pytest tests/

run:
	python main.py
