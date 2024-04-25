# Generated by Django 5.0.4 on 2024-04-25 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('Dept_name', models.CharField(max_length=20)),
                ('joining_date', models.DateField()),
                ('salary', models.IntegerField()),
            ],
        ),
    ]