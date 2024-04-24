from django.urls import path
from . import views
urlpatterns = [
    path('add_helper',views.create_helper,name="adding_helper"),
    path('add_customer',views.create_customer,name="adding_customer"),
    path('assign_helper',views.assign_helper,name="helper_assigning"),
    path('customers_info',views.cust_info,name='cust_info'),
    path("helpers_info",views.helper_info,name="helper_info")
]
