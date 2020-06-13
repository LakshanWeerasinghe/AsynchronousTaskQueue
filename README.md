# AsynchronousTaskQueue

This application demonstrates how to implement a message queue in a Django application to run tasks in background,
which need more time and more process power and memory to complete thier tasks.


# Django 

In this application we use django to create rest apis to call these tasks.

# Celery

Celery is an asynchronous task queue/job queue based on distributed message passing. 

# RabbitMQ

RabbitMQ is used as the message broker.

## How to setup the project.

create a cloudAMPQ account and create free RabbitMQ instance. visit => `https://www.cloudamqp.com`
copy the `AMPQ URL` and paste it in the `.env` file.

create a python virtual envirnment using `python3 -m venv env` and activate it.
Then run the following commands.
1. `python manage.py runserver`
2. `celery -A message --concurrency=1 worker -l info`