from django.db import migrations, models


def seed_banner_data(apps, schema_editor):
    Sua = apps.get_model("Milk", "Sua")
    BannerQuangCao = apps.get_model("Milk", "BannerQuangCao")

    Sua.objects.update_or_create(
        ma_sua="S10",
        defaults={
            "ten_sua": "Sữa chua ăn mix mật ong ngũ cốc",
            "hang_sua_id": "HS04",
            "loai_sua_id": "LS05",
            "quy_cach": "100 g, lốc 4 hộp",
            "trong_luong": 100,
            "don_vi": "g",
            "don_gia": 38000,
            "giam_gia": 0,
            "thanh_phan": "Sữa chua, mật ong, ngũ cốc và men sống probiotic",
            "loi_ich": "Giữ hệ tiêu hóa cân bằng, tăng vị ngon giàu protein và canxi",
            "hinh": "suas/ngu_coc.jpg",
        },
    )

    BannerQuangCao.objects.update_or_create(
        ma_banner="BN01",
        defaults={
            "sua_id": "S10",
            "tieu_de": "Sữa chua ăn mix mật ong ngũ cốc",
            "mo_ta": (
                "Sữa chua ngũ cốc là sự kết hợp dinh dưỡng giữa sữa chua sánh mịn "
                "và ngũ cốc dẻo giòn, mang lại vị chua nhẹ, ngọt thơm, giàu protein, canxi và chất xơ"
            ),
            "nhan": "Mới",
            "mau_nen": "#f7c514",
            "mau_chu": "#b34a00",
            "thu_tu": 1,
            "hien_thi": True,
        },
    )


def remove_banner_data(apps, schema_editor):
    BannerQuangCao = apps.get_model("Milk", "BannerQuangCao")
    Sua = apps.get_model("Milk", "Sua")

    BannerQuangCao.objects.filter(ma_banner="BN01").delete()
    Sua.objects.filter(ma_sua="S10").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("Milk", "0006_replace_svg_with_jpg_images"),
    ]

    operations = [
        migrations.CreateModel(
            name="BannerQuangCao",
            fields=[
                ("ma_banner", models.CharField(max_length=20, primary_key=True, serialize=False)),
                ("tieu_de", models.CharField(max_length=200)),
                ("mo_ta", models.TextField(blank=True)),
                ("nhan", models.CharField(blank=True, max_length=50)),
                ("mau_nen", models.CharField(default="#f8c300", max_length=20)),
                ("mau_chu", models.CharField(default="#8a3b12", max_length=20)),
                ("thu_tu", models.PositiveIntegerField(default=0)),
                ("hien_thi", models.BooleanField(default=True)),
                (
                    "sua",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=models.deletion.CASCADE,
                        related_name="banners",
                        to="Milk.sua",
                    ),
                ),
            ],
            options={
                "verbose_name": "Banner quang cao",
                "verbose_name_plural": "Banner quang cao",
                "ordering": ["thu_tu", "ma_banner"],
            },
        ),
        migrations.RunPython(seed_banner_data, remove_banner_data),
    ]
