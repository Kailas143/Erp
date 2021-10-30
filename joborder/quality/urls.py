from django.urls import path
from . import views

app_name='quality'

urlpatterns = [
    path('inspection/',views.inspectionreportdata.as_view()),
    path('inspection/report/',views.inspectionreportint.as_view()),
    path('inspection/report/check/',views.inspectionreportcheck.as_view()),

]
