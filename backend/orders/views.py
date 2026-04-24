from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItem
from .forms import OrderForm
from cart.utils import get_or_create_cart


class CreateOrderView(LoginRequiredMixin, View):
    login_url = '/users/login/'

    def get(self, request):
        form = OrderForm()
        cart = get_or_create_cart(request)
        return render(request, 'orders/shipping.html', {'form': form, 'cart': cart})

    def post(self, request):
        form = OrderForm(request.POST)
        cart = get_or_create_cart(request)

        if form.is_valid():
            order = form.save(commit=False)
            order.user        = request.user
            order.total_price = cart.get_total()
            order.save()

            for item in cart.items.all():
                OrderItem.objects.create(
                    order      = order,
                    product    = item.product,
                    quantity   = item.quantity,
                    unit_price = item.product.price,
                )
                item.product.stock -= item.quantity
                item.product.save()

            cart.items.all().delete()
            return render(request, 'orders/confirmation.html', {'order': order})

        return render(request, 'orders/shipping.html', {'form': form, 'cart': cart})
