from django.db import migrations


LOAI_SUA_UPDATES = {
    "LS01": "S\u1eefa t\u01b0\u01a1i",
    "LS02": "S\u1eefa b\u1ed9t ng\u01b0\u1eddi l\u1edbn",
    "LS03": "S\u1eefa b\u1ed9t tr\u1ebb em",
    "LS04": "S\u1eefa \u0111\u1eb7c",
    "LS05": "S\u1eefa chua \u0103n",
    "LS06": "S\u1eefa th\u1ef1c v\u1eadt",
}


HANG_SUA_UPDATES = {
    "HS01": {
        "ten_hang_sua": "TH true MILK",
        "dia_chi": "Ngh\u0129a \u0110\u00e0n, Ngh\u1ec7 An",
    },
    "HS02": {
        "ten_hang_sua": "Abbott Ensure",
        "dia_chi": "Qu\u1eadn 1, TP HCM",
    },
    "HS03": {
        "ten_hang_sua": "Nutifood GrowPLUS+",
        "dia_chi": "Qu\u1eadn 7, TP HCM",
    },
    "HS04": {
        "ten_hang_sua": "Vinamilk",
        "dia_chi": "Qu\u1eadn 7, TP HCM",
    },
    "HS05": {
        "ten_hang_sua": "Ng\u00f4i Sao Ph\u01b0\u01a1ng Nam",
        "dia_chi": "TP Th\u1ee7 \u0110\u1ee9c, TP HCM",
    },
    "HS06": {
        "ten_hang_sua": "Fami Vinasoy",
        "dia_chi": "Qu\u1ea3ng Ng\u00e3i",
    },
    "HS07": {
        "ten_hang_sua": "Optimum Gold",
        "dia_chi": "B\u00ecnh D\u01b0\u01a1ng",
    },
}


SUA_UPDATES = {
    "S01": {
        "ten_sua": "S\u1eefa t\u01b0\u01a1i ti\u1ec7t tr\u00f9ng TH true MILK",
        "quy_cach": "180 ml, Th\u00f9ng 48 h\u1ed9p",
        "thanh_phan": "S\u1eefa t\u01b0\u01a1i s\u1ea1ch, vitamin A, D",
        "loi_ich": "B\u1ed5 sung canxi v\u00e0 n\u0103ng l\u01b0\u1ee3ng m\u1ed7i ng\u00e0y",
    },
    "S02": {
        "ten_sua": "S\u1eefa b\u1ed9t ng\u01b0\u1eddi l\u1edbn Ensure Gold",
        "quy_cach": "900 g, L\u1ebb 1 lon",
        "thanh_phan": "\u0110\u1ea1m, canxi, HMB",
        "loi_ich": "H\u1ed7 tr\u1ee3 c\u01a1 x\u01b0\u01a1ng v\u00e0 s\u1ee9c \u0111\u1ec1 kh\u00e1ng",
    },
    "S03": {
        "ten_sua": "S\u1eefa b\u1ed9t ng\u01b0\u1eddi l\u1edbn GrowPLUS+ \u0110\u1ecf",
        "quy_cach": "900 g, L\u1ebb 1 lon",
        "thanh_phan": "Ch\u1ea5t b\u00e9o, vitamin v\u00e0 kho\u00e1ng ch\u1ea5t",
        "loi_ich": "B\u1ed5 sung n\u0103ng l\u01b0\u1ee3ng cho ng\u01b0\u1eddi l\u1edbn",
    },
    "S04": {
        "ten_sua": "S\u1eefa t\u01b0\u01a1i ti\u1ec7t tr\u00f9ng Vinamilk 100%",
        "quy_cach": "180 ml, Th\u00f9ng 48 h\u1ed9p",
        "thanh_phan": "S\u1eefa t\u01b0\u01a1i ti\u1ec7t tr\u00f9ng nguy\u00ean ch\u1ea5t",
        "loi_ich": "B\u1ed5 sung canxi, vitamin D",
    },
    "S05": {
        "ten_sua": "S\u1eefa t\u01b0\u01a1i ti\u1ec7t tr\u00f9ng Vinamilk c\u00f3 \u0111\u01b0\u1eddng",
        "quy_cach": "180 ml, Th\u00f9ng 48 h\u1ed9p",
        "thanh_phan": "S\u1eefa t\u01b0\u01a1i ti\u1ec7t tr\u00f9ng c\u00f3 \u0111\u01b0\u1eddng",
        "loi_ich": "Cung c\u1ea5p n\u0103ng l\u01b0\u1ee3ng v\u00e0 canxi",
    },
    "S06": {
        "ten_sua": "S\u1eefa \u0111\u1eb7c nguy\u00ean ch\u1ea5t Ng\u00f4i Sao Ph\u01b0\u01a1ng Nam",
        "quy_cach": "100 g, L\u1ebb 1 h\u1ed9p",
        "thanh_phan": "S\u1eefa \u0111\u1eb7c, \u0111\u01b0\u1eddng, ch\u1ea5t b\u00e9o s\u1eefa",
        "loi_ich": "Pha c\u00e0 ph\u00ea, l\u00e0m b\u00e1nh, t\u0103ng v\u1ecb b\u00e9o",
    },
    "S07": {
        "ten_sua": "S\u1eefa chua \u0103n Vinamilk",
        "quy_cach": "100 g, Th\u00f9ng 48 h\u1ed9p",
        "thanh_phan": "S\u1eefa l\u00ean men, men s\u1ed1ng probiotic",
        "loi_ich": "H\u1ed7 tr\u1ee3 ti\u00eau h\u00f3a, t\u0103ng \u0111\u1ec1 kh\u00e1ng",
    },
    "S08": {
        "ten_sua": "S\u1eefa th\u1ef1c v\u1eadt Fami Canxi",
        "quy_cach": "180 ml, Th\u00f9ng 48 h\u1ed9p",
        "thanh_phan": "\u0110\u1eadu n\u00e0nh, canxi, vitamin B",
        "loi_ich": "T\u1ed1t cho tim m\u1ea1ch v\u00e0 x\u01b0\u01a1ng kh\u1edbp",
    },
    "S09": {
        "ten_sua": "S\u1eefa b\u1ed9t tr\u1ebb em Optimum Gold",
        "quy_cach": "800 g, L\u1ebb 1 lon",
        "thanh_phan": "DHA, canxi, ch\u1ea5t x\u01a1 h\u00f2a tan",
        "loi_ich": "H\u1ed7 tr\u1ee3 t\u0103ng chi\u1ec1u cao v\u00e0 tr\u00ed n\u00e3o",
    },
    "S10": {
        "ten_sua": "S\u1eefa chua \u0103n mix m\u1eadt ong ng\u0169 c\u1ed1c",
        "quy_cach": "100 g, L\u1ed1c 4 h\u1ed9p",
        "thanh_phan": "S\u1eefa chua, m\u1eadt ong, ng\u0169 c\u1ed1c v\u00e0 men s\u1ed1ng probiotic",
        "loi_ich": "Gi\u1eef h\u1ec7 ti\u00eau h\u00f3a c\u00e2n b\u1eb1ng, t\u0103ng v\u1ecb ngon gi\u00e0u protein v\u00e0 canxi",
    },
}


