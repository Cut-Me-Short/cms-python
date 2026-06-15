# coding: utf-8

# flake8: noqa

"""
    CutMeShort CMS API

    Official API for the CutMeShort CMS platform.  This API allows tracking of leads and sales, including deferred lead attribution. In deferred attribution, the first lead call stores the clickId-to-customerExternalId association using `mode: deferred`. Subsequent lead events should be sent as normal events without `mode`, and the backend resolves the stored association automatically. 

    CutMeShort Python SDK
    Version: 1.0.0

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# Define package exports
__all__ = [
    "CMSClient",
    "TrackingApi",
    "ApiResponse",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "ErrorResponse",
    "LeadPayload",
    "SalePayload",
    "TrackResponse",
]

# import simplified client
from cutmeshort.client import CMSClient as CMSClient

# import apis into sdk package
from cutmeshort.api.tracking_api import TrackingApi as TrackingApi

# import ApiClient
from cutmeshort.api_response import ApiResponse as ApiResponse
from cutmeshort.api_client import ApiClient as ApiClient
from cutmeshort.configuration import Configuration as Configuration
from cutmeshort.exceptions import OpenApiException as OpenApiException
from cutmeshort.exceptions import ApiTypeError as ApiTypeError
from cutmeshort.exceptions import ApiValueError as ApiValueError
from cutmeshort.exceptions import ApiKeyError as ApiKeyError
from cutmeshort.exceptions import ApiAttributeError as ApiAttributeError
from cutmeshort.exceptions import ApiException as ApiException

# import models into sdk package
from cutmeshort.models.error_response import ErrorResponse as ErrorResponse
from cutmeshort.models.lead_payload import LeadPayload as LeadPayload
from cutmeshort.models.sale_payload import SalePayload as SalePayload
from cutmeshort.models.track_response import TrackResponse as TrackResponse

