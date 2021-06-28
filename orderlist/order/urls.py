from django.contrib import admin
from django.urls import include,path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-customer/', views.insert_data_customer),
    path('create-product/', views.insert_data_product),
    path('', views.open_mainpage),
    path('create-order/', views.insert_data_order),
    path('edit-order/', views.edit_order),

    
]