#!/usr/bin/env python3
"""Lead tracking example"""

import os
from cms_python import CMSClient

bearer_token = "your_bearer_token"

client = CMSClient(token=bearer_token)

# Standard lead
response = client.track_lead(
    click_id="5e6e1650-5641-4a2b-bec6-218288a86dbf",
    event_name="signup_started",
    customer_external_id="user_42",
    customer_name="cutmeshort",
    customer_email="cutmeshort@cms.com",
)

print(response)

# Deferred setup
response = client.track_lead(
    click_id="5e6e1650-5641-4a2b-bec6-218288a86dbf",
    event_name="lead_captured",
    customer_external_id="user_72",
    customer_name="cutmeshort",
    customer_email="cutmeshort@cms.com",
    mode="deferred",
)

print(response)

# Follow-up event
response = client.track_lead(
    event_name="kyc_completed",
    customer_external_id="user_72",
)

print(response)
