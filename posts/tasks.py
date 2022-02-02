from celery import shared_task
from posts.models import FoodPost


from django.utils import timezone

@shared_task(bind=True)
def delpost(self):
    
    FoodPost.delete_post
    return "completed deleting foodpost at {}".format(timezone.now())

