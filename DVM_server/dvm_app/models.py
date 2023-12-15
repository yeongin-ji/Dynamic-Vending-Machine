# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Orders(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, product_id) found, that is not supported. The first column is selected.
    product = models.ForeignKey('Product', models.DO_NOTHING)
    rating = models.FloatField()

    class Meta:
        managed = False
        db_table = 'orders'
        unique_together = (('user', 'product'),)


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    stock = models.IntegerField()
    price_kr = models.IntegerField()
    price_us = models.IntegerField()
    price_jp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product'


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    passwd = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    country = models.CharField(max_length=10)
    welfare = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'user'