from flask import Flask, jsonify, request


from app.task import new_task

app = Flask(__name__)


@app.route('/status')
def status():
    """Get crawler's status.

    Later: list of active crawlers.

    """
    return {'response': "Crawler's status"}


@app.route('/start-crawler', methods=['POST'])
def start_crawler():
    """Start a new domain crawler."""
    url = request.form['url']
    level = int(request.form['level'])
    try:
        target_level = int(request.form['target-level'])
    except KeyError:
        target_level = 1
    response = new_task(url=url, level=level, target_level=target_level)
    return jsonify(response)
