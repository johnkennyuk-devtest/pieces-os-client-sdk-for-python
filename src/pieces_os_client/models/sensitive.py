# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from pieces_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_client.models.flattened_asset import FlattenedAsset
from pieces_client.models.grouped_timestamp import GroupedTimestamp
from pieces_client.models.mechanism_enum import MechanismEnum
from pieces_client.models.score import Score
from pieces_client.models.sensitive_category_enum import SensitiveCategoryEnum
from pieces_client.models.sensitive_metadata import SensitiveMetadata
from pieces_client.models.sensitive_severity_enum import SensitiveSeverityEnum

class Sensitive(BaseModel):
    """
    This is a fully referenced representation of a sensitive pieces of data.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    id: StrictStr = Field(...)
    created: GroupedTimestamp = Field(...)
    updated: GroupedTimestamp = Field(...)
    deleted: Optional[GroupedTimestamp] = None
    asset: FlattenedAsset = Field(...)
    text: StrictStr = Field(...)
    mechanism: MechanismEnum = Field(...)
    category: SensitiveCategoryEnum = Field(...)
    severity: SensitiveSeverityEnum = Field(...)
    name: StrictStr = Field(...)
    description: StrictStr = Field(...)
    metadata: Optional[SensitiveMetadata] = None
    interactions: Optional[StrictInt] = Field(None, description="This is an optional value that will keep track of the number of times this has been interacted with.")
    score: Optional[Score] = None
    __properties = ["schema", "id", "created", "updated", "deleted", "asset", "text", "mechanism", "category", "severity", "name", "description", "metadata", "interactions", "score"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Sensitive:
        """Create an instance of Sensitive from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated
        if self.updated:
            _dict['updated'] = self.updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deleted
        if self.deleted:
            _dict['deleted'] = self.deleted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of asset
        if self.asset:
            _dict['asset'] = self.asset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of score
        if self.score:
            _dict['score'] = self.score.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Sensitive:
        """Create an instance of Sensitive from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Sensitive.parse_obj(obj)

        _obj = Sensitive.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "id": obj.get("id"),
            "created": GroupedTimestamp.from_dict(obj.get("created")) if obj.get("created") is not None else None,
            "updated": GroupedTimestamp.from_dict(obj.get("updated")) if obj.get("updated") is not None else None,
            "deleted": GroupedTimestamp.from_dict(obj.get("deleted")) if obj.get("deleted") is not None else None,
            "asset": FlattenedAsset.from_dict(obj.get("asset")) if obj.get("asset") is not None else None,
            "text": obj.get("text"),
            "mechanism": obj.get("mechanism"),
            "category": obj.get("category"),
            "severity": obj.get("severity"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "metadata": SensitiveMetadata.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "interactions": obj.get("interactions"),
            "score": Score.from_dict(obj.get("score")) if obj.get("score") is not None else None
        })
        return _obj

