
from django.contrib import admin
from django.urls import include, path
from FIRETEK.views import *

urlpatterns = [
    path('',index),
    #path('FIRETEK/', include('FIRETEK.urls')),
    path('admin/', admin.site.urls),
]