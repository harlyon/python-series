# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=355)
	publishedDate = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')
