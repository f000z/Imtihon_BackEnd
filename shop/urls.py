from django.urls import path
from .views import home, shop, contact, design, about


urlpatterns = [
    path('home_list', home, name='home'),
    path('shop/', shop, name='shop'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('design/', design, name='design'),
]