package com.example.duannhom;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class OrderSummary {
    @SerializedName("id")
    public String id;

    @SerializedName("ngay_dat")
    public String orderedAt;

    @SerializedName("trang_thai")
    public String statusLabel;

    @SerializedName("trang_thai_code")
    public String statusCode;

    @SerializedName("tong_tien")
    public double totalAmount;

    @SerializedName("tong_tien_hien_thi")
    public String totalAmountDisplay;

    @SerializedName("tong_san_pham")
    public int totalQuantity;

    @SerializedName("hanh_dong_chinh")
    public OrderAction primaryAction;

    @SerializedName("san_pham")
    public List<OrderItem> items;
}
