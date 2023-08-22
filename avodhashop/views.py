from shop.models import *
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def home(request, c_slug=None):
    c_page = None
    prodt = None
    if c_slug != None:
        c_page = get_object_or_404(catego, slug=c_slug)
        prodt = products.objects.filter(category=c_page, available=True)
    else:
        prodt = products.objects.all().filter(available=True)

    cat = catego.objects.all()
    paginator = Paginator(prodt, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'pr': prodt, 'ct': cat, 'pg': pro})

# def home(request):
#     items = products.objects.all()  # Retrieve all items from the Item model
#     return render(request, 'index.html', {'items': items})
