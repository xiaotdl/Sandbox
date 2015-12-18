import json
import unittest

IGNORE = ['generation', 'kind', 'lastUpdateMicros', 'selfLink']
def ordered(data):
    if isinstance(data, dict):
        return sorted((k, ordered(v)) for k, v in data.items() if k not in IGNORE)
    elif isinstance(data, list):
        return sorted(ordered(x) for x in data)
    else:
        return data

def _dump(data):
    return json.dumps(data, indent=4)

nested_data1 = {"items":[{'name': 'Apple', 'age': '11', "kind": 'xxx'}, {'name': 'Google', 'age': '21', "kind": 'yyy'}],"generation":4,"lastUpdateMicros":0,"kind":"abc","selfLink":"https://localhost/def"}
nested_data2 = {"items":[{'name': 'Apple', 'age': '11', "kind": 'diffkind'}, {'name': 'Google', 'age': '21', "kind": 'yyy'}],"generation":4,"lastUpdateMicros":0,"kind":"abc","selfLink":"what's this?"}
print _dump(ordered(nested_data1))
print nested_data1 == nested_data2

print ordered(nested_data1) == ordered(nested_data2)

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(nested_data1, nested_data2)

if __name__ == '__main__':
    unittest.main()
