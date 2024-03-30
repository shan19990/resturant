"""
URL configuration for resturant project.

"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('',TableBookingView,name="usertablebook"),
    path('list/',DisplayBookingView,name="userlistbook"),
    path('delete/<int:id>',DeleteBookingView,name="userdeletebook"),
    path('edit/<int:id>/<str:restaurant>',EditBookingView,name="usereditbook"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)