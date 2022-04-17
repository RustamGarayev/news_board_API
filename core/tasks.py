from celery import shared_task
from core.models import NewsPost


@shared_task
def reset_post_upvote():
    NewsPost.objects.all().update(number_of_upvote=0)

    return "Upvotes reset successful"
