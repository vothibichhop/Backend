package com.example.duannhom;

import java.util.ArrayList;
import java.util.List;

public class CartManager {
    private static CartManager instance;
    private List<CartItem> cartItems;

    private CartManager() {
        cartItems = new ArrayList<>();
    }

    public static synchronized CartManager getInstance() {
        if (instance == null) {
            instance = new CartManager();
        }
        return instance;
    }

    public void addToCart(CartItem item) {
        // Kiểm tra xem sản phẩm đã có trong giỏ chưa
        for (CartItem existingItem : cartItems) {
            if (existingItem.productId != null && existingItem.productId.equals(item.productId)) {
                existingItem.quantity += item.quantity;
                return;
            }
        }
        cartItems.add(item);
    }

    public int getCartCount() {
        int total = 0;
        for (CartItem item : cartItems) {
            total += item.quantity;
        }
        return total;
    }

    public List<CartItem> getCartItems() {
        return cartItems;
    }
}
