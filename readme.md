# swiftea-server

This is the server for asking to launch the [Swiftea Crawler](https://github.com/Swiftea/Crawler).

## Setup

		virtualenv -p /usr/bin/python3.7 venv

Add these lines in `venv/bin/activate`:

		export FLASK_APP=app/app.py
		export FLASK_ENV=development

Then:

		source venv/bin/activate
		pip install -r requirements.txt

### Run

		flask run

### Lint

		prospector > prospector_output.json

## Deploy

Application path: `/www/swiftea-server/app.wsgi`.

Working directory: `/www/swiftea-server`.

		pip install -r requirements.txt --user

Create folder `wroker` and upload `wroker/crawler-config.json`.
