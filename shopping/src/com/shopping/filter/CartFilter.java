/**
 * д�Ĳ���ȫ��css��img��js�ȶ�Ҫ�ٴӷ��������ٴ�����
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
			//��¼���治����
			//������һ��������
			arg2.doFilter(arg0, arg1);
			return ;
		}
		
		
		//indexOf(str)����һ���γ���str��λ�ã���������ھͷ���-1
		if(path.indexOf("/index.jsp")>-1) {
			arg2.doFilter(arg0, arg1);
			return ;
		}
		
		if(path.indexOf("/register.jsp")>-1) {
			arg2.doFilter(arg0, arg1);
			return ;
		}
		
		
		if(uId!=null) {
			//�Ѿ���¼
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
