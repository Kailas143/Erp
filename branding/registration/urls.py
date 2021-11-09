from django.urls import path 
from . import views 

urlpatterns = [
    path('register/',views.RegisterApi.as_view()),
    path('user/<int:id>/',views.Register_Update.as_view()),
    path('users/',views.Register_Update.as_view())
]
