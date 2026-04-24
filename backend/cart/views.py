from django.views.generic import DetailView, DeleteView, UpdateView
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cart, CartItem
from .utils import get_or_create_cart
from products.models import Product


class AddToCartView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        cart = get_or_create_cart(request)

        if product.stock <= 0:
            return redirect('product_detail', pk=pk)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            if cart_item.quantity < product.stock:
                cart_item.quantity += 1
                cart_item.save()
        return redirect('cart_detail')


class CartDetailView(DetailView):
    model = Cart
    template_name = 'cart/detail_cart.html'
    context_object_name = 'cart'

    def get_object(self):
        return get_or_create_cart(self.request)


class CartItemDeleteView(LoginRequiredMixin, DeleteView):
    model = CartItem
    template_name = 'cart/cartitem_delete.html'
    success_url = reverse_lazy('cart_detail')
    login_url = '/users/login/'


class CartItemUpdateView(LoginRequiredMixin, View):
    login_url = '/users/login/'

    def post(self, request, pk):
        item = get_object_or_404(CartItem, pk=pk)
        qty = int(request.POST.get('quantity', 1))
        if qty <= 0:
            item.delete()
        else:
            item.quantity = min(qty, item.product.stock)
            item.save()
        return redirect('cart_detail')
