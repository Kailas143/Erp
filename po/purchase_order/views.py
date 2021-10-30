from django.shortcuts import render
from django.views import generic
from rest_framework.response import Response
from . models import po_order_list,order_schelude_list,po_details
from . serializers import po_order_list_serializers,order_schelude_list_serializers,po_order_serializers_list,order_schelude_list_ser
from rest_framework.views import APIView
from rest_framework import mixins,generics
# Create your views here.

class add_po_order_list(APIView):

    def post(self,request):
        data={}
        serializer=po_order_list_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['success']="successfully added"
        else :
            data['error']="Not a valid data"
        return Response(data)

class add_order_schelude(APIView):

    def post(self,request):
        data={}
        serializer=order_schelude_list_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['success']="successfully added"
        else :
            data['error']="Not a valid data"
        
        return Response(data)

class po_order(generics.GenericAPIView,mixins.ListModelMixin):
    serializer_class=po_order_serializers_list
    queryset=po_order_list.objects.all()

    def get(self,request):
        return self.list(request)

class po_schedule(generics.GenericAPIView,mixins.ListModelMixin):
    serializer_class=order_schelude_list_ser
    queryset=order_schelude_list.objects.all()

    def get(self,request):
        return self.list(request)