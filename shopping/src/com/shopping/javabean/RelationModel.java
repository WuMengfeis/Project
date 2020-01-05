/**
 * 这是一个抽象的关系的模型类
 * 
 */
package com.shopping.javabean;

public class RelationModel {
	private String uId;
	private String iId;
	private int num;
	public String getuId() {
		return uId;
	}
	public void setuId(String uId) {
		this.uId = uId;
	}
	public String getiId() {
		return iId;
	}
	public void setiId(String iId) {
		this.iId = iId;
	}
	public int getNum() {
		return num;
	}
	public void setNum(int num) {
		this.num = num;
	}
	
}
