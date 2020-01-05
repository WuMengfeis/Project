
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
		//用户登录成功返回3
		//用户验证码正确，密码错误返回2
		//用户验证码错误返回1
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
	
	//写一个专门判断用户登陆的函数
	public int checkUser(HttpServletRequest request, HttpServletResponse response)
	{
		
		//b来判断返回的信息类型
		//对登录进行验证
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
					//验证码错误
					return 1;
				}else if(!rs.getString(2).equals(pwd))
				{
					//密码不正确
					return 2;
				}else if(rs.getString(2).equals(pwd)&&yzm.equals(sessionYzm))
				{
					//验证码和密码都正确
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
