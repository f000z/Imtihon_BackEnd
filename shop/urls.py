from django.urls import path
from shop.views import home, shop, ContactView, about, product, CategoryListView, FurnitureListView, \
    ShopMainViewListView, furniture_detail, create_furniture, update_furniture, delete_furniture, \
    create_furniture_api, update_furniture_api, delete_furniture_api, contact_send_done, people_list

urlpatterns = [
    # Traditional views (HTML pages)
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact-send-done/', contact_send_done, name='contact_send_done'),
    path('about/', about, name='about'),
    path('product/', product, name='product'),
    path('contact-list/', people_list, name='contact_list'),

    # API views (with DRF)
    path('api/categories/', CategoryListView.as_view(), name='category-list'),
    path('api/furnitures/', FurnitureListView.as_view(), name='furniture-list'),
    path('api/shopmainview', ShopMainViewListView.as_view(), name='shop-main-list'),

    # Furniture Details (with id)
    path('furniture/<int:id>/', furniture_detail, name='furniture_detail'),
    path('create_furniture/', create_furniture, name='create_furniture'),
    path('update_furniture/<int:id>/', update_furniture, name='update_furniture'),
    path('delete_furniture/<int:id>/', delete_furniture, name='delete_furniture'),

    # API Views for Furniture CRUD
    path('api/furniture/create/', create_furniture_api, name='create_furniture_api'),
    path('api/furniture/update/<int:id>/', update_furniture_api, name='update_furniture_api'),
    path('api/furniture/delete/<int:id>/', delete_furniture_api, name='delete_furniture_api'),
]

