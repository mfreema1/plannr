# Generated by Django 2.0.4 on 2018-04-18 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyEntry',
            fields=[
                ('daily_entry_id', models.UUIDField(primary_key=True, serialize=False)),
                ('entry_date', models.DateField()),
                ('affirmation', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Insight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LookingForwardTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyEntry',
            fields=[
                ('monthly_entry_id', models.UUIDField(primary_key=True, serialize=False)),
                ('habit', models.CharField(max_length=20)),
                ('focus', models.CharField(max_length=20)),
                ('month', models.CharField(choices=[('JANUARY', 'January'), ('FEBRUARY', 'February'), ('MARCH', 'March'), ('APRIL', 'April'), ('MAY', 'May'), ('JUNE', 'June'), ('JULY', 'July'), ('AUGUST', 'August'), ('SEPTEMBER', 'September'), ('OCTOBER', 'October'), ('NOVEMBER', 'November'), ('DECEMBER', 'December')], max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('is_complete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Obstacle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_complete', models.BooleanField()),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('is_complete', models.BooleanField()),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ThankfulFor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyEntry',
            fields=[
                ('weekly_entry_id', models.UUIDField(primary_key=True, serialize=False)),
                ('week_start', models.DateField()),
                ('week_end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekly_goal', models.CharField(choices=[('FAMILY', 'Family'), ('WORK', 'Work'), ('RELATIONSHIP', 'Relationship'), ('PERSONAL', 'Personal')], max_length=32)),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='weekly_entry_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notebook.WeeklyEntry'),
        ),
    ]
