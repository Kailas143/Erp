from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

app_name='master'

urlpatterns = [
    path('api/login/',
		jwt_views.TokenObtainPairView.as_view(),
		name ='token_obtain_pair'),
	path('api/token/refresh/',
		jwt_views.TokenRefreshView.as_view(),
		name ='token_refresh'),
    path('register/',views.User_register.as_view(),name='user_register'),

    path('roles/',views.add_roles.as_view(),name='role'),
    path('roles/<int:id>/',views.roles_Update.as_view(),name='role'),
    path('roles/list/',views.roles_list.as_view(),name='role'),

    path('company/details/',views.add_company_details.as_view(),name='add_company_details'),
    path('company/details/<int:id>/',views.company_details_Update.as_view(),name='add_company_details'),
    path('company/details/list/',views.company_list.as_view(),name='add_company_details'),

    path('suppliers/contact/',views.add_supliers_contact_details.as_view(),name='add_supliers_contact_details'),
    path('suppliers/contact/<int:id>/',views.supliers_contact_details_Update.as_view(),name='add_supliers_contact_details'),
    path('suppliers/details/list/',views.list_suppliers_details.as_view(),name='add_company_details'),
    
    path('job/company/',views.add_job_order_company_details.as_view(),name='.add_job_order_company_details'),
    path('job/company/<int:id>/',views.job_order_company_details_Update.as_view(),name='.add_job_order_company_details'),
    path('job/company/list/',views.job_order_company_details_Update.as_view(),name='.add_job_order_company_details'),

    path('job/contact/',views.add_job_order_supliers_contact_details.as_view(),name=' add_job_order_supliers_contact_details'),
    path('job/contact/<int:id>/',views.job_order_supliers_contact_details_Update.as_view(),name=' add_job_order_supliers_contact_details'),
    path('job/contact/list/',views.job_order_supliers_contact_details_Update.as_view(),name=' add_job_order_supliers_contact_details'),

    
    path('raw/',views.add_raw_components_details.as_view(),name='add_raw_components_details'),
    path('raw/<int:id>/',views.raw_components_details_Update.as_view(),name='add_raw_components_details'),
    path('raw/list/',views.raw_components_details_Update.as_view(),name='add_raw_components_details'),

    path('raw/price/',views.add_raw_components_price.as_view(),name='add_raw_components_price'),
    path('raw/price/<int:id>/',views.raw_components_price_Update.as_view(),name='add_raw_components_price'),
    path('raw/price/list/',views.raw_components_price_Update.as_view(),name='add_raw_components_price'),

    path('job/component/',views.add_job_components_details.as_view(),name='add_job_components_details'),
    path('job/component/<int:id>/',views.job_components_details_Update.as_view(),name='add_job_components_details'),
    path('job/component/list/',views.job_components_details_Update.as_view(),name='add_job_components_details'),

    path('job/order/price/',views.add_job_order_price.as_view(),name='add_job_order_price'),
    path('job/order/price/<int:id>/',views.job_order_price_Update.as_view(),name='add_job_order_price'),
    path('job/order/price/list/',views.job_order_price_Update.as_view(),name='add_job_order_price'),



    # path('suppliers/details/list/',views.list_suppliers_details.as_view(),name='add_company_details'),
    # path('company/details/',views.add_company_details.as_view(),name='add_company_details')

]
