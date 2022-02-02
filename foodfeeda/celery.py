from __future__ import absolute_import,unicode_literals
import os      
from celery import  Celery
from  django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodfeeda.settings')
app =Celery('foodfeeda')
app.conf.enable_utc = False
app.conf.update(timezone ='Asia/Kolkata')
app.config_from_object(settings,namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule ={
    'del_Post':{
        'task':'posts.tasks.delpost',
        'schedule':crontab(minute=1)
    }
}



@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')