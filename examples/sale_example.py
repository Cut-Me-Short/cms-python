#!/usr/bin/env python3
"""Sale tracking example"""

import os
from cutmeshort import CMSClient

# Get Bearer token from environment
bbearer_token = "your_bearer_token_here"

# Create client
client = CMSClient(token=bearer_token)

# Track a sale
response = client.track_sale(
    click_id="click_id",
    event_name="purchase_completed",
    customer_external_id="user_42",
    invoice_id="inv_987",
    amount=4999,  # amount in cents ($49.99)
    currency="USD",
    customer_name="cutmeshort",
    customer_email="cutmeshort@cms.com",
)
print(response)
