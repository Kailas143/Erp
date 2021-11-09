import json
import smtplib

import requests
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from branding.models import Registered_users

from .serializers import register_serializers
from superadmin.settings import EMAIL_HOST_USER


from .dynamic import dynamic_link


# from . models import Branding_Users


# Create your views here.

#GET all the registred users details from branding

class RegisterApi(APIView):
    def get(self,request):
        services='branding'
        dynamic=dynamic_link(services,'branding/users')
        response=requests.get(dynamic).json()
        return Response(response)

class accepted_users(generics.GenericAPIView,mixins.ListModelMixin):
    serializer_class=register_serializers
    queryset=Registered_users.objects.all()
    def get(self,request):
        return self.list(request)

class Register_Update(APIView):
    
    def get(self,request,id):
        services='branding'
        dynamic=dynamic_link(services,'branding/user/'+str(id))
        print(dynamic)
        response=requests.get(dynamic).json()
   
       
        return Response(response)

    def put(self,request,id):
        context={}
        services='branding'
        dynamic=dynamic_link(services,'branding/user/'+str(id))
        print(dynamic)
        response=requests.get(dynamic).json()
        name_r=response['first_name']
        company_r=response['company_name']
        email_r=response['email']
        domain_r=response['domain']
        datas={
        "first_name": response['first_name'],
        "middle_name": response['middle_name'],
        "last_name":response['last_name'],
        "email": response['email'],
        "url": response['url'],
        "company_name": response['company_name'],
        "address": response['address'],
        "phone_number": response['phone_number'],
        "city": response['city'],
        "state": response['state'],
        "country": response['country'],
        "domain" :response['domain'],
        "status": request.data['status']
        }

        services='branding'
        dynamic=dynamic_link(services,'branding/user/'+str(id))
        response=requests.put(dynamic,data=datas).json()

        if response['status'] == 'Accepted' :
            content="You request is accepted succesfully"
            mail=smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            sender='kailasvs94@gmail.com'
            recipient=str(response['email'])
            mail.login('kailasvs94@gmail.com','82@81@066@965')
            header='To:'+recipient+'\n'+'From:'\
            +sender+'\n'+'subject:Accepting Confirmation mail\n'
            content=header+content
            mail.sendmail(sender,recipient, content)
            mail.close()
            print("Accepted Succesfully")
            reg_u=Registered_users(name=name_r,company=company_r,email=email_r,domain=domain_r)
            reg_u.save()
            datas={
                "company_name": company_r,
                "address": response['address'],
                "phone_number": response['phone_number'],
                "city": response['city'],
                "state": response['state'],
                "country": response['country'],
                "domain" : domain_r,
            }

            services='apigateway'
            dynamic=dynamic_link(services,'gateway/company')
            print(dynamic,'-----')
            response=requests.post(dynamic,data=datas).json()
            print("successfully send mail")
            context["accept"]="Request Accepted"

        else :
            content="Sorry Your request can't accept by company now"
            mail=smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            sender='kailasvs94@gmail.com'
            recipient=str(response['email'])
            mail.login('kailasvs94@gmail.com','82@81@066@965')
            header='To:'+recipient+'\n'+'From:'\
            +sender+'\n'+'subject:Enquiry Mail Response\n'
            content=header+content
            mail.sendmail(sender,recipient, content)
            mail.close()
            print("Sorry Rejected")
            context['reject']="Request Rejected"


        return Response(context)

