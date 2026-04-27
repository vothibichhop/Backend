from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Milk", "0017_chitietdonhang_donhang_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="chitietdonhang",
            name="ten_lua_chon",
            field=models.CharField(blank=True, default="", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="donhang",
            name="dia_chi_giao_hang",
            field=models.CharField(blank=True, default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="donhang",
            name="phuong_thuc_nhan",
            field=models.CharField(default="giao_tan_noi", max_length=30),
        ),
        migrations.AddField(
            model_name="donhang",
            name="phuong_thuc_thanh_toan",
            field=models.CharField(default="cod", max_length=30),
        ),
        migrations.AddField(
            model_name="donhang",
            name="so_dien_thoai",
            field=models.CharField(blank=True, default="", max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="donhang",
            name="ten_nguoi_nhan",
            field=models.CharField(blank=True, default="", max_length=100),
            preserve_default=False,
        ),
    ]
