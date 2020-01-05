/**
 * 对数据库的操作
 */


package com.shopping.dao;

import java.sql.*;
import java.awt.*;
import javax.swing.*;


public class sqlHelper {
//    private String driver = "com.microsoft.sqlserver.jdbc.SQLServerDriver";
//    private String url = "jdbc:sqlserver://localhost:1433;databasename=java";
//    private String user = "sa";
//    private String pwd = "123456";

    private String driver = "com.mysql.jdbc.Driver";
    private String url = "jdbc:mysql://127.0.0.1:3306/java?"
            + "useUnicode=true&characterEncoding=UTF-8";        //指定数据源
    private String user = "root";
    private String pwd = "123456";

    private Connection ct;
    private PreparedStatement ps = null;
    private ResultSet rs = null;


    public sqlHelper() {
        try {
            Class.forName(driver);
            ct = DriverManager.getConnection(url, user, pwd);
        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }


    public ResultSet query(String sql, String[] param) {

        try {
            ps = ct.prepareStatement(sql);
            for (int i = 0; i < param.length; i++) {
                ps.setString(i + 1, param[i]);
            }
            rs = ps.executeQuery();

        } catch (Exception e) {
            e.printStackTrace();
        } finally {

        }
        return rs;
    }


    public Boolean update(String sql, String[] param) {
        Boolean flag = false;

        try {
            ps = ct.prepareStatement(sql);
            for (int i = 0; i < param.length; i++) {
                System.out.println(param[i]);
                ps.setString(i + 1, param[i]);
            }

            if (ps.executeUpdate() > 0) {
                flag = true;
            }

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
        }
//        System.out.println("注册成功！");
        return flag;
    }


    public void close() {
        try {
            if (rs != null) rs.close();
            if (ps != null) ps.close();
            if (ct != null) ct.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
