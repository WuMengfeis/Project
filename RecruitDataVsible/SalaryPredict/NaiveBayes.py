#!usr/bin/python3
# -*- coding: utf-8 -*-
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.naive_bayes import MultinomialNB
from pandas import DataFrame
import os
import time

def nb_salary(test_x,x,y):
    """
    用朴素贝叶斯算法对薪资进行分类
    :return:
    """

    begin_time = time.clock()

    y_data = DataFrame(y)
    y_data['avgwage'] = (y_data['min_wage'] + y_data['max_wage']) / 2.0
    y_data = y_data['avgwage']

    # 2）划分数据集
    x_train, x_test, y_train, y_test = train_test_split(x, y_data, test_size=0.2, random_state=10)


    # 3）特征工程：字典特征提取
    transfer = DictVectorizer(sparse=False)
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4）朴素贝叶斯算法预估器流程
    # alpha=1.0 使用拉普拉斯平滑系数
    estimator = MultinomialNB(alpha=1.0)

    if not os.path.exists("SalaryPredict/models/nb_salary.pkl"):
        # 建立模型
        estimator.fit(x_train, y_train.astype('int'))
        # 模型保存
        joblib.dump(estimator,"SalaryPredict/models/nb_salary.pkl")
        print("使用了建立的模型")
    else:
        # 模型加载
        estimator = joblib.load('SalaryPredict/models/nb_salary.pkl')
        print("使用了本地保存的模型")

    # 5）模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    # print("y_predict:\n", y_predict)
    # print("直接比对真实值和预测值:\n", y_test == y_predict)
    # # 方法2：计算准确率
    # score = estimator.score(x_test, y_test)
    # print("准确率为：\n", score)

    test_x = transfer.transform(test_x)
    print('预测条件提取特征为：', test_x)
    predict_y = estimator.predict(test_x)
    print('预测薪资为：', predict_y)

    end_time = time.clock()

    run_time = end_time - begin_time
    print("程序运行时间为：", run_time)

    return predict_y
