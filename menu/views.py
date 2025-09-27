from django.shortcuts import render
from django.views import View
from .models import MenuItem


# Create your views here.
class MenuItemView(View):
    def get(self, request):
        menu = MenuItem.objects.all()
        context = {'menu': menu}
        return render(request, "index.html", context)
