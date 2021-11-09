from django.urls import path 
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('signin/',
		jwt_views.TokenObtainPairView.as_view(),
		name ='token_obtain_pair'),
	path('token/refresh/',
		jwt_views.TokenRefreshView.as_view()),
    path('company/',views.Tenant_company_list.as_view()),
	path('signup/',views.SignupAPI.as_view()),

	path('branding/register/',views.branding_register.as_view()),
	
	path('superadmin/register/',views.get_register_users.as_view()),
	path('superadmin/register/<int:id>/',views.get_register_users.as_view()),
	path('superadmin/accept/users/',views.get_accepted_user_list.as_view()),

	path('employee/',views.add_employee.as_view()),
	path('roles/',views.add_roles.as_view()),
	path('employee/role/',views.add_emp_roles.as_view()),
	path('emp/roles/',views.emp_roles.as_view())
]
