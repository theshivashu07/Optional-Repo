# Generated by Django 3.1.7 on 2022-03-16 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='trialData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_data', models.CharField(max_length=50)),
                ('class_name', models.TextField()),
            ],
        ),
    ]
