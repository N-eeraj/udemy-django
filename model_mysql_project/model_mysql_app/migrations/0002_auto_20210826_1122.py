# Generated by Django 3.2.6 on 2021-08-26 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_mysql_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formtable',
            name='phone',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='formtable',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
