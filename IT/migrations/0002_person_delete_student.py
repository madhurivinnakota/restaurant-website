# Generated by Django 4.2.2 on 2023-06-27 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('shirt_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]