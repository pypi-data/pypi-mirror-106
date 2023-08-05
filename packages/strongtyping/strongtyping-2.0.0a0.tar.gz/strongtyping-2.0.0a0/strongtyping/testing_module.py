#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 19.08.20
@author: felix
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 16.08.20
@author: felix
"""


def matches_origin(obj, type_obj):

    type_origin = getattr(type_obj, '__origin__')

    if hasattr(type_origin, '_name'):
        type_origin_name = type_origin._name

        if type_origin_name == 'Union' or type_origin_name == 'Any':
            return 1
    return isinstance(obj, type_origin)


def which_subtype(element):
    sub_type = 0

    if hasattr(element, '_name'):
        element_name = element._name
        if element_name == 'List':
            sub_type = 1
        if element_name == 'Tuple':
            sub_type = 2
        if element_name == 'Dict':
            sub_type = 3
        if element_name == 'Set':
            sub_type = 4
        if element_name == 'Any':
            sub_type = -2
        if element_name is None:
            if hasattr(element, '__origin__'):
                if hasattr(element.__origin__, '_name'):
                    if element.__origin__._name == 'Union':
                        sub_type = -1
                    if element.__origin__._name == 'Any':
                        return -2

    return sub_type


def sub_type_result(obj, type_obj, subtype):
    result = 0

    print(obj, type_obj, subtype)

    if subtype == -1:
        result += union_element(obj, type_obj)
    if subtype == 1:
        result += list_elements(obj, type_obj)
    if subtype == 2:
        result += tuple_elements(obj, type_obj)
    if subtype == 3:
        pass
    if subtype == 4:
        result += set_elements(obj, type_obj)

    return result


def union_element(obj, type_obj):
    result = 0

    if hasattr(type_obj, '__args__'):

        type_args = getattr(type_obj, '__args__')
        for type_arg in type_args:
            ttype = which_subtype(type_arg)

            if ttype == 0:
                result += isinstance(obj, type_arg)
            elif ttype == -2:
                return 1
            else:
                sub_type_result(obj, type_obj, ttype)
    else:
        result += isinstance(obj, type_obj)

    return result


def element_check(obj, type_obj):
    result = 0

    if hasattr(type_obj, '__args__'):

        type_args = getattr(type_obj, '__args__')

        for type_arg in type_args:

            ttype = which_subtype(type_arg)

            if ttype == 0:
                result += isinstance(obj, type_arg)
            elif ttype == -2:
                return -2
            else:
                result += sub_type_result(obj, type_arg, ttype)
    else:
        result = isinstance(obj, type_obj)
    return result


def dict_elements(obj, type_obj):
    key_result = 1
    value_result = 0

    obj_len = len(obj)

    if hasattr(type_obj, '__args__'):

        if matches_origin(obj, type_obj) == 0:
            return 0

        type_args = getattr(type_obj, '__args__')
        key_type_args = type_args[0]
        value_type_args = type_args[1]

        for key_element in obj.keys():
            if hasattr(key_type_args, '__args__'):
                key_result += sub_type_result(key_element, key_type_args, which_subtype(key_type_args))
            else:
                key_result += isinstance(key_element, key_type_args)
        for value_element in obj.values():
            if hasattr(value_type_args, '__args__'):
                value_result += sub_type_result(value_element, value_type_args, which_subtype(value_type_args))
            else:
                value_result += isinstance(value_element, value_type_args)

        return key_result >= obj_len and value_result >= obj_len
    else:
        return isinstance(obj, type_obj)



def set_elements(obj, type_obj):
    result = 0

    if hasattr(type_obj, '__args__'):

        if matches_origin(obj, type_obj) == 0:
            return 0

        for set_element in obj:
            tmp = element_check(set_element, type_obj)
            if tmp == -2:
                return 1
            result += tmp

        return result >= len(obj)
    else:
        return isinstance(obj, type_obj)


def tuple_elements(obj, type_obj):
    result = 0

    if hasattr(type_obj, '__args__'):

        if matches_origin(obj, type_obj) == 0:
            return 0

        type_args = getattr(type_obj, '__args__')

        if len(obj) == len(type_args) and isinstance(obj, tuple):
            for tuple_element, type_arg in zip(obj, type_args):

                ttype = which_subtype(type_arg)

                if ttype == 0:
                    result += isinstance(tuple_element, type_arg)
                elif ttype == -2:
                    result += 1
                else:
                    result += sub_type_result(tuple_element, type_arg, ttype)
            return result >= len(obj)
        else:
            return 0
    else:
        return isinstance(obj, type_obj)


def list_elements(obj, type_obj):
    result = 0
    tmp = 0

    if hasattr(type_obj, '__args__'):

        if matches_origin(obj, type_obj) == 0:
            return 0

        for list_element in obj:
            tmp = element_check(list_element, type_obj)
            if tmp == -2:
                return 1
            result += tmp

        return result >= len(obj)
    else:
        return isinstance(obj, type_obj)

