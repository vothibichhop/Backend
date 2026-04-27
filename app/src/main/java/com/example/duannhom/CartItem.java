package com.example.duannhom;

import com.google.gson.annotations.SerializedName;

public class CartItem {
    @SerializedName("id")
    public int id;

    @SerializedName("hinh")
    public String imageUrl;

    @SerializedName("ten_sua")
    public String name;

    @SerializedName("thong_tin_hien_thi")
    public String info;

    @SerializedName("don_gia")
    public long price;

    @SerializedName("so_luong")
    public int quantity;

    @SerializedName("ma_sua")
    public String productId;

    @SerializedName("lua_chon_mua_id")
    public Integer optionId;

    public CartItem() {
    }

    public CartItem(String productId, String imageUrl, String name, String info, long price, int quantity) {
        this.productId = productId;
        this.imageUrl = imageUrl;
        this.name = name;
        this.info = info;
        this.price = price;
        this.quantity = quantity;
    }
}
