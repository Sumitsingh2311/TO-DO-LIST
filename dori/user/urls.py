from django.urls import path
from . import views

urlpatterns = [
    path('',views.register,name='register'),
    path('login',views.log_in, name='log_in'),
    path('logout',views.log_out, name='log_out'),

]