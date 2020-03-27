from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('item/add', views.ItemCreate.as_view(), name="add_item"),
    path('item/delete/<int:item_id>', views.delete_item, name="delete_item"),
]
