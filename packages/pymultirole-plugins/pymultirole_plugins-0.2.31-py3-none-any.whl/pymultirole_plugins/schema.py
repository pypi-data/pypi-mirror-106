import json
from typing import Optional, List, Any, Dict

from pydantic import BaseModel, Field


class FormDataModel(BaseModel):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class Span(BaseModel):
    start: int = Field(..., description="Start index of the span in the text", example=5)
    end: int = Field(..., description="End index of the span in the text", example=15)


class Boundary(Span):
    name: str = Field(None, description="Name of the boundary", example="body")


class Document(BaseModel):
    text: str = Field(None, description="Plain text of the converted document")
    boundaries: Optional[Dict[str, List[Boundary]]] = Field(None, description="List of boundaries by type")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Document metadata")
