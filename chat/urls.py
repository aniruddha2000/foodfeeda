from django.urls import path
from chat import views
urlpatterns = [
    path('messages/<int:sender>/<int:receiver>',
         views.message_list, name='message-detail'),
    path('messages/', views.message_list,
         name='message-list'),
]
