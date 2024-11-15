from django.urls import path
from .views import home, shop, contact, design, about, product


urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('design/', design, name='design'),
    path('product/', product, name='product')
]