"""
All the global special types used in the project.
"""

__all__ = ["DotDict"]


class DotDict(dict):
    """
    A dictionary that allows you to access its keys as attributes.
    """
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
