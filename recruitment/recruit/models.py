# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Recruit(models.Model):
    STATUS = (
      ('select','select'),
      ('Accept', 'Accept'),
      ('Reject', 'Reject')
    )
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=500)
    years_of_experience = models.FloatField()
    technologies = models.CharField(max_length=1000)
    current_organisation = models.CharField(max_length=500)
    current_CTC = models.FloatField()
    expected_CTC = models.FloatField()
    notice_period = models.IntegerField()
    description = models.TextField()
    application_status = models.CharField(max_length=100, choices = STATUS, default=STATUS[0][0], null=True)

