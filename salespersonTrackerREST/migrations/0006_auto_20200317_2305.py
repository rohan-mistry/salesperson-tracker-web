# Generated by Django 2.2.10 on 2020-03-17 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("salespersonTrackerREST", "0005_auto_20200317_2303")]

    operations = [
        migrations.AlterField(
            model_name="salesperson",
            name="Photo",
            field=models.ImageField(
                default="media/Default.png", upload_to="media/salesperson"
            ),
        )
    ]
