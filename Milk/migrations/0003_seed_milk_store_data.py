from datetime import date

from django.db import migrations


LOAI_SUA_DATA = [
    {"ma_loai_sua": "LS01", "ten_loai_sua": "Sữa tươi"},
    {"ma_loai_sua": "LS02", "ten_loai_sua": "Sữa bột người lớn"},
    {"ma_loai_sua": "LS03", "ten_loai_sua": "Sữa bột trẻ em"},
    {"ma_loai_sua": "LS04", "ten_loai_sua": "Sữa đặc"},
    {"ma_loai_sua": "LS05", "ten_loai_sua": "Sữa chua ăn"},
    {"ma_loai_sua": "LS06", "ten_loai_sua": "Sữa thực vật"},
]


HANG_SUA_DATA = [
    {
        "ma_hang_sua": "HS01",
        "ten_hang_sua": "TH true MILK",
        "dia_chi": "Nghĩa Đàn, Nghệ An",
        "dien_thoai": "02383868686",
        "email": "cs@thmilk.vn",
    },
    {
        "ma_hang_sua": "HS02",
        "ten_hang_sua": "Abbott Ensure",
        "dia_chi": "Quận 1, TP HCM",
        "dien_thoai": "02838276940",
        "email": "support@abbott.com",
    },
    {
        "ma_hang_sua": "HS03",
        "ten_hang_sua": "Nutifood GrowPLUS+",
        "dia_chi": "Quận 7, TP HCM",
        "dien_thoai": "02854155555",
        "email": "care@nutifood.com.vn",
    },
    {
        "ma_hang_sua": "HS04",
        "ten_hang_sua": "Vinamilk",
        "dia_chi": "Quận 7, TP HCM",
        "dien_thoai": "02854155555",
        "email": "vinamilk@vinamilk.com.vn",
    },
    {
        "ma_hang_sua": "HS05",
        "ten_hang_sua": "Ngôi Sao Phương Nam",
        "dia_chi": "TP Thủ Đức, TP HCM",
        "dien_thoai": "02838279379",
        "email": "hotro@vinamilk.com.vn",
    },
    {
        "ma_hang_sua": "HS06",
        "ten_hang_sua": "Fami Vinasoy",
        "dia_chi": "Quảng Ngãi",
        "dien_thoai": "02553827777",
        "email": "support@vinasoy.com.vn",
    },
    {
        "ma_hang_sua": "HS07",
        "ten_hang_sua": "Optimum Gold",
        "dia_chi": "Bình Dương",
        "dien_thoai": "02743755555",
        "email": "care@vinamilk.com.vn",
    },
]


