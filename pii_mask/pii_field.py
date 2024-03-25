# -*- coding: utf-8 -*-
from django.db.models import CharField

from .pii_context import show_pii_override
from .pii_lazy import pii_lazy


class PiiField(CharField):
    """
    Mark a field as PII to allow masking of it in unauthorized contexts.
    A model.field type "PiiField" which returns a pii_lazy maskable/unmaskable
    It is a drop-in replacement For CharField
    """

    def from_db_value(self, value, expression, connection):
        """Always return a pii_lazy."""
        return pii_lazy(value)

    def get_prep_value(self, value):
        """Unmask before saving!"""
        with show_pii_override():
            return super().get_prep_value(value)
