package com.example.duannhom;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.DELETE;
import retrofit2.http.GET;
import retrofit2.http.PATCH;
import retrofit2.http.POST;
import retrofit2.http.Path;

public interface ApiService {

    @GET("api/san-pham-sua")
    Call<List<Product>> getMilkProducts();

    @GET("api/chi-tiet-san-pham/{maSP}")
    Call<Product> getProductDetail(@Path("maSP") String maSP);

    @POST("api/gio-hang")
    Call<CartResponse> createCart();

    @GET("api/gio-hang/{ma_gio_hang}")
    Call<CartResponse> getCartDetails(@Path("ma_gio_hang") String maGioHang);

    @POST("api/gio-hang/{ma_gio_hang}/them-san-pham")
    Call<CartResponse> addProductToCart(
            @Path("ma_gio_hang") String maGioHang,
            @Body AddToCartRequest request
    );

    @PATCH("api/gio-hang/{ma_gio_hang}/chi-tiet/{chi_tiet_id}")
    Call<CartResponse> updateCartItemQuantity(
            @Path("ma_gio_hang") String maGioHang,
            @Path("chi_tiet_id") int chiTietId,
            @Body UpdateCartItemRequest request
    );

    @DELETE("api/gio-hang/{ma_gio_hang}/chi-tiet/{chi_tiet_id}")
    Call<CartResponse> deleteCartItem(
            @Path("ma_gio_hang") String maGioHang,
            @Path("chi_tiet_id") int chiTietId
    );

    @DELETE("api/gio-hang/{ma_gio_hang}/xoa-tat-ca")
    Call<CartResponse> clearCart(@Path("ma_gio_hang") String maGioHang);

    @GET("api/danh-muc")
    Call<List<Category>> getCategories();

    @GET("api/chi-tiet-danh-muc/{ma_danh_muc}")
    Call<Category> getCategoryDetail(@Path("ma_danh_muc") String maDanhMuc);

    @GET("api/banner")
    Call<List<Banner>> getBanners();

    @GET("api/banner-quang-cao")
    Call<List<Banner>> getPromoBanners();

    @GET("api/lich-su-don-hang")
    Call<List<OrderSummary>> getOrderHistory();
}
