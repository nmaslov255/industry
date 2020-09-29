#!/bin/bash
source /home/user/industry/env/bin/activate
source /home/user/industry/env/bin/postactivate
exec gunicorn -c "/home/user/industry/industry/gunicorn_config.py" config.wsgi
