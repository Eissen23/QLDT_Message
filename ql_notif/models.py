from django.db import models

# Create your models here.
class MessageNotification(models.Model):
    message_id = models.CharField(primary_key=True, max_length=8)
    sender_id = models.IntegerField()
    receiver_id = models.IntegerField()
    type = models.CharField(max_length=45, blank=True, null=True)
    related_id = models.IntegerField(blank=True, null=True)
    message = models.CharField(max_length=100, blank=True, null=True)
    is_read = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message_notification'