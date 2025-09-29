from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name="menu"),
    path('booking', views.bookings, name="booking")


]
