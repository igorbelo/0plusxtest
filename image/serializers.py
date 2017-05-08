from rest_framework import serializers
import uuid
import base64
from django.core.files.base import ContentFile
from .models import File
from .validators import check_file_size, check_file_extension

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
