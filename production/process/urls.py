from django.urls import path 
from . import views

app_name='process'

urlpatterns = [
    path('process/',views.ProcessViewset.as_view()),
    path('bom/',views.proces_bom.as_view()),
    path('bom/<int:id>/',views.process_bom_crud.as_view()),
    path('details/<int:id>/',views.process_details_crud.as_view())
]
