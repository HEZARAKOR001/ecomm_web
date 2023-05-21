from django.contrib import admin
from django.urls import path
from lufy import views
from django.conf import settings
from django.conf.urls.static import static

#Urls
urlpatterns = [
    path("", views.home, name='home'),
    #path('main', views.main, name = "customize"),
    path('generate_poster', views.generate_poster, name='generate_poster')


]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
