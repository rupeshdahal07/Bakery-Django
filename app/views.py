from django.shortcuts import redirect, render
from django.views import View
from .models import BakeryItem, Beverage, Customer, Order, OrderItem, Cart
from .forms import CustomerRegistratinForm, CustomerProfileForm
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.
class HomeView(View):
    '''This class-based view will render the home page. and display the available bakery items'''
    def get(self, request):
        cupcake_for_featured = BakeryItem.objects.filter(category='Cupcake')[ :4]
        cake_for_featured = BakeryItem.objects.filter(category='Cake')[ :4]
        cupcake = BakeryItem.objects.filter(category='Cupcake')[ :6]
        cake = BakeryItem.objects.filter(category='Cake')[ :6]
        return render(request, 'app/index-2.html', 
                      {'cupcake': cupcake,
                        'cake': cake,
                        'cupcake_for_featured': cupcake_for_featured,
                        'cake_for_featured': cake_for_featured
                       
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


class ProductDetailView(View):
    '''This class-based view will render the product detail page and display the details of the selected bakery item'''
    def get(self, request, pk):
        item = get_object_or_404(BakeryItem, pk=pk)
        return render(request, 'app/product-details.html', {'item': item})

    def post(self, request, pk):
        item = get_object_or_404(BakeryItem, pk=pk)
        return render(request, 'app/product-details.html', {'item': item})


def menu(request):
    '''This function-based view will render the menu page and display the available bakery items'''
    cupcake = BakeryItem.objects.filter(category='Cupcake')
    return render(request, 'app/menu.html', {'cupcake': cupcake})

def our_cake(request):
    cake = BakeryItem.objects.filter(category='Cake')
    cake_special = BakeryItem.objects.filter(category='Cake')[:3]
    return render(request, 'app/cake.html', {'cake': cake, 'cake_special': cake_special} )

def about(request):
    return render(request, 'app/about-us.html')

def contact(request):
    return render(request, 'app/contact.html')

def cart(request):
    return render(request, 'app/cart.html')

def add_to_cart(request, pk):
    user = request.user
    product = get_object_or_404(BakeryItem, pk=pk)
    print(BakeryItem)
    Cart(user=user, product=product).save()
    return redirect('/cart')

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = float(p.quantity * p.product.price)
                amount += tempamount
            total_amount = amount + shipping_amount
            return render(request, 'app/cart.html', {'carts': cart, 'total_amount': total_amount, 'amount': amount})
        else:
            return render(request, 'app/emptycart.html')

def checkout(request):
    return render(request, 'app/checkout.html')


def shop(request, data=None):
    '''This function-based view will render the shop page and display the available bakery items'''
    total_cakes = len(BakeryItem.objects.filter(category="Cake"))
    total_cupcakes = len(BakeryItem.objects.filter(category="Cupcake"))
    total_doughnuts = len(BakeryItem.objects.filter(category="Doughnut"))
    total_items = len(BakeryItem.objects.all())

    if data == None:
        bakery_items = BakeryItem.objects.all()
    elif data == 'Cupcake':
        bakery_items = BakeryItem.objects.filter(category=data)
    elif data == 'Cake':
        bakery_items = BakeryItem.objects.filter(category=data)
    elif data == 'Doughnut':
        bakery_items = BakeryItem.objects.filter(category=data)
    return render(request, 'app/shop.html', {'bakery_items': bakery_items,
                                             'total_cakes': total_cakes,
                                             'total_cupcakes': total_cupcakes,
                                             'total_doughnuts': total_doughnuts,
                                                'total_items': total_items
                                             })




class ProfileView(View):
    '''This class-based view will render the profile page and display the customer's profile'''
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/customerprofile.html', {'form': form, 'active': 'btn-primary'})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            customer = Customer(user=usr, name=name, email=email, phone_number=phone_number, address=address)
            customer.save()
            messages.success(request, 'Profile updated successfully')
        return render(request, 'app/customerprofile.html', {'form': form, 'active': 'btn-primary'})



class CustomerRegistrationView(View):
    '''This class-based view will render the registration page and allow the customer'''
    def get(self, request):
        form = CustomerRegistratinForm()
        return render(request, 'app/registration.html', {'form': form})
    
    def post(self, request):
        form = CustomerRegistratinForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Contratulations! Regisered Sucessfully')
            form.save()
        return render(request, 'app/registration.html', {'form': form})



def address(request):
    '''This function-based view will render the address page and display the customer's address'''
    address = Customer.objects.filter(user = request.user)
    return render(request, 'app/address.html', {'address': address, 'active': 'btn btn-primary'})