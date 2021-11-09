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
from .dynamic  import dynamic_link
import requests
import json


class Tenant_company_list(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=TenantSerializer
    queryset=Tenant_Company.objects.all()
    permission_classes = [IsAuthenticated]

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