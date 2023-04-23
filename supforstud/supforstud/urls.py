"""supforstud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from supforstud import settings


from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from support.views import *
from rest_framework import routers
from supforstud import settings


from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),

    path('captcha/', include('captcha.urls')),

    path('',include('support.urls'))
]

# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
#
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import re_path as url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', include('support.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

    # path('api/v1/suplist/', SupportViewSet.as_view({'get': 'list'})),
    # path('api/v1/suplist/<int:pk>', SupportViewSet.as_view({'put': 'update'})),
]

router = routers.DefaultRouter()
#makes sure that the API endpoints work
router.register(r'api/sup', views.PatientViewSet)
admin.autodiscover()