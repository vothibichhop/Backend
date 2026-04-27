package com.example.duannhom;

import com.google.gson.annotations.SerializedName;

public class Banner {
    @SerializedName("id")
    int id;
    
    // Thêm các bí danh phổ biến để đảm bảo nhận được dữ liệu
    @SerializedName(value = "hinh_anh", alternate = {"image", "imageUrl", "hinh"})
    String imageUrl;
    
    @SerializedName(value = "mo_ta", alternate = {"description", "content"})
    String description;
    
    @SerializedName(value = "ten_san_pham", alternate = {"product_name", "title"})
    String productName;
}
