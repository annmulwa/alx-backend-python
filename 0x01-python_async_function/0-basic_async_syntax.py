#!/usr/bin/env python3
'''
asynchronous coroutine that takes in an integer argument
named wait_random that waits for a random delay between 0
and max_delay (included and float value) seconds and
eventually returns it.
'''


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually
    returns it
    '''
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
