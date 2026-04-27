package com.example.duannhom;

import android.app.AlertDialog;
import android.content.Context;
import android.content.SharedPreferences;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import com.bumptech.glide.Glide;
import java.text.DecimalFormat;
import java.util.List;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class CartAdapter extends RecyclerView.Adapter<CartAdapter.ViewHolder> {

    private List<CartItem> list;
    private OnCartChangeListener listener;
    private Context context;
    private String cartId;

    public interface OnCartChangeListener {
        void onTotalChanged(long totalPrice);
    }

    public CartAdapter(Context context, List<CartItem> list, OnCartChangeListener listener) {
        this.context = context;
        this.list = list;
        this.listener = listener;
        
        // Lấy cart_id thật từ SharedPreferences
        SharedPreferences prefs = context.getSharedPreferences("CartPrefs", Context.MODE_PRIVATE);
        this.cartId = prefs.getString("cart_id", null);
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_cart, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        CartItem item = list.get(position);
        
        String imgUrl = item.imageUrl;
        if (imgUrl != null && !imgUrl.startsWith("http")) {
            imgUrl = "http://10.0.3.2:8000" + imgUrl;
        }

        Glide.with(holder.itemView.getContext())
                .load(imgUrl)
                .placeholder(R.drawable.thtruemilk)
                .into(holder.ivProduct);

        holder.tvName.setText(item.name);
        holder.tvInfo.setText(item.info);
        
        DecimalFormat formatter = new DecimalFormat("#,###");
        holder.tvPrice.setText(formatter.format(item.price).replace(",", ".") + "đ");
        holder.tvQuantity.setText(String.valueOf(item.quantity));

        holder.btnPlus.setOnClickListener(v -> {
            int oldQty = item.quantity;
            item.quantity++;
            notifyItemChanged(position);
            updateTotal();
            syncQuantityWithServer(item, oldQty, position);
        });

        holder.btnMinus.setOnClickListener(v -> {
            if (item.quantity > 1) {
                int oldQty = item.quantity;
                item.quantity--;
                notifyItemChanged(position);
                updateTotal();
                syncQuantityWithServer(item, oldQty, position);
            } else {
                showRemoveDialog(holder.itemView, position);
            }
        });
    }

    private void syncQuantityWithServer(CartItem item, int oldQty, int position) {
        if (cartId == null) return;
        
        ApiService apiService = RetrofitClient.getClient().create(ApiService.class);
        apiService.updateCartItemQuantity(cartId, item.productId, item).enqueue(new Callback<Void>() {
            @Override
            public void onResponse(Call<Void> call, Response<Void> response) {
                if (!response.isSuccessful()) {
                    item.quantity = oldQty;
                    notifyItemChanged(position);
                    updateTotal();
                    Toast.makeText(context, "Lỗi cập nhật server", Toast.LENGTH_SHORT).show();
                }
            }
            @Override
            public void onFailure(Call<Void> call, Throwable t) {
                item.quantity = oldQty;
                notifyItemChanged(position);
                updateTotal();
            }
        });
    }

    private void showRemoveDialog(View view, int position) {
        View dialogView = LayoutInflater.from(view.getContext()).inflate(R.layout.dialog_remove_item, null);
        AlertDialog dialog = new AlertDialog.Builder(view.getContext(), R.style.CustomDialogTheme)
                .setView(dialogView)
                .create();

        dialogView.findViewById(R.id.btnCancel).setOnClickListener(v -> dialog.dismiss());
        dialogView.findViewById(R.id.btnConfirm).setOnClickListener(v -> {
            if (cartId != null) {
                CartItem itemToRemove = list.get(position);
                ApiService apiService = RetrofitClient.getClient().create(ApiService.class);
                apiService.deleteCartItem(cartId, itemToRemove.productId).enqueue(new Callback<Void>() {
                    @Override
                    public void onResponse(Call<Void> call, Response<Void> response) {
                        if (response.isSuccessful()) {
                            list.remove(position);
                            notifyItemRemoved(position);
                            notifyItemRangeChanged(position, list.size());
                            updateTotal();
                        }
                    }
                    @Override
                    public void onFailure(Call<Void> call, Throwable t) {
                        Toast.makeText(view.getContext(), "Không thể xóa sản phẩm", Toast.LENGTH_SHORT).show();
                    }
                });
            }
            dialog.dismiss();
        });

        dialog.show();
    }

    private void updateTotal() {
        long total = 0;
        for (CartItem item : list) {
            total += item.price * item.quantity;
        }
        if (listener != null) {
            listener.onTotalChanged(total);
        }
    }

    @Override
    public int getItemCount() {
        return list.size();
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {
        ImageView ivProduct;
        TextView tvName, tvInfo, tvPrice, tvQuantity, btnPlus, btnMinus;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            ivProduct = itemView.findViewById(R.id.ivProductCart);
            tvName = itemView.findViewById(R.id.tvNameCart);
            tvInfo = itemView.findViewById(R.id.tvInfoCart);
            tvPrice = itemView.findViewById(R.id.tvPriceCart);
            tvQuantity = itemView.findViewById(R.id.tvQuantityCart);
            btnPlus = itemView.findViewById(R.id.btnPlusCart);
            btnMinus = itemView.findViewById(R.id.btnMinusCart);
        }
    }
}
