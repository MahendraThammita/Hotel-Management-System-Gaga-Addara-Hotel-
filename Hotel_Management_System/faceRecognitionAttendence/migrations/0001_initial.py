# Generated by Django 3.1.1 on 2020-10-18 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendencesheet',
            fields=[
                ('empid', models.CharField(db_column='empId', max_length=6, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('timein', models.TimeField(db_column='timeIn')),
                ('timeout', models.TimeField(db_column='timeOut')),
                ('noofhours', models.IntegerField(blank=True, db_column='NoOfHours', null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'attendencesheet',
                'managed': False,
            },
        ),
    ]
