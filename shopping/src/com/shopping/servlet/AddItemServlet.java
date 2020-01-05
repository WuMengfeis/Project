/**
 /* 添加商品到购物车
 */
package com.shopping.servlet;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.swing.JOptionPane;

import com.shopping.dao.*;
import com.shopping.javabean.*;

/**
 * Servlet implementation class AddItemServlet
 */
public class AddItemServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public AddItemServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doPost(request,response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		int num = Integer.parseInt(request.getParameter("num"));
		String iId = request.getParameter("id");
		String uId = request.getParameter("uId");
		
		//然后把指定的uId的iId的数量设为num
		//根据id在数据库中查询哪个item
		
		itemDao itemdao= new itemDao();
		Item i = itemdao.getItemById(iId);
		cartDao cartDao= new cartDao();
		boolean b= cartDao.addToDB(uId, i.getId(),num+"");
		
		if(b==true)
		{
//			JOptionPane.showMessageDialog(null, "添加成功");
		}else {
//			JOptionPane.showMessageDialog(null, "添加失败");
		}
		
		
		
		//添加历史记录
		HistoryModel hm = new HistoryModel();
		hm.addToList(iId);
		

		response.sendRedirect("/shopping/main.jsp?id="+request.getSession().getAttribute("uId"));
		
		
	}

}
