# Ref:
# - https://docs.python.org/2.7/library/json.html
# - https://www.json.org/
# - https://realpython.com/python-json/

# Serializing into JSON
#   - json.dump => file
#   - json.dumps => string

#   https://docs.python.org/2.7/library/json.html#json.JSONEncoder
#   Python             |JSON
#   -------------------+-------
#   dict                object
#   list, tuple         array
#   str                 string
#   int, long, float    number
#   True                true
#   False               false
#   None                null

# Deserializing from JSON

#   https://docs.python.org/2.7/library/json.html#json.JSONDecoder
#   JSON            Python
#   ---------------+---=-----
#   object          dict
#   array           list
#   string          unicode
#   number (int)    int, long
#   number (real)   float
#   true            True
#   false           False
#   null            None


import json


data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}

print type(data)
# >>>
# <type 'dict'>

FILENAME = "data.json"

# == json.dump(obj, fp, ...) ==
# Serialize obj as a JSON formatted stream to fp (a .write()-supporting file-like object) using this conversion table.
# Returns:
#   None
with open(FILENAME, "w") as f:
    json.dump(data, f)

# >>>
# $ cat data.json
# {"lastName": "Doe", "age": 35, "children": [{"age": 6, "firstName": "Alice"}, {"age": 8, "firstName": "Bob"}], "firstName": "Jane", "hobbies": ["running", "sky diving", "singing"]}


# == json.dumps(obj, ...) ==
# Serialize obj to a JSON formatted str using this conversion table.
# Returns:
#   JSON string: (str)
json_string = json.dumps(data)

print type(json_string)
print json_string
# >>>
# <type 'str'>
# {"lastName": "Doe", "age": 35, "children": [{"age": 6, "firstName": "Alice"}, {"age": 8, "firstName": "Bob"}], "firstName": "Jane", "hobbies": ["running", "sky diving", "singing"]}


# BEAUTIFY PRINT:
print json.dumps(data, indent=4, sort_keys=True)


# NOTE: Both the dump() and dumps() methods use the same keyword arguments.


# == json.load(fp, ...) ==
# Deserialize fp (a .read()-supporting file-like object containing a JSON document) to a Python object using this conversion table.
# Returns:
#   Python data type: (type:?)
with open(FILENAME, "r") as f:
    _data = json.load(f)

print type(_data)
print _data
# >>>
# <type 'dict'>
# {u'lastName': u'Doe', u'age': 35, u'children': [{u'age': 6, u'firstName': u'Alice'}, {u'age': 8, u'firstName': u'Bob'}], u'firstName': u'Jane', u'hobbies': [u'running', u'sky diving', u'singing']}

# == json.loads(str, ...) ==
# Deserialize s (a str or unicode instance containing a JSON document) to a Python object using this conversion table.
# Returns:
#   Python data type: (type:?)
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
_data = json.loads(json_string)

print type(_data)
print _data
# >>>
# <type 'dict'>
# {u'researcher': {u'relatives': [{u'name': u'Zaphod Beeblebrox', u'species': u'Betelgeusian'}], u'name': u'Ford Prefect', u'species': u'Betelgeusian'}}
