# Generated by Django 3.2.19 on 2023-05-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'hola"."tasks',
                'managed': False,
            },
        ),
    ]
