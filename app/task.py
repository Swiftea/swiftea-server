from app.job import CrawlerThread


def new_task(**args):
    response = 'starting crawler'
    crawler_thread = CrawlerThread(**args)
    crawler_thread.start()
    response += ' | started'
    return response
