# coding: utf-8

"""
    CutMeShort CMS API

    Official API for the CutMeShort CMS platform.  This API allows tracking of leads and sales, including deferred lead attribution. In deferred attribution, the first lead call stores the clickId-to-customerExternalId association using `mode: deferred`. Subsequent lead events should be sent as normal events without `mode`, and the backend resolves the stored association automatically. 

    CutMeShort Python SDK
    Version: 1.0.0

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class SalePayload(BaseModel):
    """
    SalePayload
    """ # noqa: E501
    click_id: StrictStr = Field(alias="clickId")
    event_name: StrictStr = Field(alias="eventName")
    timestamp: Optional[datetime] = Field(default=None, description="ISO 8601 timestamp.")
    customer_external_id: StrictStr = Field(alias="customerExternalId")
    customer_name: Optional[StrictStr] = Field(default=None, alias="customerName")
    customer_email: Optional[StrictStr] = Field(default=None, alias="customerEmail")
    customer_avatar: Optional[StrictStr] = Field(default=None, alias="customerAvatar")
    invoice_id: StrictStr = Field(alias="invoiceId")
    amount: Union[StrictFloat, StrictInt] = Field(description="Amount in cents.")
    currency: Annotated[str, Field(min_length=3, strict=True, max_length=3)] = Field(description="3-letter currency code.")
    __properties: ClassVar[List[str]] = ["clickId", "eventName", "timestamp", "customerExternalId", "customerName", "customerEmail", "customerAvatar", "invoiceId", "amount", "currency"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SalePayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SalePayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clickId": obj.get("clickId"),
            "eventName": obj.get("eventName"),
            "timestamp": obj.get("timestamp"),
            "customerExternalId": obj.get("customerExternalId"),
            "customerName": obj.get("customerName"),
            "customerEmail": obj.get("customerEmail"),
            "customerAvatar": obj.get("customerAvatar"),
            "invoiceId": obj.get("invoiceId"),
            "amount": obj.get("amount"),
            "currency": obj.get("currency")
        })
        return _obj


