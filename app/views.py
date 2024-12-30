from django.shortcuts import render

# Create your views here.
def home(request):
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
    return render(request, 'app/menu.html')

def our_cake(request):
    return render(request, 'app/cake.html')

def about(request):
    return render(request, 'app/about-us.html')

def contact(request):
    return render(request, 'app/contact.html')

def cart(request):
    return render(request, 'app/cart.html')
