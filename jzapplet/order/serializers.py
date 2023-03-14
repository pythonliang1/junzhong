from order.models import Employee, Order, OrderRelationship
from rest_framework import serializers


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    install_employee_id = EmployeeSerializers(many=True)
    class Meta:
        model = Order
        fields = "__all__"

    # def create(self, validated_data):
    #     employee = Employee.objects.get(pk=validated_data.pop('install_employee_id'))
    #     instance = Order.objects.create(**validated_data)
    #     OrderRelationship.objects.create(Employee=employee, Order=instance)
    #     return instance
    #
    # def to_representation(self, instance):
    #     representation = super(OrderSerializer, self).to_representation(instance)
    #     representation['install_employee_id'] = OrderRelationship(instance.install_employee_id.all(), many=True).data
    #     return representation


class OrderRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderRelationship
        fields = "__all__"

