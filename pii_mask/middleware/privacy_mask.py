# -*- coding: utf-8 -*-
# ./greenspace/greenspace/middleware/privacy_mask.py
# Greenspace Mental Health Ltd.
# Copyright (c) 2022

import logging

from pii_mask.pii_context import hide_pii

logger = logging.getLogger(__name__)


class PrivacyMaskMiddleware:
    """
    This middleware set up the privacy-mask context for the whole request.
    By default, things are hidden.

    """

    def __init__(self, get_response):
        # One-time configuration and initialization.
        self.get_response = get_response

    def __call__(self, request):
        hide_pii()
        if self.get_response is not None:
            return self.get_response(request)
