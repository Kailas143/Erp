from rest_framework import serializers
from . models import Stock,Stock_History

class stock_serializers(serializers.ModelSerializer):
    class Meta :
        model=Stock
        fields='__all__'

class stock_history_serializers(serializers.ModelSerializer):
    class Meta :
        model=Stock_History
        fields='__all__'
