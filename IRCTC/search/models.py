# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class StationList(models.Model):
    station = models.CharField(max_length=50, blank=True, null=True)
    station_code = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    railway_zone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station_list'

class TrainList(models.Model):
    train_no = models.TextField(db_column='Train No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    train_name = models.TextField(db_column='train Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    islno = models.BigIntegerField(blank=True, null=True)
    station_code = models.TextField(db_column='station Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    station_name = models.TextField(db_column='Station Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arrival_time = models.TextField(db_column='Arrival time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    departure_time = models.TextField(db_column='Departure time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    distance = models.BigIntegerField(db_column='Distance', blank=True, null=True)  # Field name made lowercase.
    source_station_code = models.TextField(db_column='Source Station Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    source_station_name = models.TextField(db_column='source Station Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    destination_station_code = models.TextField(db_column='Destination station Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    destination_station_name = models.TextField(db_column='Destination Station Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'train_list'
