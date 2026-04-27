package com.example.duannhom;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import java.util.ArrayList;
import java.util.List;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class CategoryDetailActivity extends AppCompatActivity {

    private TextView tvTitle, tvDescription;
    private RecyclerView rv;
    private List<Product> productList;
    private ProductAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_category_detail);

        // 1. Ánh xạ View
        tvTitle = findViewById(R.id.tvTitle);
        tvDescription = findViewById(R.id.tvDescription);
        rv = findViewById(R.id.rvCategoryProducts);
        ImageView btnBack = findViewById(R.id.btnBack);

        // 2. Thiết lập RecyclerView (Hiển thị lưới 2 cột)
        rv.setLayoutManager(new GridLayoutManager(this, 2));
        productList = new ArrayList<>();
        adapter = new ProductAdapter(productList);
        rv.setAdapter(adapter);

        // 3. Xử lý nút quay lại
        btnBack.setOnClickListener(v -> finish());

        // 4. Nhận mã danh mục gửi từ màn hình trước
        String maDanhMuc = getIntent().getStringExtra("MA_DANH_MUC");

        if (maDanhMuc != null) {
            fetchCategoryDetail(maDanhMuc);
        } else {
            if(tvDescription != null) tvDescription.setText("Không tìm thấy mã danh mục.");
        }

        // 5. Nút tìm kiếm
        ImageView ivSearch = findViewById(R.id.ivSearchCategoryDetail);
        if (ivSearch != null) {
            ivSearch.setOnClickListener(v -> {
                startActivity(new Intent(this, SearchActivity.class));
            });
        }
    }

    private void fetchCategoryDetail(String maLoai) {
        ApiService apiService = RetrofitClient.getClient().create(ApiService.class);
        
        // Gọi API chi tiết: api/danh-muc-san-pham/DM01
        apiService.getCategoryDetail(maLoai).enqueue(new Callback<Category>() {
            @Override
            public void onResponse(Call<Category> call, Response<Category> response) {
                if (response.isSuccessful() && response.body() != null) {
                    Category category = response.body();
                    
                    // Cập nhật Tiêu đề và Mô tả
                    if (tvTitle != null) tvTitle.setText(category.name);
                    if (tvDescription != null) tvDescription.setText(category.mo_ta);
                    
                    // Cập nhật danh sách sản phẩm
                    if (category.san_pham != null) {
                        productList.clear();
                        productList.addAll(category.san_pham);
                        adapter.notifyDataSetChanged();
                    }
                } else {
                    Toast.makeText(CategoryDetailActivity.this, "Không tìm thấy dữ liệu", Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<Category> call, Throwable t) {
                Toast.makeText(CategoryDetailActivity.this, "Lỗi kết nối: " + t.getMessage(), Toast.LENGTH_SHORT).show();
            }
        });
    }
}
