# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:yhq

# 幸福需求模板语句调用


def need_type(n1, n2, n3):
    '''
    需求类型判断及语句调用
    :param n1: 非常关注维度
    :param n2: 比较关注维度
    :param n3: 不太关注维度
    :return:
    '''

    a1 = len(n1)
    b1 = len(n2)
    c1 = len(n3)
    if a1 > 0 and b1 > 0 and c1 > 0:
        a = ''
        for i in n1:
            if i == '安全保障需求':
                a += "获得安全保障,"
            if i == '情感归属需求':
                a += "建立情感归属,"
            if i == '尊重认可需求':
                a += "他人的尊重认可,"
            if i == '成长成就需求':
                a += "个人发展和体现成就,"
            if i == '使命利他需求':
                a += "助人利他、社会责任,"

        c = ''
        for i in n3:
            if i == '安全保障需求':
                c += "获得安全保障,"
            if i == '情感归属需求':
                c += "建立情感归属,"
            if i == '尊重认可需求':
                c += "他人的尊重认可,"
            if i == '成长成就需求':
                c += "个人发展和体现成就,"
            if i == '使命利他需求':
                c += "助人利他、社会责任,"

        return '均衡型', "分析表明，您对自己想要什么、不想要什么，都非常清晰明确。","您非常重视%s这驱动着您的多数行动和选择，影响着您的状态和表现；您不太关注%s可能是您在这些方面已经获得满足，或者与您当下其他更关注的需要相比，这些需要暂时还没有成为您的主要驱动力量。"%(a,c)
    if a1 > 0 and b1 > 0 and c1 == 0:
        a = ''
        for i in n1:
            if i == '安全保障需求':
                a += "获得安全保障,"
            if i == '情感归属需求':
                a += "建立情感归属,"
            if i == '尊重认可需求':
                a += "他人的尊重认可,"
            if i == '成长成就需求':
                a += "个人发展和体现成就,"
            if i == '使命利他需求':
                a += "助人利他、社会责任,"

        return '积极型', '分析表明，您对五大需要都比较关注，没有不太关注的需要。','其中，您非常重视%s这驱动着您的多数行动和选择，影响着您的状态和表现。' % a

    if a1 > 0 and b1 == 0 and c1 > 0:
        a = ''
        for i in n1:
            if i == '安全保障需求':
                a += "获得安全保障,"
            if i == '情感归属需求':
                a += "建立情感归属,"
            if i == '尊重认可需求':
                a += "他人的尊重认可,"
            if i == '成长成就需求':
                a += "个人发展和体现成就,"
            if i == '使命利他需求':
                a += "助人利他、社会责任,"
        c = ''
        for i in n3:
            if i == '安全保障需求':
                c += "获得安全保障,"
            if i == '情感归属需求':
                c += "建立情感归属,"
            if i == '尊重认可需求':
                c += "他人的尊重认可,"
            if i == '成长成就需求':
                c += "个人发展和体现成就,"
            if i == '使命利他需求':
                c += "助人利他、社会责任,"

        return '分化型', '分析表明，您的需求维度表现非常分化，要么非常关注，要么不太关注，没有一般性的需要。', '您非常重视%s这驱动着您的多数行动和选择，影响着您的状态和表现；您不太关注%s可能是您在这些方面已经获得满足，或者与您当下更关注的需要相比，这些需要暂时还没有成为您生的主要驱动力量。' % (a,c)

    if a1 > 0 and b1 == 0 and c1 == 0:
        return '激进型', '分析表明，您对五大需要都非常关注，没有一般关注或不太关注的需要。', '您非常重视的需要会驱动着您的行动和选择，影响着您的状态。如果您受多个需要驱动，您会常常面临选择方面的冲突，无法取舍，非常纠结。'

    if a1 == 0 and b1 > 0 and c1 > 0:
        return '中低型', '分析表明，您有一般关注的需要，也非常明确不太关注的需要，但并没有非常关注的需要。', '您非常重视的需要会驱动着您的行动和选择，影响着您的表现和状态，如果没有特别关注的需要，可能您在生活工作中的动力并不会太强烈、持久，遇到困难有可能会退缩。'
    if a1 == 0 and b1 > 0 and c1 == 0:
        return '中和型', '分析表明，您的需要都比较中和，对所有的需要的关注程度都相对比较均衡，没有特别关注的，也没有不太关注的。', '您非常重视的需要会驱动着您的行动和选择，影响着您的表现和状态，而不太关注的需要可能是您已经获得满足的。目前您的状态可能是相对平和的，也可能是存在一些纠结和冲突，无法确定自己最想要的是什么。'
    if a1 == 0 and b1 == 0 and c1 > 0:
        return '消极型', '分析表明，结果显示您在五大需求上都不太关注，没有特别关注的，也没有比较关注的。', '您目前没有非常关注或比较关注的需要，有可能是您的大部分需要都已经获得满足，对工作生活各方面都比较满意，显得“无欲无求”；也可能是您与世无争，比较“佛系”。'


