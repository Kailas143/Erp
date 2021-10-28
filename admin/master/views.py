import re

from django.shortcuts import render
from rest_framework import generics, mixins, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (Role, User, company_details, job_components_details,
                     job_order_company_details, job_order_price,
                     job_order_supliers_contact_details,
                     raw_components_details, raw_components_price,
                     supliers_contact_details)
# Create your views here.
from .serializers import (Company_details_serializers, RoleSerializers,
                          Userserializer, job_components_details_list,
                          job_components_details_serializers,
                          job_order_company_details_serializers,
                          job_order_price_list, job_order_price_serializers,
                          job_order_supliers_contact_details_serializers,
                          job_order_supliers_list,
                          raw_components_details_serializers,
                          raw_components_price_list,
                          raw_components_price_serializers,
                          supliers_contact_details_serializers,
                          suppliers_details)


class add_roles(generics.GenericAPIView, APIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializers_class = RoleSerializers
    queryset = Role.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class User_register(generics.GenericAPIView, APIView, mixins.CreateModelMixin):
    serializer_class = Userserializer

    def post(self, request):
        data = {}
        serializer = Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'User successfully registered'
        else:
            data['error'] = 'Please Provide valid data'

        return Response(data)


class add_company_details(APIView):
    serializer_class = Company_details_serializers

    def post(self, request):
        data = {}
        serializer = Company_details_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Company successfully registered'
        else:
            data['error'] = 'Please Provide valid data'

        return Response(data)


class add_supliers_contact_details(APIView):
    serializer_class = supliers_contact_details_serializers

    def post(self, request):
        data = {}
        serializer = supliers_contact_details_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Contact successfully added'
        else:
            data['error'] = 'Please Provide valid data'

        return Response(data)


class add_job_order_company_details(APIView):
    serializer_class = job_order_company_details_serializers

    def post(self, request):
        data = {}
        serializer = job_order_company_details_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Job order successfully saved'
        else:
            data['error'] = 'Please Provide valid data'

        return Response(data)


class add_job_order_supliers_contact_details(APIView):
    serializer_class = job_order_supliers_contact_details_serializers

    def post(self, request):
        data = {}
        serializer = job_order_supliers_contact_details_serializers(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Job order supliers contact details successfully saved'
        else:
            data['error'] = 'Please Provide valid data'

        return Response(data)


class add_raw_components_details(APIView):
    serializer_class = raw_components_details_serializers

    def post(self, request):
        data = {}
        serializer = raw_components_details_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Raw component saved'
        else:
            data['error'] = 'Please Provide valid data'

        return Response(data)


class add_raw_components_price(APIView):
    serializer_class = raw_components_price_serializers

    def post(self, request):
        data = {}
        serializer = raw_components_price_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Raw component price added'
        else:
            data['error'] = 'Please Provide valid data'

        return Response(data)


class add_job_components_details(APIView):
    serializer_class = job_components_details_serializers

    def post(self, request):
        data = {}
        serializer = job_components_details_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Job component saved'
        else:
            data['error'] = 'Please Provide valid data'

        return Response(data)


class add_job_order_price(APIView):
    serializer_class = job_order_price_serializers

    def post(self, request):
        data = {}
        serializer = job_order_price_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Job price added'
        else:
            data['error'] = 'Please Provide valid data'

        return Response(data)


class list_suppliers_details(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = suppliers_details
    queryset = supliers_contact_details.objects.all()

    def get(self, request):
        return self.list(request)


class roles_list(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = RoleSerializers
    queryset = Role.objects.all()

    def get(self, request):

        return self.list(request)


class roles_Update(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = RoleSerializers
    queryset = Role.objects.all()
    lookup_field = 'id'

    def get(self, request, id):

        return self.retrieve(request, id)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class company_list(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = Company_details_serializers
    queryset = company_details.objects.all()

    def get(self, request):

        return self.list(request)


class company_details_Update(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = Company_details_serializers
    queryset = company_details.objects.all()
    lookup_field = 'id'

    def get(self, request, id):

        return self.retrieve(request, id)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class supliers_contact_details_Update(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = supliers_contact_details_serializers
    queryset = supliers_contact_details.objects.all()
    lookup_field = 'id'

    def get(self, request, id):

        return self.retrieve(request, id)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class job_order_company_details_Update(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = job_order_company_details_serializers
    queryset = job_order_company_details.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class job_order_supliers_contact_details_Update(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = job_order_supliers_list
    queryset = job_order_supliers_contact_details.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class raw_components_details_Update(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = raw_components_details_serializers
    queryset = raw_components_details.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class raw_components_price_Update(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = raw_components_price_list
    queryset = raw_components_price.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class job_components_details_Update(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = job_components_details_list
    queryset = job_components_details.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class job_order_price_Update(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = job_order_price_list
    queryset = job_order_price.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)
