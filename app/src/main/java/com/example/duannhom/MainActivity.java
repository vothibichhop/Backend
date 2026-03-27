package com.example.duannhom;

import android.content.Intent;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.google.android.material.bottomnavigation.BottomNavigationView;
import com.google.android.material.navigation.NavigationBarView;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private RecyclerView rvProduct;
    private ProductAdapter productAdapter;
    private List<Product> productList;
    private TextView tvSuccessMessage;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvSuccessMessage = findViewById(R.id.tvSuccessMessage);
        rvProduct = findViewById(R.id.rvProduct);
        EditText etSearchMain = findViewById(R.id.etSearchMain);
        ImageView imgCartMain = findViewById(R.id.imgCartMain);
        BottomNavigationView bottomNav = findViewById(R.id.bottomNav);

        // Check for success message from ProductDetailActivity
        handleIntent(getIntent());

        // Setup RecyclerView with more products
        productList = new ArrayList<>();
        productList.add(new Product(R.drawable.thtruemilk, "Sữa tươi tiệt trùng TH", "180 ml, Thùng 48 hộp", "430.000đ", "-7%"));
        productList.add(new Product(R.drawable.ongtho, "Sữa đặc Ông Thọ", "380g, Lẻ 1 lon", "25.000đ", "-5%"));
        productList.add(new Product(R.drawable.ensure, "Sữa bột Ensure Gold", "850g, Lẻ 1 lon", "750.000đ", "-10%"));
        productList.add(new Product(R.drawable.thtruemilk, "Sữa tươi TH ít đường", "110 ml, Thùng 48 hộp", "320.000đ", "-5%"));
        productList.add(new Product(R.drawable.ongtho, "Sữa đặc Ông Thọ đỏ", "380g, Lẻ 1 lon", "28.000đ", "-3%"));
        productList.add(new Product(R.drawable.ensure, "Sữa bột Ensure Vanilla", "400g, Lẻ 1 lon", "380.000đ", "-8%"));
        productList.add(new Product(R.drawable.thtruemilk, "Sữa hạt TH True Nut", "180 ml, Thùng 48 hộp", "550.000đ", "-12%"));
        productList.add(new Product(R.drawable.ongtho, "Sữa đặc Ông Thọ tuýp", "165g, Lẻ 1 tuýp", "18.000đ", "-0%"));
        productList.add(new Product(R.drawable.ensure, "Sữa nước Ensure Gold", "237ml, Thùng 24 chai", "950.000đ", "-5%"));
        productList.add(new Product(R.drawable.thtruemilk, "Sữa chua uống TH", "110 ml, Thùng 48 hộp", "280.000đ", "-15%"));

        productAdapter = new ProductAdapter(productList);
        rvProduct.setLayoutManager(new GridLayoutManager(this, 2));
        rvProduct.setAdapter(productAdapter);

        etSearchMain.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this, SearchActivity.class));
            }
        });

        imgCartMain.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this, CartActivity.class));
            }
        });

        bottomNav.setOnItemSelectedListener(new NavigationBarView.OnItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                int id = item.getItemId();
                if (id == R.id.menu_home) {
                    return true;
                } else if (id == R.id.menu_category) {
                    Intent intent = new Intent(MainActivity.this, CategoryDetailActivity.class);
                    startActivity(intent);
                    return true;
                } else if (id == R.id.menu_orders) {
                    // Navigate to Orders
                    return true;
                } else if (id == R.id.menu_account) {
                    // Navigate to Account
                    return true;
                }
                return false;
            }
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
                tvSuccessMessage.postDelayed(new Runnable() {
                    @Override
                    public void run() {
                        tvSuccessMessage.setVisibility(View.GONE);
                    }
                }, 3000);
            }
        }
    }
}
