import logging
import logging.handlers
from logging.handlers import WatchedFileHandler
import os
import multiprocessing
bind = '127.0.0.1:8000'
backlog = 512                
chdir = './'  
timeout = 30      
worker_class = 'gevent' 

workers = multiprocessing.cpu_count() * 2 + 1    
threads = 2 
loglevel = 'info' 
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"' 
# accesslog = "./log/gunicorn_access.log"      
# errorlog = "./log/gunicorn_error.log"        