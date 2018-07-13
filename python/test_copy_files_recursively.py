#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import glob
import shutil


"""
/a
└── b
    └── c
        ├── d
        │   ├── 1.gcda
        │   └── 1.gcno
        ├── e
        │   ├── 2.gcda
        │   └── 2.gcno
        └── f
            ├── 3.gcda
            └── 3.gcno
"""


def recursively_copy_files(src, dst, override=False, file_pattern=None):
    # print "copying %s => %s" % (src, dst)

    if not os.path.exists(dst):
        os.mkdir(dst)

    _fs = glob.glob(src + "/*")
    for _from in _fs:
        if os.path.isdir(_from): # dir
            _to = os.path.join(dst, _from.split('/')[-1])
            recursively_copy_files(_from, _to, override, file_pattern)
        else: # file
            if file_pattern and not re.search(file_pattern, _from):
                continue
            _to = os.path.join(dst, _from.split('/')[-1])
            if not os.path.exists(_to) or override:
                shutil.copyfile(_from, _to)


recursively_copy_files("/a", "/tmp/test", override=True, file_pattern="\.gcno$")
recursively_copy_files("/a", "/tmp/test", override=True, file_pattern="\.gcda$")


os.system("tree /a")
os.system("tree /tmp/test")
