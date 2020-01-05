<!-- 首界面 输入用户名和密码登录

实习页面的验证
实现注册页面
图片的验证码

-->

<%@ page language="java" contentType="text/html; charset=UTF-8" import="com.shopping.servlet.*"
         pageEncoding="UTF-8" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>用户登陆</title>
    <style>
        #div1 {
            align: center;
            margin-left: 100px;
        }

        #div2 {
            text-align: center;
            color: red;
        }

    </style>

    <script type="text/javascript">
        function subClick() {
            document.getElementById("identity").src = 'shopping/IdentityServlet?ts=' + new Date().getTime();


        }

    </script>

</head>

<body>
<div id="div1">
    <img src="img/login.png" height="280px" width="auto"/>
</div>
<br/>
<br/>
<form action="shopping/LoginServlet" method="post">
    <table align="center">
        <tr>
            <td>用户名 <input type="text" name="id"/></td>
        </tr>
        <tr>
            <td> 密&nbsp;&nbsp;&nbsp;&nbsp;码<input type="password" name="pwd"/></td>
        </tr>
        <tr>
            <td>验证码<input type="text" name="yzm"/></td>
            <td><img src="shopping/IdentityServlet" id="identity" onclick="subClick()"/></td>
        </tr>
        <tr>
            <td><a href="register.jsp">注册</a>&nbsp;&nbsp;&nbsp;
                <input type="submit" name="tijiao" value="提交"/>&nbsp;&nbsp;&nbsp;
                <input type="reset" name="myreset" value="重置"/></td>
        </tr>

    </table>
</form>

<div id="div2">
    <%

        //message 是登录界面返回的消息
        //info是注册页面返回的消息
        String message = request.getParameter("message");
        String info = request.getParameter("info");
        if (message != null) {

            if (Integer.valueOf(message) == 1) {
                out.println("<p>验证码错误</p>");
            } else if (Integer.valueOf(message) == 2) {
                out.println("<p>账号密码错误</p>");
            }

        }

        if (info != null) {
            out.println("<p>注册成功，请重新输入密码</p>");
        }
    %>
</div>

</body>
</html>