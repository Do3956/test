# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/8/15'
__content__ = ''
"""

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=5000, help="run on the given port", type=int)

num = 0
def startTimer():
    tornado.ioloop.PeriodicCallback(cleanCount, 1000).start()

def cleanCount():
    global num
    print num
    num = 0

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        global num
        num += 1
        self.add_header("Access-Control-Allow-Origin", "*")
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    startTimer()
    tornado.ioloop.IOLoop.instance().start()