from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import HouseKeepingBook
from .forms import HouseKeepingBookForm


def hkb_create(request):
    form = HouseKeepingBookForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = HouseKeepingBook()
    context = {
        'form': form
    }
    return render(request, 'housekeepingbook/create.html', context)


def hkb_detail(request, id):
    obj = get_object_or_404(HouseKeepingBook, id=id)
    context = {
        'object': obj
    }

    print(obj)

    return render(request, 'housekeepingbook/detail.html', context)


def hkb_list(request):
    obj = HouseKeepingBook.objects.all()
    context = {
        'object_list': obj
    }

    return render(request, 'housekeepingbook/list.html', context)


def hkb_delete(request, id):
    obj = get_object_or_404(HouseKeepingBook, id=id)

    if request.method == 'POST':
        obj.delete()
        return redirect("housekeepingbook:list")

    context = {
        'object': obj
    }

    return render(request, 'housekeepingbook/delete.html', context)


def hkb_update(request, id):
    obj = get_object_or_404(HouseKeepingBook, id=id)
    form = HouseKeepingBookForm(request.POST or None, instance=obj)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(obj.get_absolute_url())

    context = {
        "object": obj,
        "form": form
    }
    return render(request, "housekeepingbook/form.html", context)
