from app.job import CrawlerThread


from app.sync import Semaphore


sem = Semaphore()


def new_task(**args):
    global sem
    response = 'starting crawler'
    crawler_thread = CrawlerThread(sem, **args)
    crawler_thread.start()
    response += ' | started'
    return response
