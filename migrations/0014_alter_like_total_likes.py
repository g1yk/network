# Generated by Django 3.2.6 on 2021-11-30 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0013_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='total_likes',
            field=models.IntegerField(default=0, verbose_name='Total'),
        ),
    ]
