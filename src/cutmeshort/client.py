# coding: utf-8

"""
Simplified CMS Client wrapper for easy lead and sale tracking
"""

from typing import Optional
from datetime import datetime

from cutmeshort.configuration import Configuration
from cutmeshort.api_client import ApiClient
from cutmeshort.api.tracking_api import TrackingApi
from cutmeshort.models.lead_payload import LeadPayload
from cutmeshort.models.sale_payload import SalePayload
from cutmeshort.exceptions import ApiException


class CMSClient:
    def __init__(self, token: str, host: str = "https://app.cme.sh"):
        configuration = Configuration(
            access_token=token,
            host=host,
        )
        configuration.timeout = 5

        self.api_client = ApiClient(configuration)
        self._tracking = TrackingApi(self.api_client)

    def track_lead(self, event_name: str, customer_external_id: str, **kwargs) -> dict:
        if not event_name:
            raise ValueError("event_name is required")
        if not customer_external_id:
            raise ValueError("customer_external_id is required")

        try:
            payload = LeadPayload(
                event_name=event_name,
                customer_external_id=customer_external_id,
                **kwargs
            )
            response = self._tracking.track_lead(payload)
            return response.data
        except ApiException as e:
            return {
                "success": False,
                "error": e.body,
                "status_code": e.status
            }

    def track_sale(self, event_name: str, customer_external_id: str, invoice_id: str, amount: int, currency: str, click_id: Optional[str] = None, **kwargs) -> dict:
        try:
            payload = SalePayload(
                click_id=click_id,
                event_name=event_name,
                customer_external_id=customer_external_id,
                invoice_id=invoice_id,
                amount=amount,
                currency=currency,
                **kwargs
            )
            response = self._tracking.track_sale(payload)
            return response.data
        except ApiException as e:
            return {
                "success": False,
                "error": e.body,
                "status_code": e.status
            }

    def close(self):
        self.api_client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
    """
    Simplified client for tracking leads and sales.
    
    Example:
        client = CMSClient(token="your-jwt-token")
        client.track_lead(
            click_id="id_123",
            event_name="signup_started",
            customer_external_id="user_42",
        )
    """
    
    def __init__(self, token: str, host: str = "https://app.cme.sh"):
        """
        Initialize the CMS client.
        
        Args:
            token: Bearer JWT token for authentication
            host: Base URL (default: https://app.cme.sh)
        """
        configuration = Configuration(
            access_token=token,
            host=host,
        )
        self.api_client = ApiClient(configuration)
        self.tracking_api = TrackingApi(self.api_client)
    
    def track_lead(
        self,
        event_name: str,
        customer_external_id: str,
        click_id: Optional[str] = None,
        customer_name: Optional[str] = None,
        customer_email: Optional[str] = None,
        customer_avatar: Optional[str] = None,
        timestamp: Optional[datetime] = None,
        mode: Optional[str] = None,
    ) -> dict:
        """
        Track a lead event.
        
        Args:
            event_name: Name of the lead event (required)
            customer_external_id: Your unique customer ID (required)
            click_id: Click ID from the campaign (required for standard flow)
            customer_name: Customer's name (optional)
            customer_email: Customer's email (optional)
            customer_avatar: Customer's avatar URL (optional)
            timestamp: ISO 8601 timestamp (optional)
            mode: Set to "deferred" for deferred attribution (optional)
        
        Returns:
            dict: {"status": bool, "data": str}
        
        Raises:
            ApiException: If the API request fails
        """
        payload = LeadPayload(
            click_id=click_id,
            event_name=event_name,
            customer_external_id=customer_external_id,
            customer_name=customer_name,
            customer_email=customer_email,
            customer_avatar=customer_avatar,
            timestamp=timestamp,
            mode=mode,
        )
        
        response = self.tracking_api.track_lead(payload)
        return {"status": response.status, "data": response.data}
    
    def track_sale(
        self,
        event_name: str,
        customer_external_id: str,
        invoice_id: str,
        amount: int,
        currency: str,
        click_id: Optional[str] = None,
        customer_name: Optional[str] = None,
        customer_email: Optional[str] = None,
        customer_avatar: Optional[str] = None,
        timestamp: Optional[datetime] = None,
    ) -> dict:
        """
        Track a sale/purchase event.
        
        Args:
            click_id: Click ID from the campaign (optional if attribution is resolved via prior deferred lead)
            event_name: Name of the sale event (required)
            customer_external_id: Your unique customer ID (required)
            invoice_id: Invoice ID (required)
            amount: Amount in cents (required)
            currency: 3-letter currency code like USD, EUR (required)
            customer_name: Customer's name (optional)
            customer_email: Customer's email (optional)
            customer_avatar: Customer's avatar URL (optional)
            timestamp: ISO 8601 timestamp (optional)
        
        Returns:
            dict: {"status": bool, "data": str}
        
        Raises:
            ApiException: If the API request fails
        """
        payload = SalePayload(
            click_id=click_id,
            event_name=event_name,
            customer_external_id=customer_external_id,
            invoice_id=invoice_id,
            amount=amount,
            currency=currency,
            customer_name=customer_name,
            customer_email=customer_email,
            customer_avatar=customer_avatar,
            timestamp=timestamp,
        )
        
        response = self.tracking_api.track_sale(payload)
        return {"status": response.status, "data": response.data}
    
    def close(self):
        """Close the API client connection"""
        self.api_client.close()
