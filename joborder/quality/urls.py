from django.urls import path
from . import views

app_name='quality'

urlpatterns = [
    path('inspection/',views.inspectionreportdata.as_view()),
    path('inspection/report/',views.inspectionreportint.as_view()),
    path('inspection/list/',views.get_inspection.as_view()),
    path('inspection/list/<int:id>/',views.get_inspection_dc.as_view()),
    path('inspection/report/check/',views.inspectionreportcheck.as_view()),
    path('inspection/dc/',views.inspectionreportdata_dc_inward.as_view()),

]
