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

class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        if event.src_path.split('.')[-1] == 'zip':
            print 1111,event.src_path,type(event.src_path)
            print ("sh unzip_file.sh %s" % event.src_path)
            # os.system("sh unzip_file.sh %s" % event.src_path)
        # elif event.src_path.split('.')[-1] == 'sql':
        #     print 2222,event.src_path,type(event.src_path)
            # os.system("sh unzip_file.sh %s" % event.src_path)

if __name__ == "__main__":
    dir_path = r"D:\test"
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