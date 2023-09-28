install:
	poetry install

brain-games:
	poetry run brain-games

build: check
	poetry build

