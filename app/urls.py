from django.urls import path, include # Add this line to include the app's urls in the project
from . import views

urlpatterns = [
    
    path('', views.home, name="home"),
    path('home2/', views.home2, name='home2'),  # Corresponds to Home 2
    path('home3/', views.home3, name='home3'),  # Corresponds to Home 3
    path('home4/', views.home4, name='home4'),  # Corresponds to Home 4
    path('home5/', views.home5, name='home5'),  # Corresponds to Home 5
    path('menu/', views.menu, name='menu'),
    path('our-cake/', views.our_cake, name='our_cake'),  # Corresponds to Menu
    path('about/', views.about, name='about'),  # Corresponds to About   
    path('contact/', views.contact, name='contact'),  # Corresponds to Contact
    path('cart/', views.cart, name='cart'),  # Corresponds to Cart

]
