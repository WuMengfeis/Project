<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>注册</title>
    <link rel="stylesheet" type="text/css" href="css/style.css"/>


    <script type="text/javascript" src="js/register.js">

    </script>


    <style>

        #div1 {
            align: center;
        }

    </style>

</head>
<body>
<header>
    <h1>欢迎注册页面</h1>
</header>
<table height="80px"></table>


<div id="div1">
    <form action="shopping/RegisterServlet" method="post">
        <table align="center">
            <tr height="40px">
                <td>请输入用户名id</td>
                <td><input type="text" name="rg_id" id="name" onblur="isInDB();"/></td>
                <td>
                    <div id="div2">
                    </div>
                </td>
            </tr>
            <tr height="40px">
                <td>请输入密码</td>
                <td><input type="password" name="rg_pwd"/></td>
            </tr>
            <tr height="40px">
                <td>请输入用户的昵称</td>
                <td><input type="text" name="rg_name"/></td>
            </tr>
            <tr>
                <td><input type="submit" value="提交"/></td>
            </tr>
        </table>
    </form>
</div>


<nav>
    <a href="index.jsp" class="homeIcon">返回首界面</a>
</nav>
</body>
</html>