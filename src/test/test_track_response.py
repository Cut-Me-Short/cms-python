# coding: utf-8

"""
    CutMeShort CMS API

    Official API for the CutMeShort CMS platform.  This API allows tracking of leads and sales, including deferred lead attribution. In deferred attribution, the first lead call stores the clickId-to-customerExternalId association using `mode: deferred`. Subsequent lead events should be sent as normal events without `mode`, and the backend resolves the stored association automatically. 

    CutMeShort Python SDK
    Version: 1.0.0

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cutmeshort.models.track_response import TrackResponse

class TestTrackResponse(unittest.TestCase):
    """TrackResponse model tests"""

    def test_track_response_json_roundtrip(self):
        model = TrackResponse(status=True, data="successful")
        raw = model.to_json()
        loaded = TrackResponse.from_json(raw)
        self.assertTrue(loaded.status)
        self.assertEqual(loaded.data, "successful")

if __name__ == '__main__':
    unittest.main()
