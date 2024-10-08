#!/usr/bin/env python3
'''Task 1.
'''
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Generates 10floats based on a 10floats generator.
    '''
    return [n async for n in async_generator()]
