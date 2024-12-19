from rest_framework import serializers
from .models import MessageNotification

class MessageNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageNotification
        fields = ['sender_id', 'receiver_id', 'type', 'related_id', 'message','is_read']