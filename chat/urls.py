from django.urls import path

# from chat.views import message_list, message_list_receiver
from chat.views import MessageListByReceiver, MessegeList

urlpatterns = [
    path('messages/<int:sender>/<int:receiver>/',
         MessegeList.as_view(), name='message-detail'),
    path('messages/<int:receiver>/', MessageListByReceiver.as_view(),
         name='message-detail-receiver'),
    path('messages/', MessegeList.as_view(), name='message-list'),
]
