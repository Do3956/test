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

url = 'http://localhost:8080'
dir_path = r"D:\test"

def up_file(path):
    files = {'file': open(path, 'rb')}
    r = requests.post(url, files=files)
    print r.url, r.text

class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        try:
            if event.src_path.split('.')[-1] == 'zip':
                up_file(event.src_path)
                # os.system("sh unzip_file.sh %s" % event.src_path)
        except Exception as e:
            print e

def start_watch():
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, dir_path, False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_watch()