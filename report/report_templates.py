# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:yhq


"""
报告模板01
行为风格
"""
report_01 = {"report_type": "行为风格", "msg": {
    "Name": "Alice",
    "Sex": "女",
    "Age": "23",
    "CompletionTime": "36分27秒",
    "Validation": "回答真实可信，能够按照自己的实际情况如实做答，测验结果能够反映其自身的特点",
    "chart": [{"name": "能量指向", "score": -3},
              {"name": "信息收集方式", "score": 7},
              {"name": "信息加工方式", "score": -7},
              {"name": "行动方式", "score": 2},
              ],
}}

"""
报告模板02
领导风格
"""
report_02 = {"report_type": "领导风格模板", "msg": {
    "Name": "Harley",
    "Sex": "男",
    "Age": "35",
    "chart": [{"name": "高压风格", "score": 60},
              {"name": "权威风格", "score": 70},
              {"name": "亲和风格", "score": 80},
              {"name": "民主风格", "score": 90},
              {"name": "模范风格", "score": 30},
              {"name": "教练风格", "score": 40},
              ],
}}

"""
报告模板04
心理健康
"""
report_04 = {"report_type": "心理健康模板", "msg": {
    "Name": "Daf",
    "Sex": "男",
    "Age": "25",
    "CompletionTime": "38分20秒",
    "Validation": "回答较为真实，没有掩饰，结果可以相信",
    "chart": [{"name": "躯体反应", "score": 20},
              {"name": "回避行为", "score": 30},
              {"name": "幻想行为", "score": 30},
              {"name": "自责行为", "score": 20},
              {"name": "强迫行为", "score": 10},
              {"name": "偏执心理", "score": 30},
              {"name": "嫉妒心理", "score": 10},
              {"name": "人际适应", "score": 20},
              {"name": "孤独感受", "score": 40},
              {"name": "依赖心理", "score": 20},
              {"name": "猜疑心理", "score": 30},
              {"name": "焦虑情绪", "score": 40},
              {"name": "冲动控制", "score": 10},
              {"name": "抑郁倾向", "score": 20},
              {"name": "环境适应", "score": 30},
              {"name": "恐惧心理", "score": 20},
              {"name": "身心同一", "score": 30},
              ],
}}

"""
报告模板05
心理资本
"""
report_05 = {"report_type": "心理资本", "msg": {
    "Name": "Bob",
    "Sex": "男",
    "Age": "28",
    "CompletionTime": "30分20秒",
    "Validation": "回答真实可信，能够按照自己的实际情况如实做答，测验结果能够反映其自身的特点。",
    "ContentAdvantageFeature": "独立性,坚韧性,",
    "ContentWeakFeature": "进取性,支配性,容人性,利他性,",
    "ChartDataModel": [
        {"name": "进取性", "score": 10},
        {"name": "支配性", "score": 20},
        {"name": "亲和性", "score": 30},
        {"name": "开放性", "score": 40},
        {"name": "乐观性", "score": 50},
        {"name": "变通性", "score": 60},
        {"name": "内省性", "score": 70},
        {"name": "独立性", "score": 80},
        {"name": "坚韧性", "score": 80},
        {"name": "自律性", "score": 70},
        {"name": "悦纳性", "score": 60},
        {"name": "稳定性", "score": 50},
        {"name": "自信心", "score": 40},
        {"name": "尽责性", "score": 30},
        {"name": "容人性", "score": 20},
        {"name": "利他性", "score": 10},
    ],
    "ChartDataMotivation": [
        {"name": "进取性", "score": 10},
        {"name": "支配性", "score": 20},
        {"name": "亲和性", "score": 30},
    ],
    "ContentMotivationdDescription": [
        {"Aggressive": "有一定的追求成功的愿望，一般不会满足于现状，能够给自己设定具有一定挑战性的目标，为了目标的达成能够付出和努力行动"},
        {"Dominance": "有时需要外部的一些肯定或激励才会持续地投入追求更高的目标和不断的完善和超越"},
        {"Affinity": "有时需要外部的一些肯定或激励才会持续地投入追求更高的目标和不断的完善和超越"}
    ],
    "ChartDataCognition": [
        {"name": "开放性", "score": 40},
        {"name": "乐观性", "score": 50},
        {"name": "变通性", "score": 60},
        {"name": "内省性", "score": 70},
    ],
    "ChartDataCognitionDescription": [
        {"Openness": "问题解决过程中，具有从不同的角度考虑问题的习惯，"},
        {"Optimistic": "在问题不能有效解决时能够进行思路的转换，"},
        {"Workability": "也能在过程中进行调整并应对突发的事件"},
        {"Introspective": "也能在过程中进行调整并应对突发的事件。"}
    ],
    "ChartDataWill": [
        {"name": "独立性", "score": 80},
        {"name": "坚韧性", "score": 80},
        {"name": "自律性", "score": 70},
    ],
    "ContentWillDescription": [
        {"Independence": "能够明确自己行动的目的，能够独立思考，"},
        {"Resilience": "一定程度上能够自主决定，支配自己的言行并负责，"},
        {"SelfDiscipline": "有时会考虑并受到外界影响，能够接收别人的建议和批评。"}
    ],
    "ChartDataMood": [
        {"name": "悦纳性", "score": 60},
        {"name": "稳定性", "score": 50},
        {"name": "自信心", "score": 40},
    ],
    "ContentMoodDescription": [
        {"Acceptability": "基本上能够对自己肯定性评价，对自己的能力比较有信心。"},
        {"Stability": "不会回避竞争，不大会盲从权威，"},
        {"SelfConfidence": "相信自己有能力解决问题，克服困难，达成目标。"}
    ],
    "ChartDataTask": [
        {"name": "尽责性", "score": 30}
    ],
    "ContentTaskDescription": [{"Responsibility": "工作中不会推托自己应承担的任务和责任，也能完成工作职责的要求"}],
    "ChartDataPeople": [
        {"name": "容人性", "score": 20},
        {"name": "利他性", "score": 10}
    ],
    "ContentPeopleDescription": [
        {"Tolerance": "相信自己有能力解决问题，克服困难"},
        {"Altruism": "工作中不会推托自己应承担的任务和责任"}]

}}

