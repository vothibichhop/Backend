package com.example.duannhom;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;

import java.text.DecimalFormat;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class ProductDetailActivity extends AppCompatActivity {

    private int quantity = 1;
    private long currentPriceValue = 0;
    private TextView tvQuantity, tvProductName, tvProductPrice, tvProductDesc, tvSpecification, tvToolbarTitle;
    private ImageView ivProduct;
    private Button btnAddToCart;
    private Product currentProduct;
    private ApiService apiService;
    private static final String PREFS_NAME = "CartPrefs";
    private static final String KEY_CART_ID = "cart_id";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_product_detail);

        apiService = RetrofitClient.getClient().create(ApiService.class);

        // Ánh xạ View
        ImageView btnBack = findViewById(R.id.btnBack);
        TextView btnPlus = findViewById(R.id.btnPlus);
        TextView btnMinus = findViewById(R.id.btnMinus);
        tvQuantity = findViewById(R.id.tvQuantity);
        btnAddToCart = findViewById(R.id.btnAddToCart);
        tvToolbarTitle = findViewById(R.id.tvToolbarTitle);
        ivProduct = findViewById(R.id.ivProductDetail);
        tvProductName = findViewById(R.id.tvProductNameDetail);
        tvProductPrice = findViewById(R.id.tvProductPriceDetail);
        tvProductDesc = findViewById(R.id.tvDescriptionDetail);
        tvSpecification = findViewById(R.id.tvSpecificationDetail);

        String productId = getIntent().getStringExtra("PRODUCT_ID");
        if (productId != null) {
            fetchProductDetail(productId);
        }

        btnBack.setOnClickListener(v -> finish());
        btnPlus.setOnClickListener(v -> { quantity++; updateCartButton(); });
        btnMinus.setOnClickListener(v -> { if (quantity > 1) { quantity--; updateCartButton(); } });

        btnAddToCart.setOnClickListener(v -> {
            if (currentProduct != null) {
                checkAndAddToCart();
            }
        });
    }

    private void checkAndAddToCart() {
        SharedPreferences prefs = getSharedPreferences(PREFS_NAME, MODE_PRIVATE);
        String cartId = prefs.getString(KEY_CART_ID, null);

        if (cartId == null) {
            // Nếu chưa có giỏ hàng, gọi API tạo mới
            apiService.createCart().enqueue(new Callback<CartResponse>() {
                @Override
                public void onResponse(Call<CartResponse> call, Response<CartResponse> response) {
                    if (response.isSuccessful() && response.body() != null) {
                        String newCartId = response.body().getCartId();
                        prefs.edit().putString(KEY_CART_ID, newCartId).apply();
                        addToCartOnServer(newCartId);
                    } else {
                        Toast.makeText(ProductDetailActivity.this, "Không thể tạo giỏ hàng", Toast.LENGTH_SHORT).show();
                    }
                }

                @Override
                public void onFailure(Call<CartResponse> call, Throwable t) {
                    Toast.makeText(ProductDetailActivity.this, "Lỗi kết nối khi tạo giỏ", Toast.LENGTH_SHORT).show();
                }
            });
        } else {
            addToCartOnServer(cartId);
        }
    }

    private void addToCartOnServer(String cartId) {
        CartItem item = new CartItem(
                currentProduct.id,
                currentProduct.imageUrl,
                currentProduct.name,
                currentProduct.specification,
                currentPriceValue,
                quantity
        );

        apiService.addProductToCart(cartId, item).enqueue(new Callback<Void>() {
            @Override
            public void onResponse(Call<Void> call, Response<Void> response) {
                if (response.isSuccessful()) {
                    CartManager.getInstance().addToCart(item);
                    Intent intent = new Intent(ProductDetailActivity.this, MainActivity.class);
                    intent.putExtra("show_success", true);
                    intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);
                    startActivity(intent);
                    finish();
                } else if (response.code() == 404) {
                    // Nếu giỏ hàng hết hạn hoặc không tìm thấy trên server, xóa ID cũ và thử lại
                    getSharedPreferences(PREFS_NAME, MODE_PRIVATE).edit().remove(KEY_CART_ID).apply();
                    checkAndAddToCart();
                } else {
                    Toast.makeText(ProductDetailActivity.this, "Lỗi: " + response.code(), Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<Void> call, Throwable t) {
                Toast.makeText(ProductDetailActivity.this, "Lỗi kết nối server", Toast.LENGTH_SHORT).show();
            }
        });
    }

    private void fetchProductDetail(String maSP) {
        apiService.getProductDetail(maSP).enqueue(new Callback<Product>() {
            @Override
            public void onResponse(Call<Product> call, Response<Product> response) {
                if (response.isSuccessful() && response.body() != null) {
                    currentProduct = response.body();
                    displayProductData(currentProduct);
                }
            }
            @Override
            public void onFailure(Call<Product> call, Throwable t) {}
        });
    }

    private void displayProductData(Product product) {
        if (tvProductName != null) tvProductName.setText(product.name);
        if (tvToolbarTitle != null) tvToolbarTitle.setText(product.name);
        if (tvProductDesc != null) tvProductDesc.setText(product.description);
        if (tvSpecification != null) tvSpecification.setText(product.specification);
        
        try {
            String cleanPrice = product.price.replaceAll("[^0-9]", "");
            currentPriceValue = Long.parseLong(cleanPrice);
        } catch (Exception e) {
            currentPriceValue = 0;
        }

        String imgUrl = ImageUrlHelper.resolve(product.imageUrl);

        if (ivProduct != null) {
            Glide.with(this).load(imgUrl).placeholder(R.drawable.thtruemilk).into(ivProduct);
        }
        updateCartButton();
    }

    private void updateCartButton() {
        if (tvQuantity != null) tvQuantity.setText(String.valueOf(quantity));
        long totalPrice = quantity * currentPriceValue;
        DecimalFormat formatter = new DecimalFormat("#,###");
        String formattedPrice = formatter.format(totalPrice).replace(",", ".") + "đ";
        if (btnAddToCart != null) {
            btnAddToCart.setText(formattedPrice + " | Thêm vào giỏ");
        }
    }
}
