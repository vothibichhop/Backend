package com.example.duannhom;

public class UpdateCartItemRequest {
    public Integer so_luong;
    public Integer lua_chon_mua_id;

    public UpdateCartItemRequest(Integer so_luong, Integer lua_chon_mua_id) {
        this.so_luong = so_luong;
        this.lua_chon_mua_id = lua_chon_mua_id;
    }
}
