from app.job import CrawlerThread


def new_task(**args):
    crawler_thread = CrawlerThread(**args)
    crawler_thread.start()
    return 'launched'
