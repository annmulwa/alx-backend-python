#!/usr/bin/env python3
'''
function to_kv that takes a string k and an
int OR float v as arguments and returns a tuple
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    takes a string k and an int OR float
    v as arguments and returns a tuple
    '''
    return (k, float(v**2))
