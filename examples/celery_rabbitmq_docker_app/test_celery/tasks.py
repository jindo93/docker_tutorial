from __future__ import absolute_import
from test_celery.celery import app
import time
import requests


@app.task(bind=True, default_retry_delay=10)
def longtime_add(self, i):
    print('long time task begins')
    try:
        r = requests.get(i)
        print('status: ', r.status_code, "create_time: ", time.time())
        print('\n long time task finished')
    except Exception as exc:
        raise self.retry(exc=exc)
    return r.status_code
