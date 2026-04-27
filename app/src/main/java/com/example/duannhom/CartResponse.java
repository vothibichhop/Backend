package com.example.duannhom;

import com.google.gson.annotations.SerializedName;

public class CartResponse {
    @SerializedName("id")
    public String id;

    @SerializedName("ma_gio_hang")
    public String maGioHang;

    public String getCartId() {
        return maGioHang != null ? maGioHang : id;
    }
}
