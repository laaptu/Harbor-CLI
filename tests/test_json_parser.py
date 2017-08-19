import json
from lib.utils.json_parser import json_parse

def test_json_parser():
    with open('package.json', 'w') as f:
        json.dump({ 'name': 'Harbor'}, f)

    data = json_parse('package.json')

    assert data['name'] == 'Harbor'

