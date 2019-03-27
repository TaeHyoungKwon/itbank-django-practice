from django.shortcuts import (
    render, get_object_or_404, HttpResponseRedirect, redirect)
from .models import NameCard
from .forms import NameCardForm
from .utils import (search_query,)


def home(request):
    obj = NameCard.objects.all()
    query = request.GET.get("q")

    if query:
        obj = search_query(obj)

    context = {
        'object_list': obj
    }

    return render(request, 'namecard/home.html', context)


def detail(request, id):
    obj = get_object_or_404(NameCard, id=id)
    context = {
        'object': obj
    }

    return render(request, 'namecard/detail.html', context)


def create(request):
    form = NameCardForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = NameCardForm()
        return redirect("namecard:home")

    context = {
        'form': form
    }
    return render(request, 'namecard/create.html', context)


def update(request, id):
    obj = get_object_or_404(NameCard, id=id)
    form = NameCardForm(request.POST or None, instance=obj)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(obj.get_absolute_url())

    context = {
        'object': obj,
        'form': form
    }
    return render(request, "namecard/update.html", context)


def delete(request, id):
    obj = get_object_or_404(NameCard, id=id)
    print(obj)
    if request.method == 'POST':
        obj.delete()
        return redirect("namecard:home")

    context = {
        'object': obj
    }

    return render(request, 'namecard/delete.html', context)
