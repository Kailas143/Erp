from rest_framework import serializers

from . models import Process_details,Process_bom


class process_details_serializers(serializers.ModelSerializer):
    class Meta :
        model=Process_details
        fields='__all__'

class process_bom_serializers(serializers.ModelSerializer):
    class Meta :
        model=Process_bom
        fields='__all__'
