# Generated by Django 4.1.13 on 2024-03-15 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id_service', models.BigAutoField(primary_key=True, serialize=False)),
                ('type_service', models.CharField(max_length=255)),
            ],
        ),
    ]