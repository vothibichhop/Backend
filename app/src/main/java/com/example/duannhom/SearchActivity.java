package com.example.duannhom;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class SearchActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_search);

        ImageView btnClose = findViewById(R.id.btnCloseSearch);
        if (btnClose != null) {
            btnClose.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    finish(); // Thoát màn hình tìm kiếm quay về trang chủ
                }
            });
        }

        TextView tvSuaBotTreEm = findViewById(R.id.tvSuaBotTreEm);
        if (tvSuaBotTreEm != null) {
            tvSuaBotTreEm.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    // Chuyển sang màn hình danh sách sản phẩm của danh mục Sữa bột trẻ em
                    Intent intent = new Intent(SearchActivity.this, CategoryDetailActivity.class);
                    startActivity(intent);
                }
            });
        }
    }
}