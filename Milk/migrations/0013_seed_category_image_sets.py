from django.db import migrations


NEW_LOAI_SUA = [
    {
        "ma_loai_sua": "LS08",
        "ten_loai_sua": "Bột ăn dặm",
    },
]


DANH_MUC_UPDATES = [
    {
        "ma_danh_muc": "DM02",
        "loai_sua_id": "LS08",
        "mo_ta": (
            "Bột ăn dặm là nhóm thực phẩm bổ sung cho trẻ nhỏ trong giai đoạn chuyển tiếp "
            "sang ăn dặm, giúp đa dạng khẩu vị và tăng cường dưỡng chất cần thiết."
        ),
    },
]


SUA_UPSERTS = [
    {
        "ma_sua": "S01",
        "ten_sua": "Sữa tươi tiệt trùng TH true MILK không đường",
        "hang_sua_id": "HS01",
        "loai_sua_id": "LS01",
        "danh_muc_id": "DM05",
        "quy_cach": "180 ml, Thùng 48 hộp",
        "trong_luong": 180,
        "don_vi": "ml",
        "don_gia": 430000,
        "giam_gia": 7,
        "thanh_phan": "Sữa tươi sạch, vitamin A, D, canxi tự nhiên",
        "loi_ich": "Bổ sung năng lượng và canxi hằng ngày cho cả gia đình",
        "hinh": "suas/tuoi1.jpg",
    },
    {
        "ma_sua": "S02",
        "ten_sua": "Sữa bột người lớn Ensure Gold vani",
        "hang_sua_id": "HS02",
        "loai_sua_id": "LS02",
        "danh_muc_id": "DM03",
        "quy_cach": "900 g, Lẻ 1 lon",
        "trong_luong": 900,
        "don_vi": "g",
        "don_gia": 490000,
        "giam_gia": 7,
        "thanh_phan": "Đạm chất lượng cao, canxi, HMB, vitamin D",
        "loi_ich": "Hỗ trợ duy trì cơ xương và tăng cường sức đề kháng",
        "hinh": "suas/suabotnguoilon1.jpg",
    },
    {
        "ma_sua": "S03",
        "ten_sua": "Sữa bột người lớn GrowPLUS+ Adult",
        "hang_sua_id": "HS03",
        "loai_sua_id": "LS02",
        "danh_muc_id": "DM03",
        "quy_cach": "900 g, Lẻ 1 lon",
        "trong_luong": 900,
        "don_vi": "g",
        "don_gia": 470000,
        "giam_gia": 6,
        "thanh_phan": "Chất béo MCT, đạm, vitamin và khoáng chất",
        "loi_ich": "Bổ sung năng lượng và hỗ trợ phục hồi thể trạng cho người lớn",
        "hinh": "suas/suabotnguoilon2.jpg",
    },
    {
        "ma_sua": "S04",
        "ten_sua": "Sữa tươi tiệt trùng Vinamilk 100%",
        "hang_sua_id": "HS04",
        "loai_sua_id": "LS01",
        "danh_muc_id": "DM05",
        "quy_cach": "180 ml, Thùng 48 hộp",
        "trong_luong": 180,
        "don_vi": "ml",
        "don_gia": 300000,
        "giam_gia": 7,
        "thanh_phan": "Sữa tươi nguyên chất, vitamin D3, canxi",
        "loi_ich": "Giữ hương vị tự nhiên và hỗ trợ phát triển xương chắc khỏe",
        "hinh": "suas/tuoi2.jpg",
    },
    {
        "ma_sua": "S05",
        "ten_sua": "Sữa tươi tiệt trùng Vinamilk có đường",
        "hang_sua_id": "HS04",
        "loai_sua_id": "LS01",
        "danh_muc_id": "DM05",
        "quy_cach": "180 ml, Thùng 48 hộp",
        "trong_luong": 180,
        "don_vi": "ml",
        "don_gia": 300000,
        "giam_gia": 7,
        "thanh_phan": "Sữa tươi tiệt trùng, đường, vitamin A và D",
        "loi_ich": "Cung cấp năng lượng nhanh, vị ngọt dễ uống cho trẻ em",
        "hinh": "suas/tuoi3.jpg",
    },
    {
        "ma_sua": "S07",
        "ten_sua": "Sữa chua ăn Vinamilk có đường",
        "hang_sua_id": "HS04",
        "loai_sua_id": "LS05",
        "danh_muc_id": "DM04",
        "quy_cach": "100 g, Lốc 4 hũ",
        "trong_luong": 100,
        "don_vi": "g",
        "don_gia": 32000,
        "giam_gia": 5,
        "thanh_phan": "Sữa lên men, men sống probiotic, canxi",
        "loi_ich": "Hỗ trợ tiêu hóa và tăng hấp thu dưỡng chất",
        "hinh": "suas/an1.jpg",
    },
    {
        "ma_sua": "S08",
        "ten_sua": "Sữa đậu nành Fami Canxi",
        "hang_sua_id": "HS06",
        "loai_sua_id": "LS06",
        "danh_muc_id": "DM07",
        "quy_cach": "200 ml, Lốc 6 hộp",
        "trong_luong": 200,
        "don_vi": "ml",
        "don_gia": 42000,
        "giam_gia": 5,
        "thanh_phan": "Đậu nành nguyên chất, canxi, vitamin B2",
        "loi_ich": "Bổ sung canxi và đạm thực vật, phù hợp dùng mỗi ngày",
        "hinh": "suas/thucvat1.jpg",
    },
    {
        "ma_sua": "S14",
        "ten_sua": "Sữa tươi tiệt trùng TH true MILK ít đường",
        "hang_sua_id": "HS01",
        "loai_sua_id": "LS01",
        "danh_muc_id": "DM05",
        "quy_cach": "180 ml, Thùng 48 hộp",
        "trong_luong": 180,
        "don_vi": "ml",
        "don_gia": 438000,
        "giam_gia": 6,
        "thanh_phan": "Sữa tươi sạch, đường tinh luyện, vitamin D",
        "loi_ich": "Giảm độ ngọt nhưng vẫn giữ vị thơm béo dễ uống",
        "hinh": "suas/tuoi4.jpg",
    },
    {
        "ma_sua": "S15",
        "ten_sua": "Sữa bột người lớn Ensure Gold ít ngọt",
        "hang_sua_id": "HS02",
        "loai_sua_id": "LS02",
        "danh_muc_id": "DM03",
        "quy_cach": "850 g, Lẻ 1 lon",
        "trong_luong": 850,
        "don_vi": "g",
        "don_gia": 485000,
        "giam_gia": 5,
        "thanh_phan": "Đạm, HMB, chất xơ FOS, vitamin nhóm B",
        "loi_ich": "Dễ uống hơn cho người cần kiểm soát vị ngọt nhưng vẫn đủ dưỡng chất",
        "hinh": "suas/suabotnguoilon3.jpg",
    },
    {
        "ma_sua": "S16",
        "ten_sua": "Sữa bột người lớn EnPlus Gold",
        "hang_sua_id": "HS03",
        "loai_sua_id": "LS02",
        "danh_muc_id": "DM03",
        "quy_cach": "900 g, Lẻ 1 lon",
        "trong_luong": 900,
        "don_vi": "g",
        "don_gia": 455000,
        "giam_gia": 6,
        "thanh_phan": "Đạm whey, canxi, lysine, vitamin tổng hợp",
        "loi_ich": "Hỗ trợ tăng cường thể lực và giảm mệt mỏi cho người lớn tuổi",
        "hinh": "suas/suabotnguoilon4.jpg",
    },
    {
        "ma_sua": "S17",
        "ten_sua": "Sữa chua ăn Vinamilk dâu",
        "hang_sua_id": "HS04",
        "loai_sua_id": "LS05",
        "danh_muc_id": "DM04",
        "quy_cach": "100 g, Lốc 4 hũ",
        "trong_luong": 100,
        "don_vi": "g",
        "don_gia": 34000,
        "giam_gia": 5,
        "thanh_phan": "Sữa lên men, men sống probiotic, hương dâu",
        "loi_ich": "Kết hợp vị trái cây thơm ngon và lợi khuẩn tốt cho đường ruột",
        "hinh": "suas/an2.jpg",
    },
    {
        "ma_sua": "S18",
        "ten_sua": "Sữa chua ăn Vinamilk nha đam",
        "hang_sua_id": "HS04",
        "loai_sua_id": "LS05",
        "danh_muc_id": "DM04",
        "quy_cach": "100 g, Lốc 4 hũ",
        "trong_luong": 100,
        "don_vi": "g",
        "don_gia": 35000,
        "giam_gia": 4,
        "thanh_phan": "Sữa lên men, nha đam, men sống probiotic",
        "loi_ich": "Thanh mát, dễ ăn và hỗ trợ hệ tiêu hóa khỏe mạnh",
        "hinh": "suas/an3.png",
    },
    {
        "ma_sua": "S19",
        "ten_sua": "Sữa chua ăn Vinamilk ít đường",
        "hang_sua_id": "HS04",
        "loai_sua_id": "LS05",
        "danh_muc_id": "DM04",
        "quy_cach": "100 g, Lốc 4 hũ",
        "trong_luong": 100,
        "don_vi": "g",
        "don_gia": 33000,
        "giam_gia": 4,
        "thanh_phan": "Sữa lên men, lợi khuẩn, hàm lượng đường giảm",
        "loi_ich": "Phù hợp cho người thích vị thanh nhẹ nhưng vẫn giàu lợi khuẩn",
        "hinh": "suas/an4.jpg",
    },
    {
        "ma_sua": "S20",
        "ten_sua": "Sữa đậu nành Fami nguyên chất",
        "hang_sua_id": "HS06",
        "loai_sua_id": "LS06",
        "danh_muc_id": "DM07",
        "quy_cach": "200 ml, Lốc 6 hộp",
        "trong_luong": 200,
        "don_vi": "ml",
        "don_gia": 40000,
        "giam_gia": 5,
        "thanh_phan": "Đậu nành chọn lọc, đạm thực vật, vitamin E",
        "loi_ich": "Giữ hương vị đậu nành tự nhiên, phù hợp cho chế độ ăn cân bằng",
        "hinh": "suas/thucvat2.jpg",
    },
    {
        "ma_sua": "S21",
        "ten_sua": "Sữa đậu nành Fami ít đường",
        "hang_sua_id": "HS06",
        "loai_sua_id": "LS06",
        "danh_muc_id": "DM07",
        "quy_cach": "200 ml, Lốc 6 hộp",
        "trong_luong": 200,
        "don_vi": "ml",
        "don_gia": 40500,
        "giam_gia": 4,
        "thanh_phan": "Đậu nành, vitamin nhóm B, lượng đường giảm",
        "loi_ich": "Phù hợp cho người muốn dùng sữa thực vật có vị nhẹ hơn",
        "hinh": "suas/thucvat3.jpg",
    },
    {
        "ma_sua": "S22",
        "ten_sua": "Sữa ngũ cốc Fami bổ sung canxi",
        "hang_sua_id": "HS06",
        "loai_sua_id": "LS06",
        "danh_muc_id": "DM07",
        "quy_cach": "200 ml, Lốc 6 hộp",
        "trong_luong": 200,
        "don_vi": "ml",
        "don_gia": 43000,
        "giam_gia": 4,
        "thanh_phan": "Ngũ cốc, đậu nành, canxi, vitamin D",
        "loi_ich": "Bổ sung năng lượng và khoáng chất từ nguồn gốc thực vật",
        "hinh": "suas/thucvat4.jpg",
    },
    {
        "ma_sua": "S23",
        "ten_sua": "Bột ăn dặm Ridielac gà đậu Hà Lan",
        "hang_sua_id": "HS04",
        "loai_sua_id": "LS08",
        "danh_muc_id": "DM02",
        "quy_cach": "350 g, Lẻ 1 hộp",
        "trong_luong": 350,
        "don_vi": "g",
        "don_gia": 78000,
        "giam_gia": 5,
        "thanh_phan": "Bột gạo, thịt gà, đậu Hà Lan, vitamin và khoáng chất",
        "loi_ich": "Bổ sung đạm và chất xơ cho trẻ từ giai đoạn ăn dặm",
        "hinh": "suas/andam1.jpg",
    },
    {
        "ma_sua": "S24",
        "ten_sua": "Bột ăn dặm Ridielac heo cà rốt",
        "hang_sua_id": "HS04",
        "loai_sua_id": "LS08",
        "danh_muc_id": "DM02",
        "quy_cach": "350 g, Lẻ 1 hộp",
        "trong_luong": 350,
        "don_vi": "g",
        "don_gia": 79000,
        "giam_gia": 5,
        "thanh_phan": "Bột gạo, thịt heo, cà rốt, canxi và sắt",
        "loi_ich": "Tăng cường năng lượng và hỗ trợ bé làm quen vị mặn",
        "hinh": "suas/andam2.jpg",
    },
    {
        "ma_sua": "S25",
        "ten_sua": "Bột ăn dặm yến mạch sữa",
        "hang_sua_id": "HS03",
        "loai_sua_id": "LS08",
        "danh_muc_id": "DM02",
        "quy_cach": "300 g, Lẻ 1 hộp",
        "trong_luong": 300,
        "don_vi": "g",
        "don_gia": 72000,
        "giam_gia": 4,
        "thanh_phan": "Yến mạch, sữa bột, chất xơ hòa tan, vitamin B",
        "loi_ich": "Dễ tiêu hóa, phù hợp cho bữa phụ của trẻ nhỏ",
        "hinh": "suas/andam3.jpg",
    },
    {
        "ma_sua": "S26",
        "ten_sua": "Bột ăn dặm ngũ cốc rau củ",
        "hang_sua_id": "HS03",
        "loai_sua_id": "LS08",
        "danh_muc_id": "DM02",
        "quy_cach": "300 g, Lẻ 1 hộp",
        "trong_luong": 300,
        "don_vi": "g",
        "don_gia": 74000,
        "giam_gia": 4,
        "thanh_phan": "Ngũ cốc tổng hợp, rau củ sấy, vitamin A, kẽm",
        "loi_ich": "Đa dạng hương vị và hỗ trợ bổ sung vi chất cho trẻ ăn dặm",
        "hinh": "suas/andam4.jpg",
    },
]


