from  django.urls import path, include
from . import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_details, name='product_details' ),
    path('purchase_product/<int:pk>/', views.purchase_product, name='purchase_product'),
    path('purchase_succeeded/', views.purchase_succeeded, name='purchase_succeeded'),
    path ('register_user/', views.register, name='register_user'),
]