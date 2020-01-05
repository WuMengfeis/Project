/**
 * 保存购物车中所有的商品信息
 */
package com.shopping.dao;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JOptionPane;

import com.shopping.javabean.Item;
import com.shopping.javabean.RelationModel;

public class cartDao {
    private ResultSet rs;


    //设置uId和iId对应的数量
    public boolean setNumOfIt(String uId, String iId, String num) {
        boolean b = false;
        String sql = "update relation set num  = ? where uId = ? and iId = ?";
        String[] param = {num, uId, iId};
        sqlHelper sh = new sqlHelper();
        b = sh.update(sql, param);
        return b;
    }

    //清空数据库
    public boolean clearDB() {
        boolean b = false;
        String sql = "delete from relation where 1=? ";
        String[] param = {"1"};
        sqlHelper sh = new sqlHelper();
        b = sh.update(sql, param);
        return b;
    }

    //根据item对象添加到数据库
    //这个有问题要先查询数据库里面有没有这个uId&&iId
    //仔决定是加到数据库还是把count加1
    public boolean addToDB(String uId, String iId, String num) {
        boolean b = false;
        sqlHelper sh = new sqlHelper();
        if (itOfNum(uId, iId) == 0) {
            //如果不在数据库里就加入到数据库中
            String sql = "insert into relation values(?,?,?)";
            String[] param = {uId, iId, num};
            b = sh.update(sql, param);
            System.out.println("添加成功");
        } else {
            int i = itOfNum(uId, iId);
            //如果在数据库中就把num++
            int allNum = i + Integer.parseInt(num);
            b = setNumOfIt(uId, iId, allNum + "");


        }


        return b;
    }

    //看数据库中有没有iId这个物品
    public int itOfNum(String uId, String iId) {
        int i = 0;
        String sql = "select num from relation where uId =? and iId = ? ";
        String[] param = {uId, iId};
        sqlHelper sh = new sqlHelper();
        rs = sh.query(sql, param);

        try {
            if (rs.next()) {
                //说明数据库中有这个数据
                i = Integer.parseInt(rs.getString(1));
            }
        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } finally {
            sh.close();
        }


        return i;
    }


    //得到uid的所有的商品编号和用户编号
    public List getItemById(String uId) {
        List<RelationModel> l = new ArrayList<>();
        String sql = "select * from relation where uId = ?";
        String[] param = {uId};
        sqlHelper sh = new sqlHelper();
        rs = sh.query(sql, param);


        try {

            while (rs.next()) {
                RelationModel rm = new RelationModel();
                rm.setuId(uId);
                rm.setiId(rs.getString(2));
                rm.setNum(Integer.parseInt(rs.getString(3)));
                l.add(rm);

            }

        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        return l;
    }

    //根据iId删除所有的商品
    public boolean removeItem(String uId, String iId) {
        boolean b = false;
        String sql = "delete from relation where uId = ? and iId = ?";
        String[] param = {uId, iId};
        sqlHelper sh = new sqlHelper();
        b = sh.update(sql, param);

        return b;
    }


}
