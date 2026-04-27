package com.example.duannhom;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.google.android.material.bottomnavigation.BottomNavigationView;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity {

    private RecyclerView rvProduct;
    private ProductAdapter productAdapter;
    private List<Product> productList;
    private TextView tvSuccessMessage, tvCartBadge;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvSuccessMessage = findViewById(R.id.tvSuccessMessage);
        tvCartBadge = findViewById(R.id.tvCartBadge); // Ánh xạ biểu tượng số lượng giỏ hàng
        rvProduct = findViewById(R.id.rvProduct);
        EditText etSearchMain = findViewById(R.id.etSearchMain);
        ImageView imgCartMain = findViewById(R.id.imgCartMain);
        BottomNavigationView bottomNav = findViewById(R.id.bottomNav);

        bottomNav.setItemIconTintList(null);

        productList = new ArrayList<>();
        productAdapter = new ProductAdapter(productList);
        rvProduct.setLayoutManager(new GridLayoutManager(this, 3));
        rvProduct.setAdapter(productAdapter);

        fetchProducts();
        updateCartBadge(); // Cập nhật số lượng giỏ hàng khi mở app

        etSearchMain.setOnClickListener(v -> startActivity(new Intent(MainActivity.this, SearchActivity.class)));
        imgCartMain.setOnClickListener(v -> startActivity(new Intent(MainActivity.this, CartActivity.class)));

        bottomNav.setOnItemSelectedListener(item -> {
            int id = item.getItemId();
            if (id == R.id.menu_home) {
                fetchProducts();
                return true;
            } else if (id == R.id.menu_category) {
                startActivity(new Intent(MainActivity.this, CategoryActivity.class));
                return true;
            }
            return false;
        });
    }

    @Override
    protected void onResume() {
        super.onResume();
        handleIntent(getIntent());
        updateCartBadge(); // Cập nhật lại số lượng giỏ hàng khi quay về trang chủ
    }

    private void updateCartBadge() {
        if (tvCartBadge != null) {
            int count = CartManager.getInstance().getCartCount();
            if (count > 0) {
                tvCartBadge.setVisibility(View.VISIBLE);
                tvCartBadge.setText(String.valueOf(count));
            } else {
                tvCartBadge.setVisibility(View.GONE);
            }
        }
    }

    private void fetchProducts() {
        ApiService apiService = RetrofitClient.getClient().create(ApiService.class);
        apiService.getMilkProducts().enqueue(new Callback<List<Product>>() {
            @Override
            public void onResponse(Call<List<Product>> call, Response<List<Product>> response) {
                if (response.isSuccessful() && response.body() != null) {
                    productList.clear();
                    productList.addAll(response.body());
                    productAdapter.notifyDataSetChanged();
                }
            }
            @Override
            public void onFailure(Call<List<Product>> call, Throwable t) {}
        });
    }

    @Override
    protected void onNewIntent(Intent intent) {
        super.onNewIntent(intent);
        setIntent(intent);
        handleIntent(intent);
    }

    private void handleIntent(Intent intent) {
        if (intent != null && intent.getBooleanExtra("show_success", false)) {
            if (tvSuccessMessage != null) {
                tvSuccessMessage.setVisibility(View.VISIBLE);
                intent.putExtra("show_success", false);
                tvSuccessMessage.postDelayed(() -> tvSuccessMessage.setVisibility(View.GONE), 3000);
            }
        }
    }
}
