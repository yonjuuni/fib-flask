#!/usr/bin/env python
import os
from flask_script import Manager, Shell
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG', 'default'))
manager = Manager(app)
manager.add_command("shell", Shell(make_context=lambda: {'app': app}))


if __name__ == '__main__':
    manager.run()
