from django.urls import path
from .views import *

urlpatterns = [
    path('registration/', sign_up_by_html, name='sign_up_by_html'),
    path('registration/django_sign_up/', sign_up_by_django, name='sign_up_by_django'),
    path('platform/', main_page, name='main_page'),
    path('platform/shop/', shop_page, name='shop_page'),
    path('platform/cart/', cart_page, name='cart_page'),
]