def consistency(life_index, work_index):
    '''
    生活，工作一致性需求解析
    :param life_index: 指标（生活）列表
    :param work_index: 指标（工作）列表
    :return:
    '''

    a1 = []
    a2 = []
    for i in life_index:
        for j in work_index:
            if i['name'] == j['name']:
                a1.append(i)
                a2.append(j)

    life_index = a1
    work_index = a2
    ls1 = []
    ls2 = []
    ls3 = []
    for i in range(len(life_index)):
        if life_index[i]['score'] - work_index[i]['score'] >= 0:
            if life_index[i]['score'] - work_index[i]['score'] >= 60:
                ls1.append(
                    {'life': life_index[i]['name'], 'life_score': life_index[i]['score'],
                     'work': work_index[i]['name'], 'work_score': work_index[i]['score'],
                     }
                )
            elif 40 <= life_index[i]['score'] - work_index[i]['score'] < 60:
                ls2.append(
                    {'life': life_index[i]['name'], 'life_score': life_index[i]['score'],
                     'work': work_index[i]['name'], 'work_score': work_index[i]['score'],
                     }
                )

            elif 0 <= life_index[i]['score'] - work_index[i]['score'] < 40:
                ls3.append(
                    {'life': life_index[i]['name'], 'life_score': life_index[i]['score'],
                     'work': work_index[i]['name'], 'work_score': work_index[i]['score'],
                     }
                )
        else:

            if ((life_index[i]['score'] - work_index[i]['score']) * -1) >= 60:
                ls1.append(
                    {'life': life_index[i]['name'], 'life_score': life_index[i]['score'],
                     'work': work_index[i]['name'], 'work_score': work_index[i]['score'],
                     }
                )
            elif 40 <= ((life_index[i]['score'] - work_index[i]['score']) * -1) < 60:
                ls2.append(
                    {'life': life_index[i]['name'], 'life_score': life_index[i]['score'],
                     'work': work_index[i]['name'], 'work_score': work_index[i]['score'],
                     }
                )

            elif 0 <= ((life_index[i]['score'] - work_index[i]['score']) * -1) < 40:
                ls3.append(
                    {'life': life_index[i]['name'], 'life_score': life_index[i]['score'],
                     'work': work_index[i]['name'], 'work_score': work_index[i]['score'],
                     }
                )

    if len(ls1) > 0:
        return ls1, '蓝色指标分数较高时，这些指标因素您主要是通过工作获得满足，而黄色指标分数较高时，这些指标因素您主要通过生活来获得满足。'
    if len(ls1) == 0 and len(ls2) > 0:
        if len(ls2) > 5:
            ls2 = ls2[:5]
        return ls2, '蓝色指标分数较高时，这些指标因素您大多会通过工作获得满足，而黄色指标分数较高时，这些指标因素您多会通过生活来获得满足。'
    if len(ls1) == 0 and len(ls2) == 0 :
        if len(ls3) > 5:
            ls3 = ls3[:5]
        return ls3, '您对工作和生活的需求基本一致，不太会根据工作或生活的场景不同而有所改变。'