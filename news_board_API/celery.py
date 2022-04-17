from __future__ import absolute_import, unicode_literals

import os

from celery.schedules import crontab
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_board_API.settings")

app = Celery("news_board_API")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))


# REDIS_CONNECTION = "{protocol}://{username}:{password}@{host}:{port}".format(
#     protocol=os.environ.get("REDIS_PROTOCOL", "redis"),
#     username=os.environ.get("REDIS_USER", ""),
#     password=os.environ.get("REDIS_PASSWORD", ""),
#     host=os.environ.get("REDIS_HOST", "localhost"),
#     port=os.environ.get("REDIS_PORT", "6379"),
# )
#
# CELERY_CONFIG = dict(
#     BROKER_URL="{redis}/0".format(redis=REDIS_CONNECTION),
#     BROKER_TRANSPORT_OPTIONS={
#         "visibility_timeout": 3600,
#         "fanout_prefix": True,
#         "fanout_patterns": True,
#     },
#     CELERYBEAT_SCHEDULER="django_celery_beat.schedulers:DatabaseScheduler",
#     # CELERY_RESULT_BACKEND='{redis}/1'.format(redis=REDIS_CONNECTION),
#     CELERY_DISABLE_RATE_LIMITS=True,
#     CELERY_IGNORE_RESULT=True,
#     CELERY_ACCEPT_CONTENT=["application/json"],
#     CELERY_TASK_SERIALIZER="json",
#     CELERY_RESULT_SERIALIZER="json",
# )
#
#
# app.conf.update(**CELERY_CONFIG)

app.conf.beat_schedule = {
    "post-upvote-reset": {
        "task": "core.tasks.reset_post_upvote",
        "schedule": crontab(
            minute="0",
            hour="0",
            day_of_month="*",
            month_of_year="*",
            day_of_week="*",
        ),
    },
}
