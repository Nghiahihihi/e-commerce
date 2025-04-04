from django.urls import path
from .views import ViewCart, AddToCart, RemoveFromCart

urlpatterns = [
    path('view/<int:customer_id>/', ViewCart.as_view(), name='view-cart'),
    path('add/<int:customer_id>/', AddToCart.as_view(), name='add-to-cart'),
    path('remove/<int:customer_id>/<int:item_id>/', RemoveFromCart.as_view(), name='remove-from-cart'),
    
]
