"""zeroplusx_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url, include
from rest_framework import routers
from image.views import FileViewSet
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'files', FileViewSet)
schema_view = get_swagger_view(title='0+X Test API Docs')

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^$', schema_view)
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT})
    ]
