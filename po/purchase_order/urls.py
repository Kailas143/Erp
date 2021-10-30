from django.urls import path 
from . import views 


app_name='purchase_order'

urlpatterns = [
    path('order/',views.add_po_order_list.as_view()),
    path('order/list/',views.po_order.as_view()),
    path('order/schedule/',views.add_order_schelude.as_view()),
     path('order/schedule/list/',views.po_schedule.as_view())
]
