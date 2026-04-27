from rest_framework import serializers

from .models import (
    BannerQuangCao,
    ChiTietGioHang,
    DanhMucSanPham,
    GioHang,
    LuaChonMuaSua,
    Sua,
)


def dinh_dang_tien(value):
    return f"{int(value):,}".replace(",", ".") + "\u0111"


class SuaListQuerySerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True, default="")
    hang_sua = serializers.CharField(required=False, allow_blank=True)
    loai_sua = serializers.CharField(required=False, allow_blank=True)
    danh_muc = serializers.CharField(required=False, allow_blank=True)


class SuaListSerializer(serializers.ModelSerializer):
    ma_hang_sua = serializers.CharField(source="hang_sua_id", read_only=True)
    ten_hang_sua = serializers.CharField(source="hang_sua.ten_hang_sua", read_only=True)
    ma_loai_sua = serializers.CharField(source="loai_sua_id", read_only=True)
    ten_loai_sua = serializers.CharField(source="loai_sua.ten_loai_sua", read_only=True)
    ma_danh_muc = serializers.CharField(source="danh_muc_id", read_only=True)
    ten_danh_muc = serializers.CharField(source="danh_muc.ten_danh_muc", read_only=True)
    thong_tin_hien_thi = serializers.SerializerMethodField()
    gia_hien_thi = serializers.SerializerMethodField()
    nhan_giam_gia = serializers.SerializerMethodField()

    class Meta:
        model = Sua
        fields = [
            "ma_sua",
            "ten_sua",
            "ma_hang_sua",
            "ten_hang_sua",
            "ma_loai_sua",
            "ten_loai_sua",
            "ma_danh_muc",
            "ten_danh_muc",
            "quy_cach",
            "trong_luong",
            "don_vi",
            "thong_tin_hien_thi",
            "don_gia",
            "gia_hien_thi",
            "giam_gia",
            "nhan_giam_gia",
            "thanh_phan",
            "loi_ich",
            "hinh",
        ]

    def get_thong_tin_hien_thi(self, obj):
        if obj.quy_cach:
            return obj.quy_cach
        if obj.trong_luong and obj.don_vi:
            return f"{obj.trong_luong} {obj.don_vi}"
        return ""

    def get_gia_hien_thi(self, obj):
        return dinh_dang_tien(obj.don_gia)

    def get_nhan_giam_gia(self, obj):
        if not obj.giam_gia:
            return ""
        return f"-{obj.giam_gia}%"


class DanhMucSanPhamSerializer(serializers.ModelSerializer):
    ma_loai_sua = serializers.CharField(source="loai_sua_id", read_only=True)
    tong_san_pham = serializers.IntegerField(source="san_pham.count", read_only=True)

    class Meta:
        model = DanhMucSanPham
        fields = [
            "ma_danh_muc",
            "ten_danh_muc",
            "noi_bat",
            "so_luong_hien_thi",
            "tong_san_pham",
            "thu_tu",
            "hien_thi",
            "ma_loai_sua",
        ]


class ChiTietDanhMucSanPhamSerializer(serializers.ModelSerializer):
    ma_loai_sua = serializers.CharField(source="loai_sua_id", read_only=True)
    tong_san_pham = serializers.IntegerField(source="san_pham.count", read_only=True)
    san_pham = SuaListSerializer(many=True, read_only=True)

    class Meta:
        model = DanhMucSanPham
        fields = [
            "ma_danh_muc",
            "ten_danh_muc",
            "mo_ta",
            "noi_bat",
            "so_luong_hien_thi",
            "tong_san_pham",
            "thu_tu",
            "hien_thi",
            "ma_loai_sua",
            "san_pham",
        ]


