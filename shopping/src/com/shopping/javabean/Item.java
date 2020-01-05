/**
 * 商品类
 * 
 */
package com.shopping.javabean;

public class Item {
	private String id;  //商品的id
	private String name; //商品名称
	private String picture; //商品的图片的url
	private float price ;//商品的价格
	private int count; //商品的数量


	public String getId(){
		return id;
	}
	
	public void setId(String id)
	{
		this.id = id;
	}
	
	
	public String getName()
	{
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	
	public String getPicture()
	{
		return picture;
	}
	public void setPicture(String picture) {
		this.picture = picture;
	}
	
	
	public float getPrice()
	{
		return price;
	}
	public void setPrice(float price) {
		this.price = price;
	}
	
	public int getCount()
	{
		return count;
	}
	
	public void setCount(int count)
	{
		this.count = count;
	}
}
