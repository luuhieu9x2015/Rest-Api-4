from django.db import models
# from apps.events.models import PerformancesModel

from commons.models import BaseModel


class TicketModel(BaseModel):
    ticket_id = models.AutoField(primary_key=True)
    perFormance = models.ForeignKey(
        to='events.PerformancesModel', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    points_required = models.IntegerField()
    expiration_datetime = models.DateTimeField()
    drawing_flag = models.BooleanField()
    drawing_application_deadline = models.DateTimeField(null=True)
    drawing_status = models.BooleanField()
    stamp_available_flag = models.BooleanField()
    max_number_of_tickets = models.IntegerField()
    number_of_issued_tickets = models.IntegerField()
    is_seat_id_assigned = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tickets'


class DrawingModel(BaseModel):
    ticket = models.ForeignKey(TicketModel, on_delete=models.CASCADE, )
    user = models.ForeignKey(to='users.UsersModel', on_delete=models.CASCADE)
    is_elected = models.BooleanField()
    is_purchased = models.BooleanField()

    class Meta:
        db_table = 'drawing'


class UserTicketModel(BaseModel):
    user_ticket_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to='users.UsersModel', on_delete=models.CASCADE)
    ticket = models.ForeignKey(TicketModel, on_delete=models.CASCADE)
    is_settled = models.BooleanField()
    seat_id = models.CharField(max_length=255, null=True)
    expires_in = models.DateTimeField()
    status = models.BooleanField()
    used_at = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.user} - {self.ticket}'

    class Meta:
        db_table = 'user_ticket'


class TicketPurchaseReservationsModel(BaseModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserTicketModel, on_delete=models.CASCADE)
    ticket = models.ForeignKey(TicketModel, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100, null=True)
    number_of_tickets = models.IntegerField()
    reserved_at = models.DateTimeField()
    is_purchased = models.BooleanField()

    class Meta:
        db_table = 'ticket_purchase_reservations'


class TicketPurchaseHistoriesModel(BaseModel):
    id = models.AutoField(primary_key=True)
    user_ticket = models.ForeignKey(UserTicketModel, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    order_id = models.CharField(max_length=100, null=True)
    payment_type = models.CharField(max_length=15, null=True)
    purchased_at = models.DateTimeField()
    settled_at = models.DateTimeField(null=True)
    receipt_number = models.CharField(max_length=32, null=True)
    haraikomi_url = models.CharField(max_length=256, null=True)

    class Meta:
        db_table = 'ticket_purchase_histories'
