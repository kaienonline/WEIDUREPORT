# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:yhq

import xlrd


def disc():
    # 解析指标分，对照分
    # excel_path = 'test_job.xlsx'
    excel_path = r'C:\WD\WeiDuReport\report\test_job.xlsx'
    workbook = xlrd.open_workbook(excel_path)
    sheet1 = workbook.sheet_by_name('Sheet1')
    name_list = sheet1.col_values(0)
    # 指标分
    index_list = sheet1.col_values(1)
    # 对照分
    contrast_list = sheet1.col_values(2)
    name_self = "最像我-最不像我"
    name_worker = "最像我"
    name_stress = "最不像我"
    content_list = []

    # prfloat(index_list)
    for i in range(len(name_list)):
        if i == 0:
            continue
        else:
            content_list.append({'name': name_list[i], 'index': index_list[i], 'contrast': contrast_list[i]})

    return content_list
    # content_list = ''
    # return content_list
# prfloat(disc())


def disc_parse(d):
    # 解析主导特征 语句调用
    feature = ''
    BehavioralCharacte = ''
    AdvantagesandWeaknesses = ''
    CommunicationStyle = ''



    if float(d[0]['sorce_transform']) >= 14.5 and float(d[1]['sorce_transform']) >= 14.5 and float(d[2]['sorce_transform']) >= 14.5 and float(
            d[3]['sorce_transform']) >= 14.5:
        # prfloat('1')
        feature = feature + '上移位'
    elif float(d[0]['sorce_transform']) < 14.5 and float(d[1]['sorce_transform']) < 14.5 and float(d[2]['sorce_transform']) < 14.5 and float(
            d[3]['sorce_transform']) < 14.5:
        feature = feature + '下移位'
        # prfloat('2')
    else:
        # prfloat(3)
        ls = []
        for i in d:
            if float(i['sorce_transform']) >= 14.5:
                ls.append(float(i['sorce_transform']))
        # prfloat(ls)
        ls.sort(reverse=True)
        # prfloat(ls)
        for score in ls:
            for j in d:

                if str(float(j['sorce_transform'])) == str(float(score)):
                    if j['name'] not in feature:
                        feature = feature + (j['name'])

    # excel_path = 'test_statement.xlsx'
    excel_path = r'C:\WD\WeiDuReport\report\test_statement.xlsx'
    workbook = xlrd.open_workbook(excel_path)
    sheet1 = workbook.sheet_by_name('附录')
    grade_Name_list = sheet1.col_values(0)
    BehavioralCharacte_list = sheet1.col_values(1)
    AdvantagesandWeaknesses_list = sheet1.col_values(2)
    CommunicationStyle_list = sheet1.col_values(3)
    for i in range(len(grade_Name_list)):
        if grade_Name_list[i] == feature:
            
            BehavioralCharacte = BehavioralCharacte + BehavioralCharacte_list[i]
            AdvantagesandWeaknesses = AdvantagesandWeaknesses + AdvantagesandWeaknesses_list[i]
            CommunicationStyle = CommunicationStyle + CommunicationStyle_list[i]
    return feature, BehavioralCharacte, AdvantagesandWeaknesses, CommunicationStyle,


def disc_extent(v):
    '''
    # 判断分值所处区间
    :param v:
    :return:
    '''
    if 0 <= float(v) < 6.5:
        return 1
    if 6.5 <= float(v) < 10.5:
        return 2
    if 10.5 <= float(v) < 14.5:
        return 3
    if 14.5 <= float(v) < 18.5:
        return 4
    if 18.5 <= float(v) < 22.5:
        return 5
    if 22.5 <= float(v) < 29:
        return 6

