from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Model for Bakery Items
class BakeryItem(models.Model):
    class AvailabilityStatus(models.TextChoices):
        AVAILABLE = 'AV', _('Available')
        OUT_OF_STOCK = 'OOS', _('Out of Stock')
        SEASONAL = 'SEA', _('Seasonal')

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True, null=True)  # New category field
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    availability = models.CharField(
        max_length=3, choices=AvailabilityStatus.choices, default=AvailabilityStatus.AVAILABLE
    )
    image = models.ImageField(upload_to="bakery_items", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.category})"

# Model for Beverages
class Beverage(models.Model):
    name = models.CharField(max_length=200)
    size_choices = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    size = models.CharField(max_length=1, choices=size_choices, default='M')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_hot = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_size_display()})"

# Model for Customers
class Customer(models.Model):
    user          = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name          = models.CharField(max_length=200, blank=False, null=False)
    email         = models.EmailField(max_length=200, )
    phone_number  = models.CharField(max_length=15, blank=False, null=False)
    address       = models.TextField(blank=False, null=False)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

# Model for Orders
class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = 'PEN', _('Pending')
        COMPLETED = 'COM', _('Completed')
        CANCELED = 'CAN', _('Canceled')

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    items = models.ManyToManyField(BakeryItem, through="OrderItem", related_name="orders")
    beverages = models.ManyToManyField(Beverage, through="OrderBeverage", related_name="orders")
    status = models.CharField(
        max_length=3, choices=OrderStatus.choices, default=OrderStatus.PENDING
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.get_status_display()}"

# Through model for order and bakery items
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    bakery_item = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.bakery_item.name} x {self.quantity} (Order #{self.order.id})"

# Through model for order and beverages
class OrderBeverage(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    beverage = models.ForeignKey(Beverage, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.beverage.name} x {self.quantity} (Order #{self.order.id})"
