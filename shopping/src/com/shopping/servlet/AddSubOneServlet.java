/**
 * 对购物车中的某件商品数量加一减一
 */
package com.shopping.servlet;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.shopping.dao.cartDao;

/**
 * Servlet implementation class AddSubOneServlet
 */
@WebServlet("/AddSubOneServlet")
public class AddSubOneServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public AddSubOneServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		//获得cartshopping加减button的值
		/*String iId = request.getParameter("iId");
		String uId = (String)request.getSession().getAttribute("uId");
		
		String  sub = request.getParameter("sub");
		String add = request.getParameter("add");
		cartDao cartdao = new cartDao();
		int num = cartdao.itOfNum(uId,iId);
		
		if(sub!=null)
		{
			//将uId和iId对应的num-1
			//如果num为0的话就移除这个商品
			if(num>1) {
				cartdao.setNumOfIt(uId, iId, (num-1)+"");
				
			}else {
				//移除这个商品
				cartdao.removeItem(uId, iId);
			}
			
		}
		
		if(add!=null)
		{
			//num+1
			cartdao.setNumOfIt(uId, iId, (num+1)+"");
		}
		
		//返回cartShopping
		response.sendRedirect("/shopping/cartShopping.jsp");
		*/

		
		
		//利用ajax来实现
		
		String iId= request.getParameter("iId");
		String uId = (String) request.getSession().getAttribute("uId");
		String op = request.getParameter("op");
		System.out.println(op+"   "+iId+"  "+uId);
		
		response.setContentType("text/xml");    //也可以是html   
		response.setCharacterEncoding("utf-8");
		response.setHeader("Cache-Control", "no-store");   //不设置缓存
		
		cartDao cartdao = new cartDao();
		int num = cartdao.itOfNum(uId, iId);
		if(op.equals("sub"))
		{
			//把uId和iId的数减一
			
			if(num>1) {
				cartdao.setNumOfIt(uId, iId, (num-1)+"");
				response.getWriter().write("<msg>"+(num-1)+"</msg>");
				
			}else {
				//移除这个商品
				cartdao.removeItem(uId, iId);
				response.getWriter().write("<msg>null</msg>");
			}
		}
		
		if(op.equals("add"))
		{
			cartdao.setNumOfIt(uId, iId, (num+1)+"");
			response.getWriter().write("<msg>"+(num+1)+"</msg>");
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
