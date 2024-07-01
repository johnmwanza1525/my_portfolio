# urls.py

from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='index'),
    path('product_view/', views.product_view, name='product_view'),
    path('product/<int:product_id>/', views.description_view, name='product_detail'),  # Corrected for product_id
    path('category/<slug:category_slug>/', views.product_view, name='product_list_by_category'),  # Updated for category_slug
]
