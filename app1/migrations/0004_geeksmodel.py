# Generated by Django 4.2 on 2023-04-26 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_employee_rename_student_modelclass'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeeksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]
