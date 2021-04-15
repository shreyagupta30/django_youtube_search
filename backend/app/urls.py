from django.urls import path

from . import services, views

urlpatterns = [
    path('videos', views.GetVideos.as_view()),
    path('key', views.AddAPIKey.as_view()),
]

services.THREAD.start()
