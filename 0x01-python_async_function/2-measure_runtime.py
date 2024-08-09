#!/usr/bin/env python3
'''Task 2.
'''
import asyncio
import time


waitN = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Calculates the average runtime of waitN.
    '''
    start_time = time.time()
    asyncio.run(waitN(n, max_delay))
    return (time.time() - start_time) / n
