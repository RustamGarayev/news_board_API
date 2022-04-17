# News Board API

## How to start

Simply enough:

`docker-compose up --build`

[//]: # (Also, you can find postman exported json file in this repo, just import it in Postman and you will have necessary endpoints to test.)

[//]: # (The file name is `news_board.postman_collection.json`.)

## Project dependencies

The project dependency management is based on `pip`

## Additional notes

There is a script folder where helper bash scripts are defined for formatting and linting the code base.
All codebase was formatted using black, flake8 and isort.

In order to run it manually:

`./scripts/check_coding.sh`

This action was defined as pre-commit hook, at each commit it will reformat your code base.
For activating pre-commit run locally:
`pre-commit install`

In each commit, the code base will nicely be formatted.
