from django.shortcuts import render
from rest_framework.views import APIView
from .models import inspection_report_rows_raw_materials,remarks,parameters,inspection_report_details_raw_materials
from .serializers import inspec_serializer,remarkserializer,ins_parameter_Serializer,inspec_std_serializer
from rest_framework.response import Response
from rest_framework import mixins,generics

class inspectionreportdata_raw_dc(generics.GenericAPIView,APIView,mixins.CreateModelMixin,mixins.ListModelMixin):
   serializer_class =ins_parameter_Serializer
   queryset = parameters.objects.all()
   def post(self, request):
        if request.method == "POST":

            inputdata = request.data
            for m in inputdata:
                tenant_id=m['tenant_id']
                raw_dc=m['raw_dc']
                field1=m['field1']
                field2=m['field2']
                field3=m['field3']
                field4=m['field4']
                field5=m['field5']
                reportdatas = inspection_report_details_raw_materials(tenant_id=tenant_id,raw_material_fin_material_dc_inward=raw_dc)
               
                reportdatas.save()
                data_parameter = parameters(tenant_id=tenant_id,field1=field1, field2=field2, field3=field3, field4=field4, field5=field5)
                data_parameter.save()
                return Response('successfully saved')
class inspectionreportdata_raw_bill_material(generics.GenericAPIView,APIView,mixins.CreateModelMixin,mixins.ListModelMixin):
   serializer_class =ins_parameter_Serializer
   queryset = parameters.objects.all()
   def post(self, request):
        if request.method == "POST":

            inputdata = request.data
            for m in inputdata:
                tenant_id=m['tenant_id']
                raw_material=m['raw_material']
                field1=m['field1']
                field2=m['field2']
                field3=m['field3']
                field4=m['field4']
                field5=m['field5']
                reportdatas = inspection_report_details_raw_materials(tenant_id=tenant_id,raw_material_fin_material_bill_inward=raw_material)
                serializer = inspec_serializer(request.data)
                if serializer.is_valid:
                    reportdatas.save()
                    data_parameter = parameters(tenant_id=tenant_id,field1=field1, field2=field2, field3=field3, field4=field4, field5=field5)
                    data_parameter.save()
                    return Response('successfully saved')
                else:
                    return Response('not saved')

class list_parameters(generics.GenericAPIView,mixins.ListModelMixin):
    serializer_class=ins_parameter_Serializer
    queryset=parameters.objects.all()

    def get(self,request):
        return self.list(request)


class list_report_details(generics.GenericAPIView,mixins.ListModelMixin):
    serializer_class=inspec_serializer
    queryset=inspection_report_details_raw_materials.objects.all()

    def get(self,request):
        return self.list(request)

class inspectionreportint(generics.GenericAPIView,APIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class = inspec_std_serializer
    queryset = inspection_report_rows_raw_materials.objects.all()
    def get(self,request):
        return  self.list(request)
    def post(self, request):

            inputdata = request.data
            for m in inputdata:
                d=inputdata
                report_no = m['report_no']
                smp_no=m['smp_no']
                val=m['val']
                parameter_required=m['parameter']
                d=inspection_report_details_raw_materials.objects.get(report_no=report_no)
                print(smp_no)
                print(val)
                data = inspection_report_rows_raw_materials(inspection_report=d, smp_no=smp_no, val=val,parameter_required=parameter_required)
                serializer =inspec_std_serializer(request.data)
                if serializer.is_valid:
                    data.save()
            return Response('successfully saved')

class inspectionreportcheck(generics.GenericAPIView,APIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class = inspec_serializer
    queryset = inspection_report_details_raw_materials.objects.all()
    def get(self,request):
        return  self.list(request)
    def post(self, request):
            inputdata = request.data
            for m in inputdata:
                report_no=m['report_no']
                sample_size=m['sample_size']
                accepted_no=m['accepted_no']
                accepted_with_deviation_no=m['accepted_with_deviation_no']
                test_report=m['test_report']
                status=m['status']
                statusreport=m['statusreport']
                d = inspection_report_details_raw_materials.objects.get(report_no=report_no)
                inspection_report_details_raw_materials.objects.filter(report_no=report_no).update(sample_size=sample_size,accepted_no=accepted_no,accepted_with_deviation_no=accepted_with_deviation_no,test_report=test_report,status=status,statusreport=statusreport)
                serializer = remarkserializer(request.data)
                if serializer.is_valid:
                    data = remarks(inspection_report=d)
                    data.save()
                    return Response('successfully saved')
                else:
                    return Response('not saved')
            return Response('successfully saved')