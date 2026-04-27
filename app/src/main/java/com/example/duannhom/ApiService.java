package com.example.duannhom;

import java.util.List;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.DELETE;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.PUT;
import retrofit2.http.Path;

public interface ApiService {

    // API TRANG CHỦ
    @GET("api/san-pham-sua")
    Call<List<Product>> getMilkProducts();

    // API CHI TIẾT SẢN PHẨM
    @GET("api/chi-tiet-san-pham/{maSP}")
    Call<Product> getProductDetail(@Path("maSP") String maSP);

    // API TẠO GIỎ HÀNG MỚI
    @POST("api/gio-hang")
    Call<CartResponse> createCart();

    // API LẤY CHI TIẾT GIỎ HÀNG
    @GET("api/gio-hang/{ma_gio_hang}")
    Call<List<CartItem>> getCartDetails(@Path("ma_gio_hang") String maGioHang);

    // API THÊM SẢN PHẨM VÀO GIỎ
    @POST("api/gio-hang/{ma_gio_hang}/them-san-pham")
    Call<Void> addProductToCart(@Path("ma_gio_hang") String maGioHang, @Body CartItem item);

    // API CẬP NHẬT SỐ LƯỢNG
    @PUT("api/gio-hang/{ma_gio_hang}/chi-tiet/{chi_tiet_id}")
    Call<Void> updateCartItemQuantity(@Path("ma_gio_hang") String maGioHang, @Path("chi_tiet_id") String chiTietId, @Body CartItem item);

    // API XÓA 1 SẢN PHẨM
    @DELETE("api/gio-hang/{ma_gio_hang}/chi-tiet/{chi_tiet_id}")
    Call<Void> deleteCartItem(@Path("ma_gio_hang") String maGioHang, @Path("chi_tiet_id") String chiTietId);

    // API XÓA TẤT CẢ
    @DELETE("api/gio-hang/{ma_gio_hang}/xoa-tat-ca")
    Call<Void> clearCart(@Path("ma_gio_hang") String maGioHang);

    // API DANH MỤC
    @GET("api/danh-muc-sua")
    Call<List<Category>> getCategories();

    // API CHI TIẾT DANH MỤC
    @GET("api/chi-tiet-danh-muc/{ma_loai}")
    Call<Category> getCategoryDetail(@Path("ma_loai") String maLoai);

    // API BANNER
    @GET("api/banners")
    Call<List<Banner>> getBanners();

    // API QUẢNG CÁO
    @GET("api/banner-quang-cao")
    Call<List<Banner>> getPromoBanners();
}
