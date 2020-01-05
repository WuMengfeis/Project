/**
 * 连接数据库得到数据
 * 全部的商品和商品的信息
 */
package com.shopping.dao;

import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.util.*;
import com.shopping.javabean.*;

public class itemDao {
	//items 保存了数据库中所有的商品
	public  List<Item> items  = new ArrayList<Item>();
	private ResultSet rs ;
	
	

	
	//根据id返回一个Item 对象
	public  Item getItemById(String id)
	{
		Item it = new Item();
		String sql = "select * from cart where id = ?";
		String [] param = {id};
		sqlHelper sh= new sqlHelper();
		rs = sh.query(sql, param);
		
		try {
			while(rs.next()) {
			    it.setId( rs.getString(1));
			    it.setName(rs.getString(2));
			    it.setPicture(rs.getString(3));
			    it.setPrice(rs.getFloat(4));
			    
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return it;
	}
	
	
	public itemDao()
	{
		String sql = "select * from cart where 1=?";
		String [] param = {"1"};
		sqlHelper sh = new sqlHelper();
	    rs = sh.query(sql, param);
	   
	    
	    try {

			while(rs.next())
			{
			    Item it = new Item();
			    it.setId( rs.getString(1));
			    it.setName(rs.getString(2));
			    it.setPicture(rs.getString(3));
			    it.setPrice(rs.getFloat(4));
			    
			    items.add(it);
			    
			}
			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	

}
