"""
URL configuration for ecommerce_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from customer_service.views import (
    home,
    register_form,
    login_form,
    product_list,
    view_cart,
    checkout_form
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/customers/', include('customer_service.urls')),
    path('api/items/', include('item_service.urls')),
    path('api/cart/', include('cart_service.urls')),
    path('api/orders/', include('order_service.urls')),
    path('api/payments/', include('payment_service.urls')),
    path('', home, name='home'),
    path('register/', register_form),
    path('login/', login_form),
    path('products/', product_list),
    path('cart/', view_cart),
    path('checkout/', checkout_form),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)