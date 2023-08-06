import json
from pathlib import Path

from starlette.responses import Response

from pyformatters_xml_rf.xml_rf import RFXmlFormatter, RFXmlParameters
from pymultirole_plugins.schema import Document


def test_xml_rf():
    testdir = Path(__file__).parent
    source = Path(testdir, 'data/test.json')
    with source.open("r") as fin:
        doc = Document.construct(**json.load(fin))
        formatter = RFXmlFormatter()
        options = RFXmlParameters(encoding="iso-8859-1")
        resp: Response = formatter.format(doc, options)
        assert resp.status_code == 200
        assert resp.media_type == "application/xml"
