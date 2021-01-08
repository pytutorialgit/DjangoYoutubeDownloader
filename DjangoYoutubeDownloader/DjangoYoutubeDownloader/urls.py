"""DjangoYoutubeDownloader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# core.views
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #core
    path('index/', Index.as_view()),
    path('download1/', youtube_downloader, name="download1"),
    path('index2/', Index2.as_view()),
    path('get-info/', get_video_info, name="get_info"),
    path('download2/', youtube_Downloader2, name="download2")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)