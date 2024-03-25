# -*- coding: utf-8 -*-
from django.utils.functional import lazy

from .pii_context import should_show_pii


def obfuscate(message: str):
    return " ".join(["*" * len(word) for word in message.split(" ")])


def pii_mask(message: str):
    if should_show_pii():
        return message
    return obfuscate(message)


pii_lazy = lazy(pii_mask, str)
"""
	`pii_lazy` is a lazy-evaluated callable wrapper over a string
    Results are not memoized; the function is evaluated on every access.
    If the thread-global context is 'hide' it returns an obfuscated string.
    If the thread-global context is 'show' it returns the original string.


"""
