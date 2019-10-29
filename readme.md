# swiftea-server

This is the server for asking to launch the [Swiftea Crawler](https://github.com/Swiftea/Crawler).

Current version is `0.0.1`.

## Setup

		virtualenv -p /usr/bin/python3.7 venv

Add these lines in `venv/bin/activate`:

		export FLASK_APP=app/app.py
		export FLASK_ENV=development

with this command : `echo -e "export FLASK_APP=app/app.py\nexport FLASK_ENV=development" >> venv/bin/activate`

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

### Push a new version

Install the new version of `swiftea-crawler` if available.

		cd www/swiftea-server
		pip uninstall swiftea-crawler
		pip install swiftea_crawler-1.1.8-py3-none-any.whl --user
		git pull

Restart the server.

### Prod

See uwsgi logs: `tail -n 50 ~/admin/logs/uwsgi/*.log`.

See crawler logs:  `tail -n 50 ~/www/swiftea-server/app/worker/data/config/events.log`.