KHACH_HANG_UPDATES = {
    "KH01": {"ten_kh": "Nguy\u1ec5n V\u0103n An", "dia_chi": "Qu\u1eadn 3, TP HCM"},
    "KH02": {"ten_kh": "Tr\u1ea7n Th\u1ecb B\u00edch", "dia_chi": "Th\u1ee7 \u0110\u1ee9c, TP HCM"},
}


def force_unicode_data(apps, schema_editor):
    LoaiSua = apps.get_model("Milk", "LoaiSua")
    HangSua = apps.get_model("Milk", "HangSua")
    Sua = apps.get_model("Milk", "Sua")
    KhachHang = apps.get_model("Milk", "KhachHang")
    BannerQuangCao = apps.get_model("Milk", "BannerQuangCao")

    for ma_loai_sua, ten_loai_sua in LOAI_SUA_UPDATES.items():
        LoaiSua.objects.filter(ma_loai_sua=ma_loai_sua).update(ten_loai_sua=ten_loai_sua)

    for ma_hang_sua, values in HANG_SUA_UPDATES.items():
        HangSua.objects.filter(ma_hang_sua=ma_hang_sua).update(**values)

    for ma_sua, values in SUA_UPDATES.items():
        Sua.objects.filter(ma_sua=ma_sua).update(**values)

    for ma_kh, values in KHACH_HANG_UPDATES.items():
        KhachHang.objects.filter(ma_kh=ma_kh).update(**values)

    BannerQuangCao.objects.filter(ma_banner="BN01").update(
        tieu_de="S\u1eefa chua \u0103n mix m\u1eadt ong ng\u0169 c\u1ed1c",
        mo_ta=(
            "S\u1eefa chua ng\u0169 c\u1ed1c l\u00e0 s\u1ef1 k\u1ebft h\u1ee3p dinh d\u01b0\u1ee1ng gi\u1eefa s\u1eefa chua s\u00e1nh m\u1ecbn "
            "v\u00e0 ng\u0169 c\u1ed1c d\u1ebb gi\u00f2n, mang l\u1ea1i v\u1ecb chua nh\u1eb9, ng\u1ecdt th\u01a1m, gi\u00e0u protein, canxi v\u00e0 ch\u1ea5t x\u01a1"
        ),
        nhan="M\u1edbi",
    )


class Migration(migrations.Migration):
    dependencies = [
        ("Milk", "0009_normalize_vietnamese_seed_data"),
    ]

    operations = [
        migrations.RunPython(force_unicode_data, migrations.RunPython.noop),
    ]
