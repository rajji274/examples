# Generated by Django 3.2.15 on 2022-11-02 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('dateofbirth', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('emailid', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('mobilenumber', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=50)),
                ('securityquestion', models.CharField(max_length=100)),
                ('securityanswer', models.CharField(max_length=100)),
                ('securityquestion1', models.CharField(max_length=100)),
                ('securityanswer1', models.CharField(max_length=100)),
                ('securityquestion2', models.CharField(max_length=100)),
                ('securityanswer2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Weatherdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('hour', models.CharField(max_length=100)),
                ('temperature', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
                ('humidity', models.CharField(max_length=100)),
                ('pressure', models.CharField(max_length=100)),
                ('windspeed', models.CharField(max_length=100)),
            ],
        ),
    ]
