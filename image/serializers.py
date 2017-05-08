from rest_framework import serializers
from django.conf import settings
from image.models import File
import uuid
import base64
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError
import os

def check_file_size(temp_file):
    if temp_file.size > settings.MAX_IMAGE_SIZE:
        raise ValidationError('The image size (%sB) exceeded %sB.' \
                              % (temp_file.size, settings.MAX_IMAGE_SIZE))

def check_file_extension(temp_file):
    _, file_extension = os.path.splitext(temp_file.name)
    if file_extension not in settings.ALLOWED_IMAGE_EXTENSIONS:
        raise ValidationError(
            'Invalid extension for image. Allowed ones are: %s.'\
            % ', '.join(settings.ALLOWED_IMAGE_EXTENSIONS))

class CustomImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, unicode) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            id = uuid.uuid4()
            data = ContentFile(base64.b64decode(imgstr), name = id.urn[9:] + '.' + ext)
        return super(CustomImageField, self).to_internal_value(data)

class FileSerializer(serializers.ModelSerializer):
    image = CustomImageField(use_url=False,
        validators=[check_file_size, check_file_extension])

    class Meta:
        model = File
        fields = ('id', 'text', 'image')
