package com.shopping.servlet;

import java.io.IOException;
import java.sql.ResultSet;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.shopping.dao.sqlHelper;

/**
 * Servlet implementation class Ajax
 */
@WebServlet("/Ajax")
public class Ajax extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Ajax() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		  response.setContentType("text/xml");    //也可以是html   
		  response.setCharacterEncoding("utf-8");
		  response.setHeader("Cache-Control", "no-store");   //不设置缓存
		  String id = request.getParameter("id");	
		  try{	
				  sqlHelper sh = new sqlHelper();
				  String sql = "select * from login where id = ?";
				  String[] param = {id};
				  ResultSet rs = sh.query(sql, param);
				  if(rs.next()){	
					  response.getWriter().write("<msg>true</msg>");	//写会
					  
				  }else {
					  response.getWriter().write("<msg>false</msg>");
				  }
						  
				   	
			  }catch(Exception e){	
				  e.printStackTrace();	
			  }	 


	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
