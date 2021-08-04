#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime


def testjob():
    print('Running at {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
