# Generated by Django 2.2.3 on 2019-08-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='location',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='school',
            name='principal',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
