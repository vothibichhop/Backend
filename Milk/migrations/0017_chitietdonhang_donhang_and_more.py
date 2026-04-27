from datetime import datetime, timezone as dt_timezone

import django.db.models.deletion
from django.db import migrations, models


def seed_order_history(apps, schema_editor):
    DonHang = apps.get_model("Milk", "DonHang")
    ChiTietDonHang = apps.get_model("Milk", "ChiTietDonHang")
    Sua = apps.get_model("Milk", "Sua")

    products = {
        ma_sua: sua
        for ma_sua, sua in Sua.objects.in_bulk(["S01", "S02", "S10", "S11"]).items()
    }

    if len(products) < 4:
        return

    orders = {
        "DH001": DonHang.objects.update_or_create(
            id="DH001",
            defaults={
                "ngay_dat": datetime(2026, 2, 4, 14, 30, tzinfo=dt_timezone.utc),
                "trang_thai": "Dang giao",
                "tong_tien": 199000,
            },
        )[0],
        "DH002": DonHang.objects.update_or_create(
            id="DH002",
            defaults={
                "ngay_dat": datetime(2026, 2, 1, 8, 0, tzinfo=dt_timezone.utc),
                "trang_thai": "Da giao",
                "tong_tien": 356000,
            },
        )[0],
        "DH003": DonHang.objects.update_or_create(
            id="DH003",
            defaults={
                "ngay_dat": datetime(2026, 1, 28, 15, 45, tzinfo=dt_timezone.utc),
                "trang_thai": "Da huy",
                "tong_tien": 490000,
            },
        )[0],
    }

    order_lines = [
        ("DH001", "S10", 1, 45000),
        ("DH001", "S01", 1, 154000),
        ("DH002", "S11", 2, 178000),
        ("DH003", "S02", 1, 490000),
    ]

    for don_hang_id, san_pham_id, so_luong, gia_ban in order_lines:
        ChiTietDonHang.objects.update_or_create(
            don_hang=orders[don_hang_id],
            san_pham=products[san_pham_id],
            defaults={
                "so_luong": so_luong,
                "gia_ban": gia_ban,
            },
        )


class Migration(migrations.Migration):

    dependencies = [
        ("Milk", "0016_chitietgiohang_giohang_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DonHang",
            fields=[
                ("id", models.CharField(max_length=20, primary_key=True, serialize=False)),
                ("ngay_dat", models.DateTimeField()),
                ("trang_thai", models.CharField(max_length=50)),
                ("tong_tien", models.DecimalField(decimal_places=1, max_digits=12)),
            ],
            options={
                "verbose_name": "Don hang",
                "verbose_name_plural": "Don hang",
                "ordering": ["-ngay_dat", "id"],
            },
        ),
        migrations.CreateModel(
            name="ChiTietDonHang",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("so_luong", models.PositiveIntegerField(default=1)),
                ("gia_ban", models.DecimalField(decimal_places=1, max_digits=12)),
                (
                    "don_hang",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="san_pham",
                        to="Milk.donhang",
                    ),
                ),
                (
                    "san_pham",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="chi_tiet_don_hang",
                        to="Milk.sua",
                    ),
                ),
            ],
            options={
                "verbose_name": "Chi tiet don hang",
                "verbose_name_plural": "Chi tiet don hang",
                "ordering": ["id"],
            },
        ),
        migrations.RunPython(seed_order_history, migrations.RunPython.noop),
    ]
