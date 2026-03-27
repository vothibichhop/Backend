package com.example.duannhom;

public class Product {
    int imageRes;
    String name;
    String info;
    String price;
    String discount;

    public Product(int imageRes, String name, String info, String price, String discount) {
        this.imageRes = imageRes;
        this.name = name;
        this.info = info;
        this.price = price;
        this.discount = discount;
    }
}