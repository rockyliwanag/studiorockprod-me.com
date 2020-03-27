from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from .models import Item
from .forms import ItemForm
# Create your views here.


def home(request):
    items = Item.objects.all()
    return render(request, 'index.html', {
        'items': items
    })


class ItemCreate(CreateView):
    model = Item
    success_url = '/'
    fields = ['description']

    def form_valid(self, form):
        return super().form_valid(form)


def delete_item(request, item_id):
    Item.objects.get(id=item_id).delete()
    return redirect('home')
