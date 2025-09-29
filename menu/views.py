from django.shortcuts import render
from django.views import View
from .models import MenuItem
from .forms import BookingForms


# Create your views here.
def index(request):
    return render(request, "index.html")


# def menu(request):
#     return render(request, "menu.html")


class MenuItemView(View):
    def get(self, request):
        menu = MenuItem.objects.all()
        main_data = {'menu': menu}
        return render(request, "menu.html", main_data)


def bookings(request):
    form = BookingForms()

    if request.method == "POST":
        form = BookingForms(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "booking.html", {'form': form})
