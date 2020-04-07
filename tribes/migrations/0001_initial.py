# Generated by Django 2.2.7 on 2019-11-12 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('population', models.IntegerField()),
                ('region', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('religion', models.CharField(max_length=200)),
                ('existence', models.IntegerField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
