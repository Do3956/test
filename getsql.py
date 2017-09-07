#coding:utf8

num_userid = {}
with open('time.txt', "rb") as f:
    for line in f.readlines():
        ms = line.split("(127.0.0.1)")[-1].strip()[:-2]
        if float(ms) > 500:
            print ms
        elif float(ms) > 200:
            print ms
