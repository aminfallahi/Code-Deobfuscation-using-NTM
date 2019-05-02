from __future__ import absolute_import
B='application/json'
from .base import renderer as A
import json
@A('json',B,normalize=True)
def C(unrendered,**C):'\n    Renders a response using :func:`json.dumps`.\n\n    :Renderer MIME type triggers: - application/json\n    :Renderer name triggers: - json\n    ';A=unrendered;return A.rendered(json.dumps(A.response),B)