# Generated by Django 3.1.1 on 2021-01-28 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20210120_1345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='description',
            options={'verbose_name_plural': ' About Description'},
        ),
        migrations.AlterField(
            model_name='description',
            name='content',
            field=models.TextField(),
        ),
    ]
