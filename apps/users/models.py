from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.models.query import prefetch_related_objects
# from apps.events.models import EventModel
from commons.models import BaseModel
from django.contrib.auth.models import AbstractUser


class ClientModel(BaseModel):
    choice_archived = (
        (0, 'Not archived'),
        (1, 'Archived')
    )
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=255)
    seconds_delivered_per_month = models.DecimalField(max_digits=15, decimal_places=0)
    is_archived = models.SmallIntegerField(choices=choice_archived)
    class Meta:
        db_table = 'clients'

    def __str__(self):
        return self.client_name

# class UsersModel(AbstractUser):

#     choice_user = (
#         (1, 'General user'),
#         (2, 'Host user')
#     )
#     choice_login = (
#         ('email', 'EMAIL'),
#         ('insta', 'INSTAGRAM'),
#         ('facebook', 'FACEBOOK'),
#         ('twitter', 'TWITTER')
#     )
#     choice_sex = (
#         (0, 'Not known'),
#         (1, 'Male'),
#         (2, 'Female'),
#         (9, 'Not applicable')
#     )
#     choice_sex_public = (
#         (0, 'Private'),
#         (1, 'Public')
#     )

#     choice_is_date_of_birth_public = (
#         (0, 'Private'),
#         (1, 'Public')
#     )
#     choice_user_type = (
#         (1, 'Individual'),
#         (2, 'Group')
#     )
#     choice_is_authenticated = (
#         (0, 'Not authenticated'),
#         (1, 'Authenticated'),
#         (2, 'No authenticated required')
#     )
#     choice_archive = (
#         (0, 'Not archived'),
#         (1, 'Archived')
#     )

#     user_id = models.AutoField(primary_key=True)
#     client = models.ForeignKey(ClientModel, null=True, on_delete=models.CASCADE, related_name='users')
#     user_type = models.SmallIntegerField(default=0,choices=choice_user )
#     login_type = models.CharField(max_length=45, default='email', choices=choice_login)
#     email = models.CharField(max_length=254, null=True)
#     password = models.CharField(max_length=255, null=True)
#     remember_token = models.CharField(max_length=255, null=True)
#     facebook_id = CharField(max_length=255, null=True)
#     twitter_id = CharField(max_length=255, null=True)
#     apple_id = CharField(max_length=255, null=True)
#     last_name_kanji = models.CharField(max_length=255)
#     first_name_kanji = models.CharField(max_length=255)
#     last_name_kana = models.CharField(max_length=255)
#     first_name_kana = models.CharField(max_length=255)
#     nickname = models.CharField(max_length=255)
#     sex = models.SmallIntegerField(choices=choice_sex, default=1)
#     is_sex_public = models.SmallIntegerField(choices=choice_sex_public, default=1)
#     date_of_birth = models.DateField(null=True)

#     is_date_of_birth_public = models.SmallIntegerField(choices=choice_is_date_of_birth_public, default=1)
#     phone = models.CharField(max_length=45, null=True)
#     zip_code = models.CharField(max_length=8, null=True)
#     prefecture = models.ForeignKey('PrefecturesModel', null=True, on_delete=models.CASCADE)
#     city = models.CharField(max_length=255, null=True)
#     subsequent_address = models.CharField(max_length=255, null=True)
#     biography = models.TextField(null=True)
#     points_balance = models.DecimalField(max_digits=15, decimal_places=0)
#     points_received = models.DecimalField(max_digits=15, decimal_places=0)
#     stamps_balance = models.DecimalField(max_digits=15, decimal_places=0)
#     econtext_cus_id = models.CharField(max_length=255, null=True)
#     delux_membership = models.CharField(max_length=255, null=True)
#     host_user_type = models.SmallIntegerField(null=True, choices=choice_user_type, default=1)
#     # is_authenticated = models.SmallIntegerField(choices=choice_is_authenticated, default=1)
#     is_archived = models.SmallIntegerField(default=1, choices=choice_archive)
#     created_at = models.DateTimeField(blank=True, verbose_name='登録日時', auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')
#     is_deleted = models.BooleanField(default=False, verbose_name='削除フラグ')

#     class Meta:
#         db_table = 'users'

class UsersModel(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE, null=True, related_name='user_client')
    user_type = models.IntegerField(null=True)
    remember_token = models.CharField(max_length=255, null=True)
    last_name_kanji = models.CharField(max_length=255, null=True)
    first_name_kanji = models.CharField(max_length=255, null=True)
    last_name_kana = models.CharField(max_length=255, null=True)
    first_name_kana = models.CharField(max_length=255, null=True)
    nickname = models.CharField(max_length=255, null=True)
    sex = models.CharField(max_length=255, null=True)
    is_sex_public = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(null=True)
    is_date_of_birth_public = models.BooleanField(max_length=255, null=True)
    phone = models.CharField(max_length=45, null=True)
    created_at = models.DateTimeField(null=True, blank=True, verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True, verbose_name='更新日時')
    is_deleted = models.BooleanField(null=True, default=False, verbose_name='削除フラグ')

    class Meta:
        db_table = 'users'



class ImagePathModel(BaseModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UsersModel, null=True, on_delete=CASCADE)
    event = models.ForeignKey(to='events.EventModel', null=True, on_delete=CASCADE, related_name = "event_image")
    box_notification_trans_content = models.ForeignKey('BoxNotificationTransContents', null=True, on_delete=CASCADE)
    file_name = models.CharField(max_length=255)
    dir_path = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    display_order = models.BooleanField()

    def save(self, *args, **kwargs):
        self.image_url = self.file_name+self.dir_path
        super(ImagePathModel, self).save(*args, **kwargs)

    class Meta:
        db_table = 'image_paths'

class PrefecturesModel(BaseModel):
    choice_is_default = (
        (0, 'Not default'),
        (1, 'Default')
    )
    prefecture_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    display_order = models.IntegerField()
    is_default = models.SmallIntegerField(choices=choice_is_default, default=0)
    class Meta:
        db_table = 'prefecture'

class BoxNotificationTransContents(BaseModel):
    choice_from_type = (
        (1, 'Host user'),
        (2, 'Client user (Mgmt portal user)'),
        (3, 'System admin user (Mgmt portal user)')
    )
    choice_is_delivered = (
        (1, 'Not delivered'),
        (2, 'Delivered')
    )

    
    box_notification_trans_content_id = models.AutoField(primary_key=True)
    client= models.ForeignKey(ClientModel, on_delete=CASCADE)
    from_type = models.SmallIntegerField(choices=choice_from_type)
    from_user_id = models.IntegerField(null=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    to_user_ids = models.TextField(null=True)
    scheduled_at = models.DateTimeField()
    is_delivered = models.SmallIntegerField(choices=choice_is_delivered)
    delivered_at = models.DateTimeField(null=True)

    
    class Meta:
        db_table = 'box_notification_trans_contents'