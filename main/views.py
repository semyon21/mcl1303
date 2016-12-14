from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required


def index(request):
    """Домашняя страница сайта"""
    items = Item.objects.order_by('-date_added')[0::1]
    context = {'items' : items}
    return render(request, 'main/index.html', context)

def add_item(request):
    """Создает новость"""
    if request.method != 'POST':
        form = ItemForm()
    else:
        form = ItemForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('main:index'))
    context = {'form': form}
    return render(request, 'main/add_item.html', context)

def item_info(request, item_id):
    item = Item.objects.get(id = item_id)
    context = {'item': item}
    return render(request, 'main/item_info.html', context)