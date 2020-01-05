<%@ page language="java" contentType="text/html; charset=UTF-8"
         import="com.shopping.dao.*,com.shopping.javabean.*,java.util.*"
         pageEncoding="UTF-8" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>结款界面</title>
    <link rel="stylesheet" type="text/css" href="../css/style.css"/>
    <link rel="stylesheet" type="text/css" href="../css/Count.css"/>


</head>
<body>
<header>
    <h1>欢迎来到结款界面</h1>
</header>
<table height="60px"></table>

<%
    CountModel countModel = (CountModel) request.getAttribute("countModel");
    String uId = (String) request.getSession().getAttribute("uId");
    float allCount = 0;

%>
<div class="topDiv">
    <div id="top_text"><font size="4px">收款人</font></div>
    <div id="top_name"><font size="4px" color="red"><%=uId %>
    </font></div>
    <div id="top_tel"><font size="4px">13886989596</font></div>
</div>

<div class="line"></div>
<table height="40px"></table>


<div id="tabDiv">
    <table align="center">
        <tr height="50px">
            <td width="300px"><font size="4px">商品</font></td>
            <td width="300px"><font size="4px">数量</font></td>
            <td width="300px"><font size="4px">价格</font></td>
        </tr>

        <%
            for (int i = 0; i < countModel.allNum.length; i++) {
                //得到第一个商品的图片和价格和数量
                int num = countModel.allNum[i];
                Item item = countModel.itemList.get(i);
                allCount += num * item.getPrice();

        %>
        <tr height="130px">
<%--            <td width="300px"><font size="4px"><img src="../<%=item.getPicture() %>"/></font></td>--%>
            <td width="300px"><font size="4px"><img src="<%=item.getPicture() %>"/></font></td>
            <td width="300px"><font size="4px">×<%=num %>
            </font></td>
            <td width="300px"><font size="4px">￥<%=item.getPrice() * num %>
            </font></td>
        </tr>

        <%
            }
        %>

        <tr>
            <td width="300px"></td>
            <td width="300px"><font size="4px">总计</font></td>
            <td width="300px"><font size="4px">￥<%=allCount %>
            </font></td>
        </tr>

    </table>
</div>


<table height="80px"></table>
<nav>
    <a href="" class="homeIcon">提交订单</a>
    <a href="../cartShopping.jsp" class="userIcon">返回购物车</a>
</nav>
</body>
</html>