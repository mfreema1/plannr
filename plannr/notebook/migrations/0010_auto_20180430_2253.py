# Generated by Django 2.0.4 on 2018-04-30 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0009_auto_20180424_0006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dailyentry',
            options={'ordering': ['entry_date']},
        ),
        migrations.AlterModelOptions(
            name='weeklyentry',
            options={'ordering': ['week_start']},
        ),
        migrations.AlterField(
            model_name='lookingforwardto',
            name='entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='looks', to='notebook.DailyEntry'),
        ),
        migrations.AlterField(
            model_name='task',
            name='entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='notebook.DailyEntry'),
        ),
        migrations.AlterField(
            model_name='thankfulfor',
            name='entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thanks', to='notebook.DailyEntry'),
        ),
    ]