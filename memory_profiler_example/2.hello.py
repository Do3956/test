# encoding: utf-8  

""" 
@version: v1.0 
@author: do 
@time: 2017/8/23 23:30 
""" 

from memory_profiler import profile
import networkx as nx

@profile(precision=4)
def my_func():
    a = 'a' * 1024 * 1024 * 1024;
    del a
    G = nx.Graph()
    G.add_node(1)
    G.add_nodes_from([i for i in range(10000)])
    G.add_nodes_from([i for i in range(10000, 20000)])
    G.add_edges_from([(1,2), (1,4), (2, 9), (4, 1), (3, 8)])
    del G
    print "++++++"

if __name__ == '__main__':
    my_func()