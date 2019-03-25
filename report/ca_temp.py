# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:yhq


def disposal_data(data):
    '''
    整理算分服务的数据
    :param data: 算分服务发来的数据
    :return: 整理后的数据
    '''
    ls1 = ["客户驱动","创新求变",
            "系统推进","情绪调节",
            "跨界整合","激发信任",
            "释放潜能","促进成长",
            ]
    ls2 = ["自我超越",  "激情进取", "客户思维",
            "精益求精", "思维能力", "沟通能力",
           "合作能力",  "学习能力", ]

    s1 = []
    s2 = []
    index_list = data['detail']['report_data']['msg']['chart']
    for index in index_list:
        if index['name'] in ls1:
            s1.append(index)
        if index['name'] in ls2:
            s2.append(index)

    a1 = sorted(s1, key=lambda x: x['score'], reverse=True)
    a2 = sorted(s2, key=lambda x: x['score'], reverse=True)
    chart1 = []
    chart2 = []
    for i in range(len(a1)):
        chart1.append(a1[i]['name'])
        chart2.append(a2[i]['name'])

    data['detail']['report_data']['msg']['chart1'] = chart1
    data['detail']['report_data']['msg']['chart2'] = chart2
    return data


def dis_data(data):
    index_list = data['detail']['report_data']['msg']['chart']
    a1 = sorted(index_list, key=lambda x: x['score'], reverse=True)
    chart1 = []
    for i in range(len(a1)):
        chart1.append(a1[i]['name'])
    data['detail']['report_data']['msg']['chart1'] = chart1
    return data


def index_desc(index):

    '''
    输入指标，返回该指标的描述
    :param index: 指标名
    :return:
    '''

    if index == '客户驱动':
        return '从市场及客户需求研究与洞察寻找业务机会，主动引导关注客户需求与产品服务间的差距'
    elif index == '创新求变':
        return '主动思考找出产品、服务及运营需要解决的问题，推动团队致力于创新产品、服务解决方案并快速迭代'
    elif index == '系统推进':
        return '围绕客户价值实现的链条统筹考虑管理优化方案，把握推进过程中的关键问题并策略、有序地落实'
    elif index == '跨界整合':
        return '立足整体主动建立与上下左右内外的合作关系，面对分歧和差异时，能综合协调提出整合方案'
    elif index == '共启愿景':
        return '立足战略，与团队共创形成目标及达成思路，帮助团队确信目标实现的意义，形成共有感'
    elif index == '激发信任':
        return '能与团队成员一起面对问题和责任  ，明确期望并主动分享各种变化和信息，按规则和标准对待员工并兑现承诺  ，主动倾听交流，关心员工并予以帮助'
    elif index == '释放潜能':
        return '把握员工需求和特征并合理安排，接纳员工特征及风格差异并正面对待，按员工绩效及表现及时激励和肯定，赋予员工自主空间和机会让其成为主角'
    elif index == '促进成长':
        return '将团队成员成长视为自己的责任并予以历练机会，主动及时反馈辅导以促进员工和绩效成长'
    elif index == '自我超越':
        return '按角色责任和规范要求工作并力求更好成效，主动按高标准投入并致力于更高目标的达成'
    elif index == '激情进取':
        return '从整体的角度考虑问题并主动承担解决，视问题为机会，相信自己有能力解决并能持续专注的投入'
    elif index == '客户思维':
        return '始终从客户需求及变化的角度思考问题的解决和工作的输出，从他人角度来思考和约束自己，主动为他人提供服务和助益'
    elif index == '精益求精':
        return '立足客户需要及上下游环节的角度，持续寻求方法改进及环节优化，在兼顾质量、效率、成本的基础上实现高品质和高满意的服务'
    elif index == '思维能力':
        return '能快速获得分析信息把握关键并精准定义问题，能根据优先主次形成方案并做好计划安排和落实'
    elif index == '沟通能力':
        return '能主动征询、倾听、理解他人的需要和想法，能准确表达自己的想法并让对方理解和接受'
    elif index == '合作能力':
        return '能从共赢目标出发，容纳差异、化解分歧、寻求协作，对他人的需要能快速响应并提供及时帮助和专业服务'
    elif index == '学习能力':
        return '自我发展定位明确并主动学习、总结和反思来实现自身进步和突破，接纳变化并主动进行调整和改变，让自己快速融入环境并把握机会'

    else:
        return '该指标暂无描述'


def index_desc_ygzwts(index):

    '''
    输入指标，返回该指标的描述 员工自我提升
    :param index: 指标名
    :return:
    '''

    if index == '尽职尽责':
        return '能按照角色责任及岗位规范要求工作，尽自己最大的努力来完成自己的职责'
    elif index == '高效落地':
        return '能把握工作过程中的关键问题及时间节点，并能通过合理安排保证工作的有序落实'
    elif index == '主动承担':
        return '能从整体的角度考虑问题，并主动承担工作责任，积极推进问题的解决'
    elif index == '激情投入':
        return '能积极看待问题，相信自己有能力解决并能持续专注地投入'
    elif index == '严谨细致':
        return '工作上能做到细致、周全、完善，以高度负责的态度完成工作'
    elif index == '精益求精':
        return '能关注到工作的各个环节，统筹兼顾，并不断制定更高的目标'
    elif index == '同理':
        return '能设身处地的去感受别人的感受'
    elif index == '利他':
        return '能主动关心他人，并提供无私的帮助与支持'
    elif index == '寻求成长':
        return '能积极寻求自身的突破，愿意做出改变并寻求自我成长'
    elif index == '反思调整':
        return '能主动进行总结和反思，并及时调整自己的认识和行为'
    elif index == '接纳不足':
        return '能客观地认识自我，并接纳自己的不足'
    elif index == '自我肯定':
        return '能积极看待过去的经历和现状，勇敢地肯定自我的价值'
    elif index == '正面积极':
        return '能够以正面积极的心态看待问题及自我得失'
    elif index == '乐观向上':
        return '能够以乐观的心态拥抱未来，并积极地投入与应对'
    elif index == '接纳变化':
        return '能主动接受变化，并勇敢地面对不确定性的环境'
    elif index == '灵活调整':
        return '能从多个角度考虑问题，并及时、灵活调整应对策略'

    else:
        return '该指标暂无描述'