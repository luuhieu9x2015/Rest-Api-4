from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey
from apps.events.models import PerformancesModel
from apps.users.models import ClientModel, UsersModel

from commons.models import BaseModel


class PointsPackagesModel(BaseModel):
    points_package_id = models.IntegerField(max_length=11, primary_key=True)
    client_id = models.ForeignKey(ClientModel, max_length=11)
    apple_product_id = models.CharField(max_length=255, null=True)
    google_product_id = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField()
    points = models.DecimalField()
    display_order = models.BooleanField(max_length=2)

    class Meta:
        db_table = 'points_packages'


class UserPointsModel(BaseModel):
    user_point_id = models.IntegerField(max_length=11, primary_key=True)
    user_id = models.ForeignKey(UsersModel, max_length=11)
    type = models.BooleanField(max_length=2)
    deposit_reason = models.BooleanField(max_length=2, null=True)
    withdrawal_reason = models.BooleanField(max_length=2, null=True)
    points = models.DecimalField()
    transacted_at = models.DateTimeField()
    points_balance = models.DecimalField()

    class Meta:
        db_table = 'user_points'


class PointsPackagePurchaseHistoriesModel(BaseModel):
    id = models.IntegerField(max_length=11, primary_key=True)
    user_point_id = models.ForeignKey(UserPointsModel, max_length=11)
    points_package_id = models.ForeignKey(PointsPackagesModel, max_length=11)
    payment_amount = models.DecimalField()
    purchased_at = models.DateTimeField()
    apple_tans_id = models.CharField(max_length=255, null=True)
    google_trans_id = models.CharField(max_length=255, null=True)
    apple_receipt = models.TextField(null=True)
    google_receipt = models.TextField(null=True)

    class Meta:
        db_table = 'point_package_purchase_histories'


class PointSpendingHistoriesModel(BaseModel):
    id = models.IntegerField(max_length=11, primary_key=True)
    user_point_id = models.ForeignKey(UserPointsModel, max_length=11)
    # ? user_gift_id = models.ForeignKey(UserGiftsModel, max_length=11)
    spent_at = models.DateTimeField()

    class Meta:
        db_table = 'point_spending_histories'


class GiftsModel(BaseModel):
    gift_id = models.IntegerField(max_length=11, primary_key=True)
    client_id = models.ForeignKey(ClientModel, max_length=11)
    name = models.CharField(max_length=255)
    points_spent = models.DecimalField()
    image_url = models.CharField(max_length=255)
    display_order = models.BooleanField(max_length=2)

    class Meta:
        db_table = 'gifts'


class UserGiftsModel(BaseModel):
    user_gift_id = models.IntegerField(max_length=11, primary_key=True)
    user_id = models.ForeignKey(UsersModel, max_length=11)
    gift_id = models.ForeignKey(GiftsModel, max_length=11)
    status = models.BooleanField(max_length=2)
    used_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'user_gift'


class GiftPurchaseHistories(BaseModel):
    id = models.IntegerField(max_length=11, primary_key=True)
    user_gift_id = models.ForeignKey(UserGiftsModel, max_length=11)
    user_point_id = models.ForeignKey(UserPointsModel, max_length=11)
    points_spent = models.DecimalField()
    purchased_at = models.DateTimeField()

    class Meta:
        db_table = 'gift_purchase_histories'


class GiftTippingHistories(BaseModel):
    id = models.IntegerField(max_length=11, primary_key=True)
    user_gift_id = models.ForeignKey(UserGiftsModel, max_length=11)
    to_user_id = models.ForeignKey()
    points_equivalent = models.DecimalField()
    tipped_at = models.DateTimeField()

    class Meta:
        db_table = 'gift_tipping_histories'


class Follows(BaseModel):
    from_user_id = models.IntegerField(max_length=11, primary_key=True)
    to_user_id = models.IntegerField(max_length=11)

    class Meta:
        db_table = 'follows'


class StampCodesModel(BaseModel):
    stamp_code_id = models.IntegerField(max_length=11, primary_key=True)
    client_id = models.ForeignKey(ClientModel, max_length=11)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    stamps_granted = models.DecimalField()
    number_of_applicable_users = models.IntegerField(max_length=11, null=True)
    number_of_applied_users = models.IntegerField(max_length=11)
    expires_in = models.DateTimeField()

    class Meta:
        db_table = 'stamp_code'


class UserStampsModel(BaseModel):
    user_stamp_id = models.IntegerField(max_length=11, primary_key=True)
    user_id = models.ForeignKey(UsersModel, max_length=11)
    type = models.BooleanField(max_length=2)
    deposit_reason = models.BooleanField(max_length=2, null=True)
    withdrawal_reason = models.BooleanField(max_length=2, null=True)
    stamps = models.DecimalField()
    transacted_at = models.DateTimeField()
    stamps_balance = models.DecimalField()

    class Meta:
        db_table = 'user_stamps'


class StampReceiptHistoriesModel(BaseModel):
    id = models.IntegerField(max_length=11, primary_key=True)
    user_stamp_id = models.ForeignKey(UserStampsModel, max_length=11)
    live_stream_id = models.IntegerField(max_length=11, null=True)
    stamp_code_id = models.IntegerField(max_length=11, null=True)
    received_at = models.DateTimeField()

    class Meta:
        db_table = 'stamp_receipt_histories'


class StampSpendingHistoriesModel(BaseModel):
    id = models.IntegerField(max_length=11, primary_key=True)
    user_stamp_id = models.ForeignKey(UserStampsModel, max_length=11)
    spent_for = models.BooleanField(max_length=2)
    spent_at = models.DateTimeField()

    class Meta:
        db_table = 'stamp_spending_histories'


class RankingsModel(BaseModel):
    ranking_id = models.IntegerField(max_length=11, primary_key=True)
    client_id = models.ForeignKey(ClientModel, max_length=11)
    type = models.BooleanField(max_length=2)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        db_table = 'rankings'
