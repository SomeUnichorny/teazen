from django.shortcuts import render, redirect, get_object_or_404
from .models import Tea, OrderItem, User, Order
from django.views import generic
from django.core.mail import send_mail
from .forms import UserRegistrationForm, EmailForm
from mysite.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from django.contrib import messages
from django.db.models import Sum, F
from .forms import OrderForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'teazen/index.html')


class BlackTeaListView(generic.ListView):
    model = Tea
    context_object_name = 'black_tea'
    template_name = 'teazen/blacktea_list.html'

    def get_queryset(self):
        return Tea.objects.filter(vid=6)

    paginate_by = 10


class GreenTeaListView(generic.ListView):
    model = Tea
    context_object_name = 'green_tea'
    template_name = 'teazen/greentea_list.html'

    def get_queryset(self):
        return Tea.objects.filter(vid=7)

    paginate_by = 10


class FruitTeaListView(generic.ListView):
    model = Tea
    context_object_name = 'fruit_tea'
    template_name = 'teazen/fruittea_list.html'

    def get_queryset(self):
        return Tea.objects.filter(vid=8)

    paginate_by = 10


class FlowerTeaListView(generic.ListView):
    model = Tea
    context_object_name = 'flower_tea'
    template_name = 'teazen/flowertea_list.html'

    def get_queryset(self):
        return Tea.objects.filter(vid=9)

    paginate_by = 10


class MonthTeaListView(generic.ListView):
    model = Tea
    context_object_name = 'month_tea'
    template_name = 'teazen/month_tea.html'

    def get_queryset(self):
        return Tea.objects.filter(vid=10)


def bonus(request):
    return render(request, 'teazen/bonus.html')


def oplata(request):
    return render(request, 'teazen/oplata.html')


def cart(request):
    return render(request, 'teazen/cart.html')


def contact(request):
    return render(request, 'teazen/contact.html')


def about(request):
    return render(request, 'teazen/about.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Создание пользователя
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )
            user.save()
            return render(request, 'registration/register_done.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def cart(request):
    order_items = OrderItem.objects.filter(user=request.user, ordered=False)
    total = order_items.aggregate(total=Sum(F('quantity') * F('item__price')))['total']
    context = {
        'order_items': order_items,
        'total': total
    }
    return render(request, 'teazen/cart.html', context)


def add_to_cart(request, product_id):
    product = Tea.objects.get(id=product_id)
    order_item, created = OrderItem.objects.get_or_create(
        item=product,
        user=request.user,
        ordered=False
    )
    if created:
        order_item.quantity = 1
        order_item.save()
    else:
        order_item.quantity += 1
        order_item.save()
    return redirect(request.META.get('HTTP_REFERER'))


def remove_from_cart(request, product_id):
    product = Tea.objects.get(id=product_id)
    order_item = OrderItem.objects.get(
        item=product,
        user=request.user,
        ordered=False
    )
    if order_item.quantity > 1:
        order_item.quantity -= 1
        order_item.save()
    else:
        order_item.delete()
    return redirect('cart')


def get_email(request):
    form = EmailForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # Получаем email пользователя из формы и отправляем его
        email = form.cleaned_data['email']
        send_mail('Subject', 'Message', 'korchag1n1v@yandex.ru', [email], fail_silently=False)
        # Добавляем сообщение об успешной отправке
        messages.success(request, 'Email was sent successfully!')

    # Отображаем шаблон с формой и сообщением об отправке
    return render(request, 'teazen/index.html', {'form': form})


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = OrderItem.objects.filter(user=request.user, ordered=False).aggregate(
                total=Sum(F('quantity') * F('item__price')))['total']
            order.save()
            order_items = OrderItem.objects.filter(user=request.user, ordered=False)
            for item in order_items:
                item.ordered = True
                item.save()
            return render(request, 'teazen/order_confirmation.html', {'order': order})
    else:
        form = OrderForm()
    return render(request, 'teazen/create_order.html', {'form': form})


def order_confirmation(request):
    return render(request, 'teazen/order_confirmation.html')
