from django.urls import path
from . import views 

urlpatterns = [
    path('users/',views.RegisterApi.as_view()),
    path('users/<int:id>/',views.Register_Update.as_view()),
    path('users/list/',views.accepted_users.as_view())
]



