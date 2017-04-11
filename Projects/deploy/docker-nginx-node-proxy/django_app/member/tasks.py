import time

from django.utils import timezone

from config.celery import app
from member.models import CeleryTest


@app.task
def celery_test():
    request_at = timezone.now()
    time.sleep(1)
    CeleryTest.objects.create(request_at=request_at)
