# -*- coding: utf-8 -*-
from rest_framework import viewsets
from .models import File
from .serializers import FileSerializer

class FileViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()

    def get_queryset(self):
        search = self.request.query_params.get('search', None)
        if search:
            return File.objects.filter(text__icontains=search)
        else:
            return self.queryset
