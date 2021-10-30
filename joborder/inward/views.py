from django.shortcuts import render
from .models import (joborder_fin_bill_inward_details,
                     joborder_fin_material_bill_inward,
                     joborder_fin_dc_inward_details,
                     joborder_fin_material_dc_inward,receipt_no_generation)
from .serializers import (receipt_no_generation_serializers,joborder_fin_dc_inward_details_serializers,joborder_fin_material_bill_inward_serializers,joborder_fin_material_dc_inward_serializers,
                         joborder_fin_bill_inward_details_serializers,
                        )
from rest_framework import mixins,generics
from rest_framework.views import APIView
from rest_framework.response import Response

from inward import serializers
# Create your views here.

class DC_details_add(generics.GenericAPIView,APIView,mixins.ListModelMixin):
    
    serializer_class = joborder_fin_dc_inward_details_serializers
    queryset =  joborder_fin_dc_inward_details.objects.all()

    # def get(self,request):
    #     company=requests.get('http://127.0.0.1:8000/company/details/').json()
    #     return Response(company)


    def post(self,request):
        
        dcdata=request.data[0]
        dcmaterials=request.data[1]
        serializer = joborder_fin_dc_inward_details_serializers(
            data=dcdata, context={'request': request})
        data = {}
       
       
        if serializer.is_valid():
            company_idr = dcdata['tenant_id']
            dc_number_r = dcdata['dc_no']
            #calling the get_tenant function from utilities file
            # tenant_id = get_tenant(request)
            #filtering the dc details based on the financial year,to check wheather the dc details with same company exists or not
            dc = joborder_fin_dc_inward_details.objects.filter(
                tenant_id=company_idr,dc_no=dc_number_r)
            print(dc)
            if dc:
                data['error'] = 'Company with this dc number already exist !!! Try with another dc number'
            else:
                #here passing the tenant id value to the serializer of dc
                # inward=serializer.save(tenant_id=tenant_id)
                inward=serializer.save()
                for dc in dcmaterials :
                    materials=joborder_fin_material_dc_inward(tenant_id=inward.tenant_id,joborder_fin_dc_inward_details=joborder_fin_dc_inward_details.objects.get(id=inward.id),job_order_price=dc['job_order_price'],qty=dc['qty'],billed_qty=dc['billed_qty'],error=dc['error'],worker_name=inward.worker_name)
                    materials.save()
                data['success']="successfully saved"
        else :
            return Response("serialization Error")

        return Response(data)    


class add_dc(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class = joborder_fin_dc_inward_details_serializers
    queryset = joborder_fin_dc_inward_details.objects.all()

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

class add_dc_materials(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class = joborder_fin_material_dc_inward_serializers
    queryset =  joborder_fin_material_dc_inward.objects.all()

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

class list_dc_materials(generics.GenericAPIView,mixins.ListModelMixin):
    serializer_class=joborder_fin_material_dc_inward_serializers
    queryset=joborder_fin_material_dc_inward.objects.all()

    def get(self,request):
        return self.list(request)

class DC_bill_add(generics.GenericAPIView,APIView):
    
    def post(self,request):
        
        dcdata=request.data[0]
        dcmaterials=request.data[1]
        serializer = joborder_fin_bill_inward_details_serializers(
            data=dcdata, context={'request': request})
        data = {}
       
       
        if serializer.is_valid():
            # company_idr = dcdata['tenant_id']
            # dc_number_r = dcdata['dc_no']
            # #calling the get_tenant function from utilities file
            # # tenant_id = get_tenant(request)
            # #filtering the dc details based on the financial year,to check wheather the dc details with same company exists or not
            # dc = raw_component_fin_bill_inward_details.objects.filter(
            #     tenant_id=company_idr,dc_no=dc_number_r)
            # print(dc)
            # if dc:
            #     data['error'] = 'Company with this dc number already exist !!! Try with another dc number'
            # else:
                #here passing the tenant id value to the serializer of dc
                # inward=serializer.save(tenant_id=tenant_id)
            inward=serializer.save()
            for dc in dcmaterials :
                materials=joborder_fin_material_bill_inward(tenant_id=inward.id,joborder_fin_bill_inward_details=joborder_fin_bill_inward_details.objects.get(id=inward.id),job_order_price=dc['job_order_price'],qty=dc['qty'],billed_qty=dc['billed_qty'],rate_match=dc['rate_match'],error=dc['error'],error_bal=dc['error_bal'],igst_amount=dc['igst_amount'],sgst_amount=dc['sgst_amount'],cgst_amount=dc['cgst_amount'],tgst=dc['tgst'],bill_amount=dc['bill_amount'],worker_name=inward.worker_name)
                materials.save()
            data['success']="successfully saved"
        else :
            return Response("serialization Error")

        return Response(data)    

class list_dc_bill(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=joborder_fin_bill_inward_details_serializers
    queryset=joborder_fin_bill_inward_details.objects.all()

    def get(self,request):
        return self.list(request)


class list_material_bill(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=joborder_fin_material_dc_inward_serializers
    queryset=joborder_fin_material_bill_inward.objects.all()

    def get(self,request):
        return self.list(request)

class add_receipt(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=receipt_no_generation_serializers
    queryset=receipt_no_generation.objects.all()

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
  