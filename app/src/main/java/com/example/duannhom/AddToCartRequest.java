package com.example.duannhom;

public class AddToCartRequest {
    public String ma_sua;
    public Integer lua_chon_mua_id;
    public int so_luong;

    public AddToCartRequest(String ma_sua, Integer lua_chon_mua_id, int so_luong) {
        this.ma_sua = ma_sua;
        this.lua_chon_mua_id = lua_chon_mua_id;
        this.so_luong = so_luong;
    }
}
