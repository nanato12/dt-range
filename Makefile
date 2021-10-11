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

build:
	rm -rf dist/*
	rm -rf build/*
	python setup.py sdist
	python setup.py bdist_wheel

upload-test:
	twine upload --repository testpypi dist/*

upload:
	twine upload --repository pypi dist/*
