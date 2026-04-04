# CutMeShort CMS Python SDK

The CutMeShort Python SDK enables you to track lead and sales events in your **Python applications** with ease.

It provides a clean and simple interface for:

* Lead tracking
* Deferred lead attribution (`mode="deferred"`)
* Sale / purchase tracking

---

## Installation

### Install from PyPI (recommended)

```bash
pip install cms-python-client
```

### Install from GitHub

```bash
pip install git+https://github.com/CutMeShort/cms-python-client.git
```

---

## 📋 Requirements

* Python 3.9+

---

## Setup

Set your Bearer token:

```bash
export CMS_BEARER_TOKEN="your_jwt_token"
```

---

## ⚡ Quick Start

```python
import os
from cms_python import CMSClient

client = CMSClient(token=os.environ["CMS_BEARER_TOKEN"])

response = client.track_lead(
    click_id="id_123",
    event_name="signup_started",
    customer_external_id="user_42",
)

print(response)
```

---

## What is Deferred Attribution?

Deferred attribution allows you to track a click **before knowing the customer identity**.

### Flow:

1. **First Call (store association)**

   * Send `click_id` + `mode="deferred"`

2. **Later Calls**

   * Send normal events without `click_id`
   * Backend automatically resolves mapping

### Example Use Case

User clicks an ad → later signs up → events get linked automatically.

---

## Track a Lead Event (Standard Flow)

```python
from cms_python import CMSClient

client = CMSClient(token="your_jwt_token")

response = client.track_lead(
    click_id="id_123",
    event_name="signup_started",
    customer_external_id="user_42",
    customer_name="Jane Doe",            # optional
    customer_email="jane@example.com",   # optional
)

print(response)
```

---

## Track a Lead Event (Deferred Flow)

### Step 1: Store association

```python
response = client.track_lead(
    click_id="id_123",
    event_name="lead_captured",
    customer_external_id="user_42",
    mode="deferred",
)
```

### Step 2: Send follow-up event

```python
response = client.track_lead(
    event_name="kyc_completed",
    customer_external_id="user_42",
)
```

---

## Track a Sale Event

```python
from cms_python import CMSClient

client = CMSClient(token="your_jwt_token")

response = client.track_sale(
    click_id="id_123",
    event_name="purchase_completed",
    customer_external_id="user_42",
    invoice_id="inv_987",
    amount=4999,          # in cents
    currency="USD",       # 3-letter code
    customer_email="jane@example.com",  # optional
)

print(response)
```

---

## CMSClient Reference

### Initialization

```python
from cms_python import CMSClient

client = CMSClient(token="your_jwt_token")

# Custom base URL
client = CMSClient(token="your_jwt_token", host="https://custom.com")
```

---

## Methods

### `track_lead()`

Track a lead event.

**Required:**

* `event_name: str`
* `customer_external_id: str`

**Optional:**

* `click_id: str`
* `customer_name: str`
* `customer_email: str`
* `customer_avatar: str`
* `timestamp: datetime`
* `mode: str` (`"deferred"` only)

---

### `track_sale()`

Track a sale event.

**Required:**

* `click_id: str`
* `event_name: str`
* `customer_external_id: str`
* `invoice_id: str`
* `amount: int` (in cents)
* `currency: str` (3-letter code)

**Optional:**

* `customer_name: str`
* `customer_email: str`
* `customer_avatar: str`
* `timestamp: datetime`

---

## Response Format

All methods return a dictionary:

### Success Response

```json
{
  "success": true,
  "message": "Event tracked successfully",
  "data": {...}
}
```

### Error Response

```json
{
  "success": false,
  "error": "Validation failed",
  "status_code": 422
}
```

---

## Error Handling

Errors are handled internally by the SDK.

```python
response = client.track_lead(...)

if response.get("success"):
    print("Success:", response["data"])
else:
    print("Error:", response)
```

---

## 📊 Payload Reference

### Lead Payload

**Required:**

* `event_name`
* `customer_external_id`

**Conditionally Required:**

* `click_id` (for standard flow or deferred setup)

**Optional:**

* `timestamp`
* `customer_name`
* `customer_email`
* `customer_avatar`
* `mode` (`"deferred"` only)

---

### Sale Payload

**Required:**

* `click_id`
* `event_name`
* `customer_external_id`
* `invoice_id`
* `amount`
* `currency`

**Optional:**

* `timestamp`
* `customer_name`
* `customer_email`
* `customer_avatar`

---

## Example Scripts

- [examples/lead_example.py](examples/lead_example.py) – Lead tracking and deferred attribution
- [examples/sale_example.py](examples/sale_example.py) – Sale tracking
