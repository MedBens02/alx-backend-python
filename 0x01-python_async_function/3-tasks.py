#!/usr/bin/env python3
'''Task 3.
'''
import asyncio


waitRand = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creates an async task for waitRand.
    '''
    return asyncio.create_task(waitRand(max_delay))
