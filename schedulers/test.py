#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
from main import scheduler


def job(arg):
    import time
    time.sleep(4)
    print('Running job.')
