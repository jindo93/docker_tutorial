FROM python:3.7
ADD requirements.txt /app/requirements.txt
ADD ./test_celery/ /app/
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT celery -A test_celery worker --concurrency=20 --loglevel=info