class BannerQuangCaoSerializer(serializers.ModelSerializer):
    ma_sua = serializers.CharField(source="sua_id", read_only=True)
    ten_sua = serializers.CharField(source="sua.ten_sua", read_only=True)
    ma_danh_muc = serializers.CharField(source="sua.danh_muc_id", read_only=True)
    ten_danh_muc = serializers.CharField(source="sua.danh_muc.ten_danh_muc", read_only=True)
    hinh = serializers.ImageField(source="sua.hinh", read_only=True)
    thong_tin_hien_thi = serializers.SerializerMethodField()
    gia_hien_thi = serializers.SerializerMethodField()

    class Meta:
        model = BannerQuangCao
        fields = [
            "ma_banner",
            "tieu_de",
            "mo_ta",
            "nhan",
            "mau_nen",
            "mau_chu",
            "thu_tu",
            "hien_thi",
            "ma_sua",
            "ten_sua",
            "ma_danh_muc",
            "ten_danh_muc",
            "thong_tin_hien_thi",
            "gia_hien_thi",
            "hinh",
        ]

    def get_thong_tin_hien_thi(self, obj):
        if obj.sua is None:
            return ""
        if obj.sua.quy_cach:
            return obj.sua.quy_cach
        if obj.sua.trong_luong and obj.sua.don_vi:
            return f"{obj.sua.trong_luong} {obj.sua.don_vi}"
        return ""

    def get_gia_hien_thi(self, obj):
        if obj.sua is None:
            return ""
        return dinh_dang_tien(obj.sua.don_gia)


class LuaChonMuaSuaSerializer(serializers.ModelSerializer):
    gia_hien_thi = serializers.SerializerMethodField()
    nhan_giam_gia = serializers.SerializerMethodField()

    class Meta:
        model = LuaChonMuaSua
        fields = [
            "id",
            "ten_lua_chon",
            "don_gia",
            "gia_hien_thi",
            "giam_gia",
            "nhan_giam_gia",
            "mac_dinh",
            "thu_tu",
            "hien_thi",
        ]

    def get_gia_hien_thi(self, obj):
        return dinh_dang_tien(obj.don_gia)

    def get_nhan_giam_gia(self, obj):
        if not obj.giam_gia:
            return ""
        return f"-{obj.giam_gia}%"


class ChiTietSuaSerializer(serializers.ModelSerializer):
    ma_hang_sua = serializers.CharField(source="hang_sua_id", read_only=True)
    ten_hang_sua = serializers.CharField(source="hang_sua.ten_hang_sua", read_only=True)
    ma_loai_sua = serializers.CharField(source="loai_sua_id", read_only=True)
    ten_loai_sua = serializers.CharField(source="loai_sua.ten_loai_sua", read_only=True)
    ma_danh_muc = serializers.CharField(source="danh_muc_id", read_only=True)
    ten_danh_muc = serializers.CharField(source="danh_muc.ten_danh_muc", read_only=True)
    mo_ta_chi_tiet = serializers.SerializerMethodField()
    thong_tin_hien_thi = serializers.SerializerMethodField()
    gia_hien_thi = serializers.SerializerMethodField()
    nhan_giam_gia = serializers.SerializerMethodField()
    lua_chon_mua = serializers.SerializerMethodField()

    class Meta:
        model = Sua
        fields = [
            "ma_sua",
            "ten_sua",
            "ma_hang_sua",
            "ten_hang_sua",
            "ma_loai_sua",
            "ten_loai_sua",
            "ma_danh_muc",
            "ten_danh_muc",
            "mo_ta_chi_tiet",
            "quy_cach",
            "trong_luong",
            "don_vi",
            "thong_tin_hien_thi",
            "don_gia",
            "gia_hien_thi",
            "giam_gia",
            "nhan_giam_gia",
            "thanh_phan",
            "loi_ich",
            "hinh",
            "lua_chon_mua",
        ]

    def get_thong_tin_hien_thi(self, obj):
        if obj.quy_cach:
            return obj.quy_cach
        if obj.trong_luong and obj.don_vi:
            return f"{obj.trong_luong} {obj.don_vi}"
        return ""

    def get_mo_ta_chi_tiet(self, obj):
        if obj.mo_ta_chi_tiet:
            return obj.mo_ta_chi_tiet

        detail_parts = []
        if obj.thanh_phan:
            detail_parts.append(f"Th\u00e0nh ph\u1ea7n n\u1ed5i b\u1eadt: {obj.thanh_phan}.")
        if obj.loi_ich:
            detail_parts.append(f"L\u1ee3i \u00edch ch\u00ednh: {obj.loi_ich}.")
        if obj.quy_cach:
            detail_parts.append(f"Quy c\u00e1ch \u0111\u00f3ng g\u00f3i: {obj.quy_cach}.")

        return " ".join(detail_parts)

    def get_gia_hien_thi(self, obj):
        return dinh_dang_tien(obj.don_gia)

    def get_nhan_giam_gia(self, obj):
        if not obj.giam_gia:
            return ""
        return f"-{obj.giam_gia}%"

    def get_lua_chon_mua(self, obj):
        lua_chon_hien_thi = obj.lua_chon_mua.filter(hien_thi=True)
        if lua_chon_hien_thi.exists():
            return LuaChonMuaSuaSerializer(lua_chon_hien_thi, many=True, context=self.context).data

        ten_lua_chon = self.get_thong_tin_hien_thi(obj) or "Quy c\u00e1ch chu\u1ea9n"
        return [
            {
                "id": None,
                "ten_lua_chon": ten_lua_chon,
                "don_gia": int(obj.don_gia),
                "gia_hien_thi": self.get_gia_hien_thi(obj),
                "giam_gia": obj.giam_gia,
                "nhan_giam_gia": self.get_nhan_giam_gia(obj),
                "mac_dinh": True,
                "thu_tu": 1,
                "hien_thi": True,
            }
        ]


