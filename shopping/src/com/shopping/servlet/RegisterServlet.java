package com.shopping.servlet;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.swing.JOptionPane;

import com.shopping.dao.sqlHelper;

/**
 * Servlet implementation class RegisterServlet
 */
@WebServlet("/RegisterServlet")
public class RegisterServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    /**
     * @see HttpServlet#HttpServlet()
     */
    public RegisterServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

    /**
     * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
     */
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // TODO Auto-generated method stub

        //����ע���û�  �����ݿ��������
        request.setCharacterEncoding("UTF-8");
        String id = request.getParameter("rg_id");
        String pwd = request.getParameter("rg_pwd");
        String name = request.getParameter("rg_name");
        System.out.println(name);

        //System.out.println(id+pwd+name);

        String sql = "insert into login values(?,?,?)";
        String[] param = {id, pwd, name};
        sqlHelper sh = new sqlHelper();
        if (sh.update(sql, param)) {
//            JOptionPane.showMessageDialog(null, "���³ɹ�");
//            System.out.println("ע��ɹ�");
            response.sendRedirect("/shopping/input.jsp");
        } else {
//            JOptionPane.showMessageDialog(null, "����ʧ��");
            response.sendRedirect("/shopping/input.jsp");
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
