from django.urls import path
from . import views

urlpatterns=[
    path('',views.ev_page,name='ev_page'),
]