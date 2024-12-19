from django.urls import path
from .views import MessageSender
# create your vỉew here
urlpatterns = [
    path("message-sender", MessageSender.as_view(), name="message-sender"),
]
