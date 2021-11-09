from rest_framework import serializers
from . models import Register


class RegisterSerializer(serializers.ModelSerializer):
    class Meta :
        model=Register
        fields=['first_name','middle_name','last_name','email','url','address','phone_number','city','state','company_name','domain','country']
     
    

class RegisterUpdateSerializer(serializers.ModelSerializer):
    class Meta :
        model=Register
        fields='__all__'