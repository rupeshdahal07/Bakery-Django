from django.urls import path, include # Add this line to include the app's urls in the project
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm

urlpatterns = [
    
    path('', views.HomeView.as_view(), name="home"),
    path('home2/', views.home2, name='home2'),  # Corresponds to Home 2
    path('home3/', views.home3, name='home3'),  # Corresponds to Home 3
    path('home4/', views.home4, name='home4'),  # Corresponds to Home 4
    path('home5/', views.home5, name='home5'),  # Corresponds to Home 5
    path('menu/', views.menu, name='menu'),
    path('our-cake/', views.our_cake, name='our_cake'),  # Corresponds to Menu
    path('about/', views.about, name='about'),  # Corresponds to About   
    path('contact/', views.contact, name='contact'),  # Corresponds to Contact
    path('cart/', views.cart, name='cart'),  # Corresponds to Cart
    path('checkout/', views.checkout, name='checkout'),  # Corresponds to Checkout
    path('shop/', views.shop, name='main_shop'),  # Corresponds to Shop

    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html', 
                                                        authentication_form=LoginForm),
                                                        name='login'),
    path('logout/' ,auth_view.LogoutView.as_view(next_page ='login'), name='logout'),

    

]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
