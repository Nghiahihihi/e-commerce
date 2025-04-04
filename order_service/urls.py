from django.urls import path
from .views import CreateOrderView, CustomerOrderHistoryView

urlpatterns = [
    path('create/<int:customer_id>/', CreateOrderView.as_view(), name='create-order'),
    path('history/<int:customer_id>/', CustomerOrderHistoryView.as_view(), name='order-history'),
]
