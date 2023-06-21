from django.contrib import admin
from .models import Tea, Product, Order, OrderItem



class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name')
admin.site.register(Product, ProductAdmin)

class TeaAdmin(admin.ModelAdmin):
    list_display = ('name','price','status')
admin.site.register(Tea, TeaAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user')
admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('user','ordered')
admin.site.register(OrderItem, OrderItemAdmin)


