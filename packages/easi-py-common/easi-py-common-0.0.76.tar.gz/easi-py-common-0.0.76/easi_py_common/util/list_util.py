# -*- coding: utf-8 -*-
from typing import Tuple, List


def map_group(data, key=None):
    m = {}
    for val in data:
        ret = key(val)
        k = ret
        if isinstance(ret, Tuple) or isinstance(ret, List):
            if len(ret) > 1:
                k = ret[0]
                val = ret[1]
        if k not in m:
            m[k] = []
        m[k].append(val)
    return m
