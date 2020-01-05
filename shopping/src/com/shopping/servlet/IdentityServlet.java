package com.shopping.servlet;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.util.Random;

import javax.imageio.ImageIO;
import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;


/**
 * Servlet implementation class IdentityServlet
 */
@WebServlet("/IdentityServlet")
public class IdentityServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	//定义验证码池
	public static final char[] chars= {'0','1','2','3','4','5','6','7','8','9','0','A','B','C','D'};
	public static Random random = new Random(); //产生一个随机数
	
	
	//获得6位随机数，放在图片中
	public static String getRandomString()
	{
		//StringBuffer，StringBuilder是可以更改的string 
		//stringbuffer 线程安全
		StringBuffer buffer = new StringBuffer();
		
		for(int i = 0;i<4;i++)
		{
			buffer.append(chars[random.nextInt(chars.length)]);
		}
		return buffer.toString();
	}
	
	
	//获得随机数的颜色
	public static Color getRandomColor()
	{
		return new Color(random.nextInt(255),random.nextInt(255),random.nextInt(255));
		
	}
	
	
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public IdentityServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		
		response.setContentType("image/jpeg");
		String randomString  = getRandomString();
		int width = 100;
		int height = 30;
		
		
		Color color = getRandomColor();
		//用来存照片
		BufferedImage bi = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
		//用来绘图
		Graphics2D g = bi.createGraphics();
		g.setFont(new Font(Font.SANS_SERIF ,Font.BOLD,16));
		g.setColor(color);
		g.drawString(randomString,18,20);
		
		//画干扰线
		for(int i = 0,n =random.nextInt(50);i<n;i++)
		{
			g.drawLine(random.nextInt(width), random.nextInt(height),random.nextInt(width) ,random.nextInt(height));
		}
		
		//输出到屏幕
		ServletOutputStream sos = response.getOutputStream(); 
		ImageIO.write(bi, "png", sos);
		HttpSession Session =request.getSession(true);
		Session.setAttribute("randomString",randomString);//放到session
		
		//禁止图像缓存
		response.setHeader("Paragma", "no-cache");
		response.setHeader("Cache-Control", "no-cache");
		response.setDateHeader("Expires", 0);
		response.setContentType("image/png");
		
		//关闭sos
		sos.close();
//		
//		//JPEGImageEncoder encoder = JPEGCodec.createJPEGEncoder(sos); //编码
//		sos.flush();
		
		
		
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
