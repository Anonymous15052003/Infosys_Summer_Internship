# Generated by Django 5.0.4 on 2024-04-25 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('mail', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('phoneno', models.IntegerField()),
            ],
        ),
    ]
