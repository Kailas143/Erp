from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from .models import (raw_component_fin_bill_inward_details,
                     raw_component_fin_dc_inward_details,
                     raw_component_fin_material_bill_inward,
                     raw_component_fin_material_dc_inward,
                     receipt_no_generation)


class raw_component_fin_bill_inward_details_serializers(serializers.ModelSerializer):
    class Meta :
        model=raw_component_fin_bill_inward_details
        fields='__all__'


class raw_component_fin_dc_inward_details_serializers(serializers.ModelSerializer):
    class Meta :
        model=raw_component_fin_dc_inward_details
        fields='__all__'

class raw_component_fin_material_bill_inward_serializers(serializers.ModelSerializer):
    class Meta :
        model=raw_component_fin_material_bill_inward
        fields='__all__'


class raw_component_fin_material_dc_inward_serializers(serializers.ModelSerializer):
    class Meta :
        model=raw_component_fin_material_dc_inward
        fields='__all__'

class raw_component_fin_material_serializers(serializers.ModelSerializer):
    raw_component_fin_dc_inward_details=raw_component_fin_bill_inward_details_serializers()
    class Meta :
        model=raw_component_fin_material_dc_inward
        fields='__all__'

class receipt_no_generation_serializers(serializers.ModelSerializer):
    class Meta :
        model=receipt_no_generation
        fields='__all__'

class  raw_component_fin_material_bill_serializers(serializers.ModelSerializer):
    raw_component_fin_bill_inward_details=raw_component_fin_dc_inward_details_serializers()
    class Meta :
        model=raw_component_fin_material_dc_inward
        fields='__all__'