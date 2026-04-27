from rest_framework import status
from rest_framework.test import APITestCase

from .models import LuaChonMuaSua


class SuaApiTests(APITestCase):
    def test_list_milk_products(self):
        response = self.client.get("/api/san-pham-sua")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 26)
        self.assertEqual(response.data[0]["ma_sua"], "S01")
        self.assertIn("ti\u1ec7t tr\u00f9ng", response.data[0]["ten_sua"].lower())
        self.assertEqual(response.data[0]["gia_hien_thi"], "430.000\u0111")
        self.assertTrue(response.data[0]["hinh"].startswith("http://testserver/media/suas/"))

    def test_filter_milk_products(self):
        response = self.client.get("/api/danh-sach-san-pham", {"q": "Ensure", "danh_muc": "DM03"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertTrue(all(item["ma_danh_muc"] == "DM03" for item in response.data))
        self.assertTrue(all("Ensure" in item["ten_sua"] for item in response.data))

    def test_retrieve_milk_product(self):
        response = self.client.get("/api/san-pham-sua/S01")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["ma_sua"], "S01")
        self.assertEqual(response.data["ma_loai_sua"], "LS01")
        self.assertEqual(response.data["ma_hang_sua"], "HS01")
        self.assertIn("mo_ta_chi_tiet", response.data)
        self.assertEqual(len(response.data["lua_chon_mua"]), 2)
        self.assertEqual(response.data["lua_chon_mua"][0]["ten_lua_chon"], "Thung 48 hop")
        self.assertEqual(response.data["lua_chon_mua"][0]["gia_hien_thi"], "400.000\u0111")
        self.assertEqual(response.data["lua_chon_mua"][0]["nhan_giam_gia"], "-8%")

    def test_product_detail_alias_endpoint(self):
        response = self.client.get("/api/chi-tiet-san-pham/S01")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["ma_sua"], "S01")
        self.assertEqual(response.data["ten_hang_sua"], "TH true MILK")
        self.assertEqual(response.data["ten_danh_muc"], "S\u1eefa t\u01b0\u01a1i nguy\u00ean ch\u1ea5t")
        self.assertEqual(response.data["lua_chon_mua"][1]["ten_lua_chon"], "Loc 4 hop")
        self.assertEqual(response.data["lua_chon_mua"][1]["gia_hien_thi"], "41.400\u0111")

    def test_product_detail_fallback_for_any_clicked_product(self):
        response = self.client.get("/api/chi-tiet-san-pham/S02")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["ma_sua"], "S02")
        self.assertIn("Th\u00e0nh ph\u1ea7n n\u1ed5i b\u1eadt", response.data["mo_ta_chi_tiet"])
        self.assertIn("L\u1ee3i \u00edch ch\u00ednh", response.data["mo_ta_chi_tiet"])
        self.assertEqual(len(response.data["lua_chon_mua"]), 1)
        self.assertEqual(response.data["lua_chon_mua"][0]["ten_lua_chon"], "900 g, L\u1ebb 1 lon")
        self.assertEqual(response.data["lua_chon_mua"][0]["gia_hien_thi"], "490.000\u0111")
        self.assertEqual(response.data["lua_chon_mua"][0]["nhan_giam_gia"], "-7%")
        self.assertTrue(response.data["lua_chon_mua"][0]["mac_dinh"])


