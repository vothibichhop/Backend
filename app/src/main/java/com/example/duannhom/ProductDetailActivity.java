package com.example.duannhom;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
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
    private TextView tvQuantity;
    private TextView tvProductName;
    private TextView tvProductPrice;
    private TextView tvProductDesc;
    private TextView tvSpecification;
    private TextView tvToolbarTitle;
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
        btnPlus.setOnClickListener(v -> {
            quantity++;
            updateCartButton();
        });
        btnMinus.setOnClickListener(v -> {
            if (quantity > 1) {
                quantity--;
                updateCartButton();
            }
        });

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
            apiService.createCart().enqueue(new Callback<CartResponse>() {
                @Override
                public void onResponse(Call<CartResponse> call, Response<CartResponse> response) {
                    if (response.isSuccessful() && response.body() != null) {
                        String newCartId = response.body().getCartId();
                        prefs.edit().putString(KEY_CART_ID, newCartId).apply();
                        addToCartOnServer(newCartId);
                    } else {
                        Toast.makeText(ProductDetailActivity.this, "Khong the tao gio hang", Toast.LENGTH_SHORT).show();
                    }
                }

                @Override
                public void onFailure(Call<CartResponse> call, Throwable t) {
                    Toast.makeText(ProductDetailActivity.this, "Loi ket noi khi tao gio", Toast.LENGTH_SHORT).show();
                }
            });
        } else {
            addToCartOnServer(cartId);
        }
    }

    private void addToCartOnServer(String cartId) {
        AddToCartRequest request = new AddToCartRequest(
                currentProduct.id,
                resolveSelectedOptionId(),
                quantity
        );

        apiService.addProductToCart(cartId, request).enqueue(new Callback<CartResponse>() {
            @Override
            public void onResponse(Call<CartResponse> call, Response<CartResponse> response) {
                if (response.isSuccessful() && response.body() != null) {
                    CartManager.getInstance().syncCart(response.body());
                    Intent intent = new Intent(ProductDetailActivity.this, MainActivity.class);
                    intent.putExtra("show_success", true);
                    intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);
                    startActivity(intent);
                    finish();
                } else if (response.code() == 404) {
                    getSharedPreferences(PREFS_NAME, MODE_PRIVATE).edit().remove(KEY_CART_ID).apply();
                    checkAndAddToCart();
                } else {
                    Toast.makeText(ProductDetailActivity.this, "Loi: " + response.code(), Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<CartResponse> call, Throwable t) {
                Toast.makeText(ProductDetailActivity.this, "Loi ket noi server", Toast.LENGTH_SHORT).show();
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
            public void onFailure(Call<Product> call, Throwable t) {
            }
        });
    }

    private void displayProductData(Product product) {
        if (tvProductName != null) {
            tvProductName.setText(product.name);
        }
        if (tvToolbarTitle != null) {
            tvToolbarTitle.setText(product.name);
        }
        if (tvProductDesc != null) {
            tvProductDesc.setText(product.description);
        }
        if (tvSpecification != null) {
            tvSpecification.setText(resolveDisplaySpecification(product));
        }

        currentPriceValue = resolveCurrentPrice(product);
        if (tvProductPrice != null) {
            DecimalFormat formatter = new DecimalFormat("#,###");
            tvProductPrice.setText(formatter.format(currentPriceValue).replace(",", ".") + "\u0111");
        }

        String imgUrl = product.imageUrl;
        if (imgUrl != null && !imgUrl.startsWith("http")) {
            imgUrl = "http://10.0.3.2:8000" + imgUrl;
        }

        if (ivProduct != null) {
            Glide.with(this).load(imgUrl).placeholder(R.drawable.thtruemilk).into(ivProduct);
        }
        updateCartButton();
    }

    private Integer resolveSelectedOptionId() {
        if (currentProduct == null || currentProduct.options == null || currentProduct.options.isEmpty()) {
            return null;
        }

        for (Product.ProductOption option : currentProduct.options) {
            if (option != null && option.isDefault && option.id != null) {
                return option.id;
            }
        }

        for (Product.ProductOption option : currentProduct.options) {
            if (option != null && option.id != null) {
                return option.id;
            }
        }

        return null;
    }

    private long resolveCurrentPrice(Product product) {
        if (product != null && product.options != null) {
            for (Product.ProductOption option : product.options) {
                if (option != null && option.isDefault) {
                    return option.priceValue;
                }
            }
            for (Product.ProductOption option : product.options) {
                if (option != null && option.priceValue > 0) {
                    return option.priceValue;
                }
            }
        }

        try {
            String cleanPrice = product.price.replaceAll("[^0-9]", "");
            return Long.parseLong(cleanPrice);
        } catch (Exception e) {
            return 0;
        }
    }

    private String resolveDisplaySpecification(Product product) {
        if (product != null && product.options != null) {
            for (Product.ProductOption option : product.options) {
                if (option != null && option.isDefault && option.optionName != null) {
                    return option.optionName;
                }
            }
            for (Product.ProductOption option : product.options) {
                if (option != null && option.optionName != null) {
                    return option.optionName;
                }
            }
        }
        return product != null ? product.specification : "";
    }

    private void updateCartButton() {
        if (tvQuantity != null) {
            tvQuantity.setText(String.valueOf(quantity));
        }
        long totalPrice = quantity * currentPriceValue;
        DecimalFormat formatter = new DecimalFormat("#,###");
        String formattedPrice = formatter.format(totalPrice).replace(",", ".") + "\u0111";
        if (btnAddToCart != null) {
            btnAddToCart.setText(formattedPrice + " | Them vao gio");
        }
    }
}
