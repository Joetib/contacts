# Generated by Django 2.2 on 2019-06-02 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190602_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateTimeField(default='django.utils.timezone.now'),
        ),
    ]
