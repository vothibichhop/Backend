package com.example.duannhom;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class CartResponse {
    @SerializedName("id")
    public String id;

    @SerializedName("ma_gio_hang")
    public String maGioHang;

    @SerializedName("tong_mat_hang")
    public int tongMatHang;

    @SerializedName("tong_so_luong")
    public int tongSoLuong;

    @SerializedName("tong_tien")
    public long tongTien;

    @SerializedName("tong_tien_hien_thi")
    public String tongTienHienThi;

    @SerializedName("items")
    public List<CartItem> items;

    public String getCartId() {
        return maGioHang != null ? maGioHang : id;
    }
}
