/**
 * �������ݿ�õ�����
 * ȫ������Ʒ����Ʒ����Ϣ
 */
package com.shopping.dao;

import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.util.*;
import com.shopping.javabean.*;

public class itemDao {
	//items ���������ݿ������е���Ʒ
	public  List<Item> items  = new ArrayList<Item>();
	private ResultSet rs ;
	
	

	
	//����id����һ��Item ����
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
