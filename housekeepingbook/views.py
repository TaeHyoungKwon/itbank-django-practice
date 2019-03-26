from django.shortcuts import render, HttpResponse
from .models import HouseKeepingBook


def index(request):
    acc_type = request.GET.get('type')
    amount = request.GET.get('amount')
    print(amount)

    if acc_type == 'out' and amount != "0":
        obj = HouseKeepingBook.objects.filter(expense__gt=int(amount))
    elif acc_type == 'in' and amount != "0":
        obj = HouseKeepingBook.objects.filter(income__gt=int(amount))
    else:
        obj = HouseKeepingBook.objects.all()

    context = {
        "data": obj
    }
    return render(request, "housekeepingbook/home.html", context)


def income_list(request):
    obj = HouseKeepingBook.objects.filter(income__gt=0)
    print(obj)
    context = {
        "data": obj
    }
    return render(request, "housekeepingbook/home.html", context)


def expense_list(request):
    obj = HouseKeepingBook.objects.filter(expense__gt=0)
    context = {
        "data": obj
    }
    return render(request, "housekeepingbook/home.html", context)


def list(request):
    obj = HouseKeepingBook.objects.all()
    context = {
        "data": obj
    }
    return render(request, "housekeepingbook/home.html", context)
