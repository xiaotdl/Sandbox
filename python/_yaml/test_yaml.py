#!/usr/bin/env python

import yaml

with open("example.yaml", 'r') as f:
    try:
        print(yaml.load(f))
    except yaml.YAMLError as e:
        print("ERROR: %s" % e)
