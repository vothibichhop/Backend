package com.example.duannhom;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class Product {
    @SerializedName("ma_sua")
    public String id;

    @SerializedName("ten_sua")
    public String name;

    @SerializedName("don_gia")
    public String price;

    @SerializedName("nhan_giam_gia")
    public String discount;

    @SerializedName("hinh")
    public String imageUrl;

    @SerializedName("quy_cach")
    public String specification;

    @SerializedName("mo_ta_chi_tiet")
    public String description;

    @SerializedName("lua_chon_mua")
    public List<ProductOption> options;

    public Product() {
    }

    public static class ProductOption {
        @SerializedName("id")
        public Integer id;

        @SerializedName("ten_lua_chon")
        public String optionName;

        @SerializedName("gia_hien_thi")
        public String displayPrice;

        @SerializedName("nhan_giam_gia")
        public String discountLabel;

        @SerializedName("don_gia")
        public long priceValue;

        @SerializedName("mac_dinh")
        public boolean isDefault;
    }
}
