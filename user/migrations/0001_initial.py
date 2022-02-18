# Generated by Django 4.0.2 on 2022-02-18 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=200)),
                ('Last_name', models.CharField(max_length=200)),
                ('Gender', models.CharField(max_length=200)),
                ('Date_of_birth', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_number', models.CharField(max_length=10)),
                ('Password', models.CharField(max_length=256)),
            ],
        ),
    ]