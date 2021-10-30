from rest_framework import serializers
from . models import po_order_list,order_schelude_list,po_details
from drf_writable_nested.serializers import WritableNestedModelSerializer

class po_details_serializers(serializers.ModelSerializer):
    class Meta :
        model = po_order_list
        fields='__all__'

class po_order_list_serializers(serializers.ModelSerializer):
    class Meta :
        model = po_order_list
        fields='__all__'


class order_schelude_list_serializers(serializers.ModelSerializer):
    class Meta :
        model = order_schelude_list
        fields='__all__'

class po_order_serializers_list(serializers.ModelSerializer):
    po_details=po_details_serializers()
    class Meta :
        model = po_order_list
        fields=['po_details','tenant_id','tenant_id','raw_components_price','qty','bal_qty','bill_amt','igst_amount','sgst_amount','cgst_amount','tgst','t_amount']

class order_schelude_list_ser(serializers.ModelSerializer):
    po_order_list=po_order_serializers_list()
    class Meta :
        model = order_schelude_list
        fields=['tenant_id','po_order_list','delivery_date','qty','bal_qty','table_no']
