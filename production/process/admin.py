from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin 

# Register your models here.
from . models import Process_details,Process_bom

admin.site.register(Process_details,DraggableMPTTAdmin)
admin.site.register(Process_bom)