class ThemSanPhamVaoGioHangSerializer(serializers.Serializer):
    ma_sua = serializers.CharField()
    lua_chon_mua_id = serializers.IntegerField(required=False, allow_null=True)
    so_luong = serializers.IntegerField(min_value=1, default=1)

    def validate(self, attrs):
        try:
            sua = Sua.objects.prefetch_related("lua_chon_mua").get(ma_sua=attrs["ma_sua"])
        except Sua.DoesNotExist as exc:
            raise serializers.ValidationError({"ma_sua": "San pham khong ton tai."}) from exc

        lua_chon_mua_id = attrs.get("lua_chon_mua_id")
        if lua_chon_mua_id is not None:
            try:
                lua_chon_mua = sua.lua_chon_mua.get(id=lua_chon_mua_id, hien_thi=True)
            except LuaChonMuaSua.DoesNotExist as exc:
                raise serializers.ValidationError(
                    {"lua_chon_mua_id": "Lua chon mua khong hop le cho san pham nay."}
                ) from exc
        else:
            lua_chon_mua = (
                sua.lua_chon_mua.filter(hien_thi=True, mac_dinh=True).order_by("thu_tu", "id").first()
                or sua.lua_chon_mua.filter(hien_thi=True).order_by("thu_tu", "id").first()
            )

        attrs["sua"] = sua
        attrs["lua_chon_mua"] = lua_chon_mua
        return attrs


class CapNhatChiTietGioHangSerializer(serializers.Serializer):
    so_luong = serializers.IntegerField(min_value=1, required=False)
    lua_chon_mua_id = serializers.IntegerField(required=False, allow_null=True)

    def validate(self, attrs):
        if not attrs:
            raise serializers.ValidationError("Can gui it nhat mot truong de cap nhat.")

        chi_tiet = self.context["chi_tiet"]
        if "lua_chon_mua_id" in attrs:
            lua_chon_mua_id = attrs["lua_chon_mua_id"]
            if lua_chon_mua_id is None:
                lua_chon_mua = (
                    chi_tiet.sua.lua_chon_mua.filter(hien_thi=True, mac_dinh=True)
                    .order_by("thu_tu", "id")
                    .first()
                )
            else:
                try:
                    lua_chon_mua = chi_tiet.sua.lua_chon_mua.get(
                        id=lua_chon_mua_id,
                        hien_thi=True,
                    )
                except LuaChonMuaSua.DoesNotExist as exc:
                    raise serializers.ValidationError(
                        {"lua_chon_mua_id": "Lua chon mua khong hop le cho san pham nay."}
                    ) from exc
            attrs["lua_chon_mua"] = lua_chon_mua
        return attrs


