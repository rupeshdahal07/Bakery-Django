from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BakeryItem, Beverage, Customer, Order, OrderItem, OrderBeverage, Cart

# Customize BakeryItem Admin
@admin.register(BakeryItem)
class BakeryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'availability', 'created_at', 'updated_at')
    list_filter = ('availability', 'category', 'created_at')
    search_fields = ('name', 'category', 'description')
    ordering = ('-created_at',)

# Customize Beverage Admin
@admin.register(Beverage)
class BeverageAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'price', 'is_hot', 'created_at', 'updated_at')
    list_filter = ('size', 'is_hot', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)

# Customize Customer Admin
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'phone_number', 'created_at', 'updated_at')
    search_fields = ('user__username', 'name', 'email', 'phone_number')
    ordering = ('-created_at',)

# Customize Order Admin
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderBeverageInline(admin.TabularInline):
    model = OrderBeverage
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'total_price', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer__user__username', 'customer__email', 'id')
    ordering = ('-created_at',)
    inlines = [OrderItemInline, OrderBeverageInline]

# Inline Admin for Order Items
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'bakery_item', 'quantity')
    list_filter = ('order',)
    search_fields = ('order__id', 'bakery_item__name')

# Inline Admin for Order Beverages
@admin.register(OrderBeverage)
class OrderBeverageAdmin(admin.ModelAdmin):
    list_display = ('order', 'beverage', 'quantity')
    list_filter = ('order',)
    search_fields = ('order__id', 'beverage__name')

# Customize Cart Admin
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')
    list_filter = ('user',)
    search_fields = ('user__username', 'product__name')
    ordering = ('-id',)