class DanhMucSanPhamApiTests(APITestCase):
    def test_list_category_menu_from_mockup(self):
        response = self.client.get("/api/danh-muc")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 7)
        self.assertEqual(response.data[0]["ma_danh_muc"], "DM01")
        self.assertEqual(response.data[0]["so_luong_hien_thi"], 20)
        self.assertEqual(response.data[1]["so_luong_hien_thi"], 25)
        self.assertEqual(response.data[2]["so_luong_hien_thi"], 24)
        self.assertEqual(response.data[4]["noi_bat"], "Best")
        self.assertEqual(response.data[4]["so_luong_hien_thi"], 50)
        self.assertEqual(response.data[6]["ma_danh_muc"], "DM07")
        self.assertEqual(response.data[6]["so_luong_hien_thi"], 30)

    def test_list_full_category_detail_with_products(self):
        response = self.client.get("/api/chi-tiet-danh-muc")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 7)
        self.assertEqual(response.data[0]["ma_danh_muc"], "DM01")
        self.assertIn("dinh d\u01b0\u1ee1ng", response.data[0]["mo_ta"].lower())
        self.assertIn("san_pham", response.data[0])
        self.assertEqual(response.data[0]["san_pham"][0]["ma_danh_muc"], "DM01")
        self.assertTrue(
            response.data[0]["san_pham"][0]["hinh"].startswith("http://testserver/media/suas/")
        )

    def test_retrieve_category_detail(self):
        response = self.client.get("/api/danh-muc-san-pham/DM05")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["ma_danh_muc"], "DM05")
        self.assertEqual(response.data["ten_danh_muc"], "S\u1eefa t\u01b0\u01a1i nguy\u00ean ch\u1ea5t")
        self.assertEqual(response.data["noi_bat"], "Best")
        self.assertEqual(response.data["so_luong_hien_thi"], 50)
        self.assertIn("h\u01b0\u01a1ng v\u1ecb t\u1ef1 nhi\u00ean", response.data["mo_ta"].lower())
        self.assertEqual(len(response.data["san_pham"]), 4)
        self.assertEqual(response.data["san_pham"][0]["ma_danh_muc"], "DM05")
        self.assertTrue(
            response.data["san_pham"][0]["hinh"].startswith("http://testserver/media/suas/")
        )

    def test_click_category_detail_endpoint(self):
        response = self.client.get("/api/chi-tiet-danh-muc/DM01")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["ma_danh_muc"], "DM01")
        self.assertEqual(response.data["ten_danh_muc"], "S\u1eefa b\u1ed9t tr\u1ebb em")
        self.assertIn("dinh d\u01b0\u1ee1ng", response.data["mo_ta"].lower())
        self.assertEqual(len(response.data["san_pham"]), 1)
        self.assertEqual(response.data["san_pham"][0]["ma_danh_muc"], "DM01")

    def test_search_categories_for_search_screen(self):
        response = self.client.get("/api/tim-kiem-loai-sua")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 7)
        self.assertEqual(response.data[0]["ma_danh_muc"], "DM01")
        self.assertEqual(response.data[0]["ten_danh_muc"], "S\u1eefa b\u1ed9t tr\u1ebb em")

    def test_search_categories_matches_keyword_without_diacritics(self):
        response = self.client.get("/api/tim-kiem-loai-sua", {"q": "sua"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)
        self.assertEqual(response.data[0]["ma_danh_muc"], "DM01")
        self.assertNotIn("DM02", [item["ma_danh_muc"] for item in response.data])

    def test_search_categories_filters_by_keyword(self):
        response = self.client.get("/api/tim-kiem-loai-sua", {"q": "thuc vat"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["ma_danh_muc"], "DM07")
        self.assertEqual(response.data[0]["ten_danh_muc"], "S\u1eefa th\u1ef1c v\u1eadt")

    def test_recommended_categories_with_image_for_search_screen(self):
        response = self.client.get("/api/danh-cho-ban")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["ma_danh_muc"], "DM01")
        self.assertEqual(response.data[0]["tieu_de_hien_thi"], "S\u1eefa b\u1ed9t tr\u1ebb em")
        self.assertTrue(response.data[0]["hinh_dai_dien"].startswith("http://testserver/media/suas/"))
        self.assertIsNotNone(response.data[0]["ma_sua_dai_dien"])


class BannerQuangCaoApiTests(APITestCase):
    def test_list_banner(self):
        response = self.client.get("/api/banner")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["ma_banner"], "BN01")
        self.assertEqual(response.data[0]["ma_sua"], "S10")
        self.assertEqual(response.data[0]["nhan"], "M\u1edbi")
        self.assertIn("m\u1eadt ong ng\u0169 c\u1ed1c", response.data[0]["tieu_de"].lower())
        self.assertIn("ng\u0169 c\u1ed1c", response.data[0]["mo_ta"].lower())
        self.assertTrue(response.data[0]["hinh"].startswith("http://testserver/media/suas/"))


