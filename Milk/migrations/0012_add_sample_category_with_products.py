from django.db import migrations


LOAI_SUA_DATA = {
    "ma_loai_sua": "LS07",
    "ten_loai_sua": "Sữa bột trẻ em cao cấp",
}


DANH_MUC_DATA = {
    "ma_danh_muc": "DM08",
    "ten_danh_muc": "Sữa bột trẻ em cao cấp",
    "mo_ta": (
        "Danh mục sữa bột trẻ em cao cấp tập hợp các sản phẩm dinh dưỡng dành cho trẻ nhỏ, "
        "hỗ trợ phát triển chiều cao, trí não và tăng cường đề kháng trong từng giai đoạn."
    ),
    "noi_bat": "New",
    "loai_sua_id": "LS07",
    "thu_tu": 8,
    "hien_thi": True,
}


THUOC_TINH_DATA = [
    {
        "ma_thuoc_tinh": "DM08_AGE",
        "danh_muc_id": "DM08",
        "ten_thuoc_tinh": "Độ tuổi",
        "kieu_du_lieu": "text",
        "don_vi": "",
        "bat_buoc": True,
        "thu_tu": 1,
    },
    {
        "ma_thuoc_tinh": "DM08_STAGE",
        "danh_muc_id": "DM08",
        "ten_thuoc_tinh": "Giai đoạn",
        "kieu_du_lieu": "text",
        "don_vi": "",
        "bat_buoc": False,
        "thu_tu": 2,
    },
    {
        "ma_thuoc_tinh": "DM08_PACK",
        "danh_muc_id": "DM08",
        "ten_thuoc_tinh": "Đóng gói",
        "kieu_du_lieu": "text",
        "don_vi": "",
        "bat_buoc": False,
        "thu_tu": 3,
    },
]


SUA_DATA = [
    {
        "ma_sua": "S10",
        "ten_sua": "Sữa bột trẻ em Vinamilk Dielac Alpha Gold 4",
        "hang_sua_id": "HS04",
        "loai_sua_id": "LS07",
        "danh_muc_id": "DM08",
        "quy_cach": "900 g, Lẻ 1 lon",
        "trong_luong": 900,
        "don_vi": "g",
        "don_gia": 345000,
        "giam_gia": 5,
        "thanh_phan": "DHA, lutein, canxi, vitamin D3, chất xơ hòa tan",
        "loi_ich": "Hỗ trợ phát triển trí não, chiều cao và hệ miễn dịch cho trẻ từ 2 tuổi",
        "hinh": "suas/SUABOT1.jpg",
    },
    {
        "ma_sua": "S11",
        "ten_sua": "Sữa bột trẻ em Optimum Gold 4",
        "hang_sua_id": "HS07",
        "loai_sua_id": "LS07",
        "danh_muc_id": "DM08",
        "quy_cach": "850 g, Lẻ 1 lon",
        "trong_luong": 850,
        "don_vi": "g",
        "don_gia": 380000,
        "giam_gia": 7,
        "thanh_phan": "HMO, DHA, canxi, đạm whey giàu alpha-lactalbumin",
        "loi_ich": "Tăng sức đề kháng, hỗ trợ tiêu hóa và hấp thu tốt hơn",
        "hinh": "suas/SUABOT2.jpg",
    },
    {
        "ma_sua": "S12",
        "ten_sua": "Sữa bột trẻ em GrowPLUS+ Xanh 3+",
        "hang_sua_id": "HS03",
        "loai_sua_id": "LS07",
        "danh_muc_id": "DM08",
        "quy_cach": "900 g, Lẻ 1 lon",
        "trong_luong": 900,
        "don_vi": "g",
        "don_gia": 420000,
        "giam_gia": 6,
        "thanh_phan": "Kẽm, lysine, vitamin nhóm B, chất béo MCT",
        "loi_ich": "Hỗ trợ tăng cân lành mạnh và bổ sung năng lượng cho trẻ biếng ăn",
        "hinh": "suas/SUABOT3.jpg",
    },
    {
        "ma_sua": "S13",
        "ten_sua": "Sữa bột trẻ em Vinamilk Yoko Gold 3",
        "hang_sua_id": "HS04",
        "loai_sua_id": "LS07",
        "danh_muc_id": "DM08",
        "quy_cach": "850 g, Lẻ 1 lon",
        "trong_luong": 850,
        "don_vi": "g",
        "don_gia": 360000,
        "giam_gia": 4,
        "thanh_phan": "FOS, DHA, taurine, canxi, vitamin A",
        "loi_ich": "Hỗ trợ tiêu hóa, tăng cường thị lực và phát triển toàn diện",
        "hinh": "suas/SUABOT4.jpg",
    },
]


