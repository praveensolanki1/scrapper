from django.urls import path
from . views import *


urlpatterns = [
     path('get_data',get_data,name='get_data'),
]
