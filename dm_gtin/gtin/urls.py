from django.urls import path
from gtin.views import *
from . import views

urlpatterns = [
    path('', loginUser.as_view(), name='login'),
    path('logout/', logout.as_view(), name='logout'),
    path('dashboard/', generateGtin.as_view(), name='generate_gtin'),
    path('gtin-list/', GTINList.as_view(), name='gtin-list'),
    path('gtin-product-entry/', GTINProductEntry.as_view(), name='gtin-product-entry'),
    path('add-gtin-product-entry/', addGTINProductEntry.as_view(), name='add-gtin-product-entry'),
    path('edit-gtin-product-entry/', editGTINProductEntry.as_view(), name='edit-gtin-product-entry'),
]