from typing import Type
from pydantic import BaseModel, Field
from pymultirole_plugins.formatter import FormatterBase, FormatterParameters
from pymultirole_plugins.schema import Document
from starlette.responses import Response


class RFXmlParameters(FormatterParameters):
    encoding: str = Field("iso-8859-1", description="Encoding of the output XML file")


class RFXmlFormatter(FormatterBase):
    """Inscriptis HTML pretty converter.
    """

    def format(self, document: Document, parameters: FormatterParameters) \
            -> Response:
        """Parse the input document and return a formatted response.

        :param document: An annotated document.
        :param options: options of the parser.
        :returns: Response.
        """
        parameters: RFXmlParameters = parameters
        data = """<?xml version="1.0"?>
        <shampoo>
        <Header>
            Apply shampoo here.
        </Header>
        <Body>
            You'll have to use soap here.
        </Body>
        </shampoo>"""
        return Response(content=data, media_type="application/xml")

    @classmethod
    def get_model(cls) -> Type[BaseModel]:
        return RFXmlParameters
