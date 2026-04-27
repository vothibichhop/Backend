from rest_framework import status
from rest_framework.test import APITestCase


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
