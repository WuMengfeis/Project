/**
 * �Թ��ﳵ�е�ĳ����Ʒ������һ��һ
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
		//���cartshopping�Ӽ�button��ֵ
		/*String iId = request.getParameter("iId");
		String uId = (String)request.getSession().getAttribute("uId");
		
		String  sub = request.getParameter("sub");
		String add = request.getParameter("add");
		cartDao cartdao = new cartDao();
		int num = cartdao.itOfNum(uId,iId);
		
		if(sub!=null)
		{
			//��uId��iId��Ӧ��num-1
			//���numΪ0�Ļ����Ƴ������Ʒ
			if(num>1) {
				cartdao.setNumOfIt(uId, iId, (num-1)+"");
				
			}else {
				//�Ƴ������Ʒ
				cartdao.removeItem(uId, iId);
			}
			
		}
		
		if(add!=null)
		{
			//num+1
			cartdao.setNumOfIt(uId, iId, (num+1)+"");
		}
		
		//����cartShopping
		response.sendRedirect("/shopping/cartShopping.jsp");
		*/

		
		
		//����ajax��ʵ��
		
		String iId= request.getParameter("iId");
		String uId = (String) request.getSession().getAttribute("uId");
		String op = request.getParameter("op");
		System.out.println(op+"   "+iId+"  "+uId);
		
		response.setContentType("text/xml");    //Ҳ������html   
		response.setCharacterEncoding("utf-8");
		response.setHeader("Cache-Control", "no-store");   //�����û���
		
		cartDao cartdao = new cartDao();
		int num = cartdao.itOfNum(uId, iId);
		if(op.equals("sub"))
		{
			//��uId��iId������һ
			
			if(num>1) {
				cartdao.setNumOfIt(uId, iId, (num-1)+"");
				response.getWriter().write("<msg>"+(num-1)+"</msg>");
				
			}else {
				//�Ƴ������Ʒ
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
