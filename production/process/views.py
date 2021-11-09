from django.contrib.admin.utils import lookup_field
from django.shortcuts import render
from django.views import generic
from mptt import querysets
from rest_framework import mixins,generics, serializers
from rest_framework.views import APIView
from . models import Process_bom,Process_details
from .serializers import process_bom_serializers,process_details_serializers
import mptt
from mptt.fields import TreeForeignKey
from rest_framework.response import Response
from mptt.templatetags.mptt_tags import cache_tree_children, tree_info
import requests,json
from .dynamic import dynamic_link

# Create your views here.
class ProcessViewset(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin,generics.GenericAPIView,APIView):
    serializer_class = process_details_serializers
  

    queryset = Process_details.objects.all()
    queryset = cache_tree_children(queryset)
    def get(self,request):
        return self.list(request)

    def post(self,request):
        # category_slug = hierarchy.split('/')
        parent =request.data['children']
        name=request.data['name']
        sluglist=request.data['slug']
        category_type=request.data['category']
        p_id=request.data['pid']
        print(parent)
        print(name)
        print(sluglist)
        x=Process_details.objects.all().last()
        print(x)
    # y=x.slug
        if category_type == 'M':
            if parent == 0 :
                root= Process_details(process_name=name,slug=sluglist)
                root.save()
                print(root)
                return Response("categories successfully added")
            
        elif category_type == 'S':
           
                ft=Process_details.objects.get(id=p_id)
                print('................'+''+str(ft))
                x=Process_details.objects.all().last()
         
            
                # print('...............=======.'+''+str(z))
                root= Process_details(process_name=name,slug=sluglist,parent=ft)
                root.save()
                return Response("sub categories add")


class proces_bom(generics.GenericAPIView,mixins.ListModelMixin,APIView):
    serializer_class=process_bom_serializers
    queryset=Process_bom.objects.all()
    def get(self,request) :
        return self.list(request)

    def post(self,request):
        bom_title=request.data['title']
        pd=request.data['process_details']
        reqd_qty=request.data['reqd_qty']
        rid=request.data['raw_material']
        job=request.data['job_order']
        slug=request.data['slug']

        pbom=Process_bom(title=bom_title,process_details=Process_details.objects.get(id=pd),reqd_qty=reqd_qty,job_order=job,raw_material=rid,slug=slug)
        #if joborder is null or 0 stock will be filter based on raw materials an update the stock and create stock history
        if job == 0:
            services = 'raw_materials'
            dynamic=dynamic_link(services,'store/raw/'+str(rid))
            response=requests.get(dynamic).json()
            qnty_r=response['quantity']
            mins=response['min_stock']
            maxs=response['max_stock']
            avgs=response['avg_stock']
            rawm=response['raw_materials']
            tenant_id=response['tenant_id']
            if qnty_r  > reqd_qty :
                n_qty=qnty_r-reqd_qty
                datas={
                        'quantity' : n_qty,
                        'tenant_id' :tenant_id,
                        'min_stock' :mins,
                        'max_stock' :maxs,
                        'avg_stock' : avgs,
                        'worker_name':'hgg',
                        'raw_materials' : rawm,
                    }
                update=requests.put(dynamic,data=datas).json()
     
            
        elif rid== 0 :
            services = 'joborder'
            dynamic=dynamic_link(services,'store/stock/'+str(job))
            response=requests.get(dynamic).json()
            qnty_r=response['quantity']
            mins=response['min_stock']
            maxs=response['max_stock']
            avgs=response['avg_stock']
            jobm=response['job_order']
            tenant_id=response['tenant_id']
            print(qnty_r,'qqqq')
            if qnty_r  > reqd_qty :
                n_qty=qnty_r-reqd_qty
                datas={
                        'quantity' : n_qty,
                        'tenant_id' :tenant_id,
                        'min_stock' :mins,
                        'max_stock' :maxs,
                        'avg_stock' : avgs,
                        'worker_name':'hgg',
                        'job_order' : jobm,
                    }
                update=requests.put(dynamic,data=datas).json()
            
        pbom.save()
        
    
        return Response("successfully saved")

class process_bom_crud(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin):
    serializer_class=process_bom_serializers
    queryset=Process_bom.objects.all()
    lookup_field='id'

    def get(self,request,id=None):
        if id :
            return self.retrieve(request)
        else : 
            return self.list(request)

    def put(self,request,id) :
       return self.update(request,id)
    
    def delete(self,request,id):
        return self.destory(request,id)

class process_details_crud(generics.GenericAPIView,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=process_details_serializers
    queryset=Process_details.objects.all()
    lookup_field='id'

    def get(self,request,id=None):
        if id :
            return self.retrieve(request,id)
        else :
            return self.list(request)

    def put(self,request,id) :
        return self.update(request,id)
    
    def delete(self,request,id):
        return self.destroy(request,id)