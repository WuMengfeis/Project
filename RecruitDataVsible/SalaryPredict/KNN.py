#!usr/bin/python3
# -*- coding: utf-8 -*-
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction import DictVectorizer
from pandas import DataFrame
import os
import time

def knn_salary(test_x,x,y):
    """
    用K-近邻算法对薪资进行分类
    流程分析：
    1）获取数据
    2）划分数据集
    3）特征工程
        字典（文本）特征抽取
    4）KNN算法预估流程
	5）模型选择与调优
	6）模型评估
    :return:
    """

    begin_time = time.clock()

    # 1）获取数据

    y_data = DataFrame(y)
    y_data['avgwage'] = (y_data['min_wage'] + y_data['max_wage']) / 2.0
    # y_data.dropna()
    # y_data.fillna(y_data['avgwage'].mean())
    y_data = y_data['avgwage']

    # 2）划分数据集
    x_train, x_test, y_train, y_test = train_test_split(x, y_data, test_size=0.2, random_state=22)

    # 3）特征工程：字典特征提取
    transfer = DictVectorizer(sparse=False)
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4）KNN算法预估器
    estimator = KNeighborsClassifier()

    # # 加入网格搜索与交叉验证
    # # 参数准备
    # param_dict = {"n_neighbors": [1, 3, 5, 7, 9, 11]}
    # # 暴力查询最好的k值（n_neighbors值）cv：交叉验证多少次
    # estimator = GridSearchCV(estimator, param_grid=param_dict, cv=10)

    # 5）模型建立与保存
    if not os.path.exists("SalaryPredict/models/knn_salary.pkl"):
        # 建立模型
        estimator.fit(x_train, y_train.astype('int'))

        # 模型保存
        joblib.dump(estimator,"SalaryPredict/models/knn_salary.pkl")

        print("使用了建立的模型")
    else:
        # 模型加载
        estimator = joblib.load('SalaryPredict/models/knn_salary.pkl')
        print("使用了本地保存的模型")

    # 6）模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    # print("y_predict:\n", y_predict)
    # print("直接比对真实值和预测值:\n", y_test == y_predict)
    #
    # # 方法2：计算准确率
    # score = estimator.score(x_test, y_test)
    # print("准确率为：\n", score)

    # 7）模型预测
    test_x = transfer.transform(test_x)
    print('预测条件提取特征为：',test_x)
    predict_y = estimator.predict(test_x)
    print('预测薪资为：',predict_y)

    end_time = time.clock()

    run_time = end_time-begin_time
    print("程序运行时间为：",run_time)

    return predict_y



