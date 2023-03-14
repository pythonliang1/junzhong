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
        verbose_name = '员工表'
        verbose_name_plural = verbose_name


class Order(models.Model):
    order_number = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100, verbose_name="客户姓名")
    customer_phone = models.CharField(max_length=100, verbose_name="客户电话")
    order_region = models.CharField(max_length=100,verbose_name="订单地址")
    car_company = models.CharField(max_length=100, verbose_name="车企车型")
    cable_specification = models.CharField(max_length=100, verbose_name="线缆规格")
    cable_length = models.IntegerField(verbose_name="用线长度")
    charge = models.IntegerField(verbose_name="总收费")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    note = models.CharField(max_length=300, blank=True, default='', verbose_name="备注")
    install_employee_id = models.ManyToManyField(Employee, through='OrderRelationship', verbose_name='订单关系表')

    def __str__(self):
        return f'order number: {self.order_number}'

    class Meta:
        db_table = 'Order'
        verbose_name = '订单表'
        verbose_name_plural = verbose_name

# order1.orderrelationship_set.all()   QuerySet
# em.orderrelationship_set.all()
class OrderRelationship(models.Model):
    order_id = models.ForeignKey(Order, verbose_name='订单id', on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, verbose_name='员工id', on_delete=models.CASCADE)
    note = models.CharField(max_length=300, blank=True, default='', null=True, verbose_name="备注")

    class Meta:
        db_table = 'order_relationship'
        verbose_name = '订单关系表'
        verbose_name_plural = verbose_name



