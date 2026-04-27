from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BannerQuangCaoViewSet, DanhMucSanPhamViewSet, GioHangViewSet, SuaViewSet

router = DefaultRouter(trailing_slash=False)
router.register("banner-quang-cao", BannerQuangCaoViewSet, basename="banner-quang-cao")
router.register("danh-muc-san-pham", DanhMucSanPhamViewSet, basename="danh-muc-san-pham")
router.register("san-pham-sua", SuaViewSet, basename="san-pham-sua")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "gio-hang",
        GioHangViewSet.as_view({"post": "create"}),
        name="tao-gio-hang",
    ),
    path(
        "gio-hang/<uuid:ma_gio_hang>",
        GioHangViewSet.as_view({"get": "retrieve"}),
        name="chi-tiet-gio-hang",
    ),
    path(
        "gio-hang/<uuid:ma_gio_hang>/them-san-pham",
        GioHangViewSet.as_view({"post": "them_san_pham"}),
        name="them-san-pham-vao-gio",
    ),
    path(
        "gio-hang/<uuid:ma_gio_hang>/chi-tiet/<int:chi_tiet_id>",
        GioHangViewSet.as_view(
            {
                "patch": "cap_nhat_chi_tiet",
                "delete": "xoa_chi_tiet",
            }
        ),
        name="cap-nhat-chi-tiet-gio-hang",
    ),
    path(
        "gio-hang/<uuid:ma_gio_hang>/xoa-tat-ca",
        GioHangViewSet.as_view({"delete": "xoa_tat_ca"}),
        name="xoa-tat-ca-gio-hang",
    ),
    path(
        "chi-tiet-san-pham/<str:ma_sua>",
        SuaViewSet.as_view({"get": "retrieve"}),
        name="chi-tiet-san-pham",
    ),
    path(
        "banner",
        BannerQuangCaoViewSet.as_view({"get": "banner"}),
        name="banner",
    ),
    path(
        "chi-tiet-danh-muc/<str:ma_danh_muc>",
        DanhMucSanPhamViewSet.as_view({"get": "retrieve"}),
        name="chi-tiet-mot-danh-muc",
    ),
    path(
        "chi-tiet-danh-muc",
        DanhMucSanPhamViewSet.as_view({"get": "chi_tiet_danh_muc"}),
        name="chi-tiet-danh-muc",
    ),
    path(
        "danh-muc",
        DanhMucSanPhamViewSet.as_view({"get": "danh_muc"}),
        name="danh-muc",
    ),
    path(
        "danh-sach-san-pham",
        SuaViewSet.as_view({"get": "danh_sach_san_pham"}),
        name="danh-sach-san-pham",
    ),
]
