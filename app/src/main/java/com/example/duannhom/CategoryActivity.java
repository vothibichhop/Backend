package com.example.duannhom;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import com.bumptech.glide.Glide;
import com.google.android.material.bottomnavigation.BottomNavigationView;
import java.util.ArrayList;
import java.util.List;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class CategoryActivity extends AppCompatActivity {
    private RecyclerView rvCategories;
    private CategoryAdapter adapter;
    private List<Category> categoryList;
    private ImageView ivBannerProduct;
    private TextView tvBannerDesc, tvBannerProductName, tvCartBadge;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_category);

        // 1. Ánh xạ các View
        rvCategories = findViewById(R.id.rvCategories);
        ivBannerProduct = findViewById(R.id.ivBannerProduct);
        tvBannerDesc = findViewById(R.id.tvBannerDesc);
        tvBannerProductName = findViewById(R.id.tvBannerProductName);
        tvCartBadge = findViewById(R.id.tvCartBadgeCategory);

        // Ánh xạ nút mũi tên chuyển trang (Fix lỗi null mã danh mục)
        ImageView ivNext = findViewById(R.id.ivNextPage);

        // 2. Thiết lập RecyclerView
        categoryList = new ArrayList<>();
        adapter = new CategoryAdapter(categoryList);
        rvCategories.setLayoutManager(new LinearLayoutManager(this));
        rvCategories.setAdapter(adapter);

        // 3. Xử lý sự kiện Click chuyển trang (Mũi tên mặc định cho DM01)
        if (ivNext != null) {
            ivNext.setOnClickListener(v -> {
                Intent intent = new Intent(CategoryActivity.this, CategoryDetailActivity.class);
                intent.putExtra("MA_DANH_MUC", "DM01"); // Mặc định chuyển đến danh mục đầu tiên
                startActivity(intent);
            });
        }

        // 4. Xử lý Bottom Navigation
        BottomNavigationView bottomNav = findViewById(R.id.bottomNavCategory);
        if (bottomNav != null) {
            bottomNav.setSelectedItemId(R.id.menu_category);
            bottomNav.setItemIconTintList(null);
            bottomNav.setOnItemSelectedListener(item -> {
                int id = item.getItemId();
                if (id == R.id.menu_home) {
                    startActivity(new Intent(this, MainActivity.class));
                    finish();
                    return true;
                }
                return id == R.id.menu_category;
            });
        }

        // 5. Lấy dữ liệu từ API
        fetchCategories();
        fetchBannerData();
        updateCartBadge();
    }

    @Override
    protected void onResume() {
        super.onResume();
        updateCartBadge(); // Cập nhật lại số lượng giỏ hàng khi quay về
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

    private void fetchBannerData() {
        ApiService apiService = RetrofitClient.getClient().create(ApiService.class);
        apiService.getBanners().enqueue(new Callback<List<Banner>>() {
            @Override
            public void onResponse(Call<List<Banner>> call, Response<List<Banner>> response) {
                if (response.isSuccessful() && response.body() != null && !response.body().isEmpty()) {
                    Banner banner = response.body().get(0);
                    if (tvBannerProductName != null) tvBannerProductName.setText(banner.productName);
                    if (tvBannerDesc != null) tvBannerDesc.setText(banner.description);
                    if (ivBannerProduct != null && banner.imageUrl != null) {
                        Glide.with(CategoryActivity.this)
                                .load(ImageUrlHelper.resolve(banner.imageUrl))
                                .placeholder(R.drawable.thtruemilk)
                                .into(ivBannerProduct);
                    }
                }
            }
            @Override
            public void onFailure(Call<List<Banner>> call, Throwable t) {}
        });
    }

    private void fetchCategories() {
        ApiService apiService = RetrofitClient.getClient().create(ApiService.class);
        apiService.getCategories().enqueue(new Callback<List<Category>>() {
            @Override
            public void onResponse(Call<List<Category>> call, Response<List<Category>> response) {
                if (response.isSuccessful() && response.body() != null) {
                    categoryList.clear();
                    categoryList.addAll(response.body());
                    adapter.notifyDataSetChanged();
                } else {
                    loadDummyData();
                }
            }
            @Override
            public void onFailure(Call<List<Category>> call, Throwable t) {
                loadDummyData();
            }
        });
    }

    private void loadDummyData() {
        categoryList.clear();
        categoryList.add(new Category("DM01", "Sữa bột trẻ em", 20));
        categoryList.add(new Category("DM02", "Bột ăn dặm", 25));
        categoryList.add(new Category("DM03", "Sữa bột người lớn", 24));
        categoryList.add(new Category("DM04", "Sữa chua ăn", 50));
        categoryList.add(new Category("DM05", "Sữa tươi nguyên chất", 50));
        categoryList.add(new Category("DM06", "Sữa đặc nguyên chất", 40));
        categoryList.add(new Category("DM07", "Sữa thực vật", 30));
        adapter.notifyDataSetChanged();
    }
}
