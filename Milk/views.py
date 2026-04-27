import unicodedata

from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import BannerQuangCao, ChiTietGioHang, DanhMucSanPham, DonHang, GioHang, Sua
from .serializers import (
    BannerQuangCaoSerializer,
    CapNhatChiTietGioHangSerializer,
    ChiTietDanhMucSanPhamSerializer,
    ChiTietSuaSerializer,
    DanhMucGoiYSerializer,
    DanhMucSanPhamSearchQuerySerializer,
    DanhMucSanPhamSerializer,
    DonHangSerializer,
    GioHangSerializer,
    SuaListQuerySerializer,
    SuaListSerializer,
    ThemSanPhamVaoGioHangSerializer,
)


def _normalize_search_text(value):
    normalized = unicodedata.normalize("NFD", value or "")
    without_diacritics = "".join(char for char in normalized if unicodedata.category(char) != "Mn")
    return without_diacritics.casefold().strip()


class SuaViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    lookup_field = "ma_sua"

    def get_queryset(self):
        queryset = (
            Sua.objects.select_related("hang_sua", "loai_sua", "danh_muc")
            .prefetch_related("lua_chon_mua")
            .order_by("ma_sua")
        )

        query_serializer = SuaListQuerySerializer(data=self.request.query_params)
        query_serializer.is_valid(raise_exception=True)
        params = query_serializer.validated_data

        if params.get("q"):
            queryset = queryset.filter(
                Q(ten_sua__icontains=params["q"])
                | Q(quy_cach__icontains=params["q"])
                | Q(thanh_phan__icontains=params["q"])
                | Q(loi_ich__icontains=params["q"])
            )
        if params.get("hang_sua"):
            queryset = queryset.filter(hang_sua_id=params["hang_sua"])
        if params.get("loai_sua"):
            queryset = queryset.filter(loai_sua_id=params["loai_sua"])
        if params.get("danh_muc"):
            queryset = queryset.filter(danh_muc_id=params["danh_muc"])

        return queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ChiTietSuaSerializer
        return SuaListSerializer

    @action(detail=False, methods=["get"], url_path="danh-sach-san-pham")
    def danh_sach_san_pham(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class DanhMucSanPhamViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    lookup_field = "ma_danh_muc"

    def get_queryset(self):
        return (
            DanhMucSanPham.objects.filter(hien_thi=True)
            .select_related("loai_sua")
            .prefetch_related("san_pham__hang_sua", "san_pham__loai_sua", "san_pham__danh_muc")
            .order_by("thu_tu", "ma_danh_muc")
        )

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ChiTietDanhMucSanPhamSerializer
        return DanhMucSanPhamSerializer

    @action(detail=False, methods=["get"], url_path="danh-muc")
    def danh_muc(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="chi-tiet-danh-muc")
    def chi_tiet_danh_muc(self, request):
        serializer = ChiTietDanhMucSanPhamSerializer(
            self.get_queryset(),
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="tim-kiem-loai-sua")
    def tim_kiem_loai_sua(self, request):
        query_serializer = DanhMucSanPhamSearchQuerySerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)
        q = query_serializer.validated_data["q"].strip()

        queryset = self.get_queryset()
        if q:
            normalized_q = _normalize_search_text(q)
            queryset = [
                danh_muc
                for danh_muc in queryset
                if normalized_q in _normalize_search_text(danh_muc.ten_danh_muc)
                or normalized_q in _normalize_search_text(danh_muc.mo_ta)
                or normalized_q in _normalize_search_text(danh_muc.noi_bat)
                or normalized_q in _normalize_search_text(
                    danh_muc.loai_sua.ten_loai_sua if danh_muc.loai_sua else ""
                )
            ]

        serializer = DanhMucSanPhamSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="danh-cho-ban")
    def danh_cho_ban(self, request):
        queryset = [danh_muc for danh_muc in self.get_queryset() if danh_muc.san_pham.exists()][:3]
        serializer = DanhMucGoiYSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)


class BannerQuangCaoViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    serializer_class = BannerQuangCaoSerializer
    lookup_field = "ma_banner"

    def get_queryset(self):
        return (
            BannerQuangCao.objects.filter(hien_thi=True)
            .select_related("sua", "sua__danh_muc")
            .order_by("thu_tu", "ma_banner")
        )

    @action(detail=False, methods=["get"], url_path="banner")
    def banner(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class GioHangViewSet(viewsets.ViewSet):
    def _get_queryset(self):
        return GioHang.objects.prefetch_related(
            "chi_tiet__sua__danh_muc",
            "chi_tiet__lua_chon_mua",
        )

    def _get_gio_hang(self, ma_gio_hang):
        return get_object_or_404(self._get_queryset(), ma_gio_hang=ma_gio_hang)

    def _touch_gio_hang(self, gio_hang):
        GioHang.objects.filter(ma_gio_hang=gio_hang.ma_gio_hang).update(cap_nhat_luc=timezone.now())

    def _serialize_gio_hang(self, gio_hang, request, status_code=status.HTTP_200_OK):
        gio_hang = self._get_gio_hang(gio_hang.ma_gio_hang)
        serializer = GioHangSerializer(gio_hang, context={"request": request})
        return Response(serializer.data, status=status_code)

    def _them_hoac_cong_don(self, gio_hang, validated_data):
        chi_tiet, created = ChiTietGioHang.objects.get_or_create(
            gio_hang=gio_hang,
            sua=validated_data["sua"],
            lua_chon_mua=validated_data["lua_chon_mua"],
            defaults={"so_luong": validated_data["so_luong"]},
        )
        if not created:
            chi_tiet.so_luong += validated_data["so_luong"]
            chi_tiet.save(update_fields=["so_luong", "cap_nhat_luc"])
        self._touch_gio_hang(gio_hang)
        return chi_tiet

    def create(self, request):
        with transaction.atomic():
            gio_hang = GioHang.objects.create()
            if request.data:
                serializer = ThemSanPhamVaoGioHangSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self._them_hoac_cong_don(gio_hang, serializer.validated_data)
        return self._serialize_gio_hang(gio_hang, request, status.HTTP_201_CREATED)

    def retrieve(self, request, ma_gio_hang=None):
        gio_hang = self._get_gio_hang(ma_gio_hang)
        return self._serialize_gio_hang(gio_hang, request)

    def them_san_pham(self, request, ma_gio_hang=None):
        gio_hang = self._get_gio_hang(ma_gio_hang)
        serializer = ThemSanPhamVaoGioHangSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            self._them_hoac_cong_don(gio_hang, serializer.validated_data)
        return self._serialize_gio_hang(gio_hang, request)

    def cap_nhat_chi_tiet(self, request, ma_gio_hang=None, chi_tiet_id=None):
        gio_hang = self._get_gio_hang(ma_gio_hang)
        chi_tiet = get_object_or_404(
            ChiTietGioHang.objects.select_related("sua", "lua_chon_mua").prefetch_related(
                "sua__lua_chon_mua"
            ),
            gio_hang=gio_hang,
            id=chi_tiet_id,
        )
        serializer = CapNhatChiTietGioHangSerializer(
            data=request.data,
            partial=True,
            context={"chi_tiet": chi_tiet},
        )
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            so_luong_moi = serializer.validated_data.get("so_luong", chi_tiet.so_luong)
            lua_chon_mua_moi = serializer.validated_data.get("lua_chon_mua", chi_tiet.lua_chon_mua)

            trung_item = (
                ChiTietGioHang.objects.filter(
                    gio_hang=gio_hang,
                    sua=chi_tiet.sua,
                    lua_chon_mua=lua_chon_mua_moi,
                )
                .exclude(id=chi_tiet.id)
                .first()
            )
            if trung_item is not None:
                trung_item.so_luong += so_luong_moi
                trung_item.save(update_fields=["so_luong", "cap_nhat_luc"])
                chi_tiet.delete()
            else:
                chi_tiet.so_luong = so_luong_moi
                chi_tiet.lua_chon_mua = lua_chon_mua_moi
                chi_tiet.save(update_fields=["so_luong", "lua_chon_mua", "cap_nhat_luc"])
            self._touch_gio_hang(gio_hang)

        return self._serialize_gio_hang(gio_hang, request)

    def xoa_chi_tiet(self, request, ma_gio_hang=None, chi_tiet_id=None):
        gio_hang = self._get_gio_hang(ma_gio_hang)
        chi_tiet = get_object_or_404(ChiTietGioHang, gio_hang=gio_hang, id=chi_tiet_id)
        chi_tiet.delete()
        self._touch_gio_hang(gio_hang)
        return self._serialize_gio_hang(gio_hang, request)

    def xoa_tat_ca(self, request, ma_gio_hang=None):
        gio_hang = self._get_gio_hang(ma_gio_hang)
        gio_hang.chi_tiet.all().delete()
        self._touch_gio_hang(gio_hang)
        return self._serialize_gio_hang(gio_hang, request)


class DonHangViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = DonHangSerializer

    def get_queryset(self):
        return DonHang.objects.prefetch_related("san_pham__san_pham").order_by("-ngay_dat", "id")

    @action(detail=False, methods=["get"], url_path="lich-su-don-hang")
    def lich_su_don_hang(self, request):
        serializer = self.get_serializer(
            self.get_queryset(),
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)
