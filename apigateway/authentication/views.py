from rest_framework import generics,mixins, permissions 
from rest_framework.views import APIView
from . models import User,Tenant_Company,emp_roles,Employee
from . serializers import TenantSerializer,RegisterSerializer,Employee_RegisterSerializer,emp_role_serializers,employee_roles_details,employee_roles
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsJoborder,IsProduction,IsRawmaterials
from .dynamic  import dynamic_link
import requests
import json
from .utilities import get_tenant


class Tenant_company_list(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=TenantSerializer
    queryset=Tenant_Company.objects.all()
    permission_classes = [IsAuthenticated,IsRawmaterials]

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)


class SignupAPI(generics.GenericAPIView, mixins.ListModelMixin, APIView):

    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registerd Succesfully'
            data['username'] = account.username
            data['tenant_company'] = account.tenant_company.company_name
            data['is_admin'] = account.is_admin
            token, create = Token.objects.get_or_create(user=account)
            domain=account.tenant_company.domain
        else:
            data = serializer.errors

        # it returns all the datas in the data dictionary as a Response after the registration

        return Response(data)

class branding_register(APIView):
    permission_classes = [IsAuthenticated,IsRawmaterials]

    def get(self, request):
        
        services = 'branding'
        dynamic = dynamic_link(services, 'branding/register')
        
        response = requests.get(dynamic).json()
      
        return Response(response)

    def post(self, request):
       
        # the details for new registration or branding,this datas should be post in the url
        datas = {
            "first_name": request.data['first_name'],
            "middle_name": request.data['middle_name'],
            "last_name": request.data['last_name'],
            "email": request.data['email'],
            "address": request.data['address'],
            "url": request.data['url'],
            "company_name": request.data['company_name'],
            "phone_number": request.data['phone_number'],
            "city": request.data['city'],
            "state": request.data['state'],
            "domain" :request.data['domain'],
            "country": request.data['country']

        }
        # connecting the url from the branding project and then the datas as dictionary as passing with the url for POST method
        
        services = 'branding'
        dynamic = dynamic_link(services,'branding/register')
        response = requests.post(dynamic, data=datas).json()
        return Response(response)

    
class get_register_users(APIView):
    def get(self,request) :
        services='superadmin'
        dynamic=dynamic_link(services,'branding/users')
        response=requests.get(dynamic).json()
        return Response(response)


class get_accepted_user_list(APIView):
    def get(self,request):
        services='superadmin'
        dynamic=dynamic_link(services,'branding/users/list')
        response=requests.get(dynamic).json()
        return Response(response)


class superadmin_update_status(APIView):
     def get(self,request,id):
        services='branding'
        dynamic=dynamic_link(services,'branding/user/'+str(id))
        print(dynamic)
        response=requests.get(dynamic).json()
   
       
        return Response(response)

