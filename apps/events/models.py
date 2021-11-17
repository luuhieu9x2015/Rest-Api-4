from django.core.validators import MaxLengthValidator
from django.db import models
from commons.models import BaseModel


class EventModel(BaseModel):
    choice_type = (
        (1, 'Live stream event'),
        (2, 'Offline event)')
    )

    choice_is_private = (
        (1, 'Live stream event'),
        (2, 'Offline event)')
    )

    choice_is_archived = (
        (0, 'Not archived'),
        (1, 'Archived')
    )
    event_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(to='users.ClientModel',on_delete=models.CASCADE)
    type = models.SmallIntegerField(choices=choice_type)
    title = models.CharField(max_length=255)
    body = models.TextField()
    is_private = models.SmallIntegerField(choices=choice_type)
    private_key = models.CharField(max_length=255, null=True)
    is_archived = models.SmallIntegerField(choices=choice_is_archived)
    class Meta:
        db_table = 'events'

class EventAuthorizedUserModel(BaseModel):
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE)
    user_id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'event_authorized_users'

class PerformancesModel(BaseModel):
    choice_ticket_available_flag = (
        (0, 'Not available'),
        (1, 'Available')
    )
    performance_id = models.AutoField(primary_key=True)
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE)
    streaming_method = models.IntegerField(null=True)
    name =  models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    capacity = models.IntegerField(null=True)
    ticket_available_flag = models.SmallIntegerField(choices=choice_ticket_available_flag)
    class Meta:
        db_table = 'performances'
    