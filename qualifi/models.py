# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class QualifiAgency(models.Model):
    agency = models.CharField(max_length=50)
    code = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'qualifi_agency'
    def __str__(self):
        return self.agency


class QualifiBrand(models.Model):
    brand = models.CharField(max_length=50, primary_key=True)
    code = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'qualifi_brand'
    def __str__(self):
        return self.brand

class QualifiCampaign(models.Model):
    agency = models.CharField(max_length=50)
    brand = models.ForeignKey(QualifiBrand, models.DO_NOTHING, db_column='brand', blank=True, null=True)
    campaign = models.CharField(max_length=255)
    platform = models.CharField(max_length=50)
    channel = models.CharField(max_length=50)
    advertiser_name = models.CharField(max_length=50, blank=True)
    advertiser_id = models.CharField(max_length=20, blank=True, null=True)
    market = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    impression_goal = models.BigIntegerField(blank=True, null=True)
    csm = models.CharField(max_length=50, blank=True, null=True)
    sales = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    update_flag = models.BooleanField(blank=True, null=True)
    entry_date = models.DateField(blank=True, null=True)
    #id = models.CharField(max_length=2^1000, primary_key=True)


    class Meta:
        managed = False
        db_table = 'qualifi_campaign'

    def __str__(self):
        return self.campaign


class QualifiChannel(models.Model):
    channel = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'qualifi_channel'


class QualifiMarket(models.Model):
    market = models.CharField(max_length=50)
    code = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'qualifi_market'


class QualifiPeople(models.Model):
    name = models.CharField(max_length=25)
    role = models.CharField(max_length=25)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qualifi_people'


class QualifiPlatform(models.Model):
    platform = models.CharField(max_length=50)
    code = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'qualifi_platform'
