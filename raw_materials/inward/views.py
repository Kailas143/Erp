from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from .models import (raw_component_fin_bill_inward_details,
                     raw_component_fin_dc_inward_details,
                     raw_component_fin_material_bill_inward,
                     raw_component_fin_material_dc_inward,receipt_no_generation)
from .serializers import (receipt_no_generation_serializers,raw_component_fin_material_bill_serializers,raw_component_fin_bill_inward_details_serializers,raw_component_fin_bill_inward_details_serializers,
                          raw_component_fin_dc_inward_details_serializers,
                          raw_component_fin_material_dc_inward_serializers,
                          raw_component_fin_material_serializers,raw_component_fin_material_bill_inward_serializers)

# Create your views here.


class DC_details_add(generics.GenericAPIView,APIView,mixins.ListModelMixin):
    
    serializer_class = raw_component_fin_dc_inward_details_serializers
    queryset = raw_component_fin_dc_inward_details.objects.all()

    # def get(self,request):
    #     company=requests.get('http://127.0.0.1:8000/company/details/').json()
    #     return Response(company)


    def post(self,request):
        
        dcdata=request.data[0]
        dcmaterials=request.data[1]
        serializer = raw_component_fin_dc_inward_details_serializers(
            data=dcdata, context={'request': request})
        data = {}
       
       
        if serializer.is_valid():
            
            dc_number_r = dcdata['dc_no']
            #calling the get_tenant function from utilities file
            # tenant_id = get_tenant(request)
            #filtering the dc details based on the financial year,to check wheather the dc details with same company exists or not
            dc = raw_component_fin_dc_inward_details.objects.filter(dc_no=dc_number_r).exists()
            print(dc)
            if dc:
                data['error'] = 'This dc number already exist !!! Try with another dc number'
            else:
                #here passing the tenant id value to the serializer of dc
                # inward=serializer.save(tenant_id=tenant_id)
                inward=serializer.save()
                for dc in dcmaterials :
                    materials=raw_component_fin_material_dc_inward(tenant_id=1,raw_component_fin_dc_inward_details=raw_component_fin_dc_inward_details.objects.get(id=inward.id),raw_component_price=dc['raw_component_price'],qty=dc['qty'],billed_qty=dc['billed_qty'],error=dc['error'])
                    materials.save()
                data['success']="successfully saved"
        else :
            return Response("serialisation Error")

        return Response(data)    

class DC_bill_add(generics.GenericAPIView,APIView):
    
    def post(self,request):
        
        dcdata=request.data[0]
        dcmaterials=request.data[1]
        serializer = raw_component_fin_bill_inward_details_serializers(
            data=dcdata, context={'request': request})
        data = {}
       
       
        if serializer.is_valid():
            # company_idr = dcdata['tenant_id']
            dc_number_r = dcdata['bill_no']
            # #calling the get_tenant function from utilities file
            # # tenant_id = get_tenant(request)
            # #filtering the dc details based on the financial year,to check wheather the dc details with same company exists or not
            dc = raw_component_fin_bill_inward_details.objects.filter(bill_no=dc_number_r)
            # print(dc)
            if dc:
                data['error'] = 'Bill number already exist !!! Try another one'
            else:
               
                inward=serializer.save()
                for dc in dcmaterials :
                    materials=raw_component_fin_material_bill_inward(raw_component_fin_bill_inward_details=raw_component_fin_bill_inward_details.objects.get(id=inward.id),raw_component_price=dc['raw_component_price'],qty=dc['qty'],billed_qty=dc['billed_qty'],rate_match=dc['rate_match'],error=dc['error'],error_bal=dc['error_bal'],igst_amount=dc['igst_amount'],sgst_amount=dc['sgst_amount'],cgst_amount=dc['cgst_amount'],tgst=dc['tgst'],bill_amount=dc['bill_amount'],worker_name=dc['worker_name'])
                    materials.save()
                    data['success']="successfully saved"
        else :
            return Response("serialization Error")

        return Response(data)    

class add_dc_details(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=raw_component_fin_dc_inward_details_serializers
    queryset = raw_component_fin_dc_inward_details.objects.all()


    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

class add_dc_materials(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=raw_component_fin_material_dc_inward_serializers
    queryset =raw_component_fin_material_dc_inward.objects.all()


    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)


class list_raw_component_dc_materials(generics.GenericAPIView,mixins.ListModelMixin):
    serializer_class=raw_component_fin_material_serializers
    queryset=raw_component_fin_material_dc_inward.objects.all()

    def get(self,request):
        return self.list(request)

class add_dc_bill_details(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=raw_component_fin_bill_inward_details_serializers
    queryset=raw_component_fin_bill_inward_details.objects.all()

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class list_materials_bill_details(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=raw_component_fin_material_bill_serializers
    queryset=raw_component_fin_material_bill_inward.objects.all()

    def get(self,request):
        return self.list(request)

class list_dc_bill_details(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=raw_component_fin_bill_inward_details_serializers
    queryset=raw_component_fin_bill_inward_details.objects.all()

    def get(self,request):
        return self.list(request)


class list_dc_details(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=raw_component_fin_dc_inward_details_serializers
    queryset=raw_component_fin_dc_inward_details.objects.all()

    def get(self,request):
        return self.list(request)

class add_receipt(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=receipt_no_generation_serializers
    queryset=receipt_no_generation.objects.all()

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)