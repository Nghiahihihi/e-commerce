from django.urls import path
from .views import AddItemView, ItemDetailView, ItemListView

urlpatterns = [
    path('add/', AddItemView.as_view(), name='add-item'),
    path('list/', ItemListView.as_view(), name='item-list'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('edit/<int:pk>/', ItemDetailView.as_view(), name='item-edit'),     # dùng chung view
    path('delete/<int:pk>/', ItemDetailView.as_view(), name='item-delete'),
    path('create/', AddItemView.as_view(), name='item-create'), 
]
