
from django.urls import path
from . import views
urlpatterns = [
    path('', views.customer_list),
    path('add/', views.addCustomer),
    path('edit/<id>', views.editCustomer),
    path('delete/<eid>', views.deleteCustomer),
    path('view/<eid>', views.viewCustomer),
]
