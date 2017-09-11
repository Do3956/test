#coding:utf-8
# 测试redis操作时长，多进程

import redis
import random
import time
import multiprocessing

h = "127.0.0.1" #r-wz95bd3a73645344.redis.rds.aliyuncs.com #10.44.127.92
p = 6379
rds = redis.Redis(host = h, port = p)
# a = "Zyl_Baoshi@redis#1"   # Zyl123456 Zyl_Baoshi@redis#1
# rds = redis.Redis(host = h, port = p, password = a)

num = 10
def write_to():
    s = time.time()
    for i in xrange(1, num):
        key = "hu:%s" % i
        rds.hmset(key, {"money" : i, "name" : "testyxb%d" % i, "nickname" : "tests2sdgghjsfgdfsfsd", "exp" : i, "lastmoney" : i, "offlinetime" : time.time()} )

    print "write",num,":", time.time() - s

def rand_read():
    s = time.time()
    for i in xrange(1, num):
        key =  "hu:%d" % random.randint(1, num)
        rds.hgetall(key)

    print "rand_read",num,":", time.time() - s

def rand_incr():
    s = time.time()
    for i in xrange(1, num):
        key =  "hu:%d" % random.randint(1, num)
        rds.hincrby(key, "money", 1)

    print "rand_incr",num,":", time.time() - s

def rand_deincr():
    s = time.time()
    for i in xrange(1, num):
        key =  "hu:%d" % random.randint(1, num)
        rds.hincrby(key, "money", -1)

    print "rand_deincr",num,":", time.time() - s



if __name__ == "__main__":
    t0 = time.time()

    all_process = []
    f = [rand_read, rand_incr, rand_deincr, rand_incr]
    pool = multiprocessing.Pool(processes=60)
    print '----start---'
    start = time.time()
    for i in xrange(60):
        pool.apply_async(f[i / 15])

    pool.close()
    pool.join()

    print "end",time.time() - start,time.time()-t0

    
