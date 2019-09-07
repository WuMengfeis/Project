// 置顶操作

$(function(){
    //窗口的滚动事件
    $(window).scroll(function(){
        if($(this).scrollTop()>=200){
            $("#top").show();
        }else{
            $("#top").hide();
        }
    });

    //当鼠标点击的时候
    $("#top").click(function(){
        //$("html,body").scrollTop(0);
        $("html,body").animate({"scrollTop":0},400);
    });
});