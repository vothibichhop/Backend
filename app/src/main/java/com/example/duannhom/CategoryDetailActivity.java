package com.example.duannhom;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import java.util.ArrayList;
import java.util.List;

public class CategoryDetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_category_detail);

        ImageView btnBack = findViewById(R.id.btnBack);
        btnBack.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });

        ImageView ivSearch = findViewById(R.id.ivSearchCategoryDetail);
        if (ivSearch != null) {
            ivSearch.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    Intent intent = new Intent(CategoryDetailActivity.this, SearchActivity.class);
                    startActivity(intent);
                }
            });
        }

        RecyclerView rv = findViewById(R.id.rvCategoryProducts);
        rv.setLayoutManager(new GridLayoutManager(this, 2));

        // Diversifying products in the Category Detail screen
        List<Product> list = new ArrayList<>();
        list.add(new Product(R.drawable.ongtho, "Sữa bột Optimum Gold 1", "400g, Lẻ 1 lon", "210.000đ", "-5%"));
        list.add(new Product(R.drawable.ongtho, "Sữa bột Dielac Alpha", "900g, Lẻ 1 lon", "250.000đ", "-7%"));
        list.add(new Product(R.drawable.ongtho, "Sữa bột Similac IQ", "400g, Lẻ 1 lon", "320.000đ", "-3%"));
        list.add(new Product(R.drawable.ongtho, "Sữa bột Enfamil A+", "830g, Lẻ 1 lon", "580.000đ", "-10%"));
        list.add(new Product(R.drawable.ongtho, "Sữa bột Grow Plus+", "900g, Lẻ 1 lon", "350.000đ", "-5%"));
        list.add(new Product(R.drawable.ongtho, "Sữa bột Meiji Nhật", "800g, Lẻ 1 lon", "520.000đ", "-0%"));

        ProductAdapter adapter = new ProductAdapter(list);
        rv.setAdapter(adapter);
    }
}
