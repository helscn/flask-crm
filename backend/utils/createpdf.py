#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from flask import render_template


def CreateQuotationPDF():
    return render_template('create_quotation.html', info='''abc
axd
  fdafdsa
afdfa
    ''')
