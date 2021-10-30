from django.urls import path
from . import views 

app_name='inward'

urlpatterns = [
    path('dc/',views.DC_details_add.as_view()),
    path('dc/add/',views.add_dc.as_view()),
    path('dc/bill/list/',views.list_dc_bill.as_view()),

    path('dc/bill/',views.DC_bill_add.as_view()),

    path('materials/add/',views.add_dc_materials.as_view()),
    path('materials/list/',views.list_dc_materials.as_view()),
    path('materials/bill/',views.list_material_bill.as_view()),

    path('receipt/',views.add_receipt.as_view())

]