class add_employee(generics.GenericAPIView,APIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=Employee_RegisterSerializer
    queryset=User.emp_objects.all()
    def get(self,request) :
        return self.list(request)
    
    def post(self,request) :
        return self.create(request)

class add_roles(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=emp_role_serializers
    queryset= emp_roles.objects.all()

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

class add_emp_roles(generics.GenericAPIView,APIView,mixins.CreateModelMixin,mixins.ListModelMixin):
  
    serializer_class= employee_roles_details
    queryset=Employee.objects.all()

    def get(self,request):
        return self.list(request)
    
    def post(self,request) :
        return self.create(request)

class emp_roles(generics.GenericAPIView,APIView,mixins.CreateModelMixin,mixins.ListModelMixin):
  
    serializer_class= employee_roles
    queryset=Employee.objects.all()

    def get(self,request):
        return self.list(request)

class get_company_details(APIView):
    # #permission_classes = [IsAuthenticated,]

    def get(self,request):
        
    
        services='admin'
        dynamic=dynamic_link(services,'master/company/details/list')
        response=requests.get(dynamic).json()
        return Response(response)


         

class get_purchase_company_details(APIView):
   
    def get(self,request):
        
        # username_r=request.user.username
        # tenant_id=request.user.tenant_company.id
        # user=User.admin_objects.get_queryset(username=username_r,tenant_id=tenant_id).exists()
        # print(user)
        # data={}
        # if user :
    
            services='admin'
            dynamic=dynamic_link(services,'master/purchase/company/list')
            response=requests.get(dynamic).json()
            return Response(response)

        # else :

        #    data['error']="Please login as admin user"
        #    return Response(data)

class get_supplier_contact(APIView):
    #permission_classes = [IsAuthenticated,]

    def get(self,request):
     
        #username_r=request.user.username
        # tenant_id=request.user.tenant_company.id
        # user=User.admin_objects.get_queryset(username=username_r,tenant_id=tenant_id).exists()
        # print(user)
        # data={}
        # if user :
    
            services='admin'
            dynamic=dynamic_link(services,'master/suppliers/details/list')
            response=requests.get(dynamic).json()
            return Response(response)

        # else :

        #    data['error']="Please login as admin user"
        #    return Response(data)

class get_joborder_company_details(APIView):
    #permission_classes = [IsAuthenticated,]

    def get(self,request):
     
        # username_r=request.user.username
        # tenant_id=request.user.tenant_company.id
        # user=User.admin_objects.get_queryset(username=username_r,tenant_id=tenant_id).exists()
        # data={}
        # if user :
    
            services='admin'
            dynamic=dynamic_link(services,'master/job/company/list')
            response=requests.get(dynamic).json()
            return Response(response)

        # else :

        #    data['error']="Please login as admin user"
        #    return Response(data)

class get_joborder_company_details(APIView):
    # #permission_classes = [IsAuthenticated,]

    def get(self,request):
     
        # username_r=request.user.username
        # tenant_id=request.user.tenant_company.id
        # user=User.admin_objects.get_queryset(username=username_r,tenant_id=tenant_id).exists()
        # data={}
        # if user :
    
            services='admin'
            dynamic=dynamic_link(services,'master/job/company/list')
            response=requests.get(dynamic).json()
            return Response(response)

        # else :

        #    data['error']="Please login as admin user"
        #    return Response(data)

class get_joborder_contact_details(APIView):
    # #permission_classes = [IsAuthenticated,]

    def get(self,request):
     
        # username_r=request.user.username
        # tenant_id=request.user.tenant_company.id
        # user=User.admin_objects.get_queryset(username=username_r,tenant_id=tenant_id).exists()
        # data={}
        # if user :
    
            services='admin'
            dynamic=dynamic_link(services,'master/job/contact/list')
            response=requests.get(dynamic).json()
            return Response(response)

        # else :

        #    data['error']="Please login as admin user"
        #    return Response(data)


class get_rawmaterials_details(APIView):
    #permission_classes = [IsAuthenticated,]

    def get(self,request):
     
        # username_r=request.user.username
        # tenant_id=request.user.tenant_company.id
        # user=User.admin_objects.get_queryset(username=username_r,tenant_id=tenant_id).exists()
        # data={}
        # if user :
    
            services='admin'
            dynamic=dynamic_link(services,'master/raw/list')
            response=requests.get(dynamic).json()
            return Response(response)

        # else :

        #    data['error']="Please login as admin user"
        #    return Response(data)

class get_raw_price_details(APIView):
    #permission_classes = [IsAuthenticated,]

    def get(self,request):
     
        # username_r=request.user.username
        # tenant_id=request.user.tenant_company.id
        # user=User.admin_objects.get_queryset(username=username_r,tenant_id=tenant_id).exists()
        # data={}
        # if user :
    
            services='admin'
            dynamic=dynamic_link(services,'master/raw/price/list')
            response=requests.get(dynamic).json()
            return Response(response)

        # else :

        #    data['error']="Please login as admin user"
        #    return Response(data)

class get_job_component_details(APIView):
    #permission_classes = [IsAuthenticated,]

    def get(self,request):
     
        # username_r=request.user.username
        # tenant_id=request.user.tenant_company.id
        # user=User.admin_objects.get_queryset(username=username_r,tenant_id=tenant_id).exists()
        # data={}
        # if user :
    
            services='admin'
            dynamic=dynamic_link(services,'master/job/component/list')
            response=requests.get(dynamic).json()
            return Response(response)

        # else :

        #    data['error']="Please login as admin user"
        #    return Response(data)

class get_job_order_price(APIView):
    #permission_classes = [IsAuthenticated,]

    def get(self,request):
        # print(';;;')
        # username_r=request.user.username
        # print(request.user.tenant_company.domain,'ll')
        # # print(get_tenant(request),'88')
        # tenant_id=request.user.tenant_company.id
        # # print(tenant_id,'ttt')
        # user=User.admin_objects.get_queryset(username=username_r,tenant_id=tenant_id).exists()
        # data={}
        # if user :
    
            services='admin'
            dynamic=dynamic_link(services,'master/job/order/price/list')
            response=requests.get(dynamic).json()
            return Response(response)

        # else :

        #    data['error']="Please login as admin user"
        #    return Response(data)



class add_company_details(APIView):
    # #permission_classes = [IsAuthenticated,]

    def post(self,request):
        
        # username_r=request.user.username
        # tenant_id=request.user.tenant_company.id
        # # tenant_id=get_tenant(request)
        # user=User.admin_objects.get_queryset(username=username_r,tenant_id=tenant_id).exists()
        # print(user)
        # data={}
        # if user :
        #     datas={
               
        #         "tenant_id" : tenant_id,
        #         "company_name": request.data['company_name'],
        #         "address_line1":request.data['address_line1'],
        #         "address_line2":request.data['address_line2'],
        #         "address_line3":request.data['address_line3'],
        #         "office_email": request.data['office_email'],
        #         "office_pnone_no": request.data['office_pnone_no'],
        #         "gst_no": request.data['gst_no'],
        #         "acc_no": request.data['acc_no'],
        #         "ifsc_code": request.data['ifsc_code'],
        #         "bank_name": request.data['bank_name'],
        #         "branch_name": request.data['branch_name'],
        #         "purchase_company":request.data['purchase_company'],
        #         "ratings": request.data['ratings'],
        #         "vendor_code": request.data['vendor_code'],
        #         "description": request.data['description'],
            
        #     } 
            services='admin'
            dynamic=dynamic_link(services,'master/company/details')
            response=requests.post(dynamic,data=request.data).json()
           
            return Response(response)

        # else :

        #    data['error']="Sorry data are not added"
        #    return Response(data)

class add_supplier_contact(APIView):
    # #permission_classes = [IsAuthenticated,]

    def post(self,request):
        data={}
        
    #     username_r=request.user.username
    #     tenant_id=request.user.tenant_company.id
    #     # tenant_id=get_tenant(request)
    #     user=User.admin_objects.get_queryset(username=username_r,tenant_id=tenant_id).exists()
    #     print(user)
    #     data={}
    #     if user :
    #         datas={
    #                 "tenant_id": tenant_id,
    #                 "company_details": request.data['company_details'],
    #                 "email": request.data['email'],
    #                 "phone_no": request.data['phone_no'],
    #                 "name": request.data['name'],
    #                 "post":request.data['post']
    
            
    #         } 
        services='admin'
        dynamic=dynamic_link(services,'master/suppliers/contact')
        response=requests.post(dynamic,data=request.data).json()
        data['success']="Record added successfully"
        return Response(response)

        # else :

        #    data['error']="Sorry data are not added"
        #    return Response(data)

class add_joborder_company_details(APIView):
    #permission_classes = [IsAuthenticated,]

    def post(self,request):
        
        # username_r=request.user.username
        # tenant_id=request.user.tenant_company.id
        # # tenant_id=get_tenant(request)
        # user=User.admin_objects.get_queryset(username=username_r,tenant_id=tenant_id).exists()
        # print(user)
        # data={}
        # if user :
            # datas= {
                  
                    # "tenant_id": tenant_id,
                    # "company_name": request.data['company_name'],
                    # "address_line1": request.data['address_line1'],
                    # "address_line2": request.data['address_line2'],
                    # "address_line3": request.data['address_line3'],
                    # "office_email": request.data['office_email'],
                    # "office_pnone_no": request.data['office_pnone_no'],
                    # "gst_no": request.data['gst_no'],
                    # "acc_no": request.data['acc_no'],
                    # "ifsc_code": request.data['ifsc_code'],
                    # "bank_name": request.data['bank_name'],
                    # "branch_name": request.data['branch_name'],
                    # "job_work_code": request.data['job_work_code'],
                    # "ratings": request.data['ratings'],
                    # "description": request.data['description']
            services='admin'
            dynamic=dynamic_link(services,'master/job/company')
            response=requests.post(dynamic,data=request.data).json()
          
            return Response(response)

        # else :

        #    data['error']="Sorry data are not added"
        #    return Response(data)

class add_joborder_contact_details(APIView):
    #permission_classes = [IsAuthenticated,]

    def post(self,request):
        
    #     username_r=request.user.username
    #     tenant_id=request.user.tenant_company.id
    #     # tenant_id=get_tenant(request)
    #     user=User.admin_objects.get_queryset(username=username_r,tenant_id=tenant_id).exists()
    #     print(user)
    #     data={}
    #     if user :
    #         datas= {
                  
    #                 "tenant_id": tenant_id,
    #                 "supliers_details": request.data['supliers_details'],
    #                 "email": request.data['email'],
    #                 "phone_no":request.data['phone_no'],
    #                 "name": request.data['phone_no'],
    #                 "post": request.data['post'],
    # }

            services='admin'
            dynamic=dynamic_link(services,'master/job/contact')
            response=requests.post(dynamic,data=request.data).json()
            return Response(response)

        # else :

        #    data['error']="Sorry data are not added"
        #    return Response(data)

class add_rawmaterials_details(APIView):
    #permission_classes = [IsAuthenticated,]

    def post(self,request):
        
        # username_r=request.user.username
        # tenant_id=request.user.tenant_company.id
        # # tenant_id=get_tenant(request)
        # user=User.admin_objects.get_queryset(username=username_r,tenant_id=tenant_id).exists()
        # print(user)
        # data={}
        # if user :
        #     datas= {
                   
        #             "tenant_id":tenant_id,
        #             "c_name": request.data['c_name'],
        #             "c_code":  request.data['c_code'],
        #             "c_unit":  request.data['c_unit'],
        #             "c_material_grade":  request.data['c_material_grade'],
        #             "c_model_name":  request.data['c_model_name'],
        #             "wire":  request.data['wire'],
        #             "winding":  request.data['winding'],
        #             "shaft":  request.data['shaft']
        #     }
                

            services='admin'
            dynamic=dynamic_link(services,'master/raw')
            response=requests.post(dynamic,data=request.data).json()
            return Response(response)

       

class add_raw_price_details(APIView):
    #permission_classes = [IsAuthenticated,]

    def post(self,request):
        
        # username_r=request.user.username
        # tenant_id=request.user.tenant_company.id
        # # tenant_id=get_tenant(request)
        # user=User.admin_objects.get_queryset(username=username_r,tenant_id=tenant_id).exists()
        # print(user)
        # data={}
        # if user :
        #     datas= {
                     
        #             "tenant_id":tenant_id,
        #             "company_details":request.data['company_details'],
        #             "raw_components_details": request.data['raw_components_details'],
        #             "c_sgst":  request.data['c_sgst'],
        #             "c_cgst":  request.data['c_cgst'],
        #             "c_igst":  request.data['c_igst'],
        #             "price":  request.data['price'],
        #             "debit_price":  request.data['debit_price'],
        #             "expire":  request.data['expire']
        #     }
                

            services='admin'
            dynamic=dynamic_link(services,'master/raw/price')
            response=requests.post(dynamic,data=request.data).json()
            # data['success']="Record added successfully"
            return Response(response)

        # else :

        #    data['error']="Sorry data are not added"
        #    return Response(data)

class add_job_component_details(APIView):
    #permission_classes = [IsAuthenticated,]

    def post(self,request):
        
        # username_r=request.user.username
        # tenant_id=request.user.tenant_company.id
        # # tenant_id=get_tenant(request)
        # user=User.admin_objects.get_queryset(username=username_r,tenant_id=tenant_id).exists()
        # print(user)
        # data={}
        # if user :
        #     datas= {
                     
        #             "tenant_id":tenant_id,
        #             "job_order_company_details": request.data['job_order_company_details'],
        #             "job_components_details":  request.data['job_components_details'],
        #             "c_sgst":  request.data['c_sgst'],
        #             "c_cgst":  request.data['c_cgst'],
        #             "c_igst":  request.data['c_igst'],
        #             "price":  request.data['price'],
        #             "debit_price":  request.data['debit_price'],
        #             "expire":  request.data['expire']
        #     }
                

            services='admin'
            dynamic=dynamic_link(services,'master/job/component')
            response=requests.post(dynamic,data=request.data).json()
            # data['success']="Record added successfully"
            return Response(response)

        # else :

        #    data['error']="Sorry data are not added"
        #    return Response(data)


class add_job_order_price(APIView):
    #permission_classes = [IsAuthenticated,]

    def post(self,request):
        
        # username_r=request.user.username
        # tenant_id=request.user.tenant_company.id
        # # tenant_id=get_tenant(request)
        # user=User.admin_objects.get_queryset(username=username_r,tenant_id=tenant_id).exists()
        # print(user)
        # data={}
        # if user :
        #     datas= {
                     
        #             "tenant_id":tenant_id,
        #             "job_order_company_details": request.data['job_order_company_details'],
        #             "job_components_details":  request.data['job_components_details'],
        #             "c_sgst":  request.data['c_sgst'],
        #             "c_cgst":  request.data['c_cgst'],
        #             "c_igst":  request.data['c_igst'],
        #             "price":  request.data['price'],
        #             "debit_price":  request.data['debit_price'],
        #             "expire":  request.data['expire']
        #     }
                

            services='admin'
            dynamic=dynamic_link(services,'master/job/component')
            response=requests.post(dynamic,data=request.data).json()
            # data['success']="Record added successfully"
            return Response(response)

        # else :

        #    data['error']="Sorry data are not added"
        #    return Response(data)

class get_inward_dc_details(APIView):

    def get(self,request):
            services='raw_materials'
            dynamic=dynamic_link(services,'inward/dc/list')
            response=requests.get(dynamic,data=request.data).json()
            # data['success']="Record added successfully"
            return Response(response)


class get_inward_dc_materials(APIView):

    def get(self,request):
            services='raw_materials'
            dynamic=dynamic_link(services,'inward/materials/list')
            response=requests.get(dynamic,data=request.data).json()
            # data['success']="Record added successfully"
            return Response(response)


class get_inward_dc_bill(APIView):

    def get(self,request):
            services='raw_materials'
            dynamic=dynamic_link(services,'inward/dc/bill/list')
            response=requests.get(dynamic,data=request.data).json()
            # data['success']="Record added successfully"
            return Response(response)

class get_inward_dc_materials_bill(APIView):

    def get(self,request):
            services='raw_materials'
            dynamic=dynamic_link(services,'inward/materials/bill/list')
            response=requests.get(dynamic,data=request.data).json()
            # data['success']="Record added successfully"
            return Response(response)

class add_inward_dc(APIView):

    def post(self,request):
            services='raw_materials'
            dynamic=dynamic_link(services,'inward/dc')
            response=requests.post(dynamic,json=request.data).json()
            # data['success']="Record added successfully"
            return Response(response)


class add_inward_dc_bill(APIView):

    def post(self,request):
            services='raw_materials'
            dynamic=dynamic_link(services,'inward/dc/bill')
            response=requests.post(dynamic,json=request.data).json()
            # data['success']="Record added successfully"
            return Response(response)