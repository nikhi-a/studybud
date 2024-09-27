# Generated by Django 5.1.1 on 2024-09-27 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_alter_message_options_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="bio",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
