from typing import Callable, Dict, Type, Any, Optional, TypeVar

DEFAULT = "default"
T = TypeVar('T')


def switch_case(unknown_type_object: object, all_cases: Dict[Optional[Type], Callable[[Any],
                                                                                      T]]) -> T:
    """This method will call the method given in all_cases that corresponds to the type of
    unknown_type_object and return the result. All the methods given must take exactly one
    parameters, which will be unknown_type_object"""
    for current_type in list(all_cases.keys()):
        if current_type is not None:
            if isinstance(unknown_type_object, current_type):
                return all_cases[current_type](unknown_type_object)
    return all_cases[None](unknown_type_object)

