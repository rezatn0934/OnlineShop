from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


app_name = 'store'
urlpatterns = [
    path('products/', views.ProductListView.as_view()),
    path('products/<slug:slug>', views.ProductDetail.as_view(), name='product_details'),
]
