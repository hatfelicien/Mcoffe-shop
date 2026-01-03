from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product

def products(request):
    template = loader.get_template('products.html')
    return HttpResponse(template.render())
def home(request):
    return render(request, 'products.html')
def product(request):
    return render(request, 'product.html')
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('Home')

@login_required
def dashboard(request):
    products = Product.objects.all()
    return render(request, 'dashboard.html', {'products': products})


@login_required
def add_product(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            price=request.POST['price'],
            image_url=request.POST['image_url']
        )
        return redirect('dashboard')

    return render(request, 'add_product.html')


@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.image_url = request.POST['image_url']
        product.save()
        return redirect('dashboard')

    return render(request, 'edit_product.html', {'product': product})


@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('dashboard')





# from django.http import HttpResponse
# from django.template import loader

# def products(request):
#   template = loader.get_template('products.html')
#   return HttpResponse(template.render())
