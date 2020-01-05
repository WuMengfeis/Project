<%@ page language="java" contentType="text/html; charset=UTF-8"
         import="com.shopping.javabean.*,com.shopping.dao.*,java.sql.*,java.util.*"
         pageEncoding="UTF-8" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>购物车</title>
    <link rel="stylesheet" type="text/css" href="css/style.css"/>

    <style type="text/css">
        #div1 {
            margin: 20px 20px 0 0;
            padding: 20px;
            border: 10px;
            float: left;
        }

        .div2 {
            display: inline;
        }


    </style>

    <script src="js/cartShopping.js">
    </script>

</head>
<body>
<header>
    <h1>欢迎来到购物车</h1>
</header>
<table height="30px"></table>


<form action="" method="post">

    <%
        String uId = (String) request.getSession().getAttribute("uId");
        cartDao cs = new cartDao();
        ArrayList<RelationModel> al = (ArrayList) cs.getItemById(uId);


        for (int i = 0; i < al.size(); i++) {
            //获得第i个商品
            RelationModel rm = al.get(i);

            //根据rm.getiId()获得商品的集合
            itemDao itemdao = new itemDao();
            Item temp = itemdao.getItemById(rm.getiId());

    %>

    <div id="div1">
        <img src="<%=temp.getPicture() %>" width="140" height="140"/>
        <p>名称<%=temp.getName() %>
        </p>
        <p>价格<%=temp.getPrice() %>
        </p>
        <%--在div2后面加一个商品的编号可以区别是那个商品 --%>
        数量
        <div id="div2<%=rm.getiId() %>" class="div2"><%=rm.getNum() %>
        </div>
        <%--
        <button type = "submit" formaction= "shopping/AddSubOneServlet?iId=<%=temp.getId() %>" formmethod= "post" name = "sub"  value = "1" style ="height:20px;width:20px;">-</button>
        <button type = "submit" formaction= "shopping/AddSubOneServlet?iId=<%=temp.getId() %>"  formmethod = "post" name = "add"  value = "1" style ="height:20px;width:20px;">+</button>
        --%>
        <%--换成ajax 不刷新增加 --%>
        <input type="button" value="-" name="sub" onclick="addSubOne('<%=rm.getiId() %>','sub')"/>
        <input type="button" value="+" name="add" onclick="addSubOne('<%=rm.getiId() %>','add')"/>
        <input type="checkbox" name="count" value="<%=rm.getiId() %>"/>
        <p><a href="shopping/RemoveServlet?iId=<%=rm.getiId() %>">移出购物车</a></p>

    </div>


    <%
        }
    %>


    <nav>
        <a href="shopping/RemoveServlet?clear=1" class="homeIcon">清空购物车</a>
        <a href="javascript:void(0)" class="cartIcon" onclick="count()">结算</a>
        <a href="main.jsp?id=<%=request.getSession().getAttribute("uId") %>" class="userIcon">回到购物商城</a>
    </nav>

</form>
</body>
</html>