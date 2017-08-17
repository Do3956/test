# encoding: utf-8  

""" 
@version: v1.0 
@author: do 
@time: 2017/8/17 22:18 
""" 

#coding=utf-8
import requests
url = 'http://localhost:8080'
path = r'D:\test\1.zip'
print path
files = {'file': open(path, 'rb')}
r = requests.post(url, files=files)
print r.url,r.text