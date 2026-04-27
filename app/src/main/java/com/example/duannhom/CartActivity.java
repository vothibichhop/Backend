package com.example.duannhom;

import android.app.AlertDialog;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class CartActivity extends AppCompatActivity {

    private TextView tvTotalPrice;
    private TextView tvEmptyCart;
    private final List<CartItem> cartItems = new ArrayList<>();
    private CartAdapter adapter;
    private RecyclerView rvCartItems;
    private ApiService apiService;
    private String cartId;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cart);

        apiService = RetrofitClient.getClient().create(ApiService.class);
        SharedPreferences prefs = getSharedPreferences("CartPrefs", MODE_PRIVATE);
        cartId = prefs.getString("cart_id", null);

        ImageView ivBack = findViewById(R.id.ivBackCart);
        tvTotalPrice = findViewById(R.id.tvTotalPrice);
        tvEmptyCart = findViewById(R.id.tvEmptyCart);
        rvCartItems = findViewById(R.id.rvCartItems);
        TextView tvClearAll = findViewById(R.id.tvClearAll);

        ivBack.setOnClickListener(v -> finish());

        adapter = new CartAdapter(this, cartItems, totalPrice -> updateTotalPriceUI());
        rvCartItems.setLayoutManager(new LinearLayoutManager(this));
        rvCartItems.setAdapter(adapter);

        if (cartId != null) {
            fetchCartFromServer();
        } else {
            CartManager.getInstance().clear();
            updateUI();
        }

        tvClearAll.setOnClickListener(v -> {
            if (!cartItems.isEmpty()) {
                showClearAllDialog();
            }
        });
    }

    private void fetchCartFromServer() {
        apiService.getCartDetails(cartId).enqueue(new Callback<CartResponse>() {
            @Override
            public void onResponse(Call<CartResponse> call, Response<CartResponse> response) {
                if (response.isSuccessful() && response.body() != null) {
                    applyCartResponse(response.body());
                } else {
                    updateUI();
                }
            }

            @Override
            public void onFailure(Call<CartResponse> call, Throwable t) {
                Toast.makeText(CartActivity.this, "Khong the tai gio hang tu may chu", Toast.LENGTH_SHORT).show();
                updateUI();
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
            if (cartId != null) {
                apiService.clearCart(cartId).enqueue(new Callback<CartResponse>() {
                    @Override
                    public void onResponse(Call<CartResponse> call, Response<CartResponse> response) {
                        if (response.isSuccessful() && response.body() != null) {
                            applyCartResponse(response.body());
                        }
                    }

                    @Override
                    public void onFailure(Call<CartResponse> call, Throwable t) {
                        Toast.makeText(CartActivity.this, "Loi khi xoa gio hang", Toast.LENGTH_SHORT).show();
                    }
                });
            }
            dialog.dismiss();
        });

        dialog.show();
    }

    private void updateUI() {
        updateTotalPriceUI();
        if (cartItems.isEmpty()) {
            tvEmptyCart.setVisibility(View.VISIBLE);
            rvCartItems.setVisibility(View.GONE);
        } else {
            tvEmptyCart.setVisibility(View.GONE);
            rvCartItems.setVisibility(View.VISIBLE);
        }
    }

    private void updateTotalPriceUI() {
        long total = 0;
        for (CartItem item : cartItems) {
            total += item.price * item.quantity;
        }
        DecimalFormat formatter = new DecimalFormat("#,###");
        tvTotalPrice.setText(formatter.format(total).replace(",", ".") + "\u0111");
    }

    private void applyCartResponse(CartResponse response) {
        cartItems.clear();
        if (response.items != null) {
            cartItems.addAll(response.items);
        }
        CartManager.getInstance().syncCart(response);
        adapter.notifyDataSetChanged();
        updateUI();
    }
}
