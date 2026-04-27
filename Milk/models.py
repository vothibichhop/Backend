import uuid

from django.db import models


class HangSua(models.Model):
    ma_hang_sua = models.CharField(max_length=20, primary_key=True)
    ten_hang_sua = models.CharField(max_length=100)
    dia_chi = models.CharField(max_length=255, blank=True)
    dien_thoai = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        ordering = ["ma_hang_sua"]
        verbose_name = "Hang sua"
        verbose_name_plural = "Hang sua"

    def __str__(self):
        return self.ten_hang_sua


class LoaiSua(models.Model):
    ma_loai_sua = models.CharField(max_length=20, primary_key=True)
    ten_loai_sua = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["ma_loai_sua"]
        verbose_name = "Loai sua"
        verbose_name_plural = "Loai sua"

    def __str__(self):
        return self.ten_loai_sua


class DanhMucSanPham(models.Model):
    ma_danh_muc = models.CharField(max_length=20, primary_key=True)
    ten_danh_muc = models.CharField(max_length=100, unique=True)
    mo_ta = models.TextField(blank=True)
    noi_bat = models.CharField(max_length=50, blank=True)
    so_luong_hien_thi = models.PositiveIntegerField(default=0)
    thu_tu = models.PositiveIntegerField(default=0)
    hien_thi = models.BooleanField(default=True)
    loai_sua = models.OneToOneField(
        LoaiSua,
        on_delete=models.PROTECT,
        related_name="danh_muc_san_pham",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["thu_tu", "ma_danh_muc"]
        verbose_name = "Danh muc san pham"
        verbose_name_plural = "Danh muc san pham"

    def __str__(self):
        return self.ten_danh_muc


class Sua(models.Model):
    ma_sua = models.CharField(max_length=20, primary_key=True)
    ten_sua = models.CharField(max_length=200)
    mo_ta_chi_tiet = models.TextField(blank=True)
    quy_cach = models.CharField(max_length=100, blank=True)
    trong_luong = models.PositiveIntegerField(null=True, blank=True)
    don_vi = models.CharField(max_length=10, blank=True)
    don_gia = models.DecimalField(max_digits=12, decimal_places=0)
    giam_gia = models.PositiveSmallIntegerField(default=0)
    thanh_phan = models.TextField(blank=True)
    loi_ich = models.TextField(blank=True)
    hinh = models.ImageField(upload_to="suas/", blank=True, null=True)
    hang_sua = models.ForeignKey(
        HangSua,
        on_delete=models.PROTECT,
        related_name="san_pham",
    )
    loai_sua = models.ForeignKey(
        LoaiSua,
        on_delete=models.PROTECT,
        related_name="san_pham",
    )
    danh_muc = models.ForeignKey(
        DanhMucSanPham,
        on_delete=models.PROTECT,
        related_name="san_pham",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["ma_sua"]
        verbose_name = "Sua"
        verbose_name_plural = "Sua"

    def __str__(self):
        return self.ten_sua


class LuaChonMuaSua(models.Model):
    sua = models.ForeignKey(
        Sua,
        on_delete=models.CASCADE,
        related_name="lua_chon_mua",
    )
    ten_lua_chon = models.CharField(max_length=100)
    don_gia = models.DecimalField(max_digits=12, decimal_places=0)
    giam_gia = models.PositiveSmallIntegerField(default=0)
    mac_dinh = models.BooleanField(default=False)
    thu_tu = models.PositiveIntegerField(default=0)
    hien_thi = models.BooleanField(default=True)

    class Meta:
        ordering = ["thu_tu", "id"]
        verbose_name = "Lua chon mua sua"
        verbose_name_plural = "Lua chon mua sua"

    def __str__(self):
        return f"{self.sua_id} - {self.ten_lua_chon}"


class BannerQuangCao(models.Model):
    ma_banner = models.CharField(max_length=20, primary_key=True)
    sua = models.ForeignKey(
        Sua,
        on_delete=models.CASCADE,
        related_name="banners",
        blank=True,
        null=True,
    )
    tieu_de = models.CharField(max_length=200)
    mo_ta = models.TextField(blank=True)
    nhan = models.CharField(max_length=50, blank=True)
    mau_nen = models.CharField(max_length=20, default="#f8c300")
    mau_chu = models.CharField(max_length=20, default="#8a3b12")
    thu_tu = models.PositiveIntegerField(default=0)
    hien_thi = models.BooleanField(default=True)

    class Meta:
        ordering = ["thu_tu", "ma_banner"]
        verbose_name = "Banner quang cao"
        verbose_name_plural = "Banner quang cao"

    def __str__(self):
        return self.tieu_de


class GioHang(models.Model):
    ma_gio_hang = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tao_luc = models.DateTimeField(auto_now_add=True)
    cap_nhat_luc = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-cap_nhat_luc"]
        verbose_name = "Gio hang"
        verbose_name_plural = "Gio hang"

    def __str__(self):
        return str(self.ma_gio_hang)


class ChiTietGioHang(models.Model):
    gio_hang = models.ForeignKey(
        GioHang,
        on_delete=models.CASCADE,
        related_name="chi_tiet",
    )
    sua = models.ForeignKey(
        Sua,
        on_delete=models.CASCADE,
        related_name="chi_tiet_gio_hang",
    )
    lua_chon_mua = models.ForeignKey(
        LuaChonMuaSua,
        on_delete=models.SET_NULL,
        related_name="chi_tiet_gio_hang",
        blank=True,
        null=True,
    )
    so_luong = models.PositiveIntegerField(default=1)
    tao_luc = models.DateTimeField(auto_now_add=True)
    cap_nhat_luc = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Chi tiet gio hang"
        verbose_name_plural = "Chi tiet gio hang"
        constraints = [
            models.UniqueConstraint(
                fields=["gio_hang", "sua", "lua_chon_mua"],
                name="unique_cart_item_per_option",
            )
        ]

    def __str__(self):
        return f"{self.gio_hang_id} - {self.sua_id} x {self.so_luong}"


class DonHang(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    ngay_dat = models.DateTimeField()
    trang_thai = models.CharField(max_length=50)
    tong_tien = models.DecimalField(max_digits=12, decimal_places=1)

    class Meta:
        ordering = ["-ngay_dat", "id"]
        verbose_name = "Don hang"
        verbose_name_plural = "Don hang"

    def __str__(self):
        return self.id


class ChiTietDonHang(models.Model):
    don_hang = models.ForeignKey(
        DonHang,
        on_delete=models.CASCADE,
        related_name="san_pham",
    )
    san_pham = models.ForeignKey(
        Sua,
        on_delete=models.PROTECT,
        related_name="chi_tiet_don_hang",
    )
    so_luong = models.PositiveIntegerField(default=1)
    gia_ban = models.DecimalField(max_digits=12, decimal_places=1)

    class Meta:
        ordering = ["id"]
        verbose_name = "Chi tiet don hang"
        verbose_name_plural = "Chi tiet don hang"

    def __str__(self):
        return f"{self.don_hang_id} - {self.san_pham_id} x {self.so_luong}"
