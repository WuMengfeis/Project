/**
 * ����������ʷ��¼
 * ����ʷ��¼������һ��list����
 */
package com.shopping.javabean;

import com.shopping.dao.itemDao;
import com.shopping.javabean.*;

import java.util.*;

public class HistoryModel {
    public static List<Item> historyList = new ArrayList();

    //����ʷ��¼���Ƿ��Ѿ�������
    //��������ڵĻ�����ӵ�historylist��
    //����Ѿ������˾�ɾ����ǰ������µ�

    public void addToList(String iId) {

        itemDao itemdao = new itemDao();
        Item i = itemdao.getItemById(iId);

        if (isInList(iId) == false) {
            //����id�鵽��Ʒ
            historyList.add(i);

        } else {

            deleteFromList(iId);
            historyList.add(i);
        }
    }


    public boolean isInList(String iId) {
        boolean b = false;

        Iterator it = historyList.iterator();
        while (it.hasNext()) {

            Item i = (Item) it.next();
            if (i.getId().equals(iId)) {
                b = true;
                break;
            }
        }

        return b;
    }


    public void deleteFromList(String iId) {
        Iterator it = historyList.iterator();
        while (it.hasNext()) {

            Item i = (Item) it.next();
            if (i.getId().equals(iId)) {
                historyList.remove(i);
                break;
            }
        }
    }


}