SUA_DATA = [
    {
        "ma_sua": "S01",
        "ten_sua": "Sữa tươi tiệt trùng TH true MILK",
        "hang_sua_id": "HS01",
        "loai_sua_id": "LS01",
        "quy_cach": "180 ml, Thùng 48 hộp",
        "trong_luong": 180,
        "don_vi": "ml",
        "don_gia": 430000,
        "giam_gia": 7,
        "thanh_phan": "Sữa tươi sạch, vitamin A, D",
        "loi_ich": "Bổ sung canxi và năng lượng mỗi ngày",
        "hinh": "suas/th-true-milk.jpg",
    },
    {
        "ma_sua": "S02",
        "ten_sua": "Sữa bột người lớn Ensure Gold",
        "hang_sua_id": "HS02",
        "loai_sua_id": "LS02",
        "quy_cach": "900 g, Lẻ 1 lon",
        "trong_luong": 900,
        "don_vi": "g",
        "don_gia": 490000,
        "giam_gia": 7,
        "thanh_phan": "Đạm, canxi, HMB",
        "loi_ich": "Hỗ trợ cơ xương và sức đề kháng",
        "hinh": "suas/ensure.jpg",
    },
    {
        "ma_sua": "S03",
        "ten_sua": "Sữa bột người lớn GrowPLUS+ Đỏ",
        "hang_sua_id": "HS03",
        "loai_sua_id": "LS02",
        "quy_cach": "900 g, Lẻ 1 lon",
        "trong_luong": 900,
        "don_vi": "g",
        "don_gia": 490000,
        "giam_gia": 7,
        "thanh_phan": "Chất béo, vitamin và khoáng chất",
        "loi_ich": "Bổ sung năng lượng cho người lớn",
        "hinh": "suas/grow plus.jpg",
    },
    {
        "ma_sua": "S04",
        "ten_sua": "Sữa tươi tiệt trùng Vinamilk 100%",
        "hang_sua_id": "HS04",
        "loai_sua_id": "LS01",
        "quy_cach": "180 ml, Thùng 48 hộp",
        "trong_luong": 180,
        "don_vi": "ml",
        "don_gia": 300000,
        "giam_gia": 7,
        "thanh_phan": "Sữa tươi tiệt trùng nguyên chất",
        "loi_ich": "Bổ sung canxi, vitamin D",
        "hinh": "suas/dutch lady.jpg",
    },
    {
        "ma_sua": "S05",
        "ten_sua": "Sữa tươi tiệt trùng Vinamilk có đường",
        "hang_sua_id": "HS04",
        "loai_sua_id": "LS01",
        "quy_cach": "180 ml, Thùng 48 hộp",
        "trong_luong": 180,
        "don_vi": "ml",
        "don_gia": 300000,
        "giam_gia": 7,
        "thanh_phan": "Sữa tươi tiệt trùng có đường",
        "loi_ich": "Cung cấp năng lượng và canxi",
        "hinh": "suas/grow-1.jpg",
    },
    {
        "ma_sua": "S06",
        "ten_sua": "Sữa đặc nguyên chất Ngôi Sao Phương Nam",
        "hang_sua_id": "HS05",
        "loai_sua_id": "LS04",
        "quy_cach": "100 g, Lẻ 1 hộp",
        "trong_luong": 100,
        "don_vi": "g",
        "don_gia": 50000,
        "giam_gia": 7,
        "thanh_phan": "Sữa đặc, đường, chất béo sữa",
        "loi_ich": "Pha cà phê, làm bánh, tăng vị béo",
        "hinh": "suas/ngoisao.jpg",
    },
    {
        "ma_sua": "S07",
        "ten_sua": "Sữa chua ăn Vinamilk",
        "hang_sua_id": "HS04",
        "loai_sua_id": "LS05",
        "quy_cach": "100 g, Thùng 48 hộp",
        "trong_luong": 100,
        "don_vi": "g",
        "don_gia": 50000,
        "giam_gia": 7,
        "thanh_phan": "Sữa lên men, men sống probiotic",
        "loi_ich": "Hỗ trợ tiêu hóa, tăng đề kháng",
        "hinh": "suas/suachuaan.jpg",
    },
    {
        "ma_sua": "S08",
        "ten_sua": "Sữa thực vật Fami Canxi",
        "hang_sua_id": "HS06",
        "loai_sua_id": "LS06",
        "quy_cach": "180 ml, Thùng 48 hộp",
        "trong_luong": 180,
        "don_vi": "ml",
        "don_gia": 50000,
        "giam_gia": 7,
        "thanh_phan": "Đậu nành, canxi, vitamin B",
        "loi_ich": "Tốt cho tim mạch và xương khớp",
        "hinh": "suas/sua fami.jpg",
    },
    {
        "ma_sua": "S09",
        "ten_sua": "Sữa bột trẻ em Optimum Gold",
        "hang_sua_id": "HS07",
        "loai_sua_id": "LS03",
        "quy_cach": "800 g, Lẻ 1 lon",
        "trong_luong": 800,
        "don_vi": "g",
        "don_gia": 300000,
        "giam_gia": 7,
        "thanh_phan": "DHA, canxi, chất xơ hòa tan",
        "loi_ich": "Hỗ trợ tăng chiều cao và trí não",
        "hinh": "suas/sua optimum.jpg",
    },
]


KHACH_HANG_DATA = [
    {
        "ma_kh": "KH01",
        "ten_kh": "Nguyễn Văn An",
        "gioi_tinh": "M",
        "dia_chi": "Quận 3, TP HCM",
        "dien_thoai": "0901234567",
        "email": "an.nguyen@example.com",
    },
    {
        "ma_kh": "KH02",
        "ten_kh": "Trần Thị Bích",
        "gioi_tinh": "F",
        "dia_chi": "Thủ Đức, TP HCM",
        "dien_thoai": "0912345678",
        "email": "bich.tran@example.com",
    },
]


