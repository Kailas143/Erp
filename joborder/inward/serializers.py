from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from .models import (joborder_fin_bill_inward_details,
                     joborder_fin_material_bill_inward,
                     joborder_fin_dc_inward_details,
                     joborder_fin_material_dc_inward,
                     receipt_no_generation)


class joborder_fin_bill_inward_details_serializers(serializers.ModelSerializer):
    class Meta :
        model=joborder_fin_bill_inward_details
        fields='__all__'


class joborder_fin_dc_inward_details_serializers(serializers.ModelSerializer):
    class Meta :
        model=joborder_fin_dc_inward_details
        fields='__all__'

class joborder_fin_material_bill_inward_serializers(serializers.ModelSerializer):
    class Meta :
        model=joborder_fin_material_bill_inward
        fields='__all__'


class joborder_fin_material_dc_inward_serializers(serializers.ModelSerializer):
    class Meta :
        model= joborder_fin_material_dc_inward
        fields='__all__'

class joborder_fin_material_dc_inward_serializers(serializers.ModelSerializer):
    joborder_fin_dc_inward_details=joborder_fin_dc_inward_details_serializers()
    class Meta :
        model= joborder_fin_material_dc_inward
        fields=['tenant_id','joborder_fin_dc_inward_details','job_order_price','qty','billed_qty','error','worker_name']

class receipt_no_generation_serializers(serializers.ModelSerializer):
    class Meta :
        model=receipt_no_generation
        fields='__all__'

class  joborder_fin_material_dc_inward_serializers(serializers.ModelSerializer):
    joborder_fin_bill_inward_details=joborder_fin_bill_inward_details_serializers()
    class Meta :
        model= joborder_fin_material_bill_inward
        fields=['tenant_id','joborder_fin_bill_inward_details','job_order_price','qty','billed_qty','error','igst_amount','sgst_amount','tgst','cgst_amount','error_bal','worker_name']
