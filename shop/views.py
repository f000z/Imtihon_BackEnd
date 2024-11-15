from django.shortcuts import render
from .models import Category, Furniture, ShopMainView


def home(requests):
    category = Category.objects.all()
    banners = ShopMainView.objects.all()
    context = {
        'category': category,
        'banners': banners,

    }
    return render(requests, 'home.html', context)


def design(request):
    return render(request, 'design.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def shop(request):
    return render(request, 'shop.html')


def product(request):
    return render(request, 'product.html')



