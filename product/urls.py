from django.urls import path
from . import views

urlpatterns=[
path('venues/',views.listVenues.as_view()),
path('contacts/',views.listContacts.as_view()),
path('',views.basePage.as_view()),
]