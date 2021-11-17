from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from apps.events.models import PerformancesModel

from commons.models import BaseModel

class TicketModel(BaseModel):
    ticket_id = models.IntegerField(max_length=1, primary_key=True)
    perFormance_id = models.ForeignKey(PerformancesModel, max_length=1)
    name = models.CharField(max_length=255)
    price = models.DecimalField(null=True)
    points_required = models.IntegerField()
    expiration_datetime = models.DateTimeField()
    drawing_flag = models.BooleanField(max_length=1)
    drawing_application_deadline = models.DateTimeField(null=True)
    drawing_status = models.BooleanField(max_length=1)
    stamp_available_flag = models.BooleanField(max_length=1)
    max_number_of_tickets = models.IntegerField(max_length=11)
    number_of_issued_tickets = models.IntegerField(max_length=11)
    is_seat_id_assigned = models.BooleanField(max_length=1)

class DrawingModel(BaseModel):
    ticket_id = models.ForeignKey(TicketModel, max_length=11)
    user_id = models.IntegerField(max_length=11, primary_key=True)
    is_elected = models.BooleanField(max_length=1)
    is_purchased = models.BooleanField(max_length=1)

class UserTicketModel(BaseModel):
    user_ticket_id = models.IntegerField(max_length=11, primary_key=True)
    user_id = models.IntegerField(max_length=11)
    ticket_id = models.IntegerField(max_length=11)
    is_settled = models.BooleanField(max_length=1)
    seat_id = models.CharField(max_length=255, null=True)
    expires_in = models.DateTimeField()
    status = models.BooleanField(max_length=2)
    used_at = models.DateTimeField(null=True)

class TicketPurchaseReservationsModel(BaseModel):
    id = models.IntegerField(max_length=11, primary_key=True)
    user_id = models.ForeignKey(UserTicketModel, max_length=11)
    ticket_id = models.ForeignKey(TicketModel, max_length=11)
    order_id = models.CharField(max_length=100, null=True)
    number_of_tickets = models.IntegerField(max_length=11)
    reserved_at = models.DateTimeField()
    is_purchased = models.BooleanField(max_length=1)

class TicketPurchaseHistoriesModel(BaseModel):
    id = models.IntegerField(max_length=11, primary_key=True)
    user_ticket_id = models.ForeignKey(UserTicketModel, max_length=11)
    payment_amount = models.DecimalField(null=True)
    order_id = models.CharField(max_length=100, null=True)
    payment_type = models.CharField(max_length=15, null=True)
    purchased_at = models.DateTimeField()
    settled_at = models.DateTimeField(null=True)
    receipt_number = models.CharField(max_length=32, null=True)
    haraikomi_url = models.CharField(max_length=256, null=True)