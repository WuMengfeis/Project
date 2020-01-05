<!-- 历史记录 -->
<%@ page language="java" contentType="text/html; charset=UTF-8" import="java.util.*,com.shopping.javabean.*"
         pageEncoding="UTF-8" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>历史纪录</title>
    <link rel="stylesheet" type="text/css" href="css/style.css"/>


    <style type="text/css">
        #div1 {
            margin: 20px;
            padding: 20px;
            border: 10px;
            float: left;
        }


    </style>

</head>
<body>


<header>
    <h1>欢迎来到历史纪录</h1>
</header>
<table height="30px"></table>

<form action="" method="post">

    <%

        //获得historymodel总的所有的商品
        for (int i = 0; i < HistoryModel.historyList.size(); i++) {
            //获得第i个商品
            Item item = HistoryModel.historyList.get(i);


    %>

    <div id="div1">
        <img src="<%=item.getPicture() %>" width="140" height="140"/>
        <p>名称<%=item.getName() %>
        </p>
        <p>价格<%=item.getPrice() %>
        </p>
        <a href="shopping/HistoryServlet?iNo=<%=i %>">删除历史记录</a>

    </div>


    <%
        }
    %>

</form>

<nav>
    <a href="shopping/HistoryServlet?clear=1" class="homeIcon">清除历史记录</a>
    <a href="main.jsp?id=<%=request.getSession().getAttribute("uId") %>" class="userIcon">回到购物商城</a>
</nav>


</body>
</html>