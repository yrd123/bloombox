# Generated by Django 3.0.2 on 2020-06-12 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb_app', '0002_auto_20200613_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='campus',
            name='name',
            field=models.CharField(default='nurturing lives', max_length=100),
            preserve_default=False,
        ),
    ]
