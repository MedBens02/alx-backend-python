#!/usr/bin/env python3
'''Task 1.
'''

import asyncio
from typing import List

waitRand = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' Calls wait_random n times with specified max_delay.
    '''
    tasks = [asyncio.create_task(waitRand(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
