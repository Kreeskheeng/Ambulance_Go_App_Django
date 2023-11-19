from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name ='index'),
    path('', views.index ,name='index'),
    path('input-data/', views.booking_page, name='booking_page'),  # URL for Input Data (Booking Page)
    path('retrieve-data/', views.booking_history, name='booking_history'),  # URL for Retrieve Data (Booking History)
    path('confirmation/', views.confirmation_page, name='confirmation_page'),  # URL for Confirmation Page
    path('registration/', views.ambulance_registration, name='ambulance_registration'),  # URL for Confirmation Page
   
    
]

