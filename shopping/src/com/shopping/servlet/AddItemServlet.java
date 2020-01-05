/**
 /* �����Ʒ�����ﳵ
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
		
		//Ȼ���ָ����uId��iId��������Ϊnum
		//����id�����ݿ��в�ѯ�ĸ�item
		
		itemDao itemdao= new itemDao();
		Item i = itemdao.getItemById(iId);
		cartDao cartDao= new cartDao();
		boolean b= cartDao.addToDB(uId, i.getId(),num+"");
		
		if(b==true)
		{
//			JOptionPane.showMessageDialog(null, "��ӳɹ�");
		}else {
//			JOptionPane.showMessageDialog(null, "���ʧ��");
		}
		
		
		
		//�����ʷ��¼
		HistoryModel hm = new HistoryModel();
		hm.addToList(iId);
		

		response.sendRedirect("/shopping/main.jsp?id="+request.getSession().getAttribute("uId"));
		
		
	}

}
