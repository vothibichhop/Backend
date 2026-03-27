package com.example.duannhom;

public class CartItem {
    int imageRes;
    String name;
    String info;
    long price;
    int quantity;

    public CartItem(int imageRes, String name, String info, long price, int quantity) {
        this.imageRes = imageRes;
        this.name = name;
        this.info = info;
        this.price = price;
        this.quantity = quantity;
    }
}