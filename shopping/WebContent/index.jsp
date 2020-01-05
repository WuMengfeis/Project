<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">


    <title>图书商城</title>
    <link rel="stylesheet" type="text/css" href="css/style.css"/>

</head>
<body>
    <header>
        <a href="input.jsp" class="location">登录</a>
        <a href="register.jsp" class="rt_searchIcon">注册</a>
    </header>
    <div style="height:1rem;"></div>
    <!--slide-->
    <div id="slide">
        <div class="swiper-slide">
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
            <a>热销</a>
            <a>新品</a>
            <a>打折</a>
        </dt>


        <nav>
            <a href="index.jsp" class="homeIcon">首页</a>
            <a href="input.jsp" class="cartIcon">购物车</a>
            <a href="input.jsp" class="userIcon">登录</a>
        </nav>
    </dl>
</body>
</html>