"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count


def max_workers():    
    return cpu_count()

worker_class = 'gevent'
workers = max_workers()

accesslog = 'api.log'
errorlog = 'api.error.log'
capture_output = True
bind = "0.0.0.0:80"
timeout = 60