package com.example.duannhom;

import com.google.gson.annotations.SerializedName;

public class OrderItem {
    @SerializedName("ma_sua")
    public String productId;

    @SerializedName("ten_sp")
    public String productName;

    @SerializedName("so_luong")
    public int quantity;

    @SerializedName("gia_ban")
    public double unitPrice;

    @SerializedName("gia_ban_hien_thi")
    public String displayUnitPrice;

    @SerializedName("hinh_anh")
    public String imageUrl;
}
