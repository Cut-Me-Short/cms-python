# coding: utf-8

# flake8: noqa
"""
    CutMeShort CMS API

    Official API for the CutMeShort CMS platform.  This API allows tracking of leads and sales, including deferred lead attribution. In deferred attribution, the first lead call stores the clickId-to-customerExternalId association using `mode: deferred`. Subsequent lead events should be sent as normal events without `mode`, and the backend resolves the stored association automatically. 

    CutMeShort Python SDK
    Version: 1.0.0

    Do not edit the class manually.
"""  # noqa: E501

# import models into model package
from cms_python.models.error_response import ErrorResponse
from cms_python.models.lead_payload import LeadPayload
from cms_python.models.sale_payload import SalePayload
from cms_python.models.track_response import TrackResponse

