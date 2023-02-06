from django.urls import path
from gtin.views import *
from . import views

urlpatterns = [
    path('', generateGtin.as_view(), name='generate_gtin'),
    path('gtin-product-entry/', GTINProductEntry.as_view(), name='gtin-product-entry'),
]