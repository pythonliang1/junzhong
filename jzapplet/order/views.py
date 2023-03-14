from django.shortcuts import render
from order.models import Order, Employee
from order.serializers import OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from order.models import Employee, OrderRelationship
from order.serializers import EmployeeSerializers, OrderRelationshipSerializer
from rest_framework import mixins
from rest_framework import generics
# Create your views here.

from rest_framework import generics


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
#
#     def create(self, request, *args, **kwargs):
#         # request.
#         data = request.data
#         # data.install_employee_id
#         serializer = OrderSerializer(data=data, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer


# class OrderList(APIView):
#     def get(self, request, format=None):
#         order = Order.objects.all()
#         serializer = OrderSerializer(order, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         install_employee_id = request.data['install_employee_id']
#         if install_employee_id:
#             install_employee_id = install_employee_id.split(',')
#             ems = Employee.objects.filter(pk__in=install_employee_id)
#             request.data['install_employee_id'] = []
#             for em in ems:
#                 em = EmployeeSerializers(em)
#                 data = em.data
#                 request.data['install_employee_id'].append(data)
#
#             # for em in ems:
#             #     print(em)
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             # OrderRelationship.objects.add()
#
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#

class EmployeeList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EmployeeDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class OrderRelationshipList(generics.ListCreateAPIView):
    queryset = OrderRelationship.objects.all()
    serializer_class = OrderRelationshipSerializer


class OOrderRelationshipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderRelationshipSerializer