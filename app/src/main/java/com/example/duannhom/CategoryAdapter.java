package com.example.duannhom;

import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import java.util.List;

public class CategoryAdapter extends RecyclerView.Adapter<CategoryAdapter.ViewHolder> {

    private List<Category> list;

    public CategoryAdapter(List<Category> list) {
        this.list = list;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_category, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        Category category = list.get(position);

        // Hiển thị dữ liệu (Sử dụng trực tiếp field name và count)
        holder.tvName.setText(category.name);
        holder.tvCount.setText(String.valueOf(category.count));

        // Xử lý click để chuyển sang màn hình chi tiết
        holder.itemView.setOnClickListener(v -> {
            // Lấy context trực tiếp từ view click
            Context context = v.getContext();

            Intent intent = new Intent(context, CategoryDetailActivity.class);

            // Gửi mã danh mục sang màn hình sau
            // Lưu ý: Dùng field ma_danh_muc (vì class Category của bạn đang dùng public field)
            intent.putExtra("MA_DANH_MUC", category.ma_danh_muc);

            context.startActivity(intent);
        });
    }

    @Override
    public int getItemCount() {
        return list.size();
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {
        TextView tvName, tvCount;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            tvName = itemView.findViewById(R.id.tvCategoryName);
            tvCount = itemView.findViewById(R.id.tvCategoryCount);
        }
    }
}