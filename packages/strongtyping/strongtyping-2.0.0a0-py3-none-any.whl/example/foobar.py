#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 15.05.21
@author: felix
"""
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from docs_from_typing import numpy_docs_from_typing
from docs_from_typing import rest_docs_from_typing


@rest_docs_from_typing
def foo(val: int, *, val_a: Optional[str] = "foo") -> int:
    """
    some important information about this function
    this must occur even after the inclusion of the typing docstring information

    $1 component where this animation object belongs to (default None) if given,
    the animation object will be removed automatically when the parent component is no longer accessible
    $2 if False, animation object is hidden after t1, shown otherwise
    """
    return val ** 2


# @rest_docs_from_tying
# def foo_2(val: int, val_a: Optional[str] = "foo") -> int:
#     """
#     some important information about this function
#     this must occur even after the inclusion of the typing docstring information
#     """
#     return val ** 2
#
#
@numpy_docs_from_typing
def foo(val: int, /, *, val_a: Optional[str] = "foo") -> int:
    return val ** 2


# @rest_docs_from_tying
# def foo(val: List[Union[int, List[Union[int, str]]]],
#           val_a: Dict[str, Dict[str, int]], val_b: Dict[str, str]) -> int:
#     """
#     some important information about this function
#     this must occur even after the inclusion of the typing docstring information
#     """
#     return val ** 2


if __name__ == '__main__':
    print(help(foo))
