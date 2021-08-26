#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from urllib.request import urlopen

try:
    urlopen('http://localhost:8080')
    print('Server status is OK.')
    sys.exit(0)
except Exception as e:
    print(e)
    sys.exit(1)
