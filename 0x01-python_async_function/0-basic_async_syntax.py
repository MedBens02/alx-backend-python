#!/usr/bin/env python3
'''Task 0.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits a random time.
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
