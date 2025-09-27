from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuItemView.as_view(), name="menu-items"),

]
