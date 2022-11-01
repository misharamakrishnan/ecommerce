from django.urls import path
from . import views
app_name = 'common'

urlpatterns=[
    path('',views.common_index,name = 'index'),
    path('admin',views.common_admin_index,name = 'admin_login'),
    path('seller',views.common_seller_index,name = 'seller_login'),
    path('customer',views.common_customer_index,name = 'customer_login')
]