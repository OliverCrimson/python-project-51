install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install dist/*.whl

lint:
	poetry run flake8 page_loader

check:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml