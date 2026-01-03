from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='Home'),
    path('about/', views.about, name='About'),
    path('product/', views.product, name='Product'),
    path('contact/', views.contact, name='Contact'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/add/', views.add_product, name='add_product'),
    path('dashboard/edit/<int:id>/', views.edit_product, name='edit_product'),
    path('dashboard/delete/<int:id>/', views.delete_product, name='delete_product'),
]


# from django.urls import path
# from . import views
# from django.template import loader

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('products/', views.products, name='products'),
# ]
