package com.example.duannhom;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.List;

public class CartActivity extends AppCompatActivity {

    private TextView tvTotalPrice, tvEmptyCart;
    private List<CartItem> cartItems;
    private CartAdapter adapter;
    private RecyclerView rvCartItems;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cart);

        ImageView ivBack = findViewById(R.id.ivBackCart);
        tvTotalPrice = findViewById(R.id.tvTotalPrice);
        tvEmptyCart = findViewById(R.id.tvEmptyCart);
        rvCartItems = findViewById(R.id.rvCartItems);
        TextView tvClearAll = findViewById(R.id.tvClearAll);

        ivBack.setOnClickListener(v -> finish());

        cartItems = new ArrayList<>();
        cartItems.add(new CartItem(R.drawable.th, "Sữa tươi nguyên chất", "Hộp 1L", 45000, 1));
        cartItems.add(new CartItem(R.drawable.img, "Sữa đặc có đường", "chai 500ml", 35000, 2));
        cartItems.add(new CartItem(R.drawable.th, "Sữa chua việt quất", "Lốc 4 hộp", 28000, 3));

        adapter = new CartAdapter(cartItems, totalPrice -> {
            updateUI();
        });

        rvCartItems.setLayoutManager(new LinearLayoutManager(this));
        rvCartItems.setAdapter(adapter);

        updateUI();

        tvClearAll.setOnClickListener(v -> {
            if (!cartItems.isEmpty()) {
                showClearAllDialog();
            }
        });
    }

    private void showClearAllDialog() {
        View dialogView = LayoutInflater.from(this).inflate(R.layout.dialog_clear_all, null);
        AlertDialog dialog = new AlertDialog.Builder(this, R.style.CustomDialogTheme)
                .setView(dialogView)
                .create();

        dialogView.findViewById(R.id.btnCancelClear).setOnClickListener(v -> dialog.dismiss());
        dialogView.findViewById(R.id.btnConfirmClear).setOnClickListener(v -> {
            cartItems.clear();
            adapter.notifyDataSetChanged();
            updateUI();
            dialog.dismiss();
        });

        dialog.show();
    }

    private void updateUI() {
        long total = 0;
        for (CartItem item : cartItems) {
            total += item.price * item.quantity;
        }
        DecimalFormat formatter = new DecimalFormat("#,###");
        tvTotalPrice.setText(formatter.format(total).replace(",", ".") + "đ");

        if (cartItems.isEmpty()) {
            tvEmptyCart.setVisibility(View.VISIBLE);
            rvCartItems.setVisibility(View.GONE);
        } else {
            tvEmptyCart.setVisibility(View.GONE);
            rvCartItems.setVisibility(View.VISIBLE);
        }
    }
}