GIA_TRI_UPSERTS = [
    {"sua_id": "S07", "thuoc_tinh_id": "DM04_FLAVOR", "gia_tri_van_ban": "Có đường"},
    {"sua_id": "S07", "thuoc_tinh_id": "DM04_PROBIOTIC", "gia_tri_dung_sai": True},
    {"sua_id": "S07", "thuoc_tinh_id": "DM04_PACK", "gia_tri_van_ban": "Lốc 4 hũ x 100g"},
    {"sua_id": "S08", "thuoc_tinh_id": "DM07_SOURCE", "gia_tri_van_ban": "Đậu nành"},
    {"sua_id": "S08", "thuoc_tinh_id": "DM07_CALCIUM", "gia_tri_dung_sai": True},
    {"sua_id": "S08", "thuoc_tinh_id": "DM07_SUGAR", "gia_tri_dung_sai": False},
    {"sua_id": "S14", "thuoc_tinh_id": "DM05_VOLUME", "gia_tri_so": 180},
    {"sua_id": "S14", "thuoc_tinh_id": "DM05_SUGAR", "gia_tri_dung_sai": True},
    {"sua_id": "S14", "thuoc_tinh_id": "DM05_UHT", "gia_tri_dung_sai": True},
    {"sua_id": "S15", "thuoc_tinh_id": "DM03_TARGET", "gia_tri_van_ban": "Người lớn cần bổ sung dinh dưỡng dễ uống"},
    {"sua_id": "S15", "thuoc_tinh_id": "DM03_BENEFIT", "gia_tri_van_ban": "Hỗ trợ cơ xương và phục hồi sức khỏe"},
    {"sua_id": "S15", "thuoc_tinh_id": "DM03_SUGAR", "gia_tri_dung_sai": True},
    {"sua_id": "S16", "thuoc_tinh_id": "DM03_TARGET", "gia_tri_van_ban": "Người lớn tuổi hoặc người cần phục hồi thể trạng"},
    {"sua_id": "S16", "thuoc_tinh_id": "DM03_BENEFIT", "gia_tri_van_ban": "Bổ sung năng lượng và vi chất thiết yếu"},
    {"sua_id": "S16", "thuoc_tinh_id": "DM03_SUGAR", "gia_tri_dung_sai": True},
    {"sua_id": "S17", "thuoc_tinh_id": "DM04_FLAVOR", "gia_tri_van_ban": "Dâu"},
    {"sua_id": "S17", "thuoc_tinh_id": "DM04_PROBIOTIC", "gia_tri_dung_sai": True},
    {"sua_id": "S17", "thuoc_tinh_id": "DM04_PACK", "gia_tri_van_ban": "Lốc 4 hũ x 100g"},
    {"sua_id": "S18", "thuoc_tinh_id": "DM04_FLAVOR", "gia_tri_van_ban": "Nha đam"},
    {"sua_id": "S18", "thuoc_tinh_id": "DM04_PROBIOTIC", "gia_tri_dung_sai": True},
    {"sua_id": "S18", "thuoc_tinh_id": "DM04_PACK", "gia_tri_van_ban": "Lốc 4 hũ x 100g"},
    {"sua_id": "S19", "thuoc_tinh_id": "DM04_FLAVOR", "gia_tri_van_ban": "Ít đường"},
    {"sua_id": "S19", "thuoc_tinh_id": "DM04_PROBIOTIC", "gia_tri_dung_sai": True},
    {"sua_id": "S19", "thuoc_tinh_id": "DM04_PACK", "gia_tri_van_ban": "Lốc 4 hũ x 100g"},
    {"sua_id": "S20", "thuoc_tinh_id": "DM07_SOURCE", "gia_tri_van_ban": "Đậu nành"},
    {"sua_id": "S20", "thuoc_tinh_id": "DM07_CALCIUM", "gia_tri_dung_sai": False},
    {"sua_id": "S20", "thuoc_tinh_id": "DM07_SUGAR", "gia_tri_dung_sai": True},
    {"sua_id": "S21", "thuoc_tinh_id": "DM07_SOURCE", "gia_tri_van_ban": "Đậu nành"},
    {"sua_id": "S21", "thuoc_tinh_id": "DM07_CALCIUM", "gia_tri_dung_sai": False},
    {"sua_id": "S21", "thuoc_tinh_id": "DM07_SUGAR", "gia_tri_dung_sai": True},
    {"sua_id": "S22", "thuoc_tinh_id": "DM07_SOURCE", "gia_tri_van_ban": "Ngũ cốc và đậu nành"},
    {"sua_id": "S22", "thuoc_tinh_id": "DM07_CALCIUM", "gia_tri_dung_sai": True},
    {"sua_id": "S22", "thuoc_tinh_id": "DM07_SUGAR", "gia_tri_dung_sai": True},
    {"sua_id": "S23", "thuoc_tinh_id": "DM02_AGE", "gia_tri_van_ban": "Từ 6 tháng"},
    {"sua_id": "S23", "thuoc_tinh_id": "DM02_FLAVOR", "gia_tri_van_ban": "Gà đậu Hà Lan"},
    {"sua_id": "S23", "thuoc_tinh_id": "DM02_PREP", "gia_tri_van_ban": "Pha với nước ấm"},
    {"sua_id": "S24", "thuoc_tinh_id": "DM02_AGE", "gia_tri_van_ban": "Từ 7 tháng"},
    {"sua_id": "S24", "thuoc_tinh_id": "DM02_FLAVOR", "gia_tri_van_ban": "Heo cà rốt"},
    {"sua_id": "S24", "thuoc_tinh_id": "DM02_PREP", "gia_tri_van_ban": "Pha với nước ấm"},
    {"sua_id": "S25", "thuoc_tinh_id": "DM02_AGE", "gia_tri_van_ban": "Từ 6 tháng"},
    {"sua_id": "S25", "thuoc_tinh_id": "DM02_FLAVOR", "gia_tri_van_ban": "Yến mạch sữa"},
    {"sua_id": "S25", "thuoc_tinh_id": "DM02_PREP", "gia_tri_van_ban": "Pha nhanh, dùng bữa phụ"},
    {"sua_id": "S26", "thuoc_tinh_id": "DM02_AGE", "gia_tri_van_ban": "Từ 8 tháng"},
    {"sua_id": "S26", "thuoc_tinh_id": "DM02_FLAVOR", "gia_tri_van_ban": "Ngũ cốc rau củ"},
    {"sua_id": "S26", "thuoc_tinh_id": "DM02_PREP", "gia_tri_van_ban": "Pha nhanh, ăn nóng"},
]


