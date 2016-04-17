#!/usr/local/bin/python

# -*- coding: utf-8 -*-
import os
import subprocess

DIRECTORY = 'html'

print 'id, title, lock, tag, ac_rate, difficulty'

for file in os.listdir(DIRECTORY):
    if file.endswith(".html"):
        path = os.path.join(DIRECTORY, file)
        cmd = ["python", "parse.py", path]
        out, err = subprocess.Popen(
                       cmd,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE
                   ).communicate()
        print out.strip()
        if err:
            raise Exception(err)
