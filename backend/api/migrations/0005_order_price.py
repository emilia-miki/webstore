# Generated by Django 4.1.5 on 2023-02-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_product_img"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="price",
            field=models.DecimalField(decimal_places=2, default=23.4, max_digits=9),
            preserve_default=False,
        ),
    ]
