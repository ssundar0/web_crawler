# copyrights => Code by Shyam_Sundar

import threading
from queue import Queue
from spider import Spider
from general import *
from domain import *


# use capital letters for constant variables
PROJECT_NAME = input("Enter ur project name : ")
HOMEPAGE = input("Enter website address to crawl: ")
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# Create workers
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=tasks)
        t.daemon = True
        t.start()


# Creating Tasks(next link in queue)
def tasks():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# each url is new job
def create_jobs():
    for url in file_to_set(QUEUE_FILE):
        queue.put(url)
    queue.join()
    crawl()


# check if links in queued, if yes then crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + " links are there for the process.")
        create_jobs()

create_workers()
crawl()

