
install:
	python3 -m pip install dist/*.whl

build:
	poetry build

uninstall:
	pip uninstall hexlet-code

lint:
	poetry run flake8 gendiff

poet:
	poetry install

testing:
	pytest