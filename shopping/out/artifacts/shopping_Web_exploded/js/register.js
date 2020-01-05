/**
 * 
 */

var req;

//失去焦点时执行
function isInDB()
{
	var idFiled = document.getElementById("name");     //获得id的元素
	var url  ="shopping/Ajax?id="+escape(idFiled.value);   //提交服务器的地址
	req = new XMLHttpRequest();     //创建一个xmlhttprequest
	req.open("GET",url,true);     //连接
	req.send(null);               //发送
	req.onreadystatechange = callback;     //回调函数，当服务器的状态发生改变是自动调用1未初始化2得到了头3得到了部分4完成
}

function callback()
{
		if(req.readyState ==4&&req.status ==200)
		{
			
			var msg = req.responseXML.getElementsByTagName("msg")[0];     //从服务器端获得xml，也可以是纯文本req.responseText
			setMsg(msg.childNodes[0].nodeValue);                       //把值写到div2也就是id的后面
		}
	
}


//传参数时不用加var
//innerHTML是设置标签中间的值
function setMsg(msg)
{
	if(msg=="true"){
		document.getElementById("div2").innerHTML = "<font color = red>用户已被注册</font>";
	}
	else if(msg=="false"){
		document.getElementById("div2").innerHTML = "";
	}
	
}