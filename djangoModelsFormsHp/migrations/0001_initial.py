# Generated by Django 4.2.6 on 2023-11-01 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HpStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=20)),
                ('Mobile', models.IntegerField()),
            ],
            options={
                'db_table': 'hpclass',
            },
        ),
    ]
