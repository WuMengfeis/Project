/**
 * 用来移除数据库中的商品
 */
package com.shopping.servlet;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.swing.JOptionPane;

import com.shopping.dao.cartDao;

/**
 * Servlet implementation class RemoveServlet
 */
@WebServlet("/RemoveServlet")
public class RemoveServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public RemoveServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		String clear= request.getParameter("clear");
		//这个是购物车页面的清空购物车的请求
		if(clear!=null)
		{
			cartDao cartdao = new cartDao();
			boolean b =cartdao.clearDB();
			if(b==true)
			{
				JOptionPane.showMessageDialog(null, "成功清除购物车");
			}else {
				JOptionPane.showMessageDialog(null, "清除购物车失败");
			}
		}
		
		
		String iId = request.getParameter("iId");
		String uId = (String)request.getSession().getAttribute("uId");
		if(iId!=null) {
			//然后根据iId把relation数据库中的数据全部清空掉
			cartDao cartdao = new cartDao();
			boolean  b=cartdao.removeItem(uId,iId);
			if(b==true)
			{
				JOptionPane.showMessageDialog(null, "移除成功");
			}else
			{
				JOptionPane.showMessageDialog(null,"移除失败");
			}
		}
		
		//返回购物车页面
		response.sendRedirect("/shopping/cartShopping.jsp");
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
