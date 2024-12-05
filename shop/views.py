from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from shop.forms import FurnitureForm
from shop.models import Category, Furniture, ShopMainView, ContactModel
from shop.serializers import CategorySerializer, FurnitureSerializer, ShopMainViewSerializer
from shop.permissions import IsOwnerOrReadOnly
from django.views.generic.edit import CreateView

import logging
logger = logging.getLogger(__name__)


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

    def form_valid(self, form):
        # Логируем данные, которые поступили через форму
        contact_data = form.cleaned_data
        logger.info(f"New contact received: Name: {contact_data['name']}, "
                    f"Email: {contact_data['email']}, "
                    f"Phone: {contact_data['phone']}, "
                    f"Message: {contact_data['message']}")

        # Выводим в консоль для дополнительной отладки
        print(contact_data)  # Это выведет данные в консоль

        return super().form_valid(form)  # Сохраняем данные в базу


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
        furnitures = Furniture.objects.all()
        serializer = FurnitureSerializer(furnitures, many=True)
        return Response(serializer.data)


class ShopMainViewListView(APIView):
    def get(self, request):
        shop_main_views = ShopMainView.objects.all()
        serializer = ShopMainViewSerializer(shop_main_views, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_furniture_api(request):
    if request.method == 'POST':
        serializer = FurnitureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Присваиваем владельца
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Обновление объекта (проверка владельца)
@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsOwnerOrReadOnly])  # Применяем разрешение
def update_furniture_api(request, id):
    furniture = get_object_or_404(Furniture, id=id)
    if request.method == 'PUT':
        serializer = FurnitureSerializer(furniture, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Удаление объекта (проверка владельца)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsOwnerOrReadOnly])  # Применяем разрешение
def delete_furniture_api(request, id):
    furniture = get_object_or_404(Furniture, id=id)
    if request.method == 'DELETE':
        furniture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Traditional Views with Permissions (HTML pages)
def furniture_detail(request, id):
    furniture = get_object_or_404(Furniture, id=id)
    return render(request, 'pages/furniture_detail.html', {'furniture': furniture})


# Покупка мебели
def buy_furniture(request, id):
    furniture = get_object_or_404(Furniture, id=id)

    if request.method == 'POST':  # Проверяем, что запрос пришел методом POST
        # Печатаем информацию о покупке в консоль
        print(
            f"Buy Furniture_Name: {furniture.name}, Price: ${furniture.price}, User: {request.user.username if request.user.is_authenticated else 'Guest'}")

        # Здесь можно добавить дополнительные действия, например, создание заказа, оплату и т. д.

        # Для теста, после обработки запроса, перенаправим на страницу магазина
        return redirect('shop')  # Перенаправляем на страницу магазина

    # Если не POST, просто отображаем форму покупки
    return render(request, 'pages/buy_furniture.html', {'furniture': furniture})


def create_furniture(request):
    if request.method == 'POST':
        form = FurnitureForm(request.POST, request.FILES)
        if form.is_valid():
            furniture = form.save(commit=False)
            furniture.user = request.user  # Присваиваем владельца
            furniture.save()
            return redirect('shop')  # Перенаправляем обратно в магазин
    else:
        form = FurnitureForm()
    return render(request, 'Furnitures/create_furniture.html', {'form': form})


def update_furniture(request, id):
    # Get the furniture object or return 404 if it doesn't exist
    furniture = get_object_or_404(Furniture, id=id)

    # Handle POST request (form submission)
    if request.method == 'POST':
        form = FurnitureForm(request.POST, request.FILES, instance=furniture)
        if form.is_valid():
            form.save()
            return redirect('shop')  # Redirect to the shop page after update

    # Handle GET request (display the form with current furniture data)
    else:
        form = FurnitureForm(instance=furniture)

    # Render the form for updating
    return render(request, 'Furnitures/update_furniture.html', {'form': form})


def delete_furniture(request, id):
    furniture = get_object_or_404(Furniture, id=id)
    if request.method == 'POST':
        furniture.delete()
        return redirect('shop')  # Redirect back to shop view or any page you want
    return render(request, 'Furnitures/delete_furniture.html', {'furniture': furniture})


def page_not_found(request):
    return render(request, 'pages/404_error.html', status=404)


def people_list(request):
    people = ContactModel.objects.all()
    return render(request, 'contact_us/peoples_list.html', {'people': people})


def search(request):
    query = request.GET.get('q', '')
    if query:
        results = Furniture.objects.filter(name__icontains=query)
    else:
        results = Furniture.objects.all()
    context = {
        'query': query,
        'results': results
    }
    return render(request, 'search.html', context)
