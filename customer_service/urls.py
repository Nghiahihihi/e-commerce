from django.urls import path
from .views import CustomerListView, RegisterCustomer, LoginCustomer, login_form

urlpatterns = [
    path('register/', RegisterCustomer.as_view(), name='register-customer'),
    path('login/', LoginCustomer.as_view(), name='login-customer'),
    path('list/', CustomerListView.as_view(), name='list-customers'),
    path('login/', login_form),
]
