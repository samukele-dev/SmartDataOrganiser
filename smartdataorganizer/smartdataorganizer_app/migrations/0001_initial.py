# Generated by Django 4.2.7 on 2024-01-02 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spreadsheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('name', models.CharField(max_length=255)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