GIA_TRI_THUOC_TINH_DATA = [
    {"sua_id": "S10", "thuoc_tinh_id": "DM08_AGE", "gia_tri_van_ban": "2-6 tuổi"},
    {"sua_id": "S10", "thuoc_tinh_id": "DM08_STAGE", "gia_tri_van_ban": "Stage 4"},
    {"sua_id": "S10", "thuoc_tinh_id": "DM08_PACK", "gia_tri_van_ban": "Lon 900g"},
    {"sua_id": "S11", "thuoc_tinh_id": "DM08_AGE", "gia_tri_van_ban": "2-6 tuổi"},
    {"sua_id": "S11", "thuoc_tinh_id": "DM08_STAGE", "gia_tri_van_ban": "Stage 4"},
    {"sua_id": "S11", "thuoc_tinh_id": "DM08_PACK", "gia_tri_van_ban": "Lon 850g"},
    {"sua_id": "S12", "thuoc_tinh_id": "DM08_AGE", "gia_tri_van_ban": "3+ tuổi"},
    {"sua_id": "S12", "thuoc_tinh_id": "DM08_STAGE", "gia_tri_van_ban": "Stage 3+"},
    {"sua_id": "S12", "thuoc_tinh_id": "DM08_PACK", "gia_tri_van_ban": "Lon 900g"},
    {"sua_id": "S13", "thuoc_tinh_id": "DM08_AGE", "gia_tri_van_ban": "1-3 tuổi"},
    {"sua_id": "S13", "thuoc_tinh_id": "DM08_STAGE", "gia_tri_van_ban": "Stage 3"},
    {"sua_id": "S13", "thuoc_tinh_id": "DM08_PACK", "gia_tri_van_ban": "Lon 850g"},
]


def seed_category_with_products(apps, schema_editor):
    LoaiSua = apps.get_model("Milk", "LoaiSua")
    DanhMucSanPham = apps.get_model("Milk", "DanhMucSanPham")
    ThuocTinhDanhMuc = apps.get_model("Milk", "ThuocTinhDanhMuc")
    Sua = apps.get_model("Milk", "Sua")
    GiaTriThuocTinhSanPham = apps.get_model("Milk", "GiaTriThuocTinhSanPham")

    LoaiSua.objects.update_or_create(
        ma_loai_sua=LOAI_SUA_DATA["ma_loai_sua"],
        defaults={"ten_loai_sua": LOAI_SUA_DATA["ten_loai_sua"]},
    )

    DanhMucSanPham.objects.update_or_create(
        ma_danh_muc=DANH_MUC_DATA["ma_danh_muc"],
        defaults={
            "ten_danh_muc": DANH_MUC_DATA["ten_danh_muc"],
            "mo_ta": DANH_MUC_DATA["mo_ta"],
            "noi_bat": DANH_MUC_DATA["noi_bat"],
            "loai_sua_id": DANH_MUC_DATA["loai_sua_id"],
            "thu_tu": DANH_MUC_DATA["thu_tu"],
            "hien_thi": DANH_MUC_DATA["hien_thi"],
        },
    )

    for row in THUOC_TINH_DATA:
        ThuocTinhDanhMuc.objects.update_or_create(
            ma_thuoc_tinh=row["ma_thuoc_tinh"],
            defaults={
                "danh_muc_id": row["danh_muc_id"],
                "ten_thuoc_tinh": row["ten_thuoc_tinh"],
                "kieu_du_lieu": row["kieu_du_lieu"],
                "don_vi": row["don_vi"],
                "bat_buoc": row["bat_buoc"],
                "thu_tu": row["thu_tu"],
            },
        )

    for row in SUA_DATA:
        Sua.objects.update_or_create(ma_sua=row["ma_sua"], defaults=row)

    for row in GIA_TRI_THUOC_TINH_DATA:
        GiaTriThuocTinhSanPham.objects.update_or_create(
            sua_id=row["sua_id"],
            thuoc_tinh_id=row["thuoc_tinh_id"],
            defaults={
                "gia_tri_van_ban": row.get("gia_tri_van_ban", ""),
                "gia_tri_so": row.get("gia_tri_so"),
                "gia_tri_dung_sai": row.get("gia_tri_dung_sai"),
            },
        )


def remove_category_with_products(apps, schema_editor):
    LoaiSua = apps.get_model("Milk", "LoaiSua")
    DanhMucSanPham = apps.get_model("Milk", "DanhMucSanPham")
    ThuocTinhDanhMuc = apps.get_model("Milk", "ThuocTinhDanhMuc")
    Sua = apps.get_model("Milk", "Sua")
    GiaTriThuocTinhSanPham = apps.get_model("Milk", "GiaTriThuocTinhSanPham")

    GiaTriThuocTinhSanPham.objects.filter(
        thuoc_tinh_id__in=[row["ma_thuoc_tinh"] for row in THUOC_TINH_DATA]
    ).delete()
    Sua.objects.filter(ma_sua__in=[row["ma_sua"] for row in SUA_DATA]).delete()
    ThuocTinhDanhMuc.objects.filter(
        ma_thuoc_tinh__in=[row["ma_thuoc_tinh"] for row in THUOC_TINH_DATA]
    ).delete()
    DanhMucSanPham.objects.filter(ma_danh_muc=DANH_MUC_DATA["ma_danh_muc"]).delete()
    LoaiSua.objects.filter(ma_loai_sua=LOAI_SUA_DATA["ma_loai_sua"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("Milk", "0011_danhmucsanpham_thuoctinhdanhmuc_and_more"),
    ]

    operations = [
        migrations.RunPython(seed_category_with_products, remove_category_with_products),
    ]
