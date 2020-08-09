import json

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import JsonLexer


def pprint_json(in_dict):
    json_object = json.loads(json.dumps(in_dict))
    json_out = json.dumps(json_object, indent=4, sort_keys=True)
    print(highlight(json_out, JsonLexer(), TerminalFormatter(style='colorful')))
