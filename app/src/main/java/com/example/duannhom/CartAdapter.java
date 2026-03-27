package com.example.duannhom;

import android.app.AlertDialog;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import java.text.DecimalFormat;
import java.util.List;

public class CartAdapter extends RecyclerView.Adapter<CartAdapter.ViewHolder> {

    private List<CartItem> list;
    private OnCartChangeListener listener;

    public interface OnCartChangeListener {
        void onTotalChanged(long totalPrice);
    }

    public CartAdapter(List<CartItem> list, OnCartChangeListener listener) {
        this.list = list;
        this.listener = listener;
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
        holder.ivProduct.setImageResource(item.imageRes);
        holder.tvName.setText(item.name);
        holder.tvInfo.setText(item.info);
        
        DecimalFormat formatter = new DecimalFormat("#,###");
        holder.tvPrice.setText(formatter.format(item.price).replace(",", ".") + "đ");
        holder.tvQuantity.setText(String.valueOf(item.quantity));

        holder.btnPlus.setOnClickListener(v -> {
            item.quantity++;
            notifyItemChanged(position);
            updateTotal();
        });

        holder.btnMinus.setOnClickListener(v -> {
            if (item.quantity > 1) {
                item.quantity--;
                notifyItemChanged(position);
                updateTotal();
            } else {
                showRemoveDialog(holder.itemView, position);
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
            list.remove(position);
            notifyItemRemoved(position);
            notifyItemRangeChanged(position, list.size());
            updateTotal();
            dialog.dismiss();
        });

        dialog.show();
        if (dialog.getWindow() != null) {
            dialog.getWindow().setBackgroundDrawableResource(android.R.color.transparent);
        }
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