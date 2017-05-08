# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import os
import uuid

def image_upload(instance, filename):
    _, file_extension = os.path.splitext(filename)
    return "images/%s%s" % (uuid.uuid4(), file_extension)

class File(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=500, default='')
    image = models.ImageField(blank=True, null=True, upload_to=image_upload)
