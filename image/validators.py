from django.core.exceptions import ValidationError
from django.conf import settings
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
