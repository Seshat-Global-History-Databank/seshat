import multiprocessing

# The socket to bind
bind = '0.0.0.0:8000'

# The number of worker processes for handling requests
workers = multiprocessing.cpu_count() * 2 + 1

# The number of worker threads for handling requests
threads = 2

# Max number of requests per worker before restarting the worker
max_requests = 1200

# The type of workers to use
worker_class = 'sync'  # or 'gevent' for async workers

# The maximum number of simultaneous clients
worker_connections = 1000

# How long to keep an idle worker running
keepalive = 2

# Logging
errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
