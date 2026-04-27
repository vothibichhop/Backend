from django.db import migrations


LOAI_SUA_UPDATES = {
    "LS01": "Sữa tươi",
    "LS02": "Sữa bột người lớn",
    "LS03": "Sữa bột trẻ em",
    "LS04": "Sữa đặc",
    "LS05": "Sữa chua ăn",
    "LS06": "Sữa thực vật",
}


HANG_SUA_UPDATES = {
    "HS01": {
        "ten_hang_sua": "TH true MILK",
        "dia_chi": "Nghĩa Đàn, Nghệ An",
    },
    "HS02": {
        "ten_hang_sua": "Abbott Ensure",
        "dia_chi": "Quận 1, TP HCM",
    },
    "HS03": {
        "ten_hang_sua": "Nutifood GrowPLUS+",
        "dia_chi": "Quận 7, TP HCM",
    },
    "HS04": {
        "ten_hang_sua": "Vinamilk",
        "dia_chi": "Quận 7, TP HCM",
    },
    "HS05": {
        "ten_hang_sua": "Ngôi Sao Phương Nam",
        "dia_chi": "TP Thủ Đức, TP HCM",
    },
    "HS06": {
        "ten_hang_sua": "Fami Vinasoy",
        "dia_chi": "Quảng Ngãi",
    },
    "HS07": {
        "ten_hang_sua": "Optimum Gold",
        "dia_chi": "Bình Dương",
    },
}


SUA_UPDATES = {
    "S01": {
        "ten_sua": "Sữa tươi tiệt trùng TH true MILK",
        "quy_cach": "180 ml, Thùng 48 hộp",
        "thanh_phan": "Sữa tươi sạch, vitamin A, D",
        "loi_ich": "Bổ sung canxi và năng lượng mỗi ngày",
    },
    "S02": {
        "ten_sua": "Sữa bột người lớn Ensure Gold",
        "quy_cach": "900 g, Lẻ 1 lon",
        "thanh_phan": "Đạm, canxi, HMB",
        "loi_ich": "Hỗ trợ cơ xương và sức đề kháng",
    },
    "S03": {
        "ten_sua": "Sữa bột người lớn GrowPLUS+ Đỏ",
        "quy_cach": "900 g, Lẻ 1 lon",
        "thanh_phan": "Chất béo, vitamin và khoáng chất",
        "loi_ich": "Bổ sung năng lượng cho người lớn",
    },
    "S04": {
        "ten_sua": "Sữa tươi tiệt trùng Vinamilk 100%",
        "quy_cach": "180 ml, Thùng 48 hộp",
        "thanh_phan": "Sữa tươi tiệt trùng nguyên chất",
        "loi_ich": "Bổ sung canxi, vitamin D",
    },
    "S05": {
        "ten_sua": "Sữa tươi tiệt trùng Vinamilk có đường",
        "quy_cach": "180 ml, Thùng 48 hộp",
        "thanh_phan": "Sữa tươi tiệt trùng có đường",
        "loi_ich": "Cung cấp năng lượng và canxi",
    },
    "S06": {
        "ten_sua": "Sữa đặc nguyên chất Ngôi Sao Phương Nam",
        "quy_cach": "100 g, Lẻ 1 hộp",
        "thanh_phan": "Sữa đặc, đường, chất béo sữa",
        "loi_ich": "Pha cà phê, làm bánh, tăng vị béo",
    },
    "S07": {
        "ten_sua": "Sữa chua ăn Vinamilk",
        "quy_cach": "100 g, Thùng 48 hộp",
        "thanh_phan": "Sữa lên men, men sống probiotic",
        "loi_ich": "Hỗ trợ tiêu hóa, tăng đề kháng",
    },
    "S08": {
        "ten_sua": "Sữa thực vật Fami Canxi",
        "quy_cach": "180 ml, Thùng 48 hộp",
        "thanh_phan": "Đậu nành, canxi, vitamin B",
        "loi_ich": "Tốt cho tim mạch và xương khớp",
    },
    "S09": {
        "ten_sua": "Sữa bột trẻ em Optimum Gold",
        "quy_cach": "800 g, Lẻ 1 lon",
        "thanh_phan": "DHA, canxi, chất xơ hòa tan",
        "loi_ich": "Hỗ trợ tăng chiều cao và trí não",
    },
}


KHACH_HANG_UPDATES = {
    "KH01": {"ten_kh": "Nguyễn Văn An", "dia_chi": "Quận 3, TP HCM"},
    "KH02": {"ten_kh": "Trần Thị Bích", "dia_chi": "Thủ Đức, TP HCM"},
}


def apply_diacritics(apps, schema_editor):
    LoaiSua = apps.get_model("Milk", "LoaiSua")
    HangSua = apps.get_model("Milk", "HangSua")
    Sua = apps.get_model("Milk", "Sua")
    KhachHang = apps.get_model("Milk", "KhachHang")

    for ma_loai_sua, ten_loai_sua in LOAI_SUA_UPDATES.items():
        LoaiSua.objects.filter(ma_loai_sua=ma_loai_sua).update(ten_loai_sua=ten_loai_sua)

    for ma_hang_sua, values in HANG_SUA_UPDATES.items():
        HangSua.objects.filter(ma_hang_sua=ma_hang_sua).update(**values)

    for ma_sua, values in SUA_UPDATES.items():
        Sua.objects.filter(ma_sua=ma_sua).update(**values)

    for ma_kh, values in KHACH_HANG_UPDATES.items():
        KhachHang.objects.filter(ma_kh=ma_kh).update(**values)


class Migration(migrations.Migration):
    dependencies = [
        ("Milk", "0003_seed_milk_store_data"),
    ]

    operations = [
        migrations.RunPython(apply_diacritics, migrations.RunPython.noop),
    ]
