from copy import deepcopy
from typing import Dict
import functools
import inspect


def create_attribute(dict_values: Dict, attribute_name, default_value):
    """create attribute from its name and a value which is either given by a dictionary
    , or taken from a default_value"""
    if attribute_name not in dict_values.keys():
        return deepcopy(default_value)
    return dict_values[attribute_name]


def init_with_deepcopy(init_to_change):
    """decorator that takes an init function and implement the behavior expected by
    the developper, aka : if no values are given, create a new copy of the default
    value instead of giving it to use"""
    @functools.wraps(init_to_change)
    def modified_init(*args, **kwargs):
        current_nb = len(args)
        copy_values: Dict = {}
        signature = inspect.signature(init_to_change)
        while current_nb < len(signature.parameters.keys()):
            attribute_name = list(signature.parameters.keys())[current_nb]
            value_to_pass = create_attribute(
              kwargs,
              attribute_name,
              signature.parameters[attribute_name].default,
            )
            copy_values[attribute_name] = value_to_pass
            current_nb += 1
        return init_to_change(*args, **copy_values)

    return modified_init
