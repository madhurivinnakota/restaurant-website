# Generated by Django 4.2.2 on 2023-06-27 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT', '0003_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='Enquiry',
            field=models.CharField(choices=[('ORL', 'order related issues'), ('SRI', 'site related issues'), ('CRI', 'complaint related issue'), ('oth', 'others')], max_length=50),
        ),
    ]
