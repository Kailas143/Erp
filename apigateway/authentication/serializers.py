from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model
from .models import Employee, Tenant_Company, User, emp_roles
from drf_writable_nested.serializers import WritableNestedModelSerializer

User=get_user_model()

class RegisterSerializer(serializers.ModelSerializer):

    class Meta :
        model = User 
        fields = ['username','tenant_company','password','is_admin']
        
    def save(self):
        reg=User(
                username=self.validated_data['username'],
                tenant_company=self.validated_data['tenant_company'],
                is_admin=self.validated_data.get('is_admin'),
            
            )
        
        password=self.validated_data['password']
        reg.set_password(password)
        reg.save()
        return reg

class TenantSerializer(serializers.ModelSerializer):
    class Meta :
        model=Tenant_Company
        fields=['id','company_name','city','domain','address','phone_number','state','country','joined_data']


class Employee_RegisterSerializer(serializers.ModelSerializer):

    class Meta :
        model = User 
        fields = ['username','tenant_company','password','is_employee']
        
    def save(self):
        reg=User(
                username=self.validated_data['username'],
                tenant_company=self.validated_data['tenant_company'],
               
                is_employee=self.validated_data.get('is_employee')
            )
        
        password=self.validated_data['password']
        reg.set_password(password)
        reg.save()
        return reg  
 
class emp_role_serializers(serializers.ModelSerializer):
    class Meta :
        model = emp_roles
        fields='__all__'

 
class emp_role_list_serializers(serializers.ModelSerializer):
    tenant_company=TenantSerializer()
    class Meta :
        model = emp_roles
        fields=['tenant_company','roles']

class employee_roles(WritableNestedModelSerializer,serializers.ModelSerializer):
    roles=emp_role_list_serializers(many=True)
    class Meta :
        model=Employee
        fields=['employee','roles']


class employee_roles_details(serializers.ModelSerializer):
    
 
   
    # roles=emp_role_serializers(many=True,queryset=emp_roles.objects.all())
    class Meta :
        model=Employee
        fields=['tenant_company','employee','roles']