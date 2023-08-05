import io
from typing import Type, List

from fastapi import UploadFile
from inscriptis import get_text
from pydantic import BaseModel, Field
from pymultirole_plugins.converter import ConverterParameters, ConverterBase
from pymultirole_plugins.schema import Document


class InscriptisParameters(ConverterParameters):
    encoding: str = Field("utf-8", description="Encoding of the HTML file")


class InscriptisConverter(ConverterBase):
    """Inscriptis HTML pretty converter.
    """

    def convert(self, source: UploadFile, parameters: ConverterParameters) \
            -> List[Document]:
        """Parse the input source file and return a list of documents.

        :param source: A file object containing the data.
        :param parameters: options of the converter.
        :returns: List of converted documents.
        """
        parameters : InscriptisParameters = parameters
        if isinstance(source.file._file, io.TextIOWrapper):
            wrapper = source.file._file
        else:
            wrapper = io.TextIOWrapper(source.file._file, encoding=parameters.encoding)
        html = wrapper.read()
        text = get_text(html)
        doc = Document(text=text)
        return [doc]

    @classmethod
    def get_model(cls) -> Type[BaseModel]:
        return InscriptisParameters
