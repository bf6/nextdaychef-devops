import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
accesslog = "/home/ubuntu/log/gunicorn/gunicorn_access.log"
errorlog = "/home/ubuntu/log/gunicorn/gunicorn_error.log"
capture_output = True
user = "ubuntu"
group = "ubuntu"
bind = "unix:/tmp/gunicorn.sock"
