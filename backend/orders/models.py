from django.db import models
from django.conf import settings
from products.models import Product


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending',   'En attente'),
        ('confirmed', 'Confirmée'),
        ('shipped',   'Expédiée'),
        ('delivered', 'Livrée'),
        ('cancelled', 'Annulée'),
    ]
    user             = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    status           = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    shipping_address = models.TextField()
    city             = models.CharField(max_length=100)
    postal_code      = models.CharField(max_length=10)
    phone            = models.CharField(max_length=20)
    total_price      = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Commande #{self.pk} — {self.user}"

    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"


class OrderItem(models.Model):
    order      = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product    = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity   = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_subtotal(self):
        return self.unit_price * self.quantity

    class Meta:
        verbose_name = "Article de commande"
        verbose_name_plural = "Articles de commande"
