# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/9/8'
__content__ = ''
"""
import random
import time

class RandomApi():
    def __init__(self):
        self.init_chr()
        self.random_times = 0

    def init_chr(self):
        lowercase = tuple(range(65, 91))
        uppercase = tuple(range(97, 123))
        num = tuple(range(48, 58))
        self.letters = lowercase + uppercase
        self.all_chr = self.letters + num

    def change_seed(self):
        if self.random_times > 1000:
            self.random_times = 0
            random.seed()
        self.random_times += 1

    def get_num_or_letter(self):
        self.change_seed()
        return chr(random.choice(self.all_chr))

    def get_letter(self):
        self.change_seed()
        return chr(random.choice(self.all_chr))

    def get_last_ts(self, num=5):
        return str(int(time.time()))[-num:]

    def get_random_str(self):
        r1 = self.get_num_or_letter()
        r2 = self.get_last_ts()
        r3 = random.randint(0,99999)
        r4 = self.get_num_or_letter()
        r = '%s%s%s%s' % (r3, r1, r2, r4)
        return r

    def get_random_token(self):
        r1 = self.get_num_or_letter()
        r2 = self.get_last_ts()
        r3 = random.randint(0, 99999)
        r4 = self.get_num_or_letter()
        r = '%s*$^%s_)(*^&jg+.-%s|}{P|{,-cS@%s' % (r3, r1, r2, r4)
        return r

randomApi = RandomApi()

if __name__ == "__main__":
    print randomApi.get_random_str()
    print randomApi.get_random_token()
    start = time.time()
    n = 10000
    # windows(4核8G)：1W耗时5.5s，100W，560s
    # linux(4核8G)：1W耗时0.15s，100W，15.6s，10000W，15.6s
    # 未出现随机数越多，耗时越长情况
    for i in xrange(n):
        random.seed()
    print n, time.time() - start