#coding:utf-8
import redis
from redis import sentinel

s = sentinel.Sentinel([("120.25.174.76", 27380)], password = "Zyl_Baoshi@redis#1")
rds = s.master_for("mymaster")
pip = rds.pipeline(transaction=False)
keys = rds.keys("hu:*")

counter = 0 
for k in keys:
    if len(k.split(":")) >= 3:
        continue

    pip.hdel(k, "nickname")
    counter += 1

    if counter >= 1000:
        pip.execute()
        print "deleted 1000."
        counter = 0

print "over."
