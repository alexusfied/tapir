# Generated by Django 3.2.23 on 2024-07-02 15:48

import django.contrib.postgres.fields.hstore
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("log", "0006_alter_emaillogentry_email_content"),
        ("coop", "0041_auto_20231221_1403"),
    ]

    operations = [
        migrations.CreateModel(
            name="MembershipResignationCreateLogEntry",
            fields=[
                (
                    "logentry_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="log.logentry",
                    ),
                ),
                ("values", django.contrib.postgres.fields.hstore.HStoreField()),
            ],
            options={
                "abstract": False,
            },
            bases=("log.logentry",),
        ),
        migrations.CreateModel(
            name="MembershipResignationUpdateLogEntry",
            fields=[
                (
                    "logentry_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="log.logentry",
                    ),
                ),
                ("old_values", django.contrib.postgres.fields.hstore.HStoreField()),
                ("new_values", django.contrib.postgres.fields.hstore.HStoreField()),
            ],
            options={
                "abstract": False,
            },
            bases=("log.logentry",),
        ),
        migrations.CreateModel(
            name="MembershipResignation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cancellation_date",
                    models.DateField(default=django.utils.timezone.now),
                ),
                ("pay_out_day", models.DateField(null=True)),
                ("cancellation_reason", models.CharField(max_length=1000)),
                ("coop_buys_shares_back", models.BooleanField()),
                (
                    "willing_to_gift_shares_to_coop",
                    models.BooleanField(
                        help_text="Willing to gift shares to coop",
                        verbose_name="Willing to gift shares to coop",
                    ),
                ),
                ("paid_out", models.BooleanField(default=False)),
                (
                    "share_owner",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="share_owner",
                        to="coop.shareowner",
                        verbose_name="Shareowner",
                    ),
                ),
                (
                    "transfering_shares_to",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="owner_to_transfer",
                        to="coop.shareowner",
                        verbose_name="OwnerToTransfer",
                    ),
                ),
            ],
        ),
    ]
