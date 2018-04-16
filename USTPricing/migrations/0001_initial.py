# Generated by Django 2.0.4 on 2018-04-15 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USTContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evepraisalURL', models.URLField()),
                ('totalSize', models.FloatField(default=0)),
                ('totalSell', models.FloatField(default=0)),
                ('collateral', models.FloatField(default=0)),
                ('reward', models.FloatField(default=0)),
            ],
        ),
    ]
