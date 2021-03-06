﻿# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:yhq


def bh_desc(v1,v2,v3,v4):
    '''
    :param v1: 能量指向维度外倾题得分-内倾题得分
    :param v2: 信息收集方式维度感觉题得分-直觉题得分
    :param v3: 信息加工方式维度思考得分-情感题得分
    :param v4: 行动方式维度判断题得分-知觉得分
    :return: 语句描述
    '''

    if v1 < 0:
        v1 = -v1
    if v2 < 0:
        v2 = -v2
    if v3 < 0:
        v3 = -v3
    if v4 < 0:
        v4 = -v4

    s1 = ''
    s2 = ''
    s3 = ''
    s4 = ''
    # 能量指向维度外倾题得分-内倾题得分
    if 0 <= v1 < 13:
        s1 = '喜欢独自深度思考，做事谨慎，先思考后行动，沉静而专注，满足于独立工作，与人沟通有较强的选择性，只在小群体中进行分享。'
    elif 13 <= v1 < 17:
        s1 = '喜欢独立思考，做事比较谨慎，相对喜欢独立工作，较为专注，在与人沟通有一定的选择性。'
    elif 17 <= v1 < 20:
        s1 = '相对而言，能够集中于自己内心的思想和体验，倾向于独立思考，也愿意与他人开放沟通与交流，表现出一定的外倾特点。'
    elif 20 <= v1 < 28:
        s1 = '虽能将兴趣和注意力指向外部客观事物，但范围不大，在熟悉情境下能够与人开放沟通、交流分享表现一定的外向特点，有时喜欢独自思考，表现出一定的内倾特点，两者较均衡，特点不太突出。'
    elif 28 <= v1 < 37:
        s1 = '喜欢接触外界环境，愿意与别人进行沟通，较为喜欢与他人自由地分享与交流，不拘束，喜欢行动，有时会受到外部环境的影响。'
    elif 37 <= v1 <= 40:
        s1 = '合群、开放易沟通，坦率随和、好交际，愿意自由地与他人分享与交流，喜欢快节奏行动，对外部环境敏感，易于受到外部环境的影响。'
    # 信息收集方式维度感觉题得分-直觉题得分
    if 0 <= v2 < 12:
        s2 = '关注事物的全貌或整体，善于把握事物的意义、联系和发展的可能性，表现出思维跳跃、追求变化的特点，但可能忽略现实，不关心细节，不喜欢一成不变的环境。'
    elif 12 <= v2 < 16:
        s2 = '较为关注事物的全貌或整体，能够把握事物的意义、联系和发展的可能性，表现出思维跳跃、追求变化的特点，不太喜欢一成不变、细节性的事情。'
    elif 16 <= v2 < 22:
        s2 = '相对而言，能够关注事物的全貌或整体，会考虑一些事物的意义、联系和可能的变化，但也会关注当前的现实以及事务的细节，表现出一些感觉型的特点。'
    elif 22 <= v2 < 27:
        s2 = '相对而言，通过收集具体的信息了解外在世界，在一定程度上倾向于关注具体细节、做事一般能从现实出发，对具体而明确的工作有一定的偏好表现出一定的直觉型特点，但有时也能关注到事物的整体和发展规律，表现出一定的直觉型特点，两者比较均衡，特点不太突出。'
    elif 27 <= v2 < 36:
        s2 = '喜欢通过收集具体的信息了解外在世界，较为关注具体问题和事务的细节，比较喜欢从事具体而明确的工作，做事往往能从现实出发，注重结果。'
    elif 36 <= v2 <= 44:
        s2 = '善于通过收集具体的信息了解外在世界，关注具体问题和事务的细节，着眼现实，注重结果，乐于从事具体而明确的工作，做事细心周到。'
    # 信息加工方式维度思考得分-情感题得分
    if 0 <= v3 < 11:
        s3 = '常常喜欢以主观因素为依据来做决定，主要是通过权衡问题的相对价值和利益进行决策，关注对他人的影响，有时会过于考虑他人的感受。'
    elif 11 <= v3 < 14:
        s3 = '做决定时倾向于以主观因素为依据，通过权衡问题的相对价值和利益进行决策，会考虑对他人的影响以及他人的感受。'
    elif 14 <= v3 < 22:
        s3 = '相对而言，能够权衡问题的相对价值和利益进行决策，有时也会考虑客观理性，依据逻辑进行分析判断，表现出思考型的特点。'
    elif 22 <= v3 < 25:
        s3 = '相对而言，在分析问题或作判断时，一般能以事物的逻辑性和事实为依据表现出一定的思考型特点；但也会考虑决策对他人的影响，表现出一定的情感型的特点，两者较均衡，特点不太突出。'
    elif 25 <= v3 < 34:
        s3 = '能够按照客观理性、逻辑推理进行决策，能以客观事实、公正原则、现实规则解决问题；有时不太考虑决策对他人的影响。'
    elif 34 <= v3 <= 44:
        s3 = '严格按照客观理性、逻辑推理进行客观分析和决策，重视客观事实、公正原则、现实规则；在决策时不考虑决策对他人的影响，也不喜欢他人感情用事。'
    # 行动方式维度判断题得分-知觉得分
    if 0 <= v4 < 12:
        s4 = '具有很强的开放、好奇的特征，灵活性和适应性强，思考多于行动，注重过程而不是结果，对规则和约束反感，有时会欠缺计划性和坚持性。'
    elif 12 <= v4 < 16:
        s4 = '具有较强的开放、好奇的特征，由较强的灵活性和适应性，相对于结果更注重过程，不愿意受到约束，不太注重计划性。'
    elif 16 <= v4 < 20:
        s4 = '相对而言，有一定好奇、灵活适应的特征，做事情也会有一定的计划性和条理性，表现出一定的判断型特征。'
    elif 20 <= v4 < 25:
        s4 = '相对而言，有一定的计划性和条理性，有时也表现出一定的灵活性，表现出一定的知觉型特点和判断型特点，两者较均衡，特点不太突出。'
    elif 25 <= v4 < 33:
        s4 = '具有较强的计划性和条理性，能够对行动进行组织和控制，关注任务完成。'
    elif 33 <= v4 <= 40:
        s4 = '具有很强的计划性、条理性，善于组织、决断和控制，关注结果的达成，但有时缺乏弹性与灵活。'

    return s1, s3, s2, s4





