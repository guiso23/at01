from . import views
from django.urls import path

urlpatterns =[
    path('', views.home, name='home'),
    path('gun/<int:cgun_id>/', views.details, name='details'),

]