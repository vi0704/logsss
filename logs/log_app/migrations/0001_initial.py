# Generated by Django 2.1.5 on 2019-02-12 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('users_count', models.IntegerField(null=True)),
                ('session_count', models.IntegerField(null=True)),
            ],
        ),
    ]
