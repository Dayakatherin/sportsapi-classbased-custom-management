# Generated by Django 4.0 on 2021-12-29 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sport', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
