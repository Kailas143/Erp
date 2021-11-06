from django.urls import path

from . import views


urlpatterns = [
    path('add/',views.add_stock.as_view()),
    path('stocks/',views.Stock_list.as_view()),
    path('history/',views.Stock_HistoryAPI.as_view()),
    path('raw/<int:rid>/',views.stock_raw_materials.as_view())
]
