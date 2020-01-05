
package com.shopping.servlet;

import java.io.IOException;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.shopping.dao.*;


/**
 * Servlet implementation class LoginServlet
 */
@WebServlet("/LoginServlet")
public class LoginServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
    private ResultSet rs;   
	
	
    /**
     * @see HttpServlet#HttpServlet()
     */
    public LoginServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
//		String id = request.getParameter("id");
//		String pwd = request.getParameter("pwd");
//		System.out.println(id+pwd);
		doPost(request,response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		
		String id = request.getParameter("id");
		//�û���¼�ɹ�����3
		//�û���֤����ȷ��������󷵻�2
		//�û���֤����󷵻�1
		int i = checkUser(request, response);
		switch(i)
		{
		case 1:
			response.sendRedirect("/shopping/input.jsp?message=1");
			break;
		case 2:
			response.sendRedirect("/shopping/input.jsp?message=2");
			break;
		case 3:
			response.sendRedirect("/shopping/main.jsp?id="+id+"");
			break;
		}
			
		
	
		
	}
	
	//дһ��ר���ж��û���½�ĺ���
	public int checkUser(HttpServletRequest request, HttpServletResponse response)
	{
		
		//b���жϷ��ص���Ϣ����
		//�Ե�¼������֤
		String id = request.getParameter("id");
		String pwd = request.getParameter("pwd");
		String yzm = request.getParameter("yzm");
		String sessionYzm = (String)request.getSession().getAttribute("randomString");
		
		
		String sql = "select * from login where id =?";
		String [] param = {id};
		sqlHelper sh =new sqlHelper();
		rs = sh.query(sql, param);

		try {
			
			if(rs.next())
			{
				
				if(!yzm.equals(sessionYzm))
				{
					//��֤�����
					return 1;
				}else if(!rs.getString(2).equals(pwd))
				{
					//���벻��ȷ
					return 2;
				}else if(rs.getString(2).equals(pwd)&&yzm.equals(sessionYzm))
				{
					//��֤������붼��ȷ
					return 3;
				}
				
			   
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}finally {
		}
		
		return -1;
	}


}