class GioHangApiTests(APITestCase):
    def test_create_empty_cart(self):
        response = self.client.post("/api/gio-hang", {}, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data["ma_gio_hang"])
        self.assertEqual(response.data["tong_mat_hang"], 0)
        self.assertEqual(response.data["tong_so_luong"], 0)
        self.assertEqual(response.data["tong_tien"], 0)
        self.assertEqual(response.data["tong_tien_hien_thi"], "0\u0111")
        self.assertEqual(response.data["items"], [])

    def test_add_item_to_cart_and_merge_quantity(self):
        lua_chon_mac_dinh = LuaChonMuaSua.objects.get(sua_id="S01", mac_dinh=True)

        tao_gio = self.client.post(
            "/api/gio-hang",
            {
                "ma_sua": "S01",
                "lua_chon_mua_id": lua_chon_mac_dinh.id,
                "so_luong": 2,
            },
            format="json",
        )

        self.assertEqual(tao_gio.status_code, status.HTTP_201_CREATED)
        self.assertEqual(tao_gio.data["tong_mat_hang"], 1)
        self.assertEqual(tao_gio.data["tong_so_luong"], 2)
        self.assertEqual(tao_gio.data["tong_tien"], 800000)
        self.assertEqual(tao_gio.data["items"][0]["ten_lua_chon"], "Thung 48 hop")

        ma_gio_hang = tao_gio.data["ma_gio_hang"]
        them_tiep = self.client.post(
            f"/api/gio-hang/{ma_gio_hang}/them-san-pham",
            {
                "ma_sua": "S01",
                "lua_chon_mua_id": lua_chon_mac_dinh.id,
                "so_luong": 1,
            },
            format="json",
        )

        self.assertEqual(them_tiep.status_code, status.HTTP_200_OK)
        self.assertEqual(them_tiep.data["tong_mat_hang"], 1)
        self.assertEqual(them_tiep.data["tong_so_luong"], 3)
        self.assertEqual(them_tiep.data["tong_tien"], 1200000)
        self.assertEqual(them_tiep.data["items"][0]["so_luong"], 3)
        self.assertEqual(them_tiep.data["items"][0]["thanh_tien_hien_thi"], "1.200.000\u0111")

    def test_update_item_can_merge_with_same_product_and_option(self):
        lua_chon_mac_dinh = LuaChonMuaSua.objects.get(sua_id="S01", mac_dinh=True)
        lua_chon_thu_hai = LuaChonMuaSua.objects.get(sua_id="S01", mac_dinh=False)

        tao_gio = self.client.post(
            "/api/gio-hang",
            {
                "ma_sua": "S01",
                "lua_chon_mua_id": lua_chon_mac_dinh.id,
                "so_luong": 1,
            },
            format="json",
        )
        ma_gio_hang = tao_gio.data["ma_gio_hang"]
        item_dau = tao_gio.data["items"][0]["id"]

        self.client.post(
            f"/api/gio-hang/{ma_gio_hang}/them-san-pham",
            {
                "ma_sua": "S01",
                "lua_chon_mua_id": lua_chon_thu_hai.id,
                "so_luong": 2,
            },
            format="json",
        )

        cap_nhat = self.client.patch(
            f"/api/gio-hang/{ma_gio_hang}/chi-tiet/{item_dau}",
            {
                "lua_chon_mua_id": lua_chon_thu_hai.id,
                "so_luong": 4,
            },
            format="json",
        )

        self.assertEqual(cap_nhat.status_code, status.HTTP_200_OK)
        self.assertEqual(cap_nhat.data["tong_mat_hang"], 1)
        self.assertEqual(cap_nhat.data["tong_so_luong"], 6)
        self.assertEqual(cap_nhat.data["items"][0]["lua_chon_mua_id"], lua_chon_thu_hai.id)
        self.assertEqual(cap_nhat.data["items"][0]["so_luong"], 6)
        self.assertEqual(cap_nhat.data["tong_tien"], 248400)

    def test_delete_item_and_clear_cart(self):
        lua_chon_mac_dinh = LuaChonMuaSua.objects.get(sua_id="S01", mac_dinh=True)

        tao_gio = self.client.post(
            "/api/gio-hang",
            {
                "ma_sua": "S01",
                "lua_chon_mua_id": lua_chon_mac_dinh.id,
                "so_luong": 1,
            },
            format="json",
        )
        ma_gio_hang = tao_gio.data["ma_gio_hang"]
        chi_tiet_id = tao_gio.data["items"][0]["id"]

        xoa_item = self.client.delete(f"/api/gio-hang/{ma_gio_hang}/chi-tiet/{chi_tiet_id}")

        self.assertEqual(xoa_item.status_code, status.HTTP_200_OK)
        self.assertEqual(xoa_item.data["tong_mat_hang"], 0)
        self.assertEqual(xoa_item.data["tong_so_luong"], 0)

        self.client.post(
            f"/api/gio-hang/{ma_gio_hang}/them-san-pham",
            {
                "ma_sua": "S01",
                "lua_chon_mua_id": lua_chon_mac_dinh.id,
                "so_luong": 2,
            },
            format="json",
        )

        xoa_tat_ca = self.client.delete(f"/api/gio-hang/{ma_gio_hang}/xoa-tat-ca")

        self.assertEqual(xoa_tat_ca.status_code, status.HTTP_200_OK)
        self.assertEqual(xoa_tat_ca.data["tong_mat_hang"], 0)
        self.assertEqual(xoa_tat_ca.data["tong_so_luong"], 0)
        self.assertEqual(xoa_tat_ca.data["tong_tien_hien_thi"], "0\u0111")


