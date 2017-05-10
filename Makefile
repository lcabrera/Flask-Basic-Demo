.PHONY: docs test

help:
	@echo "  env         Crea un entorno virtual usando virtualenv."
	@echo "  deps        Instala dependencias usando pip y pip-tools."
	@echo "  clean       Eliminar ficheros *pyc, *.pyc, pyc's, etc."
	@echo "  lint        Comprobar el estilo  del código con varias herramientas."
	@echo "  test        Ejecuta todos los tests usando py.test"

.PHONY: env
env:
	sudo easy_install pip && \
	pip install virtualenv && \
	virtualenv env && \
	. env/bin/activate && \
	make deps

.PHONY: deps
deps:
	pip install pip-tools -U
	pip-compile --output-file requirements-prod.txt requirements-prod.in
	pip install -r requirements-prod.txt -U
	pip-compile --output-file requirements-dev.txt requirements-dev.in
	pip install -r requirements-dev.txt -U

.PHONY: isort
isort:
	isort -rc

.PHONY: pylint
pylint:
	find . -name "*.py" -type f -exec pylint '{}' \;

.PHONY: clean
clean:
	python manage.py clean

.PHONY: lint
lint:
	flake8 --exclude=env .

.PHONY: flake
flake:
	flake8 --doctests  --exclude=env .

.PHONY: doctest
doctest:
	pydocstyle --explain .

.PHONY: test
test:
	py.test tests

