package com.example.duannhom;

import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import com.bumptech.glide.Glide;
import java.util.List;

public class ProductAdapter extends RecyclerView.Adapter<ProductAdapter.ViewHolder> {
    private List<Product> list;

    public ProductAdapter(List<Product> list) {
        this.list = list;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_product, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        Product product = list.get(position);

        holder.tvName.setText(product.name);
        holder.tvPrice.setText((product.price != null ? product.price : "0") + "đ");
        holder.tvDiscount.setText("-" + (product.discount != null ? product.discount : "0") + "%");

        // Cập nhật thông tin quy cách động từ API thay vì để cứng "180 ml, Thùng 48 hộp"
        if (holder.tvInfo != null) {
            holder.tvInfo.setText(product.specification != null ? product.specification : "");
        }

        String imgUrl = ImageUrlHelper.resolve(product.imageUrl);

        Glide.with(holder.itemView.getContext())
                .load(imgUrl)
                .placeholder(R.drawable.ngu_coc)
                .into(holder.imgProduct);

        View.OnClickListener clickListener = v -> {
            Intent intent = new Intent(v.getContext(), ProductDetailActivity.class);
            intent.putExtra("PRODUCT_ID", product.id);
            v.getContext().startActivity(intent);
        };

        holder.itemView.setOnClickListener(clickListener);
        if (holder.btnSelect != null) {
            holder.btnSelect.setOnClickListener(clickListener);
        }
    }

    @Override
    public int getItemCount() {
        return list != null ? list.size() : 0;
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {
        ImageView imgProduct;
        TextView tvName, tvPrice, tvDiscount, tvInfo;
        Button btnSelect;
        
        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            imgProduct = itemView.findViewById(R.id.imgProduct);
            tvName = itemView.findViewById(R.id.tvName);
            tvPrice = itemView.findViewById(R.id.tvPrice);
            tvDiscount = itemView.findViewById(R.id.tvDiscount);
            tvInfo = itemView.findViewById(R.id.tvInfo); // Ánh xạ TextView quy cách
            btnSelect = itemView.findViewById(R.id.btnSelect);
        }
    }
}