HOA_DON_DATA = [
    {"id": 1, "khach_hang_id": "KH01", "ngay_hd": date(2026, 4, 20), "tri_gia": 920000},
    {"id": 2, "khach_hang_id": "KH02", "ngay_hd": date(2026, 4, 21), "tri_gia": 350000},
]


CHI_TIET_HOA_DON_DATA = [
    {"hoa_don_id": 1, "sua_id": "S01", "so_luong": 1, "don_gia": 430000},
    {"hoa_don_id": 1, "sua_id": "S02", "so_luong": 1, "don_gia": 490000},
    {"hoa_don_id": 2, "sua_id": "S06", "so_luong": 1, "don_gia": 50000},
    {"hoa_don_id": 2, "sua_id": "S09", "so_luong": 1, "don_gia": 300000},
]


def seed_data(apps, schema_editor):
    LoaiSua = apps.get_model("Milk", "LoaiSua")
    HangSua = apps.get_model("Milk", "HangSua")
    Sua = apps.get_model("Milk", "Sua")
    KhachHang = apps.get_model("Milk", "KhachHang")
    HoaDon = apps.get_model("Milk", "HoaDon")
    ChiTietHoaDon = apps.get_model("Milk", "ChiTietHoaDon")

    for row in LOAI_SUA_DATA:
        LoaiSua.objects.update_or_create(ma_loai_sua=row["ma_loai_sua"], defaults=row)

    for row in HANG_SUA_DATA:
        HangSua.objects.update_or_create(ma_hang_sua=row["ma_hang_sua"], defaults=row)

    for row in SUA_DATA:
        Sua.objects.update_or_create(ma_sua=row["ma_sua"], defaults=row)

    for row in KHACH_HANG_DATA:
        KhachHang.objects.update_or_create(ma_kh=row["ma_kh"], defaults=row)

    for row in HOA_DON_DATA:
        hoa_don_id = row["id"]
        defaults = {k: v for k, v in row.items() if k != "id"}
        HoaDon.objects.update_or_create(id=hoa_don_id, defaults=defaults)

    for row in CHI_TIET_HOA_DON_DATA:
        ChiTietHoaDon.objects.update_or_create(
            hoa_don_id=row["hoa_don_id"],
            sua_id=row["sua_id"],
            defaults={
                "so_luong": row["so_luong"],
                "don_gia": row["don_gia"],
            },
        )


def remove_seed_data(apps, schema_editor):
    LoaiSua = apps.get_model("Milk", "LoaiSua")
    HangSua = apps.get_model("Milk", "HangSua")
    Sua = apps.get_model("Milk", "Sua")
    KhachHang = apps.get_model("Milk", "KhachHang")
    HoaDon = apps.get_model("Milk", "HoaDon")
    ChiTietHoaDon = apps.get_model("Milk", "ChiTietHoaDon")

    for row in CHI_TIET_HOA_DON_DATA:
        ChiTietHoaDon.objects.filter(
            hoa_don_id=row["hoa_don_id"], sua_id=row["sua_id"]
        ).delete()
    HoaDon.objects.filter(id__in=[row["id"] for row in HOA_DON_DATA]).delete()
    KhachHang.objects.filter(ma_kh__in=[row["ma_kh"] for row in KHACH_HANG_DATA]).delete()
    Sua.objects.filter(ma_sua__in=[row["ma_sua"] for row in SUA_DATA]).delete()
    HangSua.objects.filter(
        ma_hang_sua__in=[row["ma_hang_sua"] for row in HANG_SUA_DATA]
    ).delete()
    LoaiSua.objects.filter(
        ma_loai_sua__in=[row["ma_loai_sua"] for row in LOAI_SUA_DATA]
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("Milk", "0002_sua_hinh_image"),
    ]

    operations = [
        migrations.RunPython(seed_data, remove_seed_data),
    ]
