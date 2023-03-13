# Generated by Django 4.1.7 on 2023-03-13 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_employee_affiliation'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employee_pwd',
            field=models.CharField(default='123456', max_length=20, verbose_name='员工密码'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_position',
            field=models.CharField(choices=[('管理员', '管理员')], max_length=100, verbose_name='职位名称'),
        ),
        migrations.CreateModel(
            name='OrderRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.ManyToManyField(to='order.employee')),
                ('order_id', models.ManyToManyField(to='order.order')),
            ],
        ),
    ]
