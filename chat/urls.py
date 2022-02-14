from django.urls import path
from chat import views
urlpatterns = [
    # URL form : "/api/messages/1/2"
    # For GET request.
    path('messages/<int:sender>/<int:receiver>',
         views.message_list, name='message-detail'),
    # URL form : "/api/messages/"
    path('messages/', views.message_list,
         name='message-list'),
]
