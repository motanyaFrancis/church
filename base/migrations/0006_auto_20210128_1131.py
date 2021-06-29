# Generated by Django 3.1.1 on 2021-01-28 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20210128_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexdescription',
            name='pub_by',
            field=models.CharField(blank=True, max_length=200, verbose_name='Published By'),
        ),
        migrations.AddField(
            model_name='indexdescription',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='date Published'),
        ),
    ]
