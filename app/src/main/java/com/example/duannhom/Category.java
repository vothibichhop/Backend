package com.example.duannhom;

import com.google.gson.annotations.SerializedName;
import java.util.List;

public class Category {
    @SerializedName("ma_danh_muc")
    public String ma_danh_muc;

    @SerializedName("ten_danh_muc")
    public String name;

    @SerializedName("mo_ta")
    public String mo_ta;

    @SerializedName("so_luong_san_pham")
    public int count;

    @SerializedName("san_pham")
    public List<Product> san_pham;

    public Category() {}

    // Constructor đầy đủ để fix lỗi mã danh mục bị null
    public Category(String ma_danh_muc, String name, int count) {
        this.ma_danh_muc = ma_danh_muc;
        this.name = name;
        this.count = count;
    }
}
