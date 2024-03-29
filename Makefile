
install:
	python3 -m pip install --user dist/*.whl

build:
	poetry build

uninstall:
	pip uninstall hexlet-code

lint:
	poetry run flake8 page_loader

poet:
	poetry install

testing:
	pytest

test-cov:
	poetry run pytest --cov=page_loader tests/ --cov-report xml
