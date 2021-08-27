#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from views import app
from models import db, init_db
from schedulers import scheduler

application = app
init_db()


if len(sys.argv) >= 2:
    # 获取命令行命令
    command = sys.argv[1].lower()

    if command == 'dropdb':
        q = input('Are you sure you want to delete all database data?[Y/N]')
        if q.upper() == 'Y':
            db.drop_all()
            print('All data has been deleted.')

    elif command.lower() == 'dev':
        if len(sys.argv) == 3:
            app.run('0.0.0.0', int(sys.argv[2]))
        elif len(sys.argv) == 4:
            app.run(sys.argv[2], int(sys.argv[3]))
        else:
            app.run('0.0.0.0', 8000)

elif __name__ == '__main__':
    print('''
    Command:
        dropdb : Delete all database data.
        dev    : Start the simple web server, you can specify the listening address by args:
                 start.py dev 127.0.0.1 80

    Current default listening address is 0.0.0.0:8000

        ''')
    app.run('0.0.0.0', 8000, use_reloader=False)
