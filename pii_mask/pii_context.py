# -*- coding: utf-8 -*-
from contextlib import ContextDecorator
from enum import Enum

from asgiref.local import Local

_default = "show"
_active = Local()
_active.value = _default


class PrivacyControl(Enum):
    """
    Enum for the privacy levels.
    """

    show = "show"
    hide = "hide"


def hide_pii():
    """Set the current context to 'hide'."""
    set_mask_level(PrivacyControl.hide)


def should_show_pii() -> bool:
    return str(get_mask_level()) == str(PrivacyControl.show)


def show_pii():
    """Set the current context to 'show'."""
    set_mask_level(PrivacyControl.show)


def set_mask_level(level: PrivacyControl):
    _active.value = str(level)


def get_mask_level() -> PrivacyControl:
    return _active.value


def reset_mask_level():
    _active.value = _default


class show_pii_override(ContextDecorator):
    """
    Temporarily override the current context to unmask all PII.
    For example, when saving to a db, we want to save the full data.

    Usage:
    ```
    with show_pii_override():
        save()
    ```
    """

    def __enter__(self):
        self.old_level = get_mask_level()
        show_pii()

    def __exit__(self, exc_type, exc_value, traceback):
        set_mask_level(self.old_level)
