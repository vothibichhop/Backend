from django.contrib import admin

from .models import ChiTietDonHang, DonHang


class ChiTietDonHangInline(admin.TabularInline):
    model = ChiTietDonHang
    extra = 1


@admin.register(DonHang)
class DonHangAdmin(admin.ModelAdmin):
    list_display = ("id", "ngay_dat", "trang_thai", "tong_tien")
    search_fields = ("id", "trang_thai")
    list_filter = ("trang_thai", "ngay_dat")
    inlines = [ChiTietDonHangInline]
