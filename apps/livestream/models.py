from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from commons.models import BaseModel

class LiveStreamModel(BaseModel):
    live_stream_id = models.IntegerField(max_length=11)
    ivs_am = models.CharField(max_length=255, null=True)
    status = models.BooleanField(max_length=2)
    host_user_id = models.IntegerField(max_length=11)
    performance_id = models.IntegerField(max_length=11, null=True)
    title = models.CharField(max_length=255, null=True)
    ingest_endpoint = models.CharField(max_length=255)
    stream_key = models.CharField(max_length=255)
    playback_url = models.CharField(max_length=255)
    comment_available_flag = models.BooleanField(max_length=1)
    tipping_available_flag = models.BooleanField(max_length=1)
    stamps_granted = models.DecimalField()
    release_datetime = models.DateTimeField()
    start_datetime = models.DateTimeField(null=True)
    end_datetime = models.DateTimeField(null=True)
    total_number_of_viewers = models.IntegerField(max_length=11, null=True)
    seconds_delivered = models.DecimalField(null=True)
    channel_id_sd = models.CharField(max_length=255, null=True)
    channel_id_fhd = models.CharField(max_length=255, null=True)
    input_id_sd = models.CharField(max_length=255, null=True)
    input_id_hd = models.CharField(max_length=255, null=True)
    vide_url_sd = models.CharField(max_length=255, null=True)
    vide_url_fhd = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'live_stream'

class LiveStreamViewerModel(BaseModel):
    live_stream_id = models.ForeignKey(LiveStreamModel, max_length=11, null=False)
    user_id = models.IntegerField(max_length=11, null=False, primary_key=True)
    viewed_at = models.DateTimeField(null=False)

    class Meta:
        db_table = 'live_stream_viewer'
    

