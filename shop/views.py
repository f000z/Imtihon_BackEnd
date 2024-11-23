from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from shop.forms import FurnitureForm
from shop.models import Category, Furniture, ShopMainView, ContactModel
from shop.serializers import CategorySerializer, FurnitureSerializer, ShopMainViewSerializer

from django.views.generic import CreateView
from django.shortcuts import get_object_or_404



# Traditional Views (HTML pages)
def home(request):
    category = Category.objects.all()
    banners = ShopMainView.objects.all()
    furniture = Furniture.objects.all()
    context = {
        'category': category,
        'banners': banners,
        'furniture': furniture,
    }
    return render(request, 'home.html', context)


class ContactView(CreateView):
    model = ContactModel
    template_name = 'contact.html'
    fields = '__all__'
    success_url = reverse_lazy('contact_send_done')


def contact_send_done(request):
    return render(request, 'pages/contact_send_done.html')


def about(request):
    return render(request, 'about.html')


def shop(request):
    furnitures = Furniture.objects.all()
    context = {
        'furnitures': furnitures,
    }
    return render(request, 'shop.html', context)


def product(request):
    return render(request, 'product.html')


# API Views (for JSON data)
class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class FurnitureListView(APIView):
    def get(self, request):
        # Fetch all furnitures and return them in JSON format
        furnitures = Furniture.objects.all()
        serializer = FurnitureSerializer(furnitures, many=True)
        return Response(serializer.data)


class ShopMainViewListView(APIView):
    def get(self, request):
        # Fetch all banners and return them in JSON format
        shop_main_views = ShopMainView.objects.all()
        serializer = ShopMainViewSerializer(shop_main_views, many=True)
        return Response(serializer.data)


def furniture_detail(request, id):
    furniture = get_object_or_404(Furniture, id=id)
    return render(request, 'pages/furniture_detail.html', {'furniture': furniture})


def create_furniture(request):
    if request.method == 'POST':
        form = FurnitureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop')  # Redirect back to shop view or any page you want
    else:
        form = FurnitureForm()
    return render(request, 'Furnitures/create_furniture.html', {'form': form})


def update_furniture(request, id):
    furniture = get_object_or_404(Furniture, id=id)
    if request.method == 'POST':
        form = FurnitureForm(request.POST, request.FILES, instance=furniture)
        if form.is_valid():
            form.save()
            return redirect('shop')  # Redirect back to shop view or any page you want
    else:
        form = FurnitureForm(instance=furniture)
    return render(request, 'Furnitures/update_furniture.html', {'form': form, 'furniture': furniture})


def delete_furniture(request, id):
    furniture = get_object_or_404(Furniture, id=id)
    if request.method == 'POST':
        furniture.delete()
        return redirect('shop')  # Redirect back to shop view or any page you want
    return render(request, 'Furnitures/delete_furniture.html', {'furniture': furniture})


@api_view(['POST'])
def create_furniture_api(request):
    if request.method == 'POST':
        serializer = FurnitureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_furniture_api(request, id):
    furniture = get_object_or_404(Furniture, id=id)
    if request.method == 'PUT':
        serializer = FurnitureSerializer(furniture, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_furniture_api(request, id):
    furniture = get_object_or_404(Furniture, id=id)
    if request.method == 'DELETE':
        furniture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def page_not_found(request, exception):
    return render(request, 'pages/404_error.html', status=404)


def people_list(request):
    people = ContactModel.objects.all()
    return render(request, 'contact_us/peoples_list.html', {'people': people})


