#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
from main import scheduler


def job(arg):
    print(datetime.now(), arg)
