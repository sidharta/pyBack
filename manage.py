#! /usr/bin/env python

import os

from flask.ext.script import Server, Manager

from py_back import create_app


app = create_app(os.getenv('PY_BACK_CONFIG', 'default'))
manager = Manager(app)
manager.add_command("runserver", Server(host='0.0.0.0', port=os.getenv('PORT', 5000)))

@manager.shell
def make_shell_context():
    return dict(app=app)

if __name__ == '__main__':
    manager.run()
