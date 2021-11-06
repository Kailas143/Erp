import datetime
from rest_framework import serializers
from .models import remarks,parameters, inspection_report_details_job_order,inspection_report_rows_job_order

class inspec_serializer(serializers.ModelSerializer):
    class Meta:
        model = inspection_report_details_job_order
        fields = '__all__'

class inspec_std_serializer(serializers.ModelSerializer):
    class Meta:
        model = inspection_report_rows_job_order
        fields = '__all__'

class ins_parameter_Serializer(serializers.ModelSerializer):
    class Meta:
        model = parameters
        fields = '__all__'

class remarkserializer(serializers.ModelSerializer):
    class Meta:
        model = remarks
        fields = '__all__'