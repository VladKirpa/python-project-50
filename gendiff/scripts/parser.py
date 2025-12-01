import json
import yaml


def parse_format(text, format):

    if format == 'json':
        return json.loads(text)

    elif format in ['yml','yaml']:
        return yaml.safe_load(text)

    else:
        raise ValueError(f"not work with :{format}")