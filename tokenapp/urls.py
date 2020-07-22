from django.urls import path
from tokenapp import views

app_name = 'tokenapp'

urlpatterns=[
    path('register/',views.register, name='register'),
    path('user_login/',views.user_login,name='user_login'),
]