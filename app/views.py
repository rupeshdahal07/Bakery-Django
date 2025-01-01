from django.shortcuts import render
from django.views import View
from .models import BakeryItem, Beverage, Customer, Order

# Create your views here.
class HomeView(View):
    '''This class-based view will render the home page. and display the available bakery items'''
    def get(self, request):
        cupcake = BakeryItem.objects.filter(category='Cupcake')
        return render(request, 'app/index-2.html', 
                      {'cupcake': cupcake
                       
                       })
    
    def post(self, request):
        return render(request, 'app/index-2.html')
    

def home2(request):
    return render(request, 'app/index.html')

def home3(request):
    return render(request, 'app/index-3.html')

def home4(request):
    return render(request, 'app/index-4.html')

def home5(request):
    return render(request, 'app/index-5.html')

def menu(request):
    '''This function-based view will render the menu page and display the available bakery items'''
    cupcake = BakeryItem.objects.filter(category='Cupcake')
    return render(request, 'app/menu.html', {'cupcake': cupcake})

def our_cake(request):
    cupcake = BakeryItem.objects.filter(category='Cupcake')
    return render(request, 'app/cake.html', {'cupcake': cupcake})

def about(request):
    return render(request, 'app/about-us.html')

def contact(request):
    return render(request, 'app/contact.html')

def cart(request):
    return render(request, 'app/cart.html')

def checkout(request):
    return render(request, 'app/checkout.html')

def shop(request):
    return render(request, 'app/shop.html')
