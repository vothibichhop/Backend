package com.example.duannhom;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

import java.text.DecimalFormat;

public class ProductDetailActivity extends AppCompatActivity {

    private int quantity = 1;
    private final long unitPrice = 400000;
    private TextView tvQuantity;
    private Button btnAddToCart;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_product_detail);

        ImageView btnBack = findViewById(R.id.btnBack);
        TextView btnPlus = findViewById(R.id.btnPlus);
        TextView btnMinus = findViewById(R.id.btnMinus);
        tvQuantity = findViewById(R.id.tvQuantity);
        btnAddToCart = findViewById(R.id.btnAddToCart);
        ImageView ivSearch = findViewById(R.id.ivSearchDetail);

        updateUI();

        btnBack.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });

        if (ivSearch != null) {
            ivSearch.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    Intent intent = new Intent(ProductDetailActivity.this, SearchActivity.class);
                    startActivity(intent);
                }
            });
        }

        btnPlus.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                quantity++;
                updateUI();
            }
        });

        btnMinus.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (quantity > 1) {
                    quantity--;
                    updateUI();
                }
            }
        });

        btnAddToCart.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(ProductDetailActivity.this, MainActivity.class);
                intent.putExtra("show_success", true);
                intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);
                startActivity(intent);
                finish();
            }
        });
    }

    private void updateUI() {
        tvQuantity.setText(String.valueOf(quantity));
        long totalPrice = quantity * unitPrice;
        DecimalFormat formatter = new DecimalFormat("#,###");
        String formattedPrice = formatter.format(totalPrice).replace(",", ".") + "đ";
        btnAddToCart.setText(formattedPrice + " | Thêm vào giỏ");
    }
}