"""
报告模板06
职业定向
"""
report_06 = {"report_type": 6, "msg": {
    "Name": "用户姓名",
    "Sex": "用户性别",
    "Age": "用户年龄",
    "ChartTheLife": "图表_生活型",
    "ChartChallenge": "图表_挑战型",
    "ChartServiceType": "图表_服务型",
    "ChartEntreType": "图表_创业型",
    "ChartSafetyStab": "图表_安全/稳定型",
    "ChartManagType": "图表_管理型",
    "ChartTechnfun": "图表_技术/职能型",
    "ContenDomCaAncType": "内容_主导职业锚类型",
    "ContentAuxiCaAnType": "内容_辅助职业锚类型",
    "ContenDomCaAncTypeDe": "内容_主导职业锚类型描述",
    "ContentAuxiCaAnTypeDe": "内容_辅助职业锚类型描述",
}}

"""
报告模板07
工作价值观
"""
report_07 = {"report_type": "工作价值观", "msg": {
    "Name": "Et",
    "TestTime": "2018年08月06日",
    "ChartDataModel": [
        {"name": "挑战/成就", "score": 8},
        {"name": "自主/独立", "score": 7},
        {"name": "专业/技术", "score": 6},
        {"name": "变化/探索", "score": 5},
        {"name": "艺术/文化", "score": 4},
        {"name": "认可/表现", "score": 3},
        {"name": "地位/职位", "score": 2},
        {"name": "权力/影响", "score": 1},
        {"name": "利他/慈善", "score": -1},
        {"name": "社交/人际", "score": -2},
        {"name": "归属/团队", "score": -3},
        {"name": "经济/报酬", "score": -4},
        {"name": "安全/稳定", "score": -5},
        {"name": "舒适/家庭", "score": -6},

    ],

    "char": [
        {"name": "挑战/成就", "Dimension": "维度1"},
        {"name": "自主/独立", "Dimension": "维度1"},
        {"name": "专业/技术", "Dimension": "维度1"},
        {"name": "变化/探索", "Dimension": "维度1"},
        {"name": "艺术/文化", "Dimension": "维度1"},
        {"name": "认可/表现", "Dimension": "维度1"},
        {"name": "地位/职位", "Dimension": "维度1"},
        {"name": "权力/影响", "Dimension": "维度1"},
        {"name": "利他/慈善", "Dimension": "维度1"},
        {"name": "社交/人际", "Dimension": "维度1"},
        {"name": "归属/团队", "Dimension": "维度1"},
        {"name": "经济/报酬", "Dimension": "维度1"},
        {"name": "安全/稳定", "Dimension": "维度1"},
        {"name": "舒适/家庭", "Dimension": "维度1"},
    ],
}}

"""
报告模板08
职业个性DISC
"""
report_08 = {"report_type": "职业个性DISC", "msg": {
    "Name": "Dive",
    "Sex": "男",
    "Age": "39",
    "ChartSelfImage_Indicator": [
        {"name": "D", "score": 4},
        {"name": "I", "score": 3},
        {"name": "S", "score": 2},
        {"name": "C", "score": 1}
    ],

    "ChartWorkMask_Indicator": [
        {"name": "D", "score": 6},
        {"name": "I", "score": 7},
        {"name": "S", "score": 7},
        {"name": "C", "score": 7}
    ],

    "ChartBR_UnderStress_Indicator": [
        {"name": "D", "score": 6},
        {"name": "I", "score": 7},
        {"name": "S", "score": 7},
        {"name": "C", "score": 7}
    ],
}}


def report01():
    # 行为风格
    return report_01


def report02():
    # 领导风格
    return report_02


def report04():
    # 心理健康
    return report_04


def report05():
    # 心理资本
    return report_05


def report06():
    # 职业定向
    return report_06


def report07():
    # 职业定向
    return report_07


def report08():
    # 职业个性DISC
    return report_08
