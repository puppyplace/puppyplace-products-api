clean: clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

install-deps:
	pip install poetry
	poetry install

run:
	poetry run python manage.py runserver

test:
	poetry run pytest -x -s

lint:
	isort . && blue . 

check-dead-fixtures:
	poetry run pytest --dead-fixtures

makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

docker-build:
	docker build -t puppyplace-products-api .

docker-run:
	docker run -p 8000:8000 -it puppyplace-products-api