class ChiTietGioHangSerializer(serializers.ModelSerializer):
    ma_sua = serializers.CharField(source="sua_id", read_only=True)
    ten_sua = serializers.CharField(source="sua.ten_sua", read_only=True)
    hinh = serializers.ImageField(source="sua.hinh", read_only=True)
    ma_danh_muc = serializers.CharField(source="sua.danh_muc_id", read_only=True)
    ten_danh_muc = serializers.CharField(source="sua.danh_muc.ten_danh_muc", read_only=True)
    lua_chon_mua_id = serializers.SerializerMethodField()
    ten_lua_chon = serializers.SerializerMethodField()
    thong_tin_hien_thi = serializers.SerializerMethodField()
    don_gia = serializers.SerializerMethodField()
    gia_hien_thi = serializers.SerializerMethodField()
    giam_gia = serializers.SerializerMethodField()
    nhan_giam_gia = serializers.SerializerMethodField()
    thanh_tien = serializers.SerializerMethodField()
    thanh_tien_hien_thi = serializers.SerializerMethodField()

    class Meta:
        model = ChiTietGioHang
        fields = [
            "id",
            "ma_sua",
            "ten_sua",
            "hinh",
            "ma_danh_muc",
            "ten_danh_muc",
            "lua_chon_mua_id",
            "ten_lua_chon",
            "thong_tin_hien_thi",
            "don_gia",
            "gia_hien_thi",
            "giam_gia",
            "nhan_giam_gia",
            "so_luong",
            "thanh_tien",
            "thanh_tien_hien_thi",
        ]

    def _don_gia(self, obj):
        if obj.lua_chon_mua is not None:
            return obj.lua_chon_mua.don_gia
        return obj.sua.don_gia

    def _giam_gia(self, obj):
        if obj.lua_chon_mua is not None:
            return obj.lua_chon_mua.giam_gia
        return obj.sua.giam_gia

    def get_lua_chon_mua_id(self, obj):
        if obj.lua_chon_mua is None:
            return None
        return obj.lua_chon_mua.id

    def get_ten_lua_chon(self, obj):
        if obj.lua_chon_mua is not None:
            return obj.lua_chon_mua.ten_lua_chon
        if obj.sua.quy_cach:
            return obj.sua.quy_cach
        if obj.sua.trong_luong and obj.sua.don_vi:
            return f"{obj.sua.trong_luong} {obj.sua.don_vi}"
        return "Quy c\u00e1ch chu\u1ea9n"

    def get_thong_tin_hien_thi(self, obj):
        return self.get_ten_lua_chon(obj)

    def get_don_gia(self, obj):
        return int(self._don_gia(obj))

    def get_gia_hien_thi(self, obj):
        return dinh_dang_tien(self._don_gia(obj))

    def get_giam_gia(self, obj):
        return self._giam_gia(obj)

    def get_nhan_giam_gia(self, obj):
        giam_gia = self._giam_gia(obj)
        if not giam_gia:
            return ""
        return f"-{giam_gia}%"

    def get_thanh_tien(self, obj):
        return int(self._don_gia(obj) * obj.so_luong)

    def get_thanh_tien_hien_thi(self, obj):
        return dinh_dang_tien(self._don_gia(obj) * obj.so_luong)


class GioHangSerializer(serializers.ModelSerializer):
    items = ChiTietGioHangSerializer(source="chi_tiet", many=True, read_only=True)
    tong_mat_hang = serializers.SerializerMethodField()
    tong_so_luong = serializers.SerializerMethodField()
    tong_tien = serializers.SerializerMethodField()
    tong_tien_hien_thi = serializers.SerializerMethodField()

    class Meta:
        model = GioHang
        fields = [
            "ma_gio_hang",
            "tao_luc",
            "cap_nhat_luc",
            "tong_mat_hang",
            "tong_so_luong",
            "tong_tien",
            "tong_tien_hien_thi",
            "items",
        ]

    def get_tong_mat_hang(self, obj):
        return obj.chi_tiet.count()

    def get_tong_so_luong(self, obj):
        return sum(item.so_luong for item in obj.chi_tiet.all())

    def get_tong_tien(self, obj):
        tong = 0
        for item in obj.chi_tiet.all():
            if item.lua_chon_mua is not None:
                tong += int(item.lua_chon_mua.don_gia) * item.so_luong
            else:
                tong += int(item.sua.don_gia) * item.so_luong
        return tong

    def get_tong_tien_hien_thi(self, obj):
        return dinh_dang_tien(self.get_tong_tien(obj))
