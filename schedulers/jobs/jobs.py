#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime


def testjob():
    a = 1/0
    print('Running at {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
