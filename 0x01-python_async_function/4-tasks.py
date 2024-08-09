#!/usr/bin/env python3
'''Task 4.
'''

import asyncio
from typing import List

taskWaitRand = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Calls taskWaitRand n times with specified max_delay.
    '''
    tasks = [taskWaitRand(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
