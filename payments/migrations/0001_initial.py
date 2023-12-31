# Generated by Django 4.2.5 on 2023-11-01 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("checkout", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("p_merchant_id", models.CharField(max_length=10)),
                ("p_currency", models.CharField(max_length=50)),
                ("p_amount", models.CharField(max_length=50)),
                ("p_redirect_url", models.CharField(max_length=50)),
                ("p_cancel_url", models.CharField(max_length=50)),
                ("p_language", models.CharField(max_length=50)),
                ("p_billing_name", models.CharField(max_length=50)),
                ("p_billing_address", models.CharField(max_length=50)),
                ("p_billing_city", models.CharField(max_length=50)),
                ("p_billing_state", models.CharField(max_length=50)),
                ("p_billing_zip", models.CharField(max_length=50)),
                ("p_billing_country", models.CharField(max_length=50)),
                ("p_billing_tel", models.CharField(max_length=50)),
                ("p_billing_email", models.CharField(max_length=50)),
                ("p_delivery_name", models.CharField(max_length=50)),
                ("p_delivery_address", models.CharField(max_length=50)),
                ("p_delivery_city", models.CharField(max_length=50)),
                ("p_delivery_state", models.CharField(max_length=50)),
                ("p_delivery_zip", models.CharField(max_length=50)),
                ("p_delivery_country", models.CharField(max_length=50)),
                ("p_delivery_tel", models.CharField(max_length=50)),
                ("p_merchant_param1", models.CharField(max_length=50)),
                ("p_merchant_param2", models.CharField(max_length=50)),
                ("p_merchant_param3", models.CharField(max_length=50)),
                ("p_merchant_param4", models.CharField(max_length=50)),
                ("p_merchant_param5", models.CharField(max_length=50)),
                ("p_integration_type", models.CharField(max_length=50)),
                ("p_promo_code", models.CharField(max_length=50)),
                ("p_customer_identifier", models.CharField(max_length=50)),
                (
                    "p_order_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="checkout.order"
                    ),
                ),
            ],
        ),
    ]
