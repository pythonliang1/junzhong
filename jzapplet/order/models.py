from django.db import models


# Create your models here.
class Employee(models.Model):
    MedalType = models.TextChoices('员工', '管理员')
    employee_name = models.CharField(max_length=30)
    affiliation = models.IntegerField(verbose_name='所属关系', blank=True, null=True)
    employee_phone = models.CharField(max_length=30, verbose_name='员工电话')
    employee_position = models.CharField(max_length=100, verbose_name='职位名称', choices=MedalType.choices)
    employee_pwd = models.CharField(max_length=20, verbose_name='员工密码', default='123456')

    class Meta:
        db_table = 'Employee'


class Order(models.Model):
    order_number = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=100)
    order_region = models.CharField(max_length=100)
    car_company = models.CharField(max_length=100)
    cable_specification = models.CharField(max_length=100)
    cable_length = models.IntegerField()
    charge = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    update_by = models.ForeignKey(Employee, on_delete=models.SET_NULL)
    note = models.CharField(max_length=300, blank=True, default='')

    def __str__(self):
        return f'order number: {self.order_number}'

    class Meta:
        db_table = 'Order'


class OrderRelation(models.Model):
    pass
    # order_id = models.ManyToManyField(Order)
    # employee_id = models.ManyToManyField(Employee)


