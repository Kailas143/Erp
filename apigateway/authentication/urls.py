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

	#superadmin
	
	path('superadmin/register/',views.get_register_users.as_view()),
	path('superadmin/register/<int:id>/',views.get_register_users.as_view()),
	path('superadmin/accept/users/',views.get_accepted_user_list.as_view()),

	#employee

	path('employee/',views.add_employee.as_view()),
	path('roles/',views.add_roles.as_view()),
	path('employee/role/',views.add_emp_roles.as_view()),
	path('emp/roles/',views.emp_roles.as_view()),

	#admin  get details
	path('admin/company/',views.get_company_details.as_view()),
	path('purchase/company/list/',views.get_purchase_company_details.as_view()),
	path('suppliers/contact/',views.get_supplier_contact.as_view()),
	path('joborder/company/',views.get_joborder_company_details.as_view()),
	path('joborder/contact/',views.get_joborder_contact_details.as_view()),#job order contact details get method
	path('admin/rawmaterials/',views.get_rawmaterials_details.as_view()),#raw_component details
	path('admin/rawmaterials/price/',views.get_raw_price_details.as_view()),#raw_component_price details
	path('admin/job/component/',views.get_job_component_details.as_view()),
	path('admin/job/order/price/',views.get_job_order_price.as_view()),

	#admin post data

	path('add/admin/company/',views.add_company_details.as_view()),
	path('add/suppliers/contact/',views.add_supplier_contact.as_view()),
	path('add/joborder/company/',views.add_joborder_company_details.as_view()),
	path('add/joborder/contact/',views.add_joborder_contact_details.as_view()),#job order contact details get method
	path('add/rawmaterials/',views.add_rawmaterials_details.as_view()),#raw_component details
	path('add/rawmaterials/price/',views.add_raw_price_details.as_view()),#raw_component_price details
	path('add/job/component/',views.add_job_component_details.as_view()),
	path('add/job/order/price/',views.add_job_order_price.as_view()),

	#rawmaterials

	#inward
	path('raw/inward/dc/list/',views.get_inward_dc_details.as_view()),
	path('raw/inward/dc/materials/list/',views.get_inward_dc_materials.as_view()),
	path('raw/inward/dc/bill/list/',views.get_inward_dc_bill.as_view()),
	path('raw/inward/materials/bill/list/',views.get_inward_dc_materials_bill.as_view()),
	path('raw/inward/add/dc/',views.add_inward_dc_bill.as_view()),
	path('raw/inward/add/dc/bill/',views.add_inward_dc_bill.as_view()),


]
