# Generated by Django 5.0.4 on 2024-04-16 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='tin',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
