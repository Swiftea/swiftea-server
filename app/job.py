from threading import Thread
import os


from crawler.main import main


class CrawlerThread(Thread):
    def __init__(self, sem, **args):
        Thread.__init__(self)
        self.args = args
        self.sem = sem

    def run(self):
        self.sem.P()
        self.crawl()
        self.sem.V()

    def crawl(self):
        os.chdir('app/worker')
        crawler = main(**self.args)
        crawler.start()
        os.chdir('../..')
