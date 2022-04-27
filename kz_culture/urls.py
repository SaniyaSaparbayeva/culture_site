from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .models import *

urlpatterns =[
    path('', index, name='index'), # http://127.0.0.1:8000/
    path('clothes/', clothes, name='clothes'),
    path('games/', games, name='games'),
    path('cuisine/', cuisine, name='cuisine'),
    path('traditions/', traditions, name='traditions'),
    path('registration/', user_registration, name='registration'),
    path('send/', send_message),
    path('contactUs/', contact, name='contact'),
    path('addPost', addPost, name='addPost')
]

urlpatterns += staticfiles_urlpatterns()