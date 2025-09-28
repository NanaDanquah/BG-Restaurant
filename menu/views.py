from django.shortcuts import render
from django.views import View
from .models import MenuItem


# Create your views here.
def index(request):
    return render(request, "index.html")


class MenuItemView(View):
    def get(self, request):
        menu = MenuItem.objects.all()
        main_data = {'menu': menu}
        return render(request, "base.html", main_data)
