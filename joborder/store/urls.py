from django.urls import path 
from . import views

urlpatterns = [
    path('add/',views.add_stock.as_view()),
    path('list/',views.stock_list.as_view()),
    path('history/',views.stock_history_list.as_view()),
    path('stock/<int:jid>/',views.stock_job_order.as_view())
]
