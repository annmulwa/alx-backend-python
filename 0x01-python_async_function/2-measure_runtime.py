#!/usr/bin/env python3
'''
measure_time function with integers n
and max_delay as arguments that measures
the total execution time for wait_n
'''

from time import time
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    measures the total execution time for wait_n
    '''
    start_time = time()
    run(wait_n(n, max_delay))
    end_time = time()
    total_time = end_time - start_time
    return total_time / n
