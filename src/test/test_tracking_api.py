# coding: utf-8

"""
    CutMeShort CMS API

    Official API for the CutMeShort CMS platform.  This API allows tracking of leads and sales, including deferred lead attribution. In deferred attribution, the first lead call stores the clickId-to-customerExternalId association using `mode: deferred`. Subsequent lead events should be sent as normal events without `mode`, and the backend resolves the stored association automatically. 

    CutMeShort Python SDK
    Version: 1.0.0

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cutmeshort.api_client import ApiClient
from cutmeshort.configuration import Configuration
from cutmeshort.api.tracking_api import TrackingApi
from cutmeshort.models.lead_payload import LeadPayload


class _DummyRestClient:
    def __init__(self):
        self.last_timeout = None

    def request(self, method, url, headers=None, body=None, post_params=None, _request_timeout=None):
        self.last_timeout = _request_timeout
        return "ok"


class TestTrackingApi(unittest.TestCase):
    """TrackingApi unit tests"""

    def test_track_lead_serialize_applies_bearer_header(self) -> None:
        config = Configuration(access_token="token-123")
        api = TrackingApi(ApiClient(config))
        payload = LeadPayload(event_name="signup_started", customer_external_id="user_42")

        method, url, headers, body, post_params = api._track_lead_serialize(
            lead_payload=payload,
            _request_auth=None,
            _content_type=None,
            _headers=None,
            _host_index=0,
        )
        self.assertEqual(method, "POST")
        self.assertTrue(url.endswith("/track/lead"))
        self.assertEqual(headers["Authorization"], "Bearer token-123")
        self.assertEqual(headers["Content-Type"], "application/json")
        self.assertIsNotNone(body)
        self.assertEqual(post_params, [])

    def test_api_client_uses_default_timeout_when_not_provided(self) -> None:
        config = Configuration()
        config.request_timeout = (1, 2)
        api_client = ApiClient(config)
        dummy = _DummyRestClient()
        api_client.rest_client = dummy

        result = api_client.call_api("GET", "https://www.cutmeshort.com/ping")
        self.assertEqual(result, "ok")
        self.assertEqual(dummy.last_timeout, (1, 2))


if __name__ == '__main__':
    unittest.main()
