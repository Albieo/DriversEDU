# Generated by Django 5.1 on 2024-09-03 13:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0011_remove_category_test_number_question_test_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="text",
            field=models.TextField(max_length=200),
        ),
    ]
