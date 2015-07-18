import os

import redis
from rq import Worker, Queue, Connection

listen = ['default']
os.environ['APP_SETTINGS'] = 'config.DevelopmentConfig'
os.environ['DATABASE_URL'] = 'postgresql://localhost/wordcount_dev'
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')


conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()