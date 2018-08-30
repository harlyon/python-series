# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Job(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=200)
