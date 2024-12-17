from django.urls import path
from . import views

urlpatterns =[
    path('main',views.show, name= 'main'),
    path('1',views.display, name= 'display'),
    path('details/<int:pk>',views.details, name='details'),
    path('edit/<int:pk>',views.edit, name= 'edit'),
    path('history',views.history,name = 'history'),

]