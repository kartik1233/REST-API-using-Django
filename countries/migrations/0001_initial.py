# Generated by Django 3.2 on 2021-04-30 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('capital', models.CharField(default='', max_length=50)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
