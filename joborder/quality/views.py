from .models import inspection_report_rows,remarks,parameters,inspection_report_details
from .serializers import inspec_serializer,remarkserializer,ins_parameter_Serializer,inspec_std_serializer
from rest_framework import mixins,generics
from rest_framework.response import Response
from rest_framework.views import APIView

class inspectionreportdata(generics.GenericAPIView,APIView,mixins.CreateModelMixin,mixins.ListModelMixin):
   serializer_class =ins_parameter_Serializer
   queryset = parameters.objects.all()
   def post(self, request):
        if request.method == "POST":

            inputdata = request.data
            print(inputdata)
           
            for m in inputdata:
                job_order=m['job_order']
                field1=m['field1']
                field2=m['field2']
                field3=m['field3']
                field4=m['field4']
                field5=m['field5']
                reportdatas = inspection_report_details(job_order=job_order)
                serializer = inspec_serializer(request.data)
                if serializer.is_valid:
                    reportdatas.save()
                    data_parameter = parameters(field1=field1, field2=field2, field3=field3, field4=field4, field5=field5)
                    data_parameter.save()
                    return Response('successfully saved')
                else:
                    return Response('not saved')

class inspectionreportint(generics.GenericAPIView,APIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class = inspec_std_serializer
    queryset = inspection_report_rows.objects.all()
    def get(self,request):
        return  self.list(request)
    def post(self, request):
        if request.method == "POST":

            inputdata = request.data
           
            for m in inputdata:
                d=inputdata
                report_no = m['report_no']
                smp_no=m['smp_no']
                val=m['val']
                parameter_required=m['parameter']
                d=inspection_report_details.objects.get(report_no=report_no)
                data = inspection_report_rows(inspection_report=d, smp_no=smp_no, val=val,parameter_required=parameter_required)
                serializer =inspec_std_serializer(request.data)
                if serializer.is_valid:
                    data.save()
            return Response('successfully saved')


class inspectionreportcheck(generics.GenericAPIView,APIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class = inspec_serializer
    queryset = inspection_report_details.objects.all()
    def get(self,request):
        return  self.list(request)
    def post(self, request):
        if request.method == "POST":
            inputdata = request.data
            for m in inputdata:
                report_no=m['report_no']
                sample_size=m['sample_size']
                accepted_no=m['accepted_no']
                accepted_with_deviation_no=m['accepted_with_deviation_no']
                test_report=m['test_report']
                status=m['status']
                statusreport=m['statusreport']
                d = inspection_report_details.objects.get(report_no=report_no)
                inspection_report_details.objects.filter(report_no=report_no).update(sample_size=sample_size,accepted_no=accepted_no,accepted_with_deviation_no=accepted_with_deviation_no,test_report=test_report,status=status,statusreport=statusreport)
                serializer = remarkserializer(request.data)
                if serializer.is_valid:
                    data = remarks(inspection_report=d)
                    data.save()
                    return Response('succesfully saved')
                else:
                    return Response('not saved')
        return Response('succesfully saved')
