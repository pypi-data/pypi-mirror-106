import abc
import json
from pathlib import Path
from typing import Optional, Dict, Any, Type, List

from fastapi import UploadFile
from pydantic import BaseModel, Field

from pymultirole_plugins.schema import FormDataModel, Document


class FormatterParameters(FormDataModel):
    foo: str = Field("foo", description="Foo")
    bar: int = Field(0, description="Bar")


class FormatterBase(metaclass=abc.ABCMeta):
    """Base class for example plugin used in the tutorial.
    """

    def __init__(self):
        pass

    @abc.abstractmethod
    def format(self, source: UploadFile, options: FormatterParameters) \
            -> List[Document]:
        """Parse the input source file and return a list of documents.

        :param source: A file object containing the data.
        :param options: options of the parser.
        :returns: Iterable producing the concepts.
        """

    @classmethod
    def get_model(cls) -> Type[BaseModel]:
        return FormatterParameters

