# Generated by Django 4.1.7 on 2023-03-13 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='affiliation',
            field=models.IntegerField(blank=True, null=True, verbose_name='所属关系'),
        ),
    ]
