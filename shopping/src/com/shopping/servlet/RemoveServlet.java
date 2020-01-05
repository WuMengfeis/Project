/**
 * �����Ƴ����ݿ��е���Ʒ
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
		//����ǹ��ﳵҳ�����չ��ﳵ������
		if(clear!=null)
		{
			cartDao cartdao = new cartDao();
			boolean b =cartdao.clearDB();
			if(b==true)
			{
				JOptionPane.showMessageDialog(null, "�ɹ�������ﳵ");
			}else {
				JOptionPane.showMessageDialog(null, "������ﳵʧ��");
			}
		}
		
		
		String iId = request.getParameter("iId");
		String uId = (String)request.getSession().getAttribute("uId");
		if(iId!=null) {
			//Ȼ�����iId��relation���ݿ��е�����ȫ����յ�
			cartDao cartdao = new cartDao();
			boolean  b=cartdao.removeItem(uId,iId);
			if(b==true)
			{
				JOptionPane.showMessageDialog(null, "�Ƴ��ɹ�");
			}else
			{
				JOptionPane.showMessageDialog(null,"�Ƴ�ʧ��");
			}
		}
		
		//���ع��ﳵҳ��
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
