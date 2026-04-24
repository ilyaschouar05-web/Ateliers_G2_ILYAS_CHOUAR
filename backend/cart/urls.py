from django.urls import path
from .views import AddToCartView, CartDetailView, CartItemDeleteView, CartItemUpdateView

urlpatterns = [
    path('', CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
    path('delete/<int:pk>/', CartItemDeleteView.as_view(), name='cartitem_delete'),
    path('update/<int:pk>/', CartItemUpdateView.as_view(), name='cartitem_update'),
]
