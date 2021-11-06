from rest_framework import serializers
from . models import Stock_job_order,Stock_History_job_order


class stock_serializers(serializers.ModelSerializer) :
    class Meta :
        model=Stock_job_order
        fields='__all__'

class stock_history_serializers(serializers.ModelSerializer) :
    class Meta :
        model = Stock_History_job_order
        fields='__all__'