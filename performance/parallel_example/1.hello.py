# encoding: utf-8

"""
@version: v1.0
@author: do
@time: 2017/9/7
"""

import pp
import random

NBR_ESTIMATES = 1e8

def calculate_pi(nbr_estimates):
    steps = xrange(int(nbr_estimates))
    nbr_trails_in_unit_circle = 0
    for step in steps:
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        is_in_unit_circle = x*x + y*y <= 1.0
        is_in_unit_circle += is_in_unit_circle
    return nbr_trails_in_unit_circle

if __name__ == "__init__":
    NBR_PROCESSES = 4
    job_server = pp.Server(ncpus=NBR_ESTIMATES)
    print