from . models import Stock_History_job_order,Stock_job_order
from . serializers import stock_history_serializers,stock_serializers

from rest_framework import generics,mixins,status 
from rest_framework.views import APIView
from rest_framework.response import Response


class add_stock(generics.GenericAPIView,APIView):

    def post(self, request, format=None):

        serializer = stock_serializers(data=request.data)
        data = {}
        # serialization validation
        if serializer.is_valid():
            # tenant_id=get_tenant(request)
            tenant_id_r=request.data['tenant_id']

            quantity_r = float(request.data['quantity'])
            # tenant_id_r=tenant_id
            job_order_r = request.data['job_order']
            min_stock_r = float(request.data['min_stock'])
            max_stock_r = float(request.data['max_stock'])
            avg_stock_r = float(request.data['avg_stock'])
            worker_name_r =(request.data['worker_name'])
            # filtering stock based on productdetails given by the user,first is given because filter is giving filtered list,here we need only single or first project 
            stock_data = Stock_job_order.objects.current_financialyear(id=tenant_id_r).filter(
                job_order=job_order_r).first()

            # if stock data is found(filtered data) 

            if stock_data:

                product_qty = stock_data.quantity + float(quantity_r)

                product = Stock_job_order.objects.filter(tenant_id=tenant_id_r,
                    job_order=job_order_r)
                
                # here new stock history record is occuring for every new updation of stock

                stock_history = Stock_History_job_order(tenant_id=tenant_id_r,stock_id=product[0], instock_qty=float(
                    product[0].quantity), after_process=float(
                    product[0].quantity)+float(quantity_r), change_in_qty=quantity_r, worker_name=worker_name_r,process="inward")
                stock_history.save()
                # after stock history is created stock will be updated
                product.update(quantity=product_qty,min_stock=min_stock_r,max_stock=max_stock_r,avg_stock=avg_stock_r,worker_name=worker_name_r)

                data['updated'] = "Stock succesfully updated"

            else:
                # if stock is not found with given details new stock will be created

                product = Stock_job_order(
                    tenant_id=1,job_order=job_order_r, quantity=quantity_r,min_stock=min_stock_r,
                    max_stock=max_stock_r,avg_stock=avg_stock_r,worker_name=worker_name_r)

                product.save()

                data['created'] = "Stock Succesfully created"
        

                # new stock history will be created

                stock_history = Stock_History_job_order(stock_id=product,tenant_id=tenant_id_r,instock_qty=float(
                    quantity_r), after_process="0.0",change_in_qty="0.0", process="inward",worker_name=worker_name_r)
                stock_history.save()

            return Response(data)
# if serialization validation errors occurs
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class stock_list(generics.GenericAPIView,mixins.ListModelMixin):
    queryset=Stock_job_order.objects.all()
    serializer_class=stock_serializers

    def get(self,request):
        return self.list(request)

class stock_history_list(generics.GenericAPIView,mixins.ListModelMixin):
    queryset=Stock_History_job_order.objects.all()
    serializer_class=stock_history_serializers

    def get(self,request):
        return self.list(request)


class stock_job_order(generics.GenericAPIView,APIView,mixins.UpdateModelMixin):
    def raw_id(self,jid) :
        stk=Stock_job_order.objects.filter(job_order=jid).first()
        return stk

    def get(self,request,jid):
        stock_data=self.raw_id(jid)
        serializer=stock_serializers(stock_data)
        return Response(serializer.data)
    
    def put(self, request, jid):
        stock_data=self.raw_id(jid)
        serializer =stock_serializers(stock_data,data=request.data)
        stock_data_id=stock_data.id
        qty=stock_data.quantity
        if serializer.is_valid():
            stk_data=serializer.save()
            aft_qty=stk_data.quantity
            chng_qty=float(qty-aft_qty)
            stock_history = Stock_History_job_order(tenant_id=stk_data.tenant_id,stock_id=stk_data,instock_qty=float(
                    qty), after_process=stk_data.quantity, change_in_qty=chng_qty,worker_name=stk_data.worker_name, process="production")
            stock_history.save()
            return Response(serializer.data)
        return Response(serializer.errors)