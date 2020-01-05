/**
 * 
 */

//在js中获得checkbox中的值

//从jsp获得按钮的iId
var req;
var id ;
function addSubOne(iId,op)
{
	id = iId;
	var url = "shopping/AddSubOneServlet?op="+escape(op)+"&iId="+escape(iId);
	req = new XMLHttpRequest();
	req.open("GET",url,true);
	req.send(null);
	req.onreadystatechange = call;
}

function call()
{
	if(req.readyState ==4&&req.status ==200)
	{
		var msg = req.responseXML.getElementsByTagName("msg")[0];     //从服务器端获得xml，也可以是纯文本req.responseText
		setMsg(msg.childNodes[0].nodeValue);                       //把值写到div2也就是id的后面
	
	}
}

function setMsg(msg)
{
	if(msg=="null"){
		//减到了0
		//刷新页面
		window.location.href ="http://localhost:8080/shopping/cartShopping.jsp";
		
	}else{
		document.getElementById("div2"+id).innerHTML = msg;
	}
	
	
}



function count()
{
	obj = document.getElementsByName("count");
	var s="";
	for(k in obj){
		if(obj[k].checked)
			s+=obj[k].value+",";
	}
	
	
	//发送到jsp中显示,不行的时候用全的url
	window.location.href = "shopping/CountServlet?allItem="+escape(s);
}