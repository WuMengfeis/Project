/**
 * ��Ʒ��
 * 
 */
package com.shopping.javabean;

public class Item {
	private String id;  //��Ʒ��id
	private String name; //��Ʒ����
	private String picture; //��Ʒ��ͼƬ��url
	private float price ;//��Ʒ�ļ۸�
	private int count; //��Ʒ������


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
