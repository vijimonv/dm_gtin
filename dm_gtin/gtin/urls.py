from django.urls import path
from gtin.views import *
from . import views

urlpatterns = [
    path('', generateGtin.as_view(), name='generate_gtin'),
    path('gtin-list/', GTINList.as_view(), name='gtin-list'),
    path('gtin-product-entry/', GTINProductEntry.as_view(), name='gtin-product-entry'),
    path('add-gtin-product-entry/', addGTINProductEntry.as_view(), name='add-gtin-product-entry'),
]