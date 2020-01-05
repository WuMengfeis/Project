/**
 * 写的不健全，css和img，js等都要再从服务器端再次申请
 */

package com.shopping.filter;

import java.io.IOException;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.*;
import javax.swing.JOptionPane;

public class CartFilter implements Filter{

	FilterConfig config;
	@Override
	public void destroy() {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void doFilter(ServletRequest arg0, ServletResponse arg1, FilterChain arg2)
			throws IOException, ServletException {
		// TODO Auto-generated method stub
		
		
		HttpServletRequest request = (HttpServletRequest)arg0;
		HttpServletResponse response = (HttpServletResponse)arg1;
		HttpSession session = request.getSession();
		
		request.setCharacterEncoding("UTF-8");
		response.setCharacterEncoding("UTF-8");
		
		String path =request.getRequestURI();
		
		String uId = (String)session.getAttribute("uId");
		
		if(path.indexOf("/input.jsp")>-1) {
			//登录界面不过滤
			//交给下一个过滤器
			arg2.doFilter(arg0, arg1);
			return ;
		}
		
		
		//indexOf(str)返回一个次出现str的位置，如果不存在就返回-1
		if(path.indexOf("/index.jsp")>-1) {
			arg2.doFilter(arg0, arg1);
			return ;
		}
		
		if(path.indexOf("/register.jsp")>-1) {
			arg2.doFilter(arg0, arg1);
			return ;
		}
		
		
		if(uId!=null) {
			//已经登录
			arg2.doFilter(arg0,arg1);
		}else {
			response.sendRedirect("input.jsp");
		}
	
		
	
		
		
		
	}

	@Override
	public void init(FilterConfig arg0) throws ServletException {
		// TODO Auto-generated method stub
		
	}

}
