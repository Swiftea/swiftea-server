from threading import Thread
import os


from crawler.main import main


class CrawlerThread(Thread):
    def __init__(self, **args):
        Thread.__init__(self)
        self.args = args

    def run(self):
        os.chdir('app/worker')
        crawler = main(**self.args)
        crawler.start()
        os.chdir('../..')
