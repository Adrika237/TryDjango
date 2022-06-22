"""MyProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact2_view, social2_view, about2_view
from products.views import (
                            product_create_d_view,
                            product_create_h_view,
                            dynamic_lookup
                           )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view),
    path('home/',home_view),
    path('contact/',contact2_view),
    path('social/',social2_view),
    path('about/',about2_view),

    path('prod_create_h/',product_create_h_view),
    path('prod_create_d/',product_create_d_view),

    path('products/<int:my_id>/',dynamic_lookup, name='product'),
]
