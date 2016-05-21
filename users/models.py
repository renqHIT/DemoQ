# -*- encoding: utf-8 -*-

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32)
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
