from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Product(models.Model):
    name = models.CharField(max_length=60, help_text="Введите тип чая")

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'

    def __str__(self):
        return self.name


class Tea(models.Model):
    image = models.ImageField(upload_to='static/img/')
    vid = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, help_text="Введите название чая")
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=0,null=True, blank=True)
    STATUS = (
        ('a', 'Доступен'),
        ('n', 'Нет в наличии'),
    )
    status = models.CharField(max_length=1, choices=STATUS, blank=True, default='a', help_text='Наличие чая')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Чай'
        verbose_name_plural = 'Чай'


    def __str__(self):
        return self.name

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Tea, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_cart_items_count(user):
        return OrderItem.objects.filter(user=user, ordered=False).aggregate(total_items=models.Sum('quantity'))['total_items'] or 0

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(OrderItem)
    full_name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order {self.id}'


