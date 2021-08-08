#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
import time

def testjob():
    time.sleep(6)
    print('Running at {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