class DonHangApiTests(APITestCase):
    def test_create_order_from_cart_for_checkout_screen(self):
        lua_chon_mac_dinh = LuaChonMuaSua.objects.get(sua_id="S01", mac_dinh=True)

        tao_gio = self.client.post(
            "/api/gio-hang",
            {
                "ma_sua": "S01",
                "lua_chon_mua_id": lua_chon_mac_dinh.id,
                "so_luong": 2,
            },
            format="json",
        )
        ma_gio_hang = tao_gio.data["ma_gio_hang"]

        response = self.client.post(
            "/api/don-hang",
            {
                "ma_gio_hang": ma_gio_hang,
                "phuong_thuc_nhan": "giao_tan_noi",
                "ten_nguoi_nhan": "Nguyen Van A",
                "so_dien_thoai": "0912345678",
                "dia_chi_giao_hang": "12 Thanh Thai, Quan 10, TP HCM",
                "phuong_thuc_thanh_toan": "cod",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["id"], "DH004")
        self.assertEqual(response.data["trang_thai"], "Ch\u1edd x\u00e1c nh\u1eadn")
        self.assertEqual(response.data["trang_thai_code"], "cho_xac_nhan")
        self.assertEqual(response.data["phuong_thuc_nhan"], "giao_tan_noi")
        self.assertEqual(response.data["phuong_thuc_nhan_hien_thi"], "Giao tan noi")
        self.assertEqual(response.data["ten_nguoi_nhan"], "Nguyen Van A")
        self.assertEqual(response.data["so_dien_thoai"], "0912345678")
        self.assertEqual(response.data["dia_chi_giao_hang"], "12 Thanh Thai, Quan 10, TP HCM")
        self.assertEqual(response.data["phuong_thuc_thanh_toan"], "cod")
        self.assertEqual(
            response.data["phuong_thuc_thanh_toan_hien_thi"],
            "Thanh toan khi nhan hang (COD)",
        )
        self.assertEqual(response.data["tong_tien"], 800000.0)
        self.assertEqual(response.data["tong_tien_hien_thi"], "800.000\u0111")
        self.assertEqual(response.data["tong_san_pham"], 2)
        self.assertEqual(len(response.data["san_pham"]), 1)
        self.assertEqual(response.data["san_pham"][0]["ten_lua_chon"], "Thung 48 hop")
        self.assertEqual(response.data["san_pham"][0]["gia_ban_hien_thi"], "400.000\u0111")

        gio_hang_sau_khi_dat = self.client.get(f"/api/gio-hang/{ma_gio_hang}")
        self.assertEqual(gio_hang_sau_khi_dat.status_code, status.HTTP_200_OK)
        self.assertEqual(gio_hang_sau_khi_dat.data["tong_mat_hang"], 0)
        self.assertEqual(gio_hang_sau_khi_dat.data["items"], [])

    def test_create_order_requires_address_when_shipping(self):
        tao_gio = self.client.post(
            "/api/gio-hang",
            {
                "ma_sua": "S10",
                "so_luong": 1,
            },
            format="json",
        )

        response = self.client.post(
            "/api/don-hang",
            {
                "ma_gio_hang": tao_gio.data["ma_gio_hang"],
                "phuong_thuc_nhan": "giao_tan_noi",
                "ten_nguoi_nhan": "Tran Thi B",
                "so_dien_thoai": "0987654321",
                "dia_chi_giao_hang": "",
                "phuong_thuc_thanh_toan": "the_noi_dia",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("dia_chi_giao_hang", response.data)

    def test_retrieve_order_detail_includes_checkout_information(self):
        response = self.client.get("/api/don-hang/DH001")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], "DH001")
        self.assertEqual(response.data["phuong_thuc_nhan"], "giao_tan_noi")
        self.assertEqual(response.data["phuong_thuc_thanh_toan"], "cod")
        self.assertEqual(response.data["san_pham"][0]["ten_lua_chon"], "")

    def test_order_history_returns_nested_products_for_android(self):
        response = self.client.get("/api/lich-su-don-hang")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["id"], "DH001")
        self.assertEqual(response.data[0]["ngay_dat"], "04/02/2026 14:30")
        self.assertEqual(response.data[0]["trang_thai"], "\u0110ang giao")
        self.assertEqual(response.data[0]["trang_thai_code"], "dang_giao")
        self.assertEqual(response.data[0]["tong_tien"], 199000.0)
        self.assertEqual(response.data[0]["tong_tien_hien_thi"], "199.000\u0111")
        self.assertEqual(response.data[0]["tong_san_pham"], 2)
        self.assertEqual(response.data[0]["hanh_dong_chinh"]["ma"], "chi_tiet")
        self.assertEqual(response.data[0]["hanh_dong_chinh"]["nhan"], "Chi ti\u1ebft")
        self.assertEqual(len(response.data[0]["san_pham"]), 2)
        self.assertEqual(response.data[0]["san_pham"][0]["ma_sua"], "S10")
        self.assertIn("ten_sp", response.data[0]["san_pham"][0])
        self.assertEqual(response.data[0]["san_pham"][0]["gia_ban_hien_thi"], "45.000\u0111")
        self.assertEqual(
            response.data[0]["san_pham"][0]["hinh_anh"],
            "http://10.0.2.2:8000/media/suas/SUABOT1.jpg",
        )
        self.assertEqual(response.data[1]["id"], "DH002")
        self.assertEqual(response.data[1]["trang_thai"], "Ho\u00e0n th\u00e0nh")
        self.assertEqual(response.data[1]["trang_thai_code"], "hoan_thanh")
        self.assertEqual(response.data[1]["tong_tien"], 356000.0)
        self.assertEqual(response.data[1]["hanh_dong_chinh"]["ma"], "danh_gia")
        self.assertEqual(response.data[1]["hanh_dong_chinh"]["nhan"], "\u0110\u00e1nh gi\u00e1")
        self.assertEqual(len(response.data[1]["san_pham"]), 1)
        self.assertEqual(response.data[2]["id"], "DH003")
        self.assertEqual(response.data[2]["trang_thai"], "\u0110\u00e3 h\u1ee7y")
        self.assertEqual(response.data[2]["trang_thai_code"], "da_huy")
        self.assertEqual(response.data[2]["tong_tien"], 490000.0)
        self.assertEqual(len(response.data[2]["san_pham"]), 1)
