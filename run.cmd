@echo off
gunicorn start:app -c gunicorn.conf.py
