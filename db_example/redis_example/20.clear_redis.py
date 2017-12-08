#coding:utf-8
import redis
from redis import sentinel

# s = sentinel.Sentinel([("120.25.174.12", 27380)], password = "123")
rds = redis.Redis(host="120.24.36.12", port=7379, password="123")
pip = rds.pipeline(transaction=False)
keys = rds.keys("hu:*")
print 'keys:',keys

counter = 0 
for k in keys:
    # if len(k.split(":")) >= 3:
    #     continue

    pip.delete(k)
    counter += 1

    if counter >= 1000:
        pip.execute()
        print "deleted 1000."
        counter = 0

print "over."
