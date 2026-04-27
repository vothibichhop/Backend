package com.example.duannhom;

public class CartItem {
    public String imageUrl;
    public String name;
    public String info;
    public long price;
    public int quantity;
    public String productId;

    public CartItem(String productId, String imageUrl, String name, String info, long price, int quantity) {
        this.productId = productId;
        this.imageUrl = imageUrl;
        this.name = name;
        this.info = info;
        this.price = price;
        this.quantity = quantity;
    }
}
