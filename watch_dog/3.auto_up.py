# encoding: utf-8

"""
@version: v1.0
@author: do
@time: 2017/7/11 23:25
"""

from watchdog.observers import Observer
from watchdog.events import *
import time
import os
import requests

dir_path = r"F:\remote"

def up_file(path):
    if "thai" in path:
        url = 'http://47.74.130.221:8080'
        files = {'file': open(path, 'rb')}
        r = requests.post(url, files=files)
        print r.url, r.text
    if "hk" in path:
        url = 'http://47.91.235.223:8080'
        files = {'file': open(path, 'rb')}
        r = requests.post(url, files=files)
        print r.url, r.text
    if "38" in path:
        url = 'http://112.74.75.38:8000'
        files = {'file': open(path, 'rb')}
        r = requests.post(url, files=files)
        print r.url, r.text
    # if "126" in path:
    #     url = 'http://112.74.75.38:8080'
    #     files = {'file': open(path, 'rb')}
    #     r = requests.post(url, files=files)
    #     print r.url, r.text

class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        try:
            if event.src_path.split('.')[-1] == 'zip':
                time.sleep(1)
                up_file(event.src_path)
                # os.system("sh unzip_file.sh %s" % event.src_path)
        except Exception as e:
            print e

def start_watch():
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, dir_path, True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_watch()