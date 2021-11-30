from __future__ import absolute_import, unicode_literals
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


from app.tasks import getPriceBtc

from celery import Celery
app = Celery("core")

app.conf.enable_utc = False

app.conf.update(timezone='Asia/kolkata')

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    'add-every-3600-seconds': {
        'task': 'app.tasks.getPriceBtc',
        'schedule': 3600,  # executes every one minute
    },
}
#app.conf.timezone = 'UTC'
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')