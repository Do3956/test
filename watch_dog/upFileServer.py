# encoding: utf-8  

""" 
@version: v1.0 
@author: do 
@time: 2017/8/17 22:18 
""" 

from BaseHTTPServer import BaseHTTPRequestHandler
import cgi
import datetime
import time

class   PostHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        start_time = time.time()
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     }
        )
        self.send_response(200)
        self.end_headers()
        self.wfile.write('%s:, ' % datetime.datetime.today())
        self.wfile.write('%s, ' % str(self.client_address)
)
        for field in form.keys():
            field_item = form[field]
            filename = field_item.filename
            filevalue  = field_item.value
            filesize = len(filevalue)#文件大小(字节)
            print filename, len(filevalue)
            self.wfile.write('file:%s, ' % filename)
            with open(filename.decode('utf-8'),'wb') as f:
                f.write(filevalue)

        use_sec = time.time() - start_time
        self.wfile.write('success, use:%s seconds'%use_sec)
        return

if __name__=='__main__':
    from BaseHTTPServer import HTTPServer
    sever = HTTPServer(('localhost',8080),PostHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    sever.serve_forever()