#!/usr/bin/env python3
"""Sale tracking example"""

import os
from cms_python import CMSClient

# Get Bearer token from environment
bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI2OTg3NTZiZGU3NTExNmU3YWMzZjVlNGQiLCJlbWFpbCI6InZpZ25lc2hyZWRkeTc5M0BnbWFpbC5jb20iLCJpYXQiOjE3NzMyMzI5ODUsImV4cCI6MTc4MTAwODk4NX0.22naMhoaQ19TkcB61kmvsXYj1kXEUrnCWoJvt-e55Pc"

# Create client
client = CMSClient(token=bearer_token, host="http://localhost:5000")
# For custom base URL: client = CMSClient(token=bearer_token)

    # Track a sale
response = client.track_sale(
    click_id="8ea29346-1ef3-4dca-b472-1a1086998738",
    event_name="purchase_completed",
    customer_external_id="user_42",
    invoice_id="inv_987",
    amount=4999,  # amount in cents ($49.99)
    currency="USD",
    customer_name="cutmeshort",
    customer_email="cutmeshort@cms.com",
)
print(response)
