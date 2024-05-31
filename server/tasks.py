import os
from .models import Db_service

from celery import Celery


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


@celery.task(name="add_record_to_poll")
def add_record_to_poll(username, age, city, country):
    db_service = Db_service()
    db_service.add_record_to_poll(username, age, city, country)
    return db_service.get_last_record_from_poll()
