from django.urls import path, re_path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^black_tea/$', views.BlackTeaListView.as_view(), name='black_tea'),
    re_path(r'^green_tea/$', views.GreenTeaListView.as_view(), name='green_tea'),
    re_path(r'^flower_tea/$', views.FlowerTeaListView.as_view(), name='flower_tea'),
    re_path(r'^fruit_tea/$', views.FruitTeaListView.as_view(), name='fruit_tea'),
    re_path(r'^month_tea/$', views.MonthTeaListView.as_view(), name='month_tea'),
    re_path(r'^oplata/$', views.oplata, name='oplata'),
    re_path(r'^contact/$', views.contact, name='contact'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^bonus_card/$', views.bonus, name='bonus_card'),
    re_path(r'^register/$', views.register, name='register'),
    path('cart/', views.cart, name='cart'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('teazen/order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation')
]
