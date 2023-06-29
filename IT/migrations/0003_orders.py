# Generated by Django 4.2.2 on 2023-06-27 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT', '0002_person_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('descrion', models.CharField(max_length=250)),
                ('member', models.BooleanField()),
                ('Enquiry', models.CharField(choices=[{'ORL', 'order related issues'}, {'SRI', 'site related issues'}, {'complaint related issue', 'CRI'}, {'others', 'oth'}], max_length=50)),
            ],
        ),
    ]