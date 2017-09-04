# encoding: utf-8  

""" 
@version: v1.0 
@author: do 
@time: 2017/8/26 18:52

读取性能分析文件
""" 

import pstats

p = pstats.Stats("my.profile")
p.sort_stats("cumulative")
p.print_stats() #标准输出
p.print_callers(6) #被调用的子函数 <- 父函数整体耗时，数字参数可以先填1，根据输出再写总的
p.print_callees(6)