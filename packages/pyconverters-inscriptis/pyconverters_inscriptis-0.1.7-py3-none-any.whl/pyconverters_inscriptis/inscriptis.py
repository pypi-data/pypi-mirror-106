import io
from pathlib import Path
from typing import Type, List

from fastapi import UploadFile
from inscriptis import get_text
from pyconverters_plugins.base import ConverterParameters, Document, ConverterBase
from pydantic import BaseModel, Field


class InscriptisParameters(ConverterParameters):
    encoding: str = Field("utf-8", description="Encoding of the HTML file")


class InscriptisConverter(ConverterBase):
    """Inscriptis HTML pretty converter.
    """

    def convert(self, source: UploadFile, options: ConverterParameters) \
            -> List[Document]:
        """Parse the input source file and return a list of documents.

        :param source: A file object containing the data.
        :param options: options of the parser.
        :returns: Iterable producing the concepts.
        """
        if isinstance(source.file._file, io.TextIOWrapper):
            wrapper = source.file._file
        else:
            wrapper = io.TextIOWrapper(source.file._file, encoding=options.encoding)
        html = wrapper.read()
        text = get_text(html)
        doc = Document(text=text)
        return [doc]

    @classmethod
    def get_model(cls) -> Type[BaseModel]:
        return InscriptisParameters
