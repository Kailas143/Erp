from django.urls import path 
from . import views 

app_name='quality'

urlpatterns = [
     path('inspection/dc/',views.inspectionreportdata_raw_dc.as_view()),
    path('inspection/',views.inspectionreportdata_raw_bill_material.as_view()),
    path('param/',views.list_parameters.as_view()),
    path('report/datas/',views.list_report_details.as_view()),
    path('report/rows/',views.inspectionreportint.as_view()),
    path('report/check/',views.inspectionreportcheck.as_view())
    
    

]
