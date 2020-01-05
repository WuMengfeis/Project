/**
 * 历史记录的servlet
 */
package com.shopping.servlet;

import com.shopping.dao.*;
import com.shopping.javabean.*;
import java.io.IOException;
import java.util.Iterator;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.swing.JOptionPane;

/**
 * Servlet implementation class HistotyServlet
 */
@WebServlet("/HistotyServlet")
public class HistoryServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public HistoryServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		String clear = request.getParameter("clear");
		if(clear!=null)
		{
			JOptionPane.showMessageDialog(null,"清除历史记录成功");
			HistoryModel.historyList.clear();
		}
		
		
		String iNo = request.getParameter("iNo");
		if(iNo!=null)
		{
			//删除这个历史记录
			JOptionPane.showMessageDialog(null, "删除记录成功");
			HistoryModel.historyList.remove(Integer.parseInt(iNo));
			
		
		}
		
		//返回购物车页面
		response.sendRedirect("/shopping/history.jsp");
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
