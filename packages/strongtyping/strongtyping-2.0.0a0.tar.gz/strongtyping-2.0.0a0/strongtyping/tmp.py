#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 20.08.20
@author: felix
"""
from dataclasses import dataclass
from typing import Type
from typing import Union

from strong_typing import match_class_typing
from strong_typing import match_typing


def with_type():
    class NoUser:
        def __repr__(self):
            return 'NoUser'

    class User:
        def __repr__(self):
            return 'User'

    class BasicUser(User):
        pass

    class ProUser(User):
        pass

    class TeamUser(BasicUser, ProUser):
        pass

    @match_typing
    def func_a(a: Type[User]):
        _a = a()
        return repr(_a)

    @match_typing
    def func_b(a: Type[User], b: Type[Union[BasicUser, ProUser]]):
        _a, _b = a(), b()
        return repr(_a), repr(_b)

    assert func_a(User) == 'User'
    assert func_b(User, TeamUser) == ('User', 'User')
    func_a(NoUser)
    func_a(NoUser, User)


def main():
    with_type()


if __name__ == '__main__':
    main()
