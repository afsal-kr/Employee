# Generated by Django 5.0.2 on 2024-05-08 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empolye',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('salary', models.IntegerField()),
            ],
        ),
    ]