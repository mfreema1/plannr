# Generated by Django 2.0.4 on 2018-04-20 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0004_auto_20180420_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notebook.DailyEntry'),
        ),
    ]
