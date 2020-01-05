<%--把账户的id保存在session里面 --%>

<%@ page language="java" contentType="text/html; charset=UTF-8" import="com.shopping.dao.*,com.shopping.javabean.*"
         pageEncoding="UTF-8" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>购物商城</title>
    <link rel="stylesheet" type="text/css" href="css/style.css"/>
</head>
<body>

<header>
    <h1><%=request.getParameter("id") %>,欢迎来到购物商城</h1>
</header>
<div style="height:1rem;"></div>
<!--slide-->
<div id="slide">
    <div class="swiper-slide" align="center">
        <a href="#">
            <img src="img/login.png"/>
        </a>
    </div>
</div>
<!--categoryList-->
<ul class="categoryLiIcon">
    <li>
        <a href="#">
            <img src="img/menu_bg_01.png"/>
            <em>小说</em>
        </a>
    </li>
    <li>
        <a href="#">
            <img src="img/menu_bg_06.png"/>
            <em>杂文</em>
        </a>
    </li>
    <li>
        <a href="#">
            <img src="img/menu_bg_10.png"/>
            <em>传记</em>
        </a>
    </li>
    <li>
        <a href="#">
            <img src="img/menu_bg_14.png"/>
            <em>诗歌</em>
        </a>
    </li>
    <li>
        <a href="#">
            <img src="img/menu_bg_03.png"/>
            <em>杂志</em>
        </a>
    </li>
    <li>
        <a href="#">
            <img src="img/menu_bg_07.png"/>
            <em>童话</em>
        </a>
    </li>
    <li>
        <a href="#">
            <img src="img/menu_bg_11.png"/>
            <em>计算机</em>
        </a>
    </li>
    <li>
        <a href="#">
            <img src="img/menu_bg_15.png"/>
            <em>畅销书</em>
        </a>
    </li>
</ul>
<!--Tab:productList-->
<dl class="tab_proList">
    <dt>
        <a>商品图片</a>
        <a>商品名称</a>
        <a>商品价格</a>
        <a>商品数量</a>
        <a>加入购物车</a>
    </dt>
</dl>

<%
    String info = request.getParameter("info");
    String uId = request.getParameter("id");
    request.getSession().setAttribute("uId", uId);
    itemDao id = new itemDao();
    for (int i = 0; i < id.items.size(); i++) {
%>


<form action="shopping/AddItemServlet" method="post">
    <table border="0">
        <tr>
            <td width="200" height="150" valign="middle">
                <img src="<%=id.items.get(i).getPicture() %>" width="140" height="140"/>
            </td>
            <td height="32" width="100">
                <%=id.items.get(i).getName() %>
            </td>
            <td height="22" width="100">
                <%=id.items.get(i).getPrice() %>
            </td>
            <td height="100" width="50">
                <input type="text" name="num"/>
            </td>
            <td height="22" width="100">
                <input type="hidden" name="id" value="<%=id.items.get(i).getId()%>"/>
            </td>
            <td>
                <input type="hidden" name="uId" value="<%=uId %>"/>
            </td>
            <td>
                <input type="submit" name="submit" value="加入购物车"/>
            </td>
        </tr>

    </table>

</form>


<%

    }
%>


<nav>
    <a href="history.jsp" class="homeIcon">历史记录</a>
    <a href="cartShopping.jsp" class="cartIcon"> 购物车</a>
    <a href="index.jsp" class="userIcon">退出登录</a>
</nav>

</body>
</html>