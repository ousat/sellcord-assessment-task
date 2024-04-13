from django.urls import path
from amazon import views

urlpatterns = [
    path("disputes", views.disputes_page),
    path("customers/create", views.save_customer),
    path("customers/list", views.get_customers),
    path("orders/create", views.save_order),
    path("orders/list", views.get_orders),
    path("returns/create", views.save_return),
    path("returns/list", views.get_returns),
    path("create-disputes", views.save_dispute),
    path("get-disputes-table", views.get_disputes),
]
