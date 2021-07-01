#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from flask import render_template


def CreateQuotaPDF():
    return render_template('create_quota_pdf.html', info='''abc
axd
  fdafdsa
afdfa
    ''')