CREATED_PRODUCT_IDS = {
    "S14",
    "S15",
    "S16",
    "S17",
    "S18",
    "S19",
    "S20",
    "S21",
    "S22",
    "S23",
    "S24",
    "S25",
    "S26",
}


def seed_category_image_sets(apps, schema_editor):
    LoaiSua = apps.get_model("Milk", "LoaiSua")
    DanhMucSanPham = apps.get_model("Milk", "DanhMucSanPham")
    Sua = apps.get_model("Milk", "Sua")
    GiaTriThuocTinhSanPham = apps.get_model("Milk", "GiaTriThuocTinhSanPham")

    for row in NEW_LOAI_SUA:
        LoaiSua.objects.update_or_create(ma_loai_sua=row["ma_loai_sua"], defaults=row)

    for row in DANH_MUC_UPDATES:
        DanhMucSanPham.objects.filter(ma_danh_muc=row["ma_danh_muc"]).update(
            loai_sua_id=row["loai_sua_id"],
            mo_ta=row["mo_ta"],
        )

    for row in SUA_UPSERTS:
        Sua.objects.update_or_create(ma_sua=row["ma_sua"], defaults=row)

    for row in GIA_TRI_UPSERTS:
        GiaTriThuocTinhSanPham.objects.update_or_create(
            sua_id=row["sua_id"],
            thuoc_tinh_id=row["thuoc_tinh_id"],
            defaults={
                "gia_tri_van_ban": row.get("gia_tri_van_ban", ""),
                "gia_tri_so": row.get("gia_tri_so"),
                "gia_tri_dung_sai": row.get("gia_tri_dung_sai"),
            },
        )


def remove_category_image_sets(apps, schema_editor):
    LoaiSua = apps.get_model("Milk", "LoaiSua")
    DanhMucSanPham = apps.get_model("Milk", "DanhMucSanPham")
    Sua = apps.get_model("Milk", "Sua")
    GiaTriThuocTinhSanPham = apps.get_model("Milk", "GiaTriThuocTinhSanPham")

    for row in GIA_TRI_UPSERTS:
        GiaTriThuocTinhSanPham.objects.filter(
            sua_id=row["sua_id"],
            thuoc_tinh_id=row["thuoc_tinh_id"],
        ).delete()

    Sua.objects.filter(ma_sua__in=CREATED_PRODUCT_IDS).delete()
    DanhMucSanPham.objects.filter(ma_danh_muc="DM02").update(loai_sua_id=None)
    LoaiSua.objects.filter(ma_loai_sua="LS08").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("Milk", "0012_add_sample_category_with_products"),
    ]

    operations = [
        migrations.RunPython(seed_category_image_sets, remove_category_image_sets),
    ]
