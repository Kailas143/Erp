from rest_framework import mixins,generics,status
from rest_framework.views import APIView


from . models import Stock_History,Stock
from . serializers import stock_history_serializers,stock_serializers
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
            raw_materials_r = request.data['raw_materials']
            min_stock_r = float(request.data['min_stock'])
            max_stock_r = float(request.data['max_stock'])
            avg_stock_r = float(request.data['avg_stock'])
            # filtering stock based on productdetails given by the user,first is given because filter is giving filtered list,here we need only single or first project 
            stock_data = Stock.objects.current_financialyear(id=tenant_id_r).filter(
                raw_materials=raw_materials_r).first()

            print(raw_materials_r)

            # if stock data is found(filtered data) 

            if stock_data:

                product_qty = stock_data.quantity + float(quantity_r)

                product = Stock.objects.filter(tenant_id=tenant_id_r,
                    raw_materials=raw_materials_r)
                
                # here new stock history record is occuring for every new updation of stock

                stock_history = Stock_History(tenant_id=tenant_id_r,stock_id=product[0], instock_qty=float(
                    product[0].quantity), after_process=float(
                    product[0].quantity)+float(quantity_r), change_in_qty=quantity_r, process="inward")
                stock_history.save()
                # after stock history is created stock will be updated
                product.update(quantity=product_qty,min_stock=min_stock_r,max_stock=max_stock_r,avg_stock=avg_stock_r)

                data['updated'] = "Stock succesfully updated"

            else:
                # if stock is not found with given details new stock will be created

                product = Stock(
                    tenant_id=1,raw_materials=raw_materials_r, quantity=quantity_r,min_stock=min_stock_r,
                    max_stock=max_stock_r,avg_stock=avg_stock_r)

                product.save()

                data['created'] = "Stock Succesfully created"
                print(quantity_r)

                # new stock history will be created

                stock_history = Stock_History(stock_id=product,tenant_id=tenant_id_r,instock_qty=float(
                    quantity_r), after_process="0.0",change_in_qty="0.0", process="inward")
                stock_history.save()

            return Response(data)
# if serialization validation errors occurs
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Stock_list(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = stock_serializers
    queryset = Stock.objects.all()

    def get(self, request):
        return self.list(request)

class Stock_HistoryAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = stock_history_serializers
    queryset=Stock_History.objects.all()
     

    def get(self, request):
            return self.list(request)

class stock_raw_materials(generics.GenericAPIView,APIView,mixins.UpdateModelMixin):
    def raw_id(self,rid) :
        stk=Stock.objects.filter(raw_materials=rid).first()
        return stk

    def get(self,request,rid):
        stock_data=self.raw_id(rid)
        serializer=stock_serializers(stock_data)
        return Response(serializer.data)
    
    def put(self, request, rid):
        stock_data=self.raw_id(rid)
        serializer =stock_serializers(stock_data,data=request.data)
        stock_data_id=stock_data.id
        qty=stock_data.quantity
        if serializer.is_valid():
            stk_data=serializer.save()
            aft_qty=stk_data.quantity
            chng_qty=float(qty-aft_qty)
            stock_history = Stock_History(tenant_id=stk_data.tenant_id,stock_id=stk_data,instock_qty=float(
                    qty), after_process=stk_data.quantity, change_in_qty=chng_qty,worker_name=stk_data.worker_name, process="production")
            stock_history.save()
            return Response(serializer.data)
        return Response(serializer.errors)