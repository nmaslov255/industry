command = '/home/user/industry/env/bin/gunicorn'
pythonpath = '/home/user/industry/industry'
bind = '127.0.0.1:8001'
workers = 3
user = 'user'
limit_requests_fields = 3200
limit_requests_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=industry.settings'
