from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import fields, serializers

from .models import (Role, User, company_details, job_components_details,
                     job_order_company_details, job_order_price,
                     job_order_supliers_contact_details,
                     raw_components_details, raw_components_price,
                     supliers_contact_details)


class RoleSerializers(serializers.ModelSerializer):
    class Meta :
        model=Role
        fields='__all__'

class Userserializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields=['username','password','roles','admin_user','status','user_type','profession','phone_no','per_to_contact','contact_per_phone_no','address_l1','address_l2','city','state','country','postcode']

    def save(self):
        reg=User(
                username=self.validated_data['username'],
                admin_user=self.validated_data.get('admin_user'),
            )
        
        password=self.validated_data['password']
        reg.set_password(password)
        reg.save()
        return reg

class Company_details_serializers(serializers.ModelSerializer):
    class Meta :
        model =company_details
        fields='__all__'

class job_components_details_serializers(serializers.ModelSerializer):
    class Meta :
        model = job_components_details
        fields='__all__'

class job_order_company_details_serializers(serializers.ModelSerializer):
    class Meta :
        model = job_order_company_details
        fields='__all__'

class job_order_price_serializers(serializers.ModelSerializer):
    class Meta :
        model = job_order_price
        fields='__all__'

class  job_order_supliers_contact_details_serializers(serializers.ModelSerializer):
    class Meta :
        model =  job_order_supliers_contact_details
        fields='__all__'

class  raw_components_details_serializers(serializers.ModelSerializer):
    class Meta :
        model =  raw_components_details
        fields='__all__'

class  raw_components_price_serializers(serializers.ModelSerializer):
    class Meta :
        model =  raw_components_price
        fields='__all__'

class  supliers_contact_details_serializers(serializers.ModelSerializer):
    class Meta :
        model = supliers_contact_details
        fields='__all__'

class suppliers_details(WritableNestedModelSerializer,serializers.ModelSerializer):
    company_details=Company_details_serializers()
    class Meta :
        model=supliers_contact_details
        fields='__all__'

class job_order_supliers_list(WritableNestedModelSerializer,serializers.ModelSerializer):
    supliers_details=job_order_company_details_serializers()
    class Meta :
        model=job_order_supliers_contact_details
        fields='__all__'

class raw_components_price_list(WritableNestedModelSerializer,serializers.ModelSerializer):
    company_details= Company_details_serializers()
    raw_components_details=raw_components_details_serializers()
    class Meta :
        model=raw_components_price
        fields='__all__'

class job_components_details_list(WritableNestedModelSerializer,serializers.ModelSerializer):
    raw_components_details=raw_components_details_serializers()
    class Meta :
        model=job_components_details
        fields='__all__'

class job_order_price_list(WritableNestedModelSerializer,serializers.ModelSerializer):
    job_order_company_details=job_order_company_details_serializers()
    job_components_details=job_components_details_serializers()
    class Meta :
        model=job_order_price
        fields='__all__'