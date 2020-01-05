/**
 * ���湺�ﳵ�����е���Ʒ��Ϣ
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


    //����uId��iId��Ӧ������
    public boolean setNumOfIt(String uId, String iId, String num) {
        boolean b = false;
        String sql = "update relation set num  = ? where uId = ? and iId = ?";
        String[] param = {num, uId, iId};
        sqlHelper sh = new sqlHelper();
        b = sh.update(sql, param);
        return b;
    }

    //������ݿ�
    public boolean clearDB() {
        boolean b = false;
        String sql = "delete from relation where 1=? ";
        String[] param = {"1"};
        sqlHelper sh = new sqlHelper();
        b = sh.update(sql, param);
        return b;
    }

    //����item������ӵ����ݿ�
    //���������Ҫ�Ȳ�ѯ���ݿ�������û�����uId&&iId
    //�о����Ǽӵ����ݿ⻹�ǰ�count��1
    public boolean addToDB(String uId, String iId, String num) {
        boolean b = false;
        sqlHelper sh = new sqlHelper();
        if (itOfNum(uId, iId) == 0) {
            //����������ݿ���ͼ��뵽���ݿ���
            String sql = "insert into relation values(?,?,?)";
            String[] param = {uId, iId, num};
            b = sh.update(sql, param);
            System.out.println("��ӳɹ�");
        } else {
            int i = itOfNum(uId, iId);
            //��������ݿ��оͰ�num++
            int allNum = i + Integer.parseInt(num);
            b = setNumOfIt(uId, iId, allNum + "");


        }


        return b;
    }

    //�����ݿ�����û��iId�����Ʒ
    public int itOfNum(String uId, String iId) {
        int i = 0;
        String sql = "select num from relation where uId =? and iId = ? ";
        String[] param = {uId, iId};
        sqlHelper sh = new sqlHelper();
        rs = sh.query(sql, param);

        try {
            if (rs.next()) {
                //˵�����ݿ������������
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


    //�õ�uid�����е���Ʒ��ź��û����
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

    //����iIdɾ�����е���Ʒ
    public boolean removeItem(String uId, String iId) {
        boolean b = false;
        String sql = "delete from relation where uId = ? and iId = ?";
        String[] param = {uId, iId};
        sqlHelper sh = new sqlHelper();
        b = sh.update(sql, param);

        return b;
    }


}
