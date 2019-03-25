# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:yhq
import re

from celery import shared_task
import time
import requests
from datetime import datetime
from report.parse import parse_data
from . import models
from report.aliyun.oss import AliyunOss
from threading import local

def close_old_connections():
    # 获取当前线程本地变量
    connections = local()
    # 根据数据库别名获取数据库连接
    if hasattr(connections, 'default'):
        conn = getattr(connections, 'default')
        # 检查连接可用性，并关闭不可用连接
        conn.close_if_unusable_or_obsolete()


@shared_task
def get_report(data):
    close_old_connections()
    tt = time.time()
    qs = models.UserReport.objects.filter(
        people_result_id=data["people_result_id"],
        report_type_id=data["report_type_id"]
    )
    if not qs.exists():
        report_info = models.UserReport.objects.create(
            people_result_id=data["people_result_id"],
            report_type_id=data["report_type_id"]
        )
    else:
        report_info = qs[0]
    # doSomething

    report_info.try_times += 1
    url_pdf = ""
    # status = '1'
    # report_info.save()
    print("发送的数据：%s" % data)
    try:
        # # 请求数据模板
        d = create_word(data['people_result_id'], data['report_type_id'])
        print('需要word服务解析的模板数据')
        print(d)
        if d["code"] == 0:
            word_path = parse_data(data['report_type_id'], d, data['people_result_id'])
            pdf_path = word_path + '.pdf'
            print(word_path)
            print(pdf_path)
            t = datetime.now().strftime('%Y-%m-%d')
            # os.path.split
            file_name1 = pdf_path[pdf_path.rfind('\\') + 1:]
            file_name2 = word_path[word_path.rfind('\\') + 1:]
            print(file_name2)
            print(file_name1)
            ttt = time.time()
            print("异步任务耗时%s" % (ttt - tt))
            try:
                url_pdf = AliyunOss().upload_file(t, file_name1, pdf_path)
                url_word = AliyunOss().upload_file(t, file_name2, word_path)
                print('%s上传成功' % url_pdf)
                status = '1'
            except  Exception as e:
                pass
        else:
            status = '2'
    except Exception as e:
        status = '2'

    # TODO 解析模板数据，生成word，拿到url,更新数据库
    qs = models.UserReport.objects.filter(
        people_result_id=data["people_result_id"],
        report_type_id=data["report_type_id"]
    )
    report_info = qs[0]  # 考虑 force_recreate
    if url_pdf or report_info.url:
        report_info.url = url_pdf
        report_info.status = '1'
        report_info.save()
    elif int(status) == 2 and int(report_info.status) != 1:
        report_info.status = '2'
        report_info.save()
    qs = models.UserReport.objects.filter(
        people_result_id=data["people_result_id"],
        report_type_id=data["report_type_id"]
    )
    report_info = qs[0]
    try:
        data1 = {
            "people_result_id": data['people_result_id'],
            "report_status": report_info.status,
            "report_url":  report_info.url
        }
        if data["report_type_id"] == 'HAMeasurePersonal_EN' or data["report_type_id"] == 'EmployeeMentalHealth_EN':
            data1 = {
                "people_result_id": data['people_result_id'],
                "report_status": report_info.status,
                "en_report_url": report_info.url
            }
        requests.post(url="http://assess.iwedoing.com/api/client/v1/front/report/info/callback/", data=data1, timeout=3)
        # requests.post(url="http://47.98.34.126/api/client/v1/front/report/info/callback/", data=data1, timeout=3)
    except Exception as e:
        print('回调接口响应超时')


def send_result_callback(people_result_id, result_status, url_pdf):
    try:
        data1 = {
            "people_result_id": people_result_id,
            "report_status": result_status,
            "report_url":  url_pdf
        }
        if data["report_type_id"] == 'HAMeasurePersonal_EN' or data["report_type_id"] == 'EmployeeMentalHealth_EN':
            data1 = {
                "people_result_id": data['people_result_id'],
                "report_status": status,
                "en_report_url": url_pdf
            }
        requests.post(url="http://assess.iwedoing.com/api/client/v1/front/report/info/callback/", data=data1, timeout=3)
    except Exception as e:
        print('回调接口响应超时')



@shared_task
def get_report_uat(data):
    tt = time.time()
    qs = models.UserReportUat.objects.filter(
        people_result_id=data["people_result_id"],
        report_type_id=data["report_type_id"]
    )
    if not qs.exists():
        report_info = models.UserReportUat.objects.create(
            people_result_id=data["people_result_id"],
            report_type_id=data["report_type_id"]
        )
    else:
        report_info = qs[0]
    # doSomething

    report_info.try_times += 1
    url_pdf = ""
    status = '1'
    # report_info.save()
    print("发送的数据：%s" % data)
    try:
        # 判断模板类型
        if data['report_type_id'] == 'PsychologicalCapital':
            # # 请求数据模板
            d = create_word(data['people_result_id'], data['report_type_id'], data['env'])
            print('需要word服务解析的模板数据')
            print(d)
            if d["code"] == 0:
                word_path = parse_data(data['report_type_id'], d, data['people_result_id'])
                pdf_path = word_path + '.pdf'
                print(word_path)
                print(pdf_path)
                t = datetime.now().strftime('%Y-%m-%d')
                # os.path.split
                file_name1 = pdf_path[pdf_path.rfind('\\')+1:]
                file_name2 = word_path[word_path.rfind('\\')+1:]
                print(file_name2)
                print(file_name1)
                ttt = time.time()
                print("异步任务耗时%s" % (ttt - tt))
                url_pdf = AliyunOss().upload_file(t, file_name1, pdf_path)
                url_word = AliyunOss().upload_file(t, file_name2, word_path)
                print(url_pdf)
                status = '1'
            else:
                if report_info.try_times < 4:
                    status = '0'
                    get_report_uat(data)
                else:
                    status = '2'
        if data['report_type_id'] == 'HAMeasurePersonal':
            # # 请求数据模板
            d = create_word(data['people_result_id'], data['report_type_id'], data['env'])
            print('需要word服务解析的模板数据')
            print(d)
            if d["code"] == 0:
                word_path = parse_data(data['report_type_id'], d, data['people_result_id'])
                pdf_path = word_path + '.pdf'
                print(word_path)
                print(pdf_path)
                t = datetime.now().strftime('%Y-%m-%d')
                # os.path.split
                file_name1 = pdf_path[pdf_path.rfind('\\') + 1:]
                file_name2 = word_path[word_path.rfind('\\') + 1:]
                print(file_name2)
                print(file_name1)
                ttt = time.time()
                print("异步任务耗时%s" % (ttt - tt))
                url_pdf = AliyunOss().upload_file(t, file_name1, pdf_path)
                url_word = AliyunOss().upload_file(t, file_name2, word_path)
                print(url_pdf)
                status = '1'
            else:
                if report_info.try_times < 4:
                    status = '0'
                    get_report.delay(data)
                else:
                    status = '2'
    except Exception as e:
        if report_info.try_times < 4:
            status = '0'
            get_report.delay(data)
        else:
            status = '2'
    # TODO 解析模板数据，生成word，拿到url,更新数据库
    report_info.url = url_pdf
    report_info.status = status
    report_info.save()
    try:
        data1 = {
            "people_result_id": data['people_result_id'],
            "report_status": status,
            "report_url":  url_pdf
        }
        requests.post(url="http://assessment.iwedoing.com/api/client/v1/front/report/info/callback/", data=data1, timeout=3)
    except Exception as e:
        print('回调接口响应超时')


def create_word(people_result_id, report_type_id):
    # if env == 'pro':
    #
    #     # 生产 环境
    #     url = "http://assess.iwedoing.com/api/client/v1/front/report/data/"
    #     data = {"people_result_id": people_result_id,
    #             "report_type_id": report_type_id
    #             }
    # else:
    #     # UAT 环境
    #     url = 'http://assessment.iwedoing.com/api/client/v1/front/report/data/'
    #     data = {"people_result_id": people_result_id,
    #             "report_type_id": report_type_id
    #             }

    # 生产 环境
    
    # url = "http://47.98.34.126/api/client/v1/front/report/data/"
    url = "http://assess.iwedoing.com/api/client/v1/front/report/data/"
    data = {"people_result_id": people_result_id,
            "report_type_id": report_type_id
            }
    try:
        res = requests.post(url=url, data=data, timeout=15)
    except Exception as e:
        print('算分服务响应超时')

    d = eval(res.text)
    print('算分服务发来的数据:%s' % d)
    if d["code"] != 0:
        res = {"code": 40400, 'detail': {'report_data': "算分服务无法提供数据,"}}
        return res

    # from .report_templates import report01
    if report_type_id == "LeaderStyle":
        try:
            report02 = d['detail']['report_data']
            print('report02打印：%s' % report02)
        except Exception as e:
            res = {"code": 40400, 'detail': {'report_data': e}}
            return res
        chart_data = report02['msg']['chart']
        ContentTheMain = ""
        ContentMinor = ""
        ContentLessUsed = ""
        ContentManagementBe = ""

        Content = [{"name": "高压风格",
                    "desc": "不断的给出命令，期望下属立刻服从；密切的监督和控制下属的工作进程；关注发现的问题，经常给出负面的、纠正性的反馈；强调不服从所导致的负面后果来激发团队成员服从；"},
                   {"name": "教练风格",
                    "desc": "鼓励员工确定长期的职业发展目标，帮助制订明确的实施计划；应用倾听技巧和开放性问题来鼓励团队成员解决自己的问题；擅长授权，会布置给员工挑战性的任务；将错误视为学习机会，为了员工的成长愿意接受暂时的失败；"},
                   {"name": "权威风格",
                    "desc": "为团队制定和传达清晰的使命和方向；用清晰的目标激励员工，让他们清楚地认识到本岗位与组织总体愿景之间的联系；会把宏大的愿景分解为个体的目标任务，并围绕组织愿景制定工作标准；允许员工自由创新、尝试各种方法，并愿意承担可衡量的风险；"},
                   {"name": "亲和风格",
                    "desc": "提倡团队成员之间保持友好的关系；关注团队成员的情感需求，而不是工作任务的指引、目标和标准；追求员工的满意以及团队的和谐，通过与员工建立牢固的感情联系，获得员工强烈的忠诚；避免与绩效相关的冲突，创造能带来积极反馈的机会；"},
                   {"name": "民主风格",
                    "desc": "愿意花时间听取集体意见，争取民意；允许员工对自己的任务目标以及工作方式保留发言权；通过组织许多会议来作出决策，希望通过深入讨论最终达成共识；"},
                   {"name": "模范风格",
                    "desc": "相信团队成员有能力为自己和团队确定合适的指引；设定特别高的业绩标准，并且以身作则，亲自示范；强迫自己更高质量、更快速地完成工作，而且要求别人跟他一样；倾向于亲力亲为，独立完成工作任务，只有紧急任务时，才与他人协调；在团队成员遇到问题时，提供详细的工作指引；"},
                   ]
        for i in chart_data:
            if i['score'] >= 60:
                # 主要使用的领导风格判断
                ContentTheMain = ContentTheMain + i['name'] + ","
            if 40 <= i['score'] < 60:
                # 次要使用的领导风格判断
                ContentMinor = ContentMinor + i['name'] + ","
            if i['score'] < 40:
                # 较少使用的领导风格判断
                ContentLessUsed = ContentLessUsed + i['name'] + ","
        # print(ContentTheMain)
        # print(ContentTheMain.split(','))
        # 管理行为判断
        for i in ContentTheMain.split(','):
            for j in Content:
                if i == j["name"]:
                    ContentManagementBe = ContentManagementBe + j["desc"]
        # print(ContentManagementBe)
        report02['msg']["ContentTheMain"] = ContentTheMain
        report02['msg']["ContentMinor"] = ContentMinor
        report02['msg']["ContentLessUsed"] = ContentLessUsed
        report02['msg']["ContentManagementBe"] = ContentManagementBe
        res = {"code": 0, 'detail': {'report_data': report02}}
        print('发送到word服务的数据:%s' % res)
        return res
    elif report_type_id == "BehavioralStyle":
        try:
            report01 = d['detail']['report_data']
            print('report01打印：%s' % report01)
        except Exception as e:
            res = {"code": 40400, 'detail': {'report_data': e}}
            return res
        res = {"code": 0, 'detail': {'report_data': report01}}
        print('发送到word服务的数据:%s' % res)
        return res
        
    elif report_type_id == "EmployeeMentalHealth":
        try:
            report04 = d['detail']['report_data']
            print('report04打印：%s' % report04)
        except Exception as e:
            res = {"code": 40400, 'detail': {'report_data': e}}
            return res
        chart_data = report04['msg']['chart']
        v = report04['msg']['Validation']
        v1 = ''
        if v >= 25:
            v1 = v1 + '没有按照自身的实际情况作答，存在较多的饰好、伪装倾向，因此无法向您提供真实的、详尽的报告，请您抽时间重新参加测验。'
        else:
            v1 = v1 + '回答较为真实，没有掩饰，结果可以相信。'
        # print(chart_data)
        # 定义黄、橙、红 指标
        ChartYellowIndex = ""
        ChartOrangeIndex = ""
        ChartRedIndex = ""
        # 定义内容
        # 躯体反应
        ContentSomaticReaction = ""
        # 回避行为
        ContentAvoidanceBehavior = ""
        # 幻想行为
        ContentFantasies = ""
        # 自责行为
        ContentSelfReproach = ""
        # 强迫行为
        ContentCompulsion = ""
        # 偏执心理
        ContentParanoia = ""
        # 嫉妒心理
        ContentJealousy = ""
        # 人际适应
        ContentInterpersonalAdaptation = ""
        # 孤独感受
        ContentLonelyFeeling = ""
        # 依赖心理
        ContentAnaclisis = ""
        # 猜疑心理
        ContentSuspicions = ""
        # 焦虑情绪
        ContentAnxiety = ""
        # 冲动控制
        ContentImpulsiveControl = ""
        # 抑郁倾向
        ContentDepressiveTendency = ""
        # 环境适应
        ContentEnvironmentalAdaptation = ""
        # 恐惧心理
        ContentFear = ""
        # 身心同一

        ContentBodyAndMind = ""
        for i in chart_data:
            if i['score'] >= 16 and i['score'] <= 20:
                # 黄色指标
                ChartYellowIndex = ChartYellowIndex + i['name'] + ","
            if i['score'] >= 21 and i['score'] <= 25:
                # 橙色指标
                ChartOrangeIndex = ChartOrangeIndex + i['name'] + ","
            if i['score'] >= 26 and i['score'] <= 30:
                # 红色指标
                ChartRedIndex = ChartRedIndex + i['name'] + ","

            if i['name'] == "躯体反应":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentSomaticReaction = ContentSomaticReaction + "一般来说，您具有良好的身体状态，可能的表现为：；[1] 精力充沛，具有较强的工作兴趣和较高的工作效率；[2] 极少产生持久而强烈的身体疼痛感；[3] 即使产生身体疲劳感，也能够通过休息很快恢复"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentSomaticReaction = ContentSomaticReaction + "一般来说，您基本具有较好的身体状态，可能的表现为：；[1] 较少表现出明显的胃肠道症状，[2] 比如腹痛、腹胀、恶心、呕吐等；较少表现出持久、严重且强烈的身体疼痛感；[3] 较少表现出明显的身体疲劳感"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentSomaticReaction = ContentSomaticReaction + "一般来说，您已经呈现出轻微的躯体症状，可能的表现为：；[1] 有时感到身体疲劳，浑身乏力；[2] 有时感到腹痛、腹胀或感到恶心、呕吐；[3] 有时郁郁寡欢，感到胸闷、气短；[4] 身体的某些部位有时会有疼痛感，有时持久且强烈"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentSomaticReaction = ContentSomaticReaction + "一般来说，您已经呈现比较明显的躯体症状，可能的表现为：；[1] 常表现出胃肠道症状，比如腹痛、恶心、腹胀、呕吐、打嗝、稀便等；[2] 常表现出呼吸系统症状，比如气短、胸痛等；[3] 常表现出自主神经兴奋症状，比如心悸、出汗、脸红、震颤等；[4] 极易过度疲劳，常感到手脚沉重或无力感；[5] 感觉到身体的疼痛感，有时持续、严重、强烈且突出"
            if i['name'] == "回避行为":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentAvoidanceBehavior = ContentAvoidanceBehavior + "一般来说，您是一个能积极面对困难和挑战的人。可能的表现为：；[1] 能坚定地专注于既定的目标，积极寻求解决任务的办法；[2] 能够用成熟的态度面对困难、挫折和失败；[3] 努力去改变现状，使情况向好的一面转化；[4] 极少受到失望、沮丧等负面情绪的影响；[5] 具有锲而不舍、不达目的决不罢休的决心"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentAvoidanceBehavior = ContentAvoidanceBehavior + "一般来说，您能够积极面对困难。可能的表现为：；[1] 能够关注既定目标的完成，寻求解决办法；[2] 能够面对困难、挫折和失败；[3] 少有回避倾向,较少受到失望、沮丧等负面情绪的影响；[4] 不会过分强调任务的困难和不可完成性"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentAvoidanceBehavior = ContentAvoidanceBehavior + "一般来说，您不太愿意直面困难和挑战。可能的表现为：；[1] 有时不能坦然面对现实环境，而是选择抱怨或逃避；[2] 在困难和挑战面前，不愿付出努力；[3] 容易放弃容易受到失望、沮丧的情绪影响；[4] 面对问题采取等待观望的态度"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentAvoidanceBehavior = ContentAvoidanceBehavior + "一般来说，您具有明显的回避困难、挫折和失败的倾向。可能的表现为：；[1] 不能坦然面对现实环境，经常报怨或逃避；[2] 不能坚守既定的目标，缺乏自信，消极退缩；[3] 常常将潜在困难看得比实际上更严重，往往感到沮丧和失望；[4] 自甘落后，回避困难，得过且过"
            if i['name'] == "幻想行为":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentFantasies = ContentFantasies + "一般说来，您是一位理性的、现实的人，能够正确的面对和应付困难。可能的表现为：；[1] 通常是现实主义者，不喜欢幻想，对现实持有清醒的认识；[2] 能够正面的看待问题，并专注于问题解决；[3] 能理智地应付困难."
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentFantasies = ContentFantasies + "一般说来，您比较理性，能够正确看待问题。可能的表现为：；[1] 很少幻想，对现实持有比较清醒的认识；[2] 解决问题比较专注，不易受外部打扰"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentFantasies = ContentFantasies + "一般说来，您不太能够正确的面对问题和困难. 可能的表现为：；[1] 面对问题会产生一些不切实际的幻想；[2] 在处理问题时注意力不能集中，容易受外部干扰"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentFantasies = ContentFantasies + "一般说来，您在应对问题的方式不太成熟。可能的表现为：；[1] 不愿意正视问题的存在，经常沉迷于幻想而逃避现实的压力；[2] 在处理问题时经常性的分散注意力"
            if i['name'] == "自责行为":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentSelfReproach = ContentSelfReproach + "一般来说，您在遇到挫折和困难时有较强的信心。可能的表现为：；[1] 能正确地认识自己，正面对待自己的经历；[2] 能够客观的评估自己的能力与不足；[3] 信任自己解决问题的能力，不轻易动摇"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentSelfReproach = ContentSelfReproach + "一般来说，您在遇到挫折和困难时比较有信心，可能的表现为：；[1] 比较能正确地认识自己，正面对待自己的经历；[2] 基本上能够客观的评估自己的能力；[3] 比较自信,信任自己解决问题的能力，不轻易动摇"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentSelfReproach = ContentSelfReproach + "一般来说，您在遇到挫折和困难时有责怪自己的倾向。可能的表现为：；[1] 对自己的困难和失败不能坦然接受，对自己的认识不够客观；[2] 忽略自己的优势，夸大自己的缺陷，产生消极的自我评价；[3] 难以正确对待自己的不足、并进行调整和修正"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentSelfReproach = ContentSelfReproach + "一般来说，您在遇到挫折和失败时有明显的自责倾向。可能的表现为：；[1] 对自己的困难和失败不能坦然接受，完全否定自己；[2] 认为自己能力不足而放弃解决问题的努力；[3] 不能正确面对自己的不足，放弃进行调整和修正"
            if i['name'] == "强迫行为":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentCompulsion = ContentCompulsion + "一般说来，您非常理性，从不为毫无根据的想法而烦恼，也不会反复去做毫无意义的事情。可能的表现为：；[1] 不是充满疑虑的人，不会时刻担心细菌、病毒的侵入，也不会反复检查煤气管道、电源开关等物件；[2] 可以有效地控制自己的思维活动，随时可以把那些奇怪的、荒谬的念头抛开；[3] 行为举止很正常，没有任何需要反复进行否则就会感到焦虑的行为习惯或癖好；[4] 对生活和工作的掌控能力比较强，不会夸大犯错的后果，也不会因此惴惴不安"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentCompulsion = ContentCompulsion + "一般说来，您比较理性，很少为毫无根据的想法而烦恼，也很少反复去做毫无意义的事情。可能的表现为：；[1] 如果明知某些念头是荒谬的、不合理的，或者觉得某些行为是过分的、无关紧要的，会有意压抑这些念头、克制这些行为；[2] 相信自己，对刚刚做完的事情比较放心，很少反复去检查；[3] 可以有效地控制自己的思维活动，适时摆脱不必要的联想或回忆；[4] 没有比较奇怪的生活习惯，也没有顽固而难以变通的行为风格；[5] 对生活和工作的掌控能力比较强，很少会夸大犯错后果，也很少会因此惴惴不安"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentCompulsion = ContentCompulsion + "一般说来，您相对理性，但有时可能为毫无根据的想法而烦恼，或者反复去做毫无意义的事情。可能的表现为：；[1] 明知某些念头是荒谬的、不合理的，或者觉得某些行为是过分的、无关紧要的，有时却无法压抑这些念头、克制这些行为；[2] 可以比较有效地控制自己的思维活动，但有时摆脱不了某些不良的念头，也难以制止某些不必要的联想或回忆；[3] 对自己信心不足，对那些刚刚做完的事情不够放心，经常去反复检查；[4] 做事的方式比较固定，很少变通，可能存在比较奇怪的生活习惯"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentCompulsion = ContentCompulsion + "一般说来，您已出现比较明显的强迫症症状，被某些不必要的念头、毫无意义的行为习惯所困扰，甚至痛苦万分。可能的表现为：；[1] 明知某些念头是荒谬的、不合理的，或者觉得某些行为是过分的、无关紧要的，却无法压抑这些念头或者克制这些行为；[2] 缺乏自信，对自己做过的事情总是持怀疑态度，而需要反复检查才能安心；[3] 难以有效地控制自己的思维活动，往往摆脱不了某些不良的念头，也难以制止某些不必要的联想或回忆，因此不仅很苦恼，而且严重影响了日常的工作与生活；[4] 为人处世有固定的行为方式，会严格遵循某些套路，不知变通"
            if i['name'] == "偏执心理":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentParanoia = ContentParanoia + "一般来说，您是一位通情达理、灵活变通的人，有可能的表现为：；[1] 乐于信任别人，极少怀疑别人的动机和愿望；[2] 心胸宽广，很少记恨别人，能够坦然宽容接受别人的过错；[3] 对自己有清晰的认识，能客观评估自己的能力"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentParanoia = ContentParanoia + "一般来说，您通情达理，通常情况下也愿意信任别人。可能的表现为：；[1] 通常能够信任别人，较少对别人的动机产生疑虑；[2] 心胸较为宽广，一般不会记恨别人；[3] 多数情况下，能够积极正面的认识别人的行为和态度，乐于与别人建立良好关系；[4] 对自己的认识比较清晰，很少高估自己的能力"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentParanoia = ContentParanoia + "一般来说，您已经表现出轻微的偏执倾向，有时敏感多疑、固执任性，可能的表现为：；[1] 有时敏感多疑，较多的信任自己，不轻易信任别人；[2] 有时不能开放坦然的正确理解和认识别人友好的行为；[3] 有时不能正确、客观地分析形势，有问题易从个人感情出发，主观片面性大；[4] 对自己的能力有较高估计，自视甚高"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentParanoia = ContentParanoia + "一般来说，您已经呈现比较明显的偏执倾向，敏感多疑、固执己见，甚至极易记恨，可能的表现为：；[1] 极度感觉过敏，对侮辱和伤害耿耿于怀，思想行为固执死板，敏感多疑、心胸狭隘；[2] 过度的自信，且只信任自己，不信任别人；[3] 过分警惕和抱有敌意，常将别人无意的、非恶意的甚至友好的行为误解为敌意或歧视，或无足够根据的怀疑会被人利用或伤害；[4]对自己的能力估计过高，在工作上往往言过其实"
            if i['name'] == "嫉妒心理":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentJealousy = ContentJealousy + "一般来说，您是一位心胸豁达，心态平和的人。可能的表现为：；[1] 对自己有清晰的认识，客观理性的评估自己的能力；[2] 能够正确看待别人的长处和优点，并能由衷赞美别人的成绩和能力；[3] 往往表现出热情、喜悦、生活充满动力，具有较高的工作效率；[4] 极好的适应能力，能够坦然面对现实环境，以客观的态度面对现实，冷静地判断事实，理性地处理问题，并形成积极应变的心态"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentJealousy = ContentJealousy + "一般来说，您的心胸较为豁达，心态较为平和。可能的表现为：；[1] 对自己的认识较为客观，很少高估自己的能力和价值；[2] 一般能够认可别人的成绩和荣誉，不会贬低别人的能力和价值；[3] 通常情况下，工作充满热情和动力，效率较高"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentJealousy = ContentJealousy + "一般来说，您表现出轻微的嫉妒倾向，有时心胸不够豁达，心态不够平和。可能的表现为:；[1] 自我感觉良好，对自己能力和价值的评价较高；[2] 有时不太认可别人的成绩和荣誉，不能客观的认识别人的能力和价值；[3] 有时缺乏乐观向上的进取心，以致影响工作效率"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentJealousy = ContentJealousy + "一般来说，您已经表现出明显的嫉妒倾向，心胸较为狭隘，心态不平衡。可能的表现为：；[1] 自我感觉非常好，过度高估自我价值和能力；[2] 习惯否定别人的成绩和荣誉，同时贬低别人的能力和价值；[2] 遇到他人优于自己的情境时，产生难以克制的痛苦感，即使是一点小事；[3] 有时缺乏信心，丧失动力，工作积极性和效率明显降低"
            if i['name'] == "人际适应":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentInterpersonalAdaptation = ContentInterpersonalAdaptation + "一般说来，您是一个外向、热情、善解人意的人，不会在细节上纠缠不清，也不会自我封闭。可能的表现为：；[1] 心胸宽广，能够分辨别人说话的意图，对无心之言、玩笑话不会放在心上，更不会生气、愤恨；[2] 非常自信，喜欢表达和展现自己，能够坦然面对别人的拒绝、冷落和负面评价；[3] 您待人宽厚，信任他人，不会仅仅从个人立场出发考虑问题；[4] 心理能量很强大，乐观大方，能够从容、坦荡地与他人交往；[5] 经常参加各种社交活动，乐意和别人打交道，并能以淡定的心态处理人际冲突或矛盾"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentInterpersonalAdaptation = ContentInterpersonalAdaptation + "一般说来，您是一个比较外向、热情、善解人意的人，很少在细节上纠缠不清，也很少在社交活动上退缩。可能的表现为：；[1] 为人宽厚，通常能够分辨别人说话的意图，对无心之言、玩笑话不会放在心上，更不会生气、愤恨；[2] 比较自信，往往喜欢表达和展现自己，能够坦然面对别人的拒绝、冷落和负面评价；[3] 比较乐观大方，能顾及他人的感受，通常能够从容、坦荡地与他人交往；[4] 乐于参加各种社交活动，愿意和别人打交道，通常情况下能以淡定的心态处理人际冲突或矛盾"
                elif i['score'] >= 16 and i['score'] <= 20:
                    ContentInterpersonalAdaptation = ContentInterpersonalAdaptation + "一般说来，您是一个相对大度、宽容、善解人意的人，但有时会在细节上纠缠不清，或者回避与他人的交往。可能的表现为：；[1] 心胸较为宽广，基本能够分辨别人说话的意图，对无心之言、玩笑话很少放在心上，也很少会生气、愤恨；[2] 相对理性，但有时会把自己的想法投射到现实中，或者仅仅从个人立场出发考虑问题；[3] 心理能量不够强大，自信心不足，一般情况下能够从容、坦荡地与他人交往；[4] 在需要的时候您会出席各种社交场合，愿意和别人打交道，一般能以平常心处理人际冲突或矛盾"
                elif i['score'] >= 21 and i['score'] <= 25:
                    ContentInterpersonalAdaptation = ContentInterpersonalAdaptation + "一般说来，您不够大度、宽容和善解人意，有时会在细节上纠缠不清，或者刻意回避与他人的交往。可能的表现为：；[1] 心胸不够宽广，有时分辨不清别人说话的意图，因而把无心之言、玩笑话放在心上，甚至生气、愤恨；[2] 比较感性，有时会把自己的想法投射到现实中，或者仅仅从个人立场出发考虑问题，情绪波动较大；[3] 心理能量相对弱小，缺乏自信心，有时难以从容、坦荡地与他人交往；[4] 对参加社交活动缺乏积极性，也很少主动和别人搭话，有时无法用平常的心态处理人际冲突或矛盾"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentInterpersonalAdaptation = ContentInterpersonalAdaptation + "一般说来，您在人际关系方面比较敏感，拒绝与别人建立亲密的关系，因而带来种种困惑和苦恼。可能的表现为：；[1] 常常在细节上纠缠不清，或者刻意回避与他人的交往；[2] 常常分辨不清别人说话的意图， 把无心之言、玩笑话放在心上，甚至生气、愤恨；[3] 十分感性，经常会把自己的想法投射到现实中，或者把细微的东西过度放大，情绪容易波动；[4] 心理能量比较弱小，骨子里比较自卑，常常难以从容、坦荡地与他人交往；[5] 不愿意参加社交活动，极少主动和别人搭话，常常无法用平常的心态处理人际冲突或矛盾"
            if i['name'] == "孤独感受":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentLonelyFeeling = ContentLonelyFeeling + "一般说来，您具有强大的、持久的精神支持，如亲情、友谊、爱情、信仰、兴趣等，关心与爱护您的人很多。可能的表现为：；[1] 能够以愉悦的方式消磨自己的空闲时间，而不会有寂寞、无所事事的感受；[2] 在遇到困难或者心情不好的时候，总是会有人帮助和安慰，有温暖、安心的感受；[3] 通常具备良好的人际关系，可以得到较多社会资源和支持；[4] 一个成熟、乐观的人,能积极应对竞争和压力、忍受拥挤和忙碌，以平和、恬淡的心态面对生活和工作"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentLonelyFeeling = ContentLonelyFeeling + "一般说来，您具有稳固的、持久的精神支持，如亲情、友谊、爱情、信仰、兴趣等，关心与爱护您的人比较多。可能的表现为：；[1] 通常能够以愉悦的方式消磨自己的空闲时间，而很少有寂寞、无所事事的感受；[2] 在遇到困难或者心情不好的时候，经常会有人帮助和安慰您，有温暖、安心感；[3] 通常具备和谐的人际关系，可以得到一定的社会资源和支持；[4] 往往是一个成熟、乐观的人，能以积极的态度应对竞争和压力、忍受拥挤和忙碌，并能较好地控制自己的情绪"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentLonelyFeeling = ContentLonelyFeeling + "一般说来，您具有比较稳固的、持久的精神支持，如亲情、友谊、爱情、信仰、兴趣等，有一些关心与爱护您的人。可能的表现为：；[1] 往往能够以愉悦的方式消磨自己的空闲时间，但有时可能会产生寂寞、无聊、烦闷的感觉；[2] 在遇到困难或者心情不好的时候，您往往可以找到合适的人帮助和安慰自己；[3] 通常具备比较和谐的人际关系，可以得到一定的社会资源和支持；[4] 比较成熟与乐观，基本上能以积极的态度应对竞争和压力、忍受拥挤和忙碌，并能合理地控制自己的情绪"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentLonelyFeeling = ContentLonelyFeeling + "一般说来，您欠缺比较稳固的、持久的精神支持，如亲情、友谊、爱情、信仰、兴趣等，几乎没有关心与爱护您的人。可能的表现为：；[1] 往往以一个人独处的方式来消磨空闲时间，常常有寂寞、无聊、烦闷的感觉；[2] 在遇到困难或者心情不好的时候，往往找不到合适的人来帮助和安慰自己，总觉得自己被周围人忽视或遗忘；[3] 往往缺乏安全感，人际关系不是很好，难以得到充分的社会资源和支持；[4] 容易悲观、情绪低落，经常以消极的态度应对竞争和压力、忍受拥挤和忙碌，有时无法适当地控制自己的情绪"
            if i['name'] == "依赖心理":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentAnaclisis = ContentAnaclisis + "一般来说，您具有较好的独立性、自主性和创造性，可能的表现为：；[1] 具有较强的理性思维，情绪控制能力较强，积极参与决策的讨论和制定；[2] 客观理性的评价自己，积极肯定认可自我价值和优势；[3] 以自己的价值取向和思维方式进行决策，不依附别人，也不受别人摆布；[4] 尊重别人的思想和意志，不以自己的利益去驾驭别人的事，不以自己的意志束缚任何人；[5]在与别人交往中保持自身的独立性，并以个体的独立价值积极参与社会活动"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentAnaclisis = ContentAnaclisis + "一般来说，您基本认可自我价值，具有一定的自主进取精神和独立意识。可能的表现为：；[1] 偏理性，能够控制自我情绪，并参与决策讨论和制定；[2] 积极认可自我能力和自我价值；[3] 不会对别人提出过多不合理的要求和期望；[4] 不依附别人，对事物能够独立的进行判断和作出决策"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentAnaclisis = ContentAnaclisis + "一般来说，您呈现出轻微的依赖倾向，有时缺乏独立意识，甚至自感无能。可能的表现为：；[1] 有时敏感多思，依恋别人，不太注意自己参与决策的能力；[2] 有时缺乏自主性和创造性，需要作出决策时，需要征求大量的建议和保证；[3] 有时自我贬低，认为别人比自己优秀，比自己有吸引力，比自己能干；[4] 主动精神较弱，有时被动服从别人的愿望和要求，即使不够合理；[5] 有时产生被人遗弃的想法和念头。"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentAnaclisis = ContentAnaclisis + "一般来说，您已呈现比较明显的依赖症状，缺乏活力，缺乏独立意识，甚至自感无能，可能的表现为：；[1] 在没有从别人处得到大量的建议和保证之前，对日常事物不能作出决策；[2] 无助感，让别人为自己作大多数的重要决定，如在何处生活，该选择什么职业等；[3] 深怕被人遗弃，一些基本目标常常只能在别人予以协助之下才能达到；[4] 无独立性，很难单独展开计划或做事；[5] 过度容忍，为讨好别人甘愿做低下的或自己不愿做的事；[6] 缺乏自尊自重，把自己看作是毫无能力的、必须依附别人的人，经常通过自我贬低以求获得别人的帮助；[7] 往往对别人有过多的不易被人理解的要求，在各方面总是寄希望于得到帮助和依靠"
            if i['name'] == "猜疑心理":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentSuspicions = ContentSuspicions + "一般说来，您是一位友善、合作的人，愿意相信别人。可能的表现为：；[1] 对他人的看法比较正面、积极，相信人性的善良，愿与他人协作；[2] 信任别人，愿意和别人建立关系，没有充分的证据，极少怀疑别人的动机；[3] 即使遇到不快，也能控制自己的情绪，而极少在语言和行为上攻击他人；[4] 比较坦率和豁达，很少记仇，不会将负面情绪带入以后的工作中"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentSuspicions = ContentSuspicions + "一般说来，您待人友好，具备较强合作性，通常情况下也愿意相信别人。可能的表现为：；[1] 对他人的看法相对积极和正面，相信别人有“善”的一面；[2] 不大喜欢与别人争论，有了误解或矛盾，愿意心平气和地进行沟通；[3] 多数时候能控制自己的情绪，以避免给工作和生活带来不良影响；[4] 一般不会选择对抗，大体上信赖他人，很少捕风捉影，鲜有过度敏感之时；[5] 通常愿意与别人建立友好的关系，很少对别人的动机心存疑虑"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentSuspicions = ContentSuspicions + "一般说来，您待人相对友好，具备一定的合作性，但不大相信别人，有较强的戒备心。可能的表现为：；[1] 对他人的看法有时是消极和负面的，甚至认为多数时候人是冷漠自私的；[2] 担心别人损害您的利益，可能出现过激情绪反应，并采取对抗排斥的应对方式；[3] 有时过度敏感，并可能对某些人持有敌意和怀疑，并将这种态度保持一段时间"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentSuspicions = ContentSuspicions + "一般说来，您是一位比较难相处的人，待人不够友善，不大愿意和别人亲近，合作性也比较差。可能的表现为：；[1] 对别人的看法往往是负面的和消极的，觉得人都是自私冷漠的,时刻保持警惕，对别人的言行举止的想法往往是过激的、甚至扭曲的；[2] 常常难以控制自己的情绪，有过摔东西、撕文件等行为，并对别人恶言相向；[3] 过于敏感，认为别人对自己存在敌意，甚至要故意伤害自己；[4] 采取敌对的方式处理问题，给工作和人际交往制造了巨大的障碍"
            if i['name'] == "焦虑情绪":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentAnxiety = ContentAnxiety + "一般说来，您是一位从容镇定、乐观豁达、心情愉悦的人。可能的表现为：；[1] 能坦然面对各种压力，并能巧妙地、高效地解决各种问题；[2] 对周围环境的掌控能力很强，对可能发生的事情有着准确的预期；[3] 性格比较随和，擅长交际，并可能喜欢在公众场合表现自己；[4] 身体健康，没有受到疾病、疼痛、不适、衰弱的困扰；[5] 心态很好，淡泊名利，极少有偏激的想法或看法，对人对事都比较宽容；[6] 往往按照惯常的方式做事，遵循既有的规则，时间管理能力也比较好，很少拖沓"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentAnxiety = ContentAnxiety + "一般说来，您的焦虑水平较低，很少因为工作和生活方面的事情而烦躁不安，常常给人从容淡定的感觉。可能的表现为：；[1] 能冷静地面对各种问题，即使自己无法解决，也很少慌乱或害怕；[2] 身体比较健康，即使稍有不适或病痛，也不会因此而苦恼；[3] 自信心比较强，对自己内在价值的认同比较高，很少在上司或权威面前惊慌失措；[4] 为人宽厚，善待别人，很少卷入名利之争，也很少有偏激的、扭曲的想法；[5] 时间管理能力比较强，较少拖沓，即使没有及时完成工作任务，也会因开朗、豁达的性格而保持表面的镇静"
                elif i['score'] >= 16 and i['score'] <= 20:
                    ContentAnxiety = ContentAnxiety + "一般说来，您的焦虑水平中等，有时为工作和生活中的麻烦事而烦躁。可能的表现为：；[1] 尚能适当地应付各种压力，但有时可能惊慌失措，产生不良情绪，带来困扰；[2] 身体相对健康，有时可能会担心身体的疾患与病痛；[3] 自信水平一般，对不确定的事情心存疑虑，对上司或权威心存敬畏；比较看重名利，有时会因为攀比、竞争而苦恼和担忧；[4] 有时瞻前顾后，做事顾虑太多、犹豫不决，并可能陷入痛失良机的懊悔之中；[5] 有时会延期完成任务，导致突击赶进度，并体验到一定程度的焦虑"
                elif i['score'] >= 21 and i['score'] <= 25:
                    ContentAnxiety = ContentAnxiety + "一般说来，您的焦虑水平较高，经常为工作和生活中的事情而烦恼，甚至担心受怕。可能的表现为：；[1] 能勉强应付各种问题，但有时力不从心，在压力面前你可能心情烦躁，采用拖拉、回避等消极方式来应对问题；[2] 可能出现负面情绪，还可能出现头晕、胸闷、尿频、出汗等躯体症状，会因为身体的疾病、疼痛而苦恼不已；[3] 往往不知道如何以确切的方式向合适的人寻求帮助，如果您是那种情绪外露的人，则可能向周围人散播焦虑的气氛；[4] 可能觉得周围充满了不确定的因素，为了增强安全感，可能竭力争夺；[5] 自我要求比较严格，有时对自身的能力、工作的进度把握不好，造成拖延，并因此体验到强烈的不安"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentAnxiety = ContentAnxiety + "一般说来，您是一个非常容易焦虑的人，缺乏安全感和掌控感，甚至陷入长期的焦躁和不安之中。可能的表现为：；[1] 面对日常工作与生活的一些问题，您往往觉得力不从心、身心疲惫，不知道如何妥善应付；[2] 有时您会无缘无故地觉得紧张，或者稍遇挫折就会情绪崩溃，给工作和生活带来严重的负面影响；[3] 经常觉得身体不舒服，长期受到疾病、疼痛的困扰，严重的时候甚至产生绝望的念头；[4] 即使您的工作能力很强，内心的力量也比较弱小，在很多场合您缺乏自信，也没有安全感；[5] 可能时间管理能力比较差，没有固定的做事习惯和工作流程，总是匆匆忙忙地赶任务，并且难以保证任务完成的质量；[6] 较难适当地表达和控制自己的情绪，对别人不够宽容，人际关系可能比较紧张；[7] 对自己的评价可能不够准确，对自身的要求比较苛刻，在理想和现实之间难以找到平衡或妥协之处。"
            if i['name'] == "冲动控制":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentImpulsiveControl = ContentImpulsiveControl + "一般来说，您是一位成熟理智而沉着冷静的人，待人比较友善。可能的表现为：；[1] 情绪状态非常稳定，极少出现突然的暴怒，情绪控制能力也较强；[2] 行为比较慎重，倾向于规避风险，做事情顾及后果，很少冲动；[3] 语言和思维能力正常，遇事能够冷静对待，并能很好的控制和调节语言举止；[4] 头脑冷静，能够平心静气、毫无偏见地分析道理而不感情用事"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentImpulsiveControl = ContentImpulsiveControl + "一般来说，您比较成熟理智，为人处世相对沉着冷静。可能的表现为：；[1] 情绪状态比较稳定，很少暴躁、发火；[2] 通常情况下，行为较为谨慎，较少冲动，采取行动之前会考虑行为的后果；[3] 一般遇事较为冷静，较好控制协调语言举止"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentImpulsiveControl = ContentImpulsiveControl + "一般来说，您已经表现出轻微的冲动症状，情绪波动较大。可能的表现为：；[1] 有时情绪不够稳定，因一件小事而大发雷霆、大动干戈；[2] 有时比较冲动，做事也常常忽略后果；[3] 有时遇事不够冷静，意识狭隘，贸然行事，不能较好控制自己的语言举止"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentImpulsiveControl = ContentImpulsiveControl + "一般来说，您已经表现出明显的冲动症状，常因微小刺激爆发强烈而难以控制的愤怒情绪，可能的表现为：；[1] 情绪控制不够稳定，往往突然暴怒，通常缺乏理智且带有盲目性；[2]稍不如意就怒火直冒、行为冲动，且不计后果和难以遏制；[3] 事后对发作时的所作所为感到后悔，甚至自责，但不能防止失控冲动的再次发生，具有明显的阵发性特点；[4]在强烈的感情冲动期间，意识明显狭隘，认知片面、判断力下降、注意范围缩小，难以控制和调节语言举止"
            if i['name'] == "抑郁倾向":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentDepressiveTendency = ContentDepressiveTendency + "一般说来，您是一位开朗、愉悦、乐观的人，精神比较饱满，能以积极、平和的心态面对日常的工作与生活。可能的表现为：；[1] 极少情绪低落、悲观失望，而往往意气风发、笑容满面；[2] 觉得生活很充实，有很多有趣的、值得做的事情，如交友、培养兴趣爱好等；[3] 思维和语言功能正常，反应灵敏；[4] 自信，并在一定程度上悦纳自己，觉得自己是一个有用的、有价值的人；[5] 身体健康，饮食睡眠状况良好，精力也比较充沛；[6] 喜欢与别人交往，人际关系良好，态度宽容、随和，经常给人阳光、活泼的感觉；[7] 能坦然接受社会现实，即使遭遇挫折和打击，也能勇敢地面对"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentDepressiveTendency = ContentDepressiveTendency + "一般说来，您是一位比较积极乐观、活泼开朗的人，能以适当的方式应对工作与生活中的各种问题。可能的表现为：；[1] 往往情绪状态良好，待人接物乐观积极，给别人愉悦、舒适的感觉；[2] 愿意与别人交往，并得到别人的理解和帮助；[3] 对身边的事物持有一定的兴趣，并有精力和体力参与各项活动；[4] 很少悲观，对前途保有一些期望，对自己也比较有信心；[5] 身体状况比较良好，没有遭受严重疾病、疼痛的侵袭，饮食睡眠也相对正常；[6] 思维和意志功能比较正常，能够对环境和事件做出合理的判断；[7] 受挫能力比较强，能坦然面对一般的压力，并妥善处理身边的问题"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentDepressiveTendency = ContentDepressiveTendency + "一般说来，您的情绪有一定的波动，在处境顺利、心满意足时愉快、乐观，但在遭受挫折、面对困难时则可能悲观失望。可能的表现为：；[1] 易受环境的影响，有时会因为环境的变化而心情大变；[2] 心情不好的时候不愿交往，甚至闭门不出，对既往的爱好也不屑一顾；[3] 思维和意志功能比较正常，但沮丧的时候容易犯糊涂和走神；[4] 不是非常自信，有时对前途感到迷惘，对近况感到失落；[5] 有时会受到疾病、疼痛的困扰，如胸闷、肠胃不适、便秘等，有时食欲不振，睡眠不佳，精神疲惫；[6] 抗压能力一般，有时会在困难面前惊慌失措"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentDepressiveTendency = ContentDepressiveTendency + "一般说来，您已呈现比较明显的抑郁症状，经常情绪低落、悲观失望，甚至产生厌世轻生的念头。可能的表现为：；[1] 常郁郁寡欢，对周围事物毫无兴趣，觉得生活是一种负担，有度日如年的感觉；[2] 常身心疲惫，对工作缺乏热情，注意力难以集中，严重影响了工作效率；[3] 觉得没有前途和希望，很不自信，怀疑自己的价值；[4] 在人际交往方面消极被动，缺乏与人沟通的意愿；[5] 思维能力有所下降，记忆力减退，行动也比较迟缓；[6] 经常生病，饮食和睡眠状况比较差，有时性功能也遭到衰竭；[7] 经常早醒，然后无法入睡，陷入悲哀的情绪之中，体重也有明显下降的趋势；[8]常感到焦虑，以批判、否定的态度看待自己，甚至有自罪观念"
            if i['name'] == "环境适应":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentEnvironmentalAdaptation = ContentEnvironmentalAdaptation + "一般说来，您的社会适应能力很强，能根据环境的变化、自身的发展来调整个人的需求，以积极的态度面对工作和生活中的困难。可能的表现为：；[1] 具备良好沟通技巧，能迅速和周围的人建立关系，甚至左右逢源、讨人喜欢；[2] 非常理性，制定的计划切合实际，操作性强，容易被别人接受；[3] 与环境保持适宜的接触，但不是只注重眼前利益的人；[4] 能够忍受一时的挫折和痛苦，能延迟满足；[5] 价值观与社会主流价值观趋同或者兼容，能对个人需求做适当的追求"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentEnvironmentalAdaptation = ContentEnvironmentalAdaptation + "一般说来，您的社会适应能力较强，通常能根据环境的变化、自身的发展来调整个人的需求，以比较积极的态度面对工作和生活中的困难。可能的表现为：；[1] 具备较好的沟通技巧，能与周围人建立和谐的关系；[2] 比较理性，制定的计划通常切合实际，操作性较强，容易被别人接受；[3] 能够从失败中吸取教训，逐渐积累经验，做事比较坚持，能忍受一时挫折和痛苦；[4] 价值观与社会主流价值观基本趋同或者兼容，能对个人需求做适当的追求"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentEnvironmentalAdaptation = ContentEnvironmentalAdaptation + "一般说来，您的社会适应能力欠佳，有时难以根据环境的变化、自身的发展来调整个人的需求，态度也不够积极。可能的表现为：；[1] 欠缺较好的沟通技巧，不善与人交往，可能需要花很长时间才能融入新的环境；[2] 有时冲动任性，想法过于单纯，提出的建议不切实际；[3] 通常能够从失败中吸取教训，逐渐积累经验，但做事缺乏毅力，缺乏长远的眼光，比较容易感到困惑和苦闷；[4] 价值观与社会主流价值观可能存在一些冲突，有时显得有些自私；[5] 抗挫折能力不是很强，有时难以克制自己的负面情绪"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentEnvironmentalAdaptation = ContentEnvironmentalAdaptation + "一般说来，您的社会适应能力严重不足，难以根据环境的变化、自身的发展来调整个人的需求，为人处世的态度也比较消极。可能的表现为：；[1] 欠缺基本的沟通技巧，不善与人交往，需要花很长时间才能融入新的环境；[2] 往往冲动任性，想法过于单纯，提出的建议不切实际；[3] 难以从失败中吸取教训，缺乏毅力，缺乏长远眼光，容易感到困惑和苦闷；[4] 价值观与社会主流价值观存在较大的冲突，有时过于自私；[5] 抗挫折能力比较差，经常难以克制自己的负面情绪"
            if i['name'] == "恐惧心理":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentFear = ContentFear + "一般说来，您是一位胆大的、泰然自若的人，遇事不慌不乱。可能的表现为：；[1] 在社交场合表现自如，即使有人盯着你看，也不会觉得不自在；[2] 敢于在公众场合表达，甚至喜欢在大庭广众之下演讲或者表演；[3] 没有什么场所或空间让您觉得害怕，可以镇定地出入各种场合；[4] 没有任何“怕得要命”的东西，即使受了惊吓，也会很快恢复过来；[5] 身体健康，极少出现胸闷、呼吸困难、晕厥，对生活和工作的把控能力很强"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentFear = ContentFear + "一般说来，您的胆子比较大，遇事很少慌乱，比较镇定自若。可能的表现为：；[1] 没有因什么生活事件或事物受到严重惊吓而留下心理阴影；[2] 可以在社交场合表现自如，比较轻松、愉快地和别人交流，但不大希望自己成为别人关注的焦点，否则您可能觉得浑身不自在；[3] 对空旷的场地没有任何恐惧，对拥挤的、密闭的房间或交通工具也毫不害怕；[4] 偶尔有一两样事物让您感到害怕，但程度并不深，恐惧的情绪消散得也比较快"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentFear = ContentFear + "一般说来，您的胆子比较大，遇事很少慌乱，比较镇定自若。可能的表现为：；[1] 没有因什么生活事件或事物受到严重惊吓而留下心理阴影；[2] 可以在社交场合表现自如，比较轻松、愉快地和别人交流，但不大希望自己成为别人关注的焦点，否则您可能觉得浑身不自在；[3] 对空旷的场地没有任何恐惧，对拥挤的、密闭的房间或交通工具也毫不害怕；[4] 偶尔有一两样事物让您感到害怕，但程度并不深，恐惧的情绪消散得也比较快"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentFear = ContentFear + "一般说来，您已经出现比较明显的恐惧症症状，对特定的事物或场景有着强烈的、不必要的恐惧，并伴随回避、退缩行为。可能的表现为：；[1] 可能对社交场合避而远之，觉得浑身不自在，难以和别人自然地交流；[2] 往往不够自信，没有悦纳自己，或者对自己的要求过高，一旦觉得自己无法胜任工作或者应付某些问题，就会失望、痛苦和害怕；[3] 可能害怕一个人去空旷的地方，或者对拥挤的、密闭的房间或交通工具心怀畏惧；[4] 当恐惧袭来的时候，往往无法摆脱,感到绝望、崩溃，出现胸闷、脸色苍白、心悸等症状，甚至当场昏厥"
            if i['name'] == "身心同一":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentBodyAndMind = ContentBodyAndMind + "一般说来，您是一位现实主义者，有责任心，可信赖。可能的表现为：；[1] 认知、意志、运动等方面都很正常，没有出现病变或互不协调的情况；[2] 情绪比较稳定，有同情心，往往比较热情，注重有距离的交往；[3] 认同权威，尊敬真正有学问和能力的人，比较顺从；[4] 人际关系比较好，待人随和，比较合群；[5] 关心个人的成功和地位，对现实情况有清醒的认识，但在做决策时往往偏于保守；[6] 有兴趣参加一些社会活动，并在工作中保持一定的主动性；[7] 偶尔显得刻板，兴趣单调，缺乏想象力"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentBodyAndMind = ContentBodyAndMind + "一般说来，您比较注重现实，有较强的责任心，值得周围人的信赖。可能的表现为：；[1] 认知、情绪、意志、运动、感觉等方面的功能都比较正常；[2] 没有出现明显的病变或统合失调；[3] 兴趣爱好相对广泛，愿意和别人建立亲密的关系，待人比较友善和礼貌；[4] 喜欢具体的东西，也喜欢抽象思考，有时会和别人讨论，但往往固执己见；[5] 对权威比较尊重，对上司相对顺从，有时显得保守一些，缺乏竞争意识；[6] 情绪比较稳定，有时不善表达情感，甚至胆怯、怕羞"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentBodyAndMind = ContentBodyAndMind + "一般说来，您比较理想主义，富有想象力，看法、理念常常与别人不同。可能的表现为：；[1] 心智功能都基本正常，有时可能出现暂时的思维错乱、情感反常和意志消沉；[2] 兴趣爱好比较广泛，但注意力容易分散，往往缺乏毅力；[3] 情绪有时波动较大，出现社会退缩，如突然变得对人冷淡、不愿和别人说话等；[4] 比较喜欢抽象的东西，如哲理，但思考的内容别人往往难以理解；[5] 往往不是责任心很强的人，对上司和权威的尊重、顺从相对有限；[6] 在境遇不佳的时候，可能通过幻想或白日梦来回避现实"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentBodyAndMind = ContentBodyAndMind + "一般说来，您已出现比较明显的精神分裂症症状，思想已经脱离现实环境，在认知、情绪、意志、运动、感觉等方面存在种种功能障碍。可能的表现为：；[1] 有时思维混乱、缺乏逻辑与目的性，或者觉得思维被别人控制了；[2] 还可能出现一些妄想，如觉得有人想伤害您、身体某部分发生了奇异的变形、自己有高贵的血统等；[3] 可能出现一些幻觉，如看到不存在的图像，或听到空气中有人对你说话；[4] 性格比较孤僻，不愿和别人打交道，懒散，工作与生活的能力严重下降；[5] 情感非常冷淡，经常面无表情，没有同情心，也难以理解别人的感受；[6] 在别人看来，您经常做些奇怪的事情，甚至荒谬可笑"

        report04['msg']["ContentSomaticReaction"] = ContentSomaticReaction
        report04['msg']["ContentAvoidanceBehavior"] = ContentAvoidanceBehavior
        report04['msg']["ContentFantasies"] = ContentFantasies
        report04['msg']["ContentSelfReproach"] = ContentSelfReproach
        report04['msg']["ContentCompulsion"] = ContentCompulsion
        report04['msg']["ContentParanoia"] = ContentParanoia
        report04['msg']["ContentJealousy"] = ContentJealousy
        report04['msg']["ContentInterpersonalAdaptation"] = ContentInterpersonalAdaptation
        report04['msg']["ContentLonelyFeeling"] = ContentLonelyFeeling
        report04['msg']["ContentAnaclisis"] = ContentAnaclisis
        report04['msg']["ContentSuspicions"] = ContentSuspicions
        report04['msg']["ContentAnxiety"] = ContentAnxiety
        report04['msg']["ContentImpulsiveControl"] = ContentImpulsiveControl
        report04['msg']["ContentDepressiveTendency"] = ContentDepressiveTendency
        report04['msg']["ContentEnvironmentalAdaptation"] = ContentEnvironmentalAdaptation
        report04['msg']["ContentFear"] = ContentFear
        report04['msg']["ContentBodyAndMind"] = ContentBodyAndMind
        report04['msg']["ChartYellowIndex"] = ChartYellowIndex
        report04['msg']["ChartOrangeIndex"] = ChartOrangeIndex
        report04['msg']["ChartRedIndex"] = ChartRedIndex
        report04['msg']['Validation'] = v1
        res = {"code": 0, 'detail': {'report_data': report04}}
        print('发送到word服务的数据:%s' % res)
        return res
    elif report_type_id == "PsychologicalCapital":
        try:
            report05 = d['detail']['report_data']
            print('report05打印：%s' % report05)
        except Exception as e:
            res = {"code": 40400, 'detail': {'report_data': e}}
            return res
        print(9999999999999999)
        print()
        chart_data = report05['msg']['ChartDataModel']
        print(chart_data)
        v = report05['msg']['Validation']
        v1 = ''
        if v >= 4:
            v1 = v1 + '不能按照自己的实际情况如实做答测验问题，测验结果不能很好地反映其自身的特点。'
        else:
            v1 = v1 + '回答真实可信，能够按照自己的实际情况如实做答，测验结果能够反映其自身的特点。'
        # print(chart_data)
        # 典型特征-优势特征
        ContentAdvantageFeature = ""
        # 典型特征-弱势特征
        ContentWeakFeature = ""

        ChartDataMotivation = []
        ContentMotivationdDescription = []
        ChartDataCognition = []
        ChartDataCognitionDescription = []
        ChartDataWill = []
        ContentWillDescription = []
        ChartDataMood = []
        ContentMoodDescription = []
        ChartDataTask = []
        ContentTaskDescription = []
        ChartDataPeople = []
        ContentPeopleDescription = []

        for i in chart_data:
            if i['score'] >= 75:
                # 黄色指标
                ContentAdvantageFeature = ContentAdvantageFeature + i['name'] + ","
            if 0 <= i['score'] < 30:
                # 黄色指标
                ContentWeakFeature = ContentWeakFeature + i['name'] + ","
            if i['name'] == "进取性":
                ChartDataMotivation.append({"name": i['name'], "score": i['score']})
                if 0 <= i['score'] < 30:
                    ContentMotivationdDescription.append({
                        "Aggressive": "获得成功的愿望稍差，不太喜欢挑战，容易安于现状，不会主动设置较高的目标，不能调动自身的能量来投入，在困难和挑战面前，不愿付出努力，容易放弃，需要依赖外部的刺激来驱动自己，前进动力不足。（极端低分：可能自甘落后，回避困难，得过且过。）"})
                elif 30 <= i['score'] < 75:
                    ContentMotivationdDescription.append({
                        "Aggressive": "有一定的追求成功的愿望，一般不会满足于现状，能够给自己设定具有一定挑战性的目标，为了目标的达成能够付出和努力行动。有时需要外部的一些肯定或激励才会持续地投入追求更高的目标和不断的完善和超越。"})
                elif i['score'] >= 75:
                    ContentMotivationdDescription.append({
                        "Aggressive": "具有强烈的渴望成功的愿望，勇于挑战现状，始终从自我价值的实现的角度设定自己的理想抱负和奋斗目标，并以此来激励自己，作为目标达成的动力，积极付出、努力行动，不断完善和超越。（极端高分：可能过于看重自己个人的成就，难以容忍些许的不足，给人以工作狂的印象。）"})
            if i['name'] == "支配性":
                ChartDataMotivation.append({"name": i['name'], "score": i['score']})
                if 0 <= i['score'] < 30:
                    ContentMotivationdDescription.append({
                        "Dominance": "工作中以自己的思想、意图影响控制他人和环境的愿望表现不充分，不愿意进行主导和影响、控制和安排，愿意服从和跟随，愿意接受安排和约束。（极端低分：可能过于被动、顺从，甚至丧失自我意志和主张。）"})
                elif 30 <= i['score'] < 75:
                    ContentMotivationdDescription.append(
                        {"Dominance": "工作中能够表现出一定的主导意愿，愿意通过自己的思想、意图影响他人和环境，能够进行组织、安排，面对外部环境的约束时，也会表现出相应的妥协。"})
                elif i['score'] >= 75:
                    ContentMotivationdDescription.append({
                        "Dominance": "工作中乐于支配和获得主导地位，喜欢以自己的思想和意图影响和改变他人和环境，喜欢组织、安排他人按自己的意愿行事，不愿受到约束。（极端高分：可能过于强势，忽略他人的感受，甚至带来关系的紧张。）"})

            if i['name'] == "亲和性":
                ChartDataMotivation.append({"name": i['name'], "score": i['score']})
                if 0 <= i['score'] < 30:
                    ContentMotivationdDescription.append({
                        "Affinity": "人际合作取向低，易于自我中心。与他人交往、参加社交活动以及建立良好关系的愿望很弱，不能从他人的角度思考问题，较难理解他人的需求和感受，不在乎是否受到欢迎，不会主动提供帮助，较难相处，亲和力较差。（极端低分：怀疑他人，待人疏远，自我中心，难以合作，可能孤傲、冷漠、无情的印象，给人可能存在人际关系不良。）"})
                elif 30 <= i['score'] < 75:
                    ContentMotivationdDescription.append(
                        {
                            "Affinity": "人际交往中，能够从他人的角度考虑问题，理解、尊重并信任他人，待人比较热情，能够关注自己给人留下的印象，在别人需要时能够提供帮助和支持，愿意与他人打交道，进行合作和建立关系。"})
                elif i['score'] >= 75:
                    ContentMotivationdDescription.append({
                        "Affinity": "人际交往中，设身处地为他人着想，善解人意，言行举止透露出对他人的信任和尊重，待人热情，受人欢迎，乐于助人、合作，注重与人建立良好的人际关系。（极端高分：可能过于关注给别人留下好印象而过分取悦他人，甚至有时会放弃原则或过度迁就他人。）"})

            if i['name'] == "开放性":
                ChartDataCognition.append({"name": i['name'], "score": i['score']})
                if 0 <= i['score'] < 30:
                    ChartDataCognitionDescription.append({
                        "Openness": "通常情况下局限于原有思维模式或习惯，比较保守，不愿接纳和尝试新事物，排斥多样性，不能容忍不确定性的模糊情境，对改革或变化持批驳和抵触，难以根据情境的变化适宜改变和修正自己的观点。（极端低分：观念僵化，思维封闭，抵制变化。）"})
                elif 30 <= i['score'] < 75:
                    ChartDataCognitionDescription.append({
                        "Openness": "通常情况下能够摆脱原有思维模式或习惯的束缚，愿意尝试新事物，不排斥变化和多样性，对不确定性的模糊情境有一定的适应性，愿意根据情境的变化适宜改变和修正自己的观点，实现自己的成长河进步。"})
                elif i['score'] >= 75:
                    ChartDataCognitionDescription.append({
                        "Openness": "不局限于既有的观念、思维模式的束缚，主动尝试新事物，主动接纳变化和多样性，对不确定性的模糊情境有较强的容忍力，善于根据情境的变化适宜改变和修正自己的观点，实现自己持续性的成长。）"})

            if i['name'] == "乐观性":
                ChartDataCognition.append({"name": i['name'], "score": i['score']})
                if 0 <= i['score'] < 30:
                    ChartDataCognitionDescription.append({
                        "Optimistic": "通常以消极的视角看待周围事物，对坏消息比较敏感，计较工作与生活中的得失，难以从正面的角度进行解释，对未来缺乏信心，较为悲观，有时会表现得很无助。（极端低分：可能过于悲观消沉，甚至消极厌世。）"})
                elif 30 <= i['score'] < 75:
                    ChartDataCognitionDescription.append({
                        "Optimistic": "通常会从正面的角度看待事物、现象和问题，对待工作和生活中的得失能够从正面的角度进行解释，能够从积极的方面憧憬未来，以比较愉悦的心情投入到工作和生活中，有时会受到负面信息的影响。"})
                elif i['score'] >= 75:
                    ChartDataCognitionDescription.append({
                        "Optimistic": "始终从正面积极的角度捕捉信息，看待各类事物、现象、问题，正面解释和对待对工作与生活中的得失，相信一切都会变得更好，对未来充满希望，踌躇满志并积极准备和投入。（极端高分：可能过于关注事物好的一面而过滤不好的一面，甚至伴随盲目的乐观。）"})
            if i['name'] == "变通性":
                ChartDataCognition.append({"name": i['name'], "score": i['score']})
                if 0 <= i['score'] < 30:
                    ChartDataCognitionDescription.append({
                        "Workability": "问题解决过程中，不具有从多角度思考问题的习惯，易于受既有框架和套路的局限和影响，问题解决的策略比较单一，对计划的执行较为僵化，突发事件应对的灵活性不足。（极端低分：可能思维过于僵化，视角单一，拘泥于简单的计划和原则。）"})
                elif 30 <= i['score'] < 75:
                    ChartDataCognitionDescription.append(
                        {
                            "Workability": "问题解决过程中，具有从不同的角度考虑问题的习惯，在问题不能有效解决时能够进行思路的转换，注意提供问题解决的备选方案，也能在过程中进行调整并应对突发的事件。"})
                elif i['score'] >= 75:
                    ChartDataCognitionDescription.append({
                        "Workability": "问题解决过程中，非常注重从不同的角度进行思考，灵活地转换思路，探索多样的问题解决策略，形成适宜解决方案并进行调整，灵活应对各种突发事件。（极端高分：可能思维过于发散和跳跃，易于频繁改变而产生无序。）"})

            if i['name'] == "内省性":
                ChartDataCognition.append({"name": i['name'], "score": i['score']})
                if 0 <= i['score'] < 30:
                    ChartDataCognitionDescription.append({
                        "Introspective": "工作生活中，不能接受外部提供的反馈信息，难以审视自己行动所隐含的信念、观点，不能对自己的思维过程、问题解决策略以及经验的适用性进行反思，回避自己的问题，极少进行总结、积累、校正和改进。（极端低分：对自己的认识可能产生较大的偏差，或者思维僵化的，或者呈现出得过且过的心态。）"})
                elif 30 <= i['score'] < 75:
                    ChartDataCognitionDescription.append({
                        "Introspective": "工作生活中，能够通过内外部信息的吸纳来审视自己行动所隐含的信念、观点，对自己的思维过程、问题解决策略以及经验的适用性进行一定的反思，基本能够正确对待自己的不足，并进行相应的总结、积累、校正、改进。"})
                elif i['score'] >= 75:
                    ChartDataCognitionDescription.append({
                        "Introspective": "工作生活中，经常积极吸纳内外部的信息，主动审视自己行动所隐含的信念、观点，检查自己的思维过程和问题解决策略，反思自己经验的适应性，勇于剖析自己的不足，并进行总结、积累、校正、改进、完善。"})

            if i['name'] == "独立性":
                ChartDataWill.append({"name": i['name'], "score": i['score']})
                if 0 <= i['score'] < 30:
                    ContentWillDescription.append({
                        "Independence": "行动时缺乏自己明确的目标性，倾向于依靠外在参照来作为行动的依据，回避一个人面对重要问题，较难独立判断和自主决定，没有主见，希望别人给自己拿主意，自己的立场和观点易于改变，屈从于别人的影响。（极端低分：可能过于依赖、回避，不能自主，易于丧失立场。）"})
                elif 30 <= i['score'] < 75:
                    ContentWillDescription.append(
                        {
                            "Independence": "能够明确自己行动的目的，能够独立思考，拥有自己的立场、观点，一定程度上能够自主决定，支配自己的言行并负责，有时会考虑并受到外界影响，能够接收别人的建议和批评。"})
                elif i['score'] >= 75:
                    ContentWillDescription.append({
                        "Independence": "具有自觉明显的目的性，充分认识到行动的意义，能够独立思考，有自己独立的立场、观点和主见，重要的问题能够自主决定并支配自己的行动，能够对自己的行动负责，愿意接受有益的建议和批评。（极端高分：过于强调行动的目的性以及个人意志，有时显得过于偏执，弹性不足。）"})

            if i['name'] == "坚韧性":
                ChartDataWill.append({"name": i['name'], "score": i['score']})
                if 0 <= i['score'] < 30:
                    ContentWillDescription.append({
                        "Resilience": "面对任务情境，具有明显的回避困难、挫折和失败的倾向，担心失败，不能坚守既定的目标，缺乏自信，消极退缩，常常将潜在困难看得比实际上更严重，往往感到沮丧和失望，缺乏心理承受能力。（极端低分：回避困难，消极退缩，易于半途而废。）"})
                elif 30 <= i['score'] < 75:
                    ContentWillDescription.append({
                        "Resilience": "面对任务情境，能够面对困难、挫折和失败，少有回避困难、挫折和失败的倾向，能够关注既定目标的完成，寻求解决办法，不会过分强调任务的困难和不可完成性，极少受到失望、沮丧等负面情绪的影响，有较强的心理承受能力。"})
                elif i['score'] >= 75:
                    ContentWillDescription.append({
                        "Resilience": "面对任务情境，勇于面对困难、挫折和失败，坚定地专注于既定的目标，积极寻求解决任务的办法，自觉地抵制一切不合目的的主客观诱因的干扰，具有锲而不舍、不达目的决不罢休的决心，坚信自己的能力，极少受到失望、沮丧等负面情绪的影响，有很强的心理承受能力。"})

            if i['name'] == "自律性":
                ChartDataWill.append({"name": i['name'], "score": i['score']})
                if 0 <= i['score'] < 30:
                    ContentWillDescription.append({
                        "SelfDiscipline": "自制力较弱，一般不能控制自己不合理的需求、欲望以及不良情绪冲动，即使有外在强制性监督，也难于约束自己的言行举止，行为难以预测，缺乏组织性、纪律性，不遵守行为规范。（极端低分：可能过于放纵自己，肆意妄为。）"})
                elif 30 <= i['score'] < 75:
                    ContentWillDescription.append({
                        "SelfDiscipline": "基本能够控制自己不合理的需求、欲望，偶尔需要在提醒情况下，抗拒来自外部和内部的诱因的干扰，克制自己不应有的情绪和冲动行为，有时在外部监督条件下能够束自己的言行举止，遵守纪律。"})
                elif i['score'] >= 75:
                    ContentWillDescription.append({
                        "SelfDiscipline": "无需外在监督就能自觉控制自己不合理的需求和欲望，抗拒来自外部和内部的诱因的干扰，克制自己不应有的情绪和冲动行为，主动严格约束自己的言行举止，自觉遵守纪律。（极端高分：可能过于追求自我节制，苛求自己，难以释放自己，给人沉闷、缺乏活力的感觉。）"})

            if i['name'] == "悦纳性":
                ChartDataMood.append({"name": i['name'], "score": i['score']})
                if 0 <= i['score'] < 30:
                    ContentMoodDescription.append({
                        "Acceptability": "对自己的过去经历不能坦然接受，对自己的认识不够客观，要么夸大自己的能力，否认自己的不足，要么忽略自己的优势，夸大自己的缺陷，产生消极的自我评价，不能正面自己的不足并进行调整和修正。（极端低分：可能产生拒绝自己、否认自己的自我对立的倾向。）"})
                elif 30 <= i['score'] < 75:
                    ContentMoodDescription.append({
                        "Acceptability": "对自己的过去经历能够接受，基本上对自己有客观的认识，能够了解自己的能力和不足，多数情况下对自己能够进行正面的肯定，欣赏自己且不会回避自己的不足，适当调整修正可以改变的行为。"})
                elif i['score'] >= 75:
                    ContentMoodDescription.append(
                        {"Acceptability": "坦然地接受自己的过去，客观地认识和评估自己的能力，对自己进行正面积极的肯定，欣赏自己并能积极面对自身的缺点和不足，并努力改正。"})
            if i['name'] == "稳定性":
                ChartDataMood.append({"name": i['name'], "score": i['score']})
                if 0 <= i['score'] < 30:
                    ContentMoodDescription.append({
                        "Stability": "情绪不太稳定，易受很小的外界因素影响，不能很好地认识、把握、调节自己的情绪，经常为负面情绪所困扰。（极端低分：可能应激反应强烈，影响自己的工作和生活，可能产生焦虑、紧张、抑郁、恐惧等情绪障碍。）"})
                elif 30 <= i['score'] < 75:
                    ContentMoodDescription.append(
                        {
                            "Stability": "情绪较为稳定，一般情况下很少为外界因素影响而波动，具有一定控制和调节自己的情绪状态的能力，通常能够保持情绪的积极状态，没有较大的负面事件的情况下，很少为负面情绪所困扰。"})
                elif i['score'] >= 75:
                    ContentMoodDescription.append({"Stability": "情绪稳定，很少为外界因素影响而波动，能够合理地控制和调节自己的情绪状态，情绪积极，很少为负面情绪所困扰。"})
            if i['name'] == "自信心":
                ChartDataMood.append({"name": i['name'], "score": i['score']})
                if 0 <= i['score'] < 30:
                    ContentMoodDescription.append(
                        {"SelfConfidence": "对自己的能力缺乏信心，回避竞争和挑战，自卑，认为自己不如别人，缺乏克服困难的决心和勇气，依赖他人，易于放弃。"})
                elif 30 <= i['score'] < 75:
                    ContentMoodDescription.append(
                        {"SelfConfidence": "基本上能够对自己肯定性评价，对自己的能力比较有信心。不会回避竞争，不大会盲从权威，一般情况下，相信自己有能力解决问题，克服困难，达成目标。"})
                elif i['score'] >= 75:
                    ContentMoodDescription.append(
                        {"SelfConfidence": "对自己始终保持持续肯定性评价，认为自己有能力解决问题的信念，愿意参与竞争或挑战，不盲从权威，有克服困难、达成目标勇气和决心，具有较强的坚持力。"})

            if i['name'] == "尽责性":
                ChartDataTask.append({"name": i['name'], "score": i['score']})
                if 0 <= i['score'] < 30:
                    ContentTaskDescription.append({
                        "Responsibility": "在严格的监督和制约下才能履行本职工作，但经常推托回避任务和责任的承担，工作中经常降低标准，敷衍了事，易于松懈和放弃，工作结果总是不尽人意，经常为自己寻找借口，难以让人信赖。"})
                elif 30 <= i['score'] < 75:
                    ContentTaskDescription.append({
                        "Responsibility": "工作中不会推托自己应承担的任务和责任，也能完成工作职责的要求，在外部要求明确或在一定的激励和监督的情况下，会按期按标准完成任务，有时未能完成任务时会从客观上找原因，有时也会感到暂时的不安。"})
                elif i['score'] >= 75:
                    ContentTaskDescription.append({
                        "Responsibility": "面对不明确的任务或职责时，总是能主动承担并努力完成，尽心尽责，一丝不苟，有始有终，工作中从不给自己找借口，从不降低标准，勤勉踏实，值得信赖。（极端高分：可能过于追求完美，自我施压，任务不能完成时易于焦虑、自责、懊恼。）"})

            if i['name'] == "容人性":
                ChartDataPeople.append({"name": i['name'], "score": i['score']})
                if 0 <= i['score'] < 30:
                    ContentPeopleDescription.append({
                        "Tolerance": "人际交往中，较为在意别人的不足和缺点，容易求全责备和计较，难以容忍别人的冒犯或不敬，难以接受不同观点的人以及与风格不同的人进行交往，容易把对别人的偏见带入交往中，甚至在小事上和别人纠缠不清，不能从未来发展的角度与人建立和发展关系。（极端低分：可能过于求全责备，容易记恨报复，排斥异己，经常让自己陷入人际冲突中。）"})
                elif 30 <= i['score'] < 75:
                    ContentPeopleDescription.append({
                        "Tolerance": "人际交往中，比较宽厚，多数情况下能够包容他人的缺点和不足，甚至不太计较别人无心的冒犯或不敬，一般不会求全责备、苛求他人，能够与持不同观点的人以及风格不同的人进行交往和发展关系。"})
                elif i['score'] >= 75:
                    ContentPeopleDescription.append({
                        "Tolerance": "人际交往中，为人宽厚大度，善于包容他人的缺点和不足，以博大的胸怀包容别人的冒犯或过错，善于接纳不同的意见、观点，善于与不同风格的人交往，不拘泥于过去的成见和是非，着眼于未来的关系发展。（极端高分：可能过于退让和迁就他人，甚至有时放弃原则，给人懦弱或世故老好人的感觉。）"})
            if i['name'] == "利他性":
                ChartDataPeople.append({"name": i['name'], "score": i['score']})
                if 0 <= i['score'] < 30:
                    ContentPeopleDescription.append({
                        "Altruism": "多数情况下较为注重利益的交换，较少表现无私助人的行为，较多地关注个人的利益而不是集体的利益，有时甚至会做出不符合社会期望的举动。（极端低分：可能过于自私自利，将个人利益凌驾于集体利益之上，缺乏社会责任感。）"})
                elif 30 <= i['score'] < 75:
                    ContentPeopleDescription.append(
                        {"Altruism": "通常情况下，能够关注别人，愿意提供帮助，行为符合社会的期望，一般能够将集体利益放在个人利益之前，有一定的社会责任感，也会注重互惠互利的利益交换。"})
                elif i['score'] >= 75:
                    ContentPeopleDescription.append(
                        {"Altruism": "具有强烈的亲社会取向，主动为他人着想，真诚、无私地帮助他人，自觉自愿地为社会服务，维护集体利益，具有强烈的社会责任感。"})

        report05['msg']["ContentAdvantageFeature"] = ContentAdvantageFeature
        report05['msg']["ContentWeakFeature"] = ContentWeakFeature
        report05['msg']["ChartDataMotivation"] = ChartDataMotivation
        report05['msg']["ContentMotivationdDescription"] = ContentMotivationdDescription
        report05['msg']["ChartDataCognition"] = ChartDataCognition
        report05['msg']["ChartDataCognitionDescription"] = ChartDataCognitionDescription
        report05['msg']["ChartDataWill"] = ChartDataWill
        report05['msg']["ContentWillDescription"] = ContentWillDescription
        report05['msg']["ChartDataMood"] = ChartDataMood
        report05['msg']["ContentMoodDescription"] = ContentMoodDescription
        report05['msg']["ChartDataTask"] = ChartDataTask
        report05['msg']["ContentTaskDescription"] = ContentTaskDescription
        report05['msg']["ChartDataPeople"] = ChartDataPeople
        report05['msg']["ContentPeopleDescription"] = ContentPeopleDescription
        report05['msg']['Validation'] = v1

        res = {"code": 0, 'detail': {'report_data': report05}}
        print('发送到word服务的数据:%s' % res)
        return res
    elif report_type_id == "WorkValueQuestionnaire":
        try:
            report07 = d['detail']['report_data']
            print('report07%s' % report07)
        except Exception as e:
            res = {"code": 40400, 'detail': {'report_data': e}}
            return res
        print(report07)
        chart_data = report07['msg']['ChartDataModel']
        char = report07['msg']['char']

        StrongIncentiveFactor = ''
        GeneralIncentiveFactor = ''
        GeneralNegativeMotivators = ''
        StrongNegativeIncentiveFactors = ''

        ls = []
        for i in chart_data:
            if i['score'] >= 4 and i['score'] <= 5:
                StrongIncentiveFactor = StrongIncentiveFactor + i['name'] + ","
            if i['score'] >= 2 and i['score'] <= 3:
                GeneralIncentiveFactor = GeneralIncentiveFactor + i['name'] + ","
            if i['score'] >= -3 and i['score'] <= -2:
                GeneralNegativeMotivators = GeneralNegativeMotivators + i['name'] + ","
            if i['score'] >= -5 and i['score'] <= -4:
                StrongNegativeIncentiveFactors = StrongNegativeIncentiveFactors + i['name'] + ","

        StrongIncentiveFactor_list = StrongIncentiveFactor.split(',')[:-1]
        GeneralIncentiveFactor_list = GeneralIncentiveFactor.split(',')[:-1]
        GeneralNegativeMotivators_list = GeneralNegativeMotivators.split(',')[:-1]
        StrongNegativeIncentiveFactors_list = StrongNegativeIncentiveFactors.split(',')[:-1]

        # j 指标名
        # [4,5]
        for i in char:
            for j in StrongIncentiveFactor_list:
                if i['name'] == j:
                    if j == '变化/探索':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "希望每天都能处理全新的事务，适应变化的环境，经常尝试新的方法"},
                                   {"Factor": "希望每一天的工作都是在解决全新的问题，对枯燥重复的工作内容感到厌倦"}, {
                                       "Suggest": "为他/她安排需要多部门合作的工作任务,避免让他/她承担过多重复性、枯燥的工作,在必须执行的重复性工作时鼓励他/她探索总结新的工作方式方法，提高工作效率,鼓励他/她在工作中，多方面拓展，了解行业内最前沿的信息和发展趋势"},
                                   {"Type": "A"}], )
                    elif j == '艺术/文化':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "重视艺术、文学等方面的工作内容，关注审美和创造，倾向于在鼓励创新的环境中工作"},
                                   {"Factor": "认为和艺术或文化有关的工作非常理想，重视创作和自我表达的机会"}, {
                                       "Suggest": "有意识多为他/她安排与艺术相关联的工作任务,在确保工作结果的基础上，鼓励他/她发挥自己的创新能力，对工作流程进行优化鼓励他/她不断提高自己的审美水平，在工作成果中体现他/她的审美能力，如PPT的制作等在团队中，营造鼓励创新的氛围"},
                                   {"Type": "A"}], )
                    elif j == '挑战/成就':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "乐于在工作生活中面对挑战，克服困难，适应竞争激烈的工作环境"},
                                   {"Factor": "乐于克服各种困难及挑战，总是试图做得比别人更好，与他人之间的竞争关系会激发更好的工作表现"}, {
                                       "Suggest": "工作时间外，只在工作任务非常紧急的时候才联系他/她,在可调整的范围内，尽量为他/她提供舒适的工作环境,避免为他/她安排过多的工作任务，尽量不要占用他/她的私人时间,向他/她说明组织需要的是完成工作任务以及绩效，而不是工作的时间长度,鼓励并帮助他/她做好工作生活两方面的时间安排"},
                                   {"Type": "A"}], )
                    elif j == '自主/独立':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "希望按自己的方式、步调或想法去安排工作时间、地点和方式，不倾向于受到太多来自他人的监督和控制"},
                                   {"Factor": "希望以自己的方式工作，过度的监督会影响工作表现"}, {
                                       "Suggest": "在确保工作任务能够保质保量完成的基础上，允许他/她自行安排工作方式，如：在家办公等,在确保工作结果的基础上，鼓励他/她在工作中尝试新的方式方法优化工作流程为他/她安排工作任务时，共同商讨确定工作目标和时间节点，允许他/她自主安排工作进度,在能力范围内，为他/她提供自由、宽松的工作氛围"},
                                   {"Type": "A"}], )
                    elif j == '专业/技术':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "追求在技术或专业领域的成长和提高，倾向于专业或技术性的工作岗位和内容"},
                                   {"Factor": "对专业或技术导向的工作感兴趣，关注工作中提供的学习新知识或技能的机会"}, {
                                       "Suggest": "关注他/她工作内容的专业性，多为他/她安排专业性上有挑战的工作任务,为他/她专业性的提高提供平台和资源支持,通过他/她完成任务是否符合专业标准来评价他/她的工作表现,重视专业人才，鼓励他/她在专业领域上精益求精，不断进步"},
                                   {"Type": "A"}], )
                    elif j == '认可/表现':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "自己的工作需要得到应有的认可和肯定，希望成为人群中的关注焦点"},
                                   {"Factor": "希望在工作中得到肯定，失去同事的认可和关注可能会是一个打击"}, {
                                       "Suggest": "鼓励他/她在自己擅长的领域培训和支持其他同事确保他/她的优异工作表现得到同事和领导的认可和赞扬,每当他/她的工作最终被证明有效，不管用了什么方式和手段，都要强调其所具有的实用价值,鼓励他/她表达自己的观点，对于他/她提出的有建设性的观点，及时的给予支持和认可,不要过多赞扬他/她，会降低赞扬的效果"},
                                   {"Type": "A"}], )
                    elif j == '地位/职位':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "关注工作或职位在的社会地位，希望得到他人的重视与尊敬"},
                                   {"Factor": "关注自己所在的职位和在组织中的地位，当无法获得他人的尊重时会感觉低落"},
                                   {
                                       "Suggest": "有意识的在各种场合，正面或侧面强调他/她在组织中的重要价值和地位在他/她的工作环境中更多的强调职务和级别,关注组织在所属行业中的地位,强调他/她能为组织做出其他人无法做出的贡献"},
                                   {"Type": "A"}], )
                    elif j == '权力/影响':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "追求领导职位，比起自己处理工作人物更倾向于指导他人工作"},
                                   {"Factor": "倾向于担任有影响力的职位并管理他人，能够承担责任"},
                                   {
                                       "Suggest": "适当放权，给予他/她担任项目负责人的工作机会，并在过程中不断的给予指导与支持,鼓励他/她勇敢表达自己的观点，采用一定的方法和策略说服和影响他人,重视他/她的合理建议，鼓励他/她参与决策并承担相应职责,确保他/她每隔一段时间都会有机会承担新的职责,明确他/她所期望的管理权限和职责范围"},
                                   {"Type": "A"}], )
                    elif j == '利他/慈善':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "渴望帮助他人，关心社会福祉，看重在工作中的自我价值实现，主动帮助他人取得成功"},
                                   {"Factor": "渴望帮助他人，关心社会福祉，重视在工作中的自我价值实现，乐意帮助他人取得成功"},
                                   {
                                       "Suggest": "强调整个组织的工作最终能使整个世界变得更好,对于他/她帮助他人的行为，及时的给予认可和奖励,帮助他/她意识到自己的工作任务对他人和社会的积极影响,鼓励他/她多参与社会公益活动，并为他/她提供公益活动的相关资源和信息"},
                                   {"Type": "A"}], )
                    elif j == '社交/人际':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "乐于结交朋友，重视建立广泛的社会联系和关系"},
                                   {"Factor": "愿意主动与他人沟通，和各种人交往，建立比较广泛的社会联系和关系"},
                                   {
                                       "Suggest": "多给予他/她一些需要跨部门沟通的工作任务，并鼓励他/她在过程中不断提高自己沟通交流的能力,向他/她提供参加行业展会、外出交流的机会,为他/她提供机会，与行业内有影响的人交流沟通,鼓励他/她参加工作应酬，建立良好的工作人脉"},
                                   {"Type": "A"}], )
                    elif j == '归属/团队':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "关注和谐的工作氛围，倾向于在团队中和他人合作开展工作"},
                                   {"Factor": "希望在和谐互助的氛围中工作，愿意成为团队的一份子，不倾向于独自工作"}, {
                                       "Suggest": "在团队中，营造融洽和谐的工作氛围，培养他/她对团队的归属感,建议团队成员为他/她在工作领域的相关问题提供心理上的关爱和帮助,多为他/她安排需要与他人合作完成的工作任务,鼓励他/她参与团体建设活动，与同事、领导建立良好的关系"},
                                   {"Type": "A"}], )

                    elif j == '经济/报酬':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "关注工作所获得的经济报酬和物质回报，自身的额外努力必须得到可见的奖励"},
                                   {"Factor": "看重物质上的实际利益，很难接受自己的工作得不到足够的物质回报"},
                                   {
                                       "Suggest": "为他/她提供行业内具有竞争力的薪资,在激励他/她时，多考虑采用物质奖励的方式,当他/她工作表现优异时，确保他/她能够得到丰厚的奖金,注意在他/她加班或担负了额外的工作任务后向其提供相应的额外报酬"},
                                   {"Type": "A"}], )
                    elif j == '安全/稳定':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "关注工作生活的安全与稳定，偏好有序的、计划性的、可预测的工作环境，不倾向于承担风险"},
                                   {"Factor": "工作和职位具有安全感会提升工作热情"}, {
                                       "Suggest": "在组织发生变动时，及时与他/她沟通，确保他/她了解具体情况，说明组织变动对组织发展的重要性建立完善的保险和福利制度，保障他/她收入的稳定,明确他/她的工作内容以及相应的职责范围,在给他/她安排工作任务时，及时与他/她进行沟通并尽可能提供明确具体的任务及计划安排"},
                                   {"Type": "A"}], )
                    elif j == '舒适/家庭':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "追求舒适、轻松、优越的工作条件和环境，关注工作与生活的平衡"},
                                   {"Factor": "认为工作不应该影响生活，轻松、舒适工作条件以及工作与家庭的平衡能够提升满意度"}, {
                                       "Suggest": "工作时间外，只在工作任务非常紧急的时候才联系他/她,在可调整的范围内，尽量为他/她提供舒适的工作环境,避免为他/她安排过多的工作任务，尽量不要占用他/她的私人时间,向他/她说明组织需要的是完成工作任务以及绩效，而不是工作的时间长度,鼓励并帮助他/她做好工作生活两方面的时间安排"},
                                   {"Type": "A"}], )

        # [2,3]
        for i in char:
            for j in GeneralIncentiveFactor_list:
                if i['name'] == j:
                    if j == '变化/探索':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "希望每天都能处理全新的事务，适应变化的环境，经常尝试新的方法"},
                                   {"Factor": "希望每一天的工作都是在解决全新的问题，对枯燥重复的工作内容感到厌倦"}, {
                                       "Suggest": "为他/她安排需要多部门合作的工作任务,避免让他/她承担过多重复性、枯燥的工作,在必须执行的重复性工作时鼓励他/她探索总结新的工作方式方法，提高工作效率,鼓励他/她在工作中，多方面拓展，了解行业内最前沿的信息和发展趋势"},
                                   {"Type": "B"}], )
                    elif j == '艺术/文化':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "重视艺术、文学等方面的工作内容，关注审美和创造，倾向于在鼓励创新的环境中工作"},
                                   {"Factor": "认为和艺术或文化有关的工作非常理想，重视创作和自我表达的机会"}, {
                                       "Suggest": "有意识多为他/她安排与艺术相关联的工作任务,在确保工作结果的基础上，鼓励他/她发挥自己的创新能力，对工作流程进行优化,鼓励他/她不断提高自己的审美水平，在工作成果中体现他/她的审美能力，如PPT的制作等,在团队中，营造鼓励创新的氛围"},
                                   {"Type": "B"}], )
                    elif j == '挑战/成就':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "乐于在工作生活中面对挑战，克服困难，适应竞争激烈的工作环境"},
                                   {"Factor": "乐于克服各种困难及挑战，总是试图做得比别人更好，与他人之间的竞争关系会激发更好的工作表现"}, {
                                       "Suggest": "工作时间外，只在工作任务非常紧急的时候才联系他/她,在可调整的范围内，尽量为他/她提供舒适的工作环境, 避免为他/她安排过多的工作任务，尽量不要占用他/她的私人时间,向他/她说明组织需要的是完成工作任务以及绩效，而不是工作的时间长度,鼓励并帮助他/她做好工作生活两方面的时间安排"},
                                   {"Type": "B"}], )
                    elif j == '自主/独立':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "希望按自己的方式、步调或想法去安排工作时间、地点和方式，不倾向于受到太多来自他人的监督和控制"},
                                   {"Factor": "希望以自己的方式工作，过度的监督会影响工作表现"}, {
                                       "Suggest": "在确保工作任务能够保质保量完成的基础上，允许他/她自行安排工作方式，如：在家办公等,在确保工作结果的基础上，鼓励他/她在工作中尝试新的方式方法优化工作流程,为他/她安排工作任务时，共同商讨确定工作目标和时间节点，允许他/她自主安排工作进度,在能力范围内，为他/她提供自由、宽松的工作氛围"},
                                   {"Type": "B"}], )
                    elif j == '专业/技术':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "追求在技术或专业领域的成长和提高，倾向于专业或技术性的工作岗位和内容"},
                                   {"Factor": "对专业或技术导向的工作感兴趣，关注工作中提供的学习新知识或技能的机会"}, {
                                       "Suggest": "关注他/她工作内容的专业性，多为他/她安排专业性上有挑战的工作任务,为他/她专业性的提高提供平台和资源支持,通过他/她完成任务是否符合专业标准来评价他/她的工作表现,重视专业人才，鼓励他/她在专业领域上精益求精，不断进步"},
                                   {"Type": "B"}], )
                    elif j == '认可/表现':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "自己的工作需要得到应有的认可和肯定，希望成为人群中的关注焦点"},
                                   {"Factor": "希望在工作中得到肯定，失去同事的认可和关注可能会是一个打击"}, {
                                       "Suggest": "鼓励他/她在自己擅长的领域培训和支持其他同事,确保他/她的优异工作表现得到同事和领导的认可和赞扬,每当他/她的工作最终被证明有效，不管用了什么方式和手段，都要强调其所具有的实用价值,鼓励他/她表达自己的观点，对于他/她提出的有建设性的观点，及时的给予支持和认可,不要过多赞扬他/她，会降低赞扬的效果"},
                                   {"Type": "B"}], )
                    elif j == '地位/职位':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "关注工作或职位在的社会地位,希望得到他人的重视与尊敬"},
                                   {"Factor": "关注自己所在的职位和在组织中的地位,当无法获得他人的尊重时会感觉低落"},
                                   {
                                       "Suggest": "有意识的在各种场合，正面或侧面强调他/她在组织中的重要价值和地位在他/她的工作环境中更多的强调职务和级别,关注组织在所属行业中的地位,强调他/她能为组织做出其他人无法做出的贡献"},
                                   {"Type": "B"}], )
                    elif j == '权力/影响':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "追求领导职位，比起自己处理工作人物更倾向于指导他人工作"},
                                   {"Factor": "倾向于担任有影响力的职位并管理他人，能够承担责任"},
                                   {
                                       "Suggest": "适当放权，给予他/她担任项目负责人的工作机会，并在过程中不断的给予指导与支持,鼓励他/她勇敢表达自己的观点，采用一定的方法和策略说服和影响他人,重视他/她的合理建议，鼓励他/她参与决策并承担相应职责,确保他/她每隔一段时间都会有机会承担新的职责,明确他/她所期望的管理权限和职责范围"},
                                   {"Type": "B"}], )
                    elif j == '利他/慈善':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "渴望帮助他人，关心社会福祉，看重在工作中的自我价值实现，主动帮助他人取得成功"},
                                   {"Factor": "渴望帮助他人，关心社会福祉，重视在工作中的自我价值实现，乐意帮助他人取得成功"},
                                   {
                                       "Suggest": "强调整个组织的工作最终能使整个世界变得更好,对于他/她帮助他人的行为，及时的给予认可和奖励,帮助他/她意识到自己的工作任务对他人和社会的积极影响,鼓励他/她多参与社会公益活动，并为他/她提供公益活动的相关资源和信息"},
                                   {"Type": "B"}], )
                    elif j == '社交/人际':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "乐于结交朋友，重视建立广泛的社会联系和关系"},
                                   {"Factor": "愿意主动与他人沟通，和各种人交往，建立比较广泛的社会联系和关系"},
                                   {
                                       "Suggest": "多给予他/她一些需要跨部门沟通的工作任务，并鼓励他/她在过程中不断提高自己沟通交流的能力,向他/她提供参加行业展会、外出交流的机会,为他/她提供机会，与行业内有影响的人交流沟通,鼓励他/她参加工作应酬，建立良好的工作人脉"},
                                   {"Type": "B"}], )
                    elif j == '归属/团队':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "关注和谐的工作氛围，倾向于在团队中和他人合作开展工作"},
                                   {"Factor": "希望在和谐互助的氛围中工作，愿意成为团队的一份子，不倾向于独自工作"}, {
                                       "Suggest": "在团队中，营造融洽和谐的工作氛围，培养他/她对团队的归属感,建议团队成员为他/她在工作领域的相关问题提供心理上的关爱和帮助,多为他/她安排需要与他人合作完成的工作任务,鼓励他/她参与团体建设活动，与同事、领导建立良好的关系"},
                                   {"Type": "B"}], )

                    elif j == '经济/报酬':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "关注工作所获得的经济报酬和物质回报，自身的额外努力必须得到可见的奖励"},
                                   {"Factor": "看重物质上的实际利益，很难接受自己的工作得不到足够的物质回报"},
                                   {
                                       "Suggest": " 为他/她提供行业内具有竞争力的薪资,在激励他/她时，多考虑采用物质奖励的方式,当他/她工作表现优异时，确保他/她能够得到丰厚的奖金,注意在他/她加班或担负了额外的工作任务后向其提供相应的额外报酬"},
                                   {"Type": "B"}], )
                    elif j == '安全/稳定':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "关注工作生活的安全与稳定，偏好有序的、计划性的、可预测的工作环境，不倾向于承担风险"},
                                   {"Factor": "工作和职位具有安全感会提升工作热情"}, {
                                       "Suggest": "在组织发生变动时，及时与他/她沟通，确保他/她了解具体情况，说明组织变动对组织发展的重要性建立完善的保险和福利制度，保障他/她收入的稳定,明确他/她的工作内容以及相应的职责范围,在给他/她安排工作任务时，及时与他/她进行沟通并尽可能提供明确具体的任务及计划安排"},
                                   {"Type": "B"}], )
                    elif j == '舒适/家庭':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "追求舒适、轻松、优越的工作条件和环境，关注工作与生活的平衡"},
                                   {"Factor": "认为工作不应该影响生活，轻松、舒适工作条件以及工作与家庭的平衡能够提升满意度"}, {
                                       "Suggest": "工作时间外，只在工作任务非常紧急的时候才联系他/她,在可调整的范围内，尽量为他/她提供舒适的工作环境,避免为他/她安排过多的工作任务，尽量不要占用他/她的私人时间,向他/她说明组织需要的是完成工作任务以及绩效，而不是工作的时间长度,鼓励并帮助他/她做好工作生活两方面的时间安排"},
                                   {"Type": "B"}], )

        # [-3,-2]
        for i in char:
            for j in GeneralNegativeMotivators_list:
                if i['name'] == j:
                    if j == '变化/探索':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "希望每天都能处理全新的事务，适应变化的环境，经常尝试新的方法"},
                                   {"Factor": "在多元多变的工作环境中会感到不安"}, {
                                       "Suggest": "避免在没有任何外部支持的情况下要求他/她负责不熟悉的业务,多让他/她承担目标明确，步骤清晰的工作任务,鼓励他/她在完成重复性工作时，总结经验，优化工作方法,在他/她承担灵活变化的工作任务时，与他/她充分沟通，明确工作目标与任务结构，设定具体的执行路线"},
                                   {"Type": "C"}], )
                    elif j == '艺术/文化':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "重视艺术、文学等方面的工作内容，关注审美和创造，倾向于在鼓励创新的环境中工作"},
                                   {"Factor": "关注实践和执行方面的工作，更看重实质内容而非外在表象，对文化艺术不太重视"}, {
                                       "Suggest": "少为他/她安排需要发挥创意和想象力的工作,鼓励他/她多参与具体执行操作的工作任务,为他/她安排工作任务时，明确具体的工作成果要求，不要求他/她在工作成果中体现他/她审美水平,避免通过他/她在工作中体现的创新能力来衡量他/她的工作表现"},
                                   {"Type": "C"}], )
                    elif j == '挑战/成就':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "乐于在工作生活中面对挑战，克服困难，适应竞争激烈的工作环境"},
                                   {"Factor": "寻求适度而非巨大的挑战，不倾向于在充满竞争的环境中工作"}, {
                                       "Suggest": "向他/她提供能够保持专注工作的环境和条件,为他/她安排足够的工作任务，确保有一定的工作量,向他/她提供有一定难度和挑战性的工作,和向他/她提供更多的休假相比，向其提供新领域的工作和学习机会，以及更好的职业发展渠道等激励手段可能会更有效"},
                                   {"Type": "C"}], )
                    elif j == '自主/独立':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "希望按自己的方式、步调或想法去安排工作时间、地点和方式，不倾向于受到太多来自他人的监督和控制"},
                                   {"Factor": "乐于听从指令及接受督导，缺乏明确指示会让其产生不安。"}, {
                                       "Suggest": "在公司内部，制定健全的工作规章制度,给予他/她明确的工作指示，并监督他/她的工作进程，即时给予反馈,避免为他/她安排需要自主管理的工作任务,对于他/她遵守公司规章制度，严格履行公司纪律的行为，给予奖励和认可"},
                                   {"Type": "C"}], )
                    elif j == '专业/技术':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "追求在技术或专业领域的成长和提高，倾向于专业或技术性的工作岗位和内容"},
                                   {"Factor": "工作是否符合自己的经历或专业并不重要，不关心学习新知识或专业技能的机会"}, {
                                       "Suggest": "与他/她沟通，了解他/她对工作内容专业性的期待,避免仅通过他/她在专业性上的进步和发展激励他/她,避免为他/她安排在专业性要求过高的工作任务,鼓励他/她多尝试多探索，找到自己希望发展的职业技能"},
                                   {"Type": "C"}], )
                    elif j == '认可/表现':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "自己的工作需要得到应有的认可和肯定，希望成为人群中的关注焦点"},
                                   {"Factor": "更高的职位并不是那么重要，也不太关心职业发展前景是否良好"}, {
                                       "Suggest": "是否得到充分的支持不会对他/她的工作动力产生太大的影响,尽量避免直接比较他/她和其它人的工作表现,建议他/她周围的人避免经常寻求他/她的协助或支持,避免仅通过对其工作表现的认可和表扬来激励他/她"},
                                   {"Type": "C"}], )
                    elif j == '地位/职位':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "关注工作或职位在的社会地位，希望得到他人的重视与尊敬"},
                                   {"Factor": "不关注外在的职务、地位和身份认可"},
                                   {
                                       "Suggest": "更多突出他/她在业务或技术方面取得的名声而不是职务级别,确保他/她的头衔更多的是关于技术或业务能力而不是管理级别,关注和赞扬他/她工作所得到的具体成果,避免仅用职位上的提升来激励他/她"},
                                   {"Type": "C"}], )
                    elif j == '权力/影响':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "追求领导职位，比起自己处理工作人物更倾向于指导他人工作"},
                                   {"Factor": "不追求工作中的权力、影响力及权威"},
                                   {
                                       "Suggest": "多让他/她担任项目工作中的参与者，而不是组织者或管理者,避免为他/她安排分配和指导他人的工作任务,鼓励他/她通过团队的讨论形成决策,明确他/她的职业成长意愿，为他/她提供合适的上升道路"},
                                   {"Type": "C"}], )
                    elif j == '利他/慈善':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "渴望帮助他人，关心社会福祉，看重在工作中的自我价值实现，主动帮助他人取得成功"},
                                   {"Factor": "不倾向于帮助他人，认为人可以自助，不太能从帮助他人中获得满足"},
                                   {
                                       "Suggest": "倡导个人的独立自主,避免通过他/她对他人的帮助来评价他/她的工作表现,不要求他/她关注公益慈善事业,鼓励他/她专注于自己本职工作又好又快的完成"},
                                   {"Type": "C"}], )
                    elif j == '社交/人际':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "乐于结交朋友，重视建立广泛的社会联系和关系"},
                                   {"Factor": "与他人的沟通互动需求比较低，不倾向于参与交际或应酬"},
                                   {
                                       "Suggest": "避免给予他/她过多交际应酬的工作任务,在他/她参与各类行业内交流活动时，引导他/她专注于专业知识的获取和学习,不强迫他/她参加工作应酬,鼓励他/她从达成工作目标角度出发，与他人相处，建立工作关系"},
                                   {"Type": "C"}], )
                    elif j == '归属/团队':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "关注和谐的工作氛围，倾向于在团队中和他人合作开展工作"},
                                   {"Factor": "希望独自承担任务，不倾向于和他人合作，不关注团队"}, {
                                       "Suggest": "避免过多关心他/她的私人生活多为他/她安排个人可独立完成的工作任务,在他/她参与团队合作工作时，与他/她充分沟通，明确他/她个人承担的工作任务,在他/她参于集体活动时，强调集体活动对团队建设和发展的意义"},
                                   {"Type": "C"}], )

                    elif j == '经济/报酬':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "关注工作所获得的经济报酬和物质回报，自身的额外努力必须得到可见的奖励"},
                                   {"Factor": "较少关注工作带来的金钱利益和其它物质回报"},
                                   {
                                       "Suggest": "与他/她沟通，了解他/她所期望的激励方式确保组织内经济报酬分配的公平合理性,尝试采用多种手段相结合的方式来评价他/她的工作表现,避免只通过薪资福利增长的方式来激励他/她"},
                                   {"Type": "C"}], )
                    elif j == '安全/稳定':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "关注工作生活的安全与稳定，偏好有序的、计划性的、可预测的工作环境，不倾向于承担风险"},
                                   {"Factor": "不介意工作中的风险因素，接受不稳定的职位、工作环境和氛围"}, {
                                       "Suggest": " 向他/她说明组织的发展状态，确保工作环境的变动在他/她可承受的范围内,鼓励他/她在完成自己职责范围内的工作后，自主拓展，承担更多的工作，提升个人能力,为他/她安排工作时，与他/她商讨确定工作目标，让他/她自主确定工作计划与安排,向他/她提供必要保险和福利"},
                                   {"Type": "C"}], )
                    elif j == '舒适/家庭':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "追求舒适、轻松、优越的工作条件和环境，关注工作与生活的平衡"},
                                   {"Factor": "不关注工作与生活的平衡，接受在常规工作时间外执行任务，不介意加班"}, {
                                       "Suggest": "向他/她提供能够保持专注工作的环境和条件为他/她安排足够的工作任务，确保有一定的工作量,向他/她提供有一定难度和挑战性的工作,和向他/她提供更多的休假相比，向其提供新领域的工作和学习机会，以及更好的职业发展渠道等激励手段可能会更有效"},
                                   {"Type": "C"}], )

        # [-5,-4]
        for i in char:
            for j in StrongNegativeIncentiveFactors_list:
                if i['name'] == j:
                    if j == '变化/探索':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "希望每天都能处理全新的事务，适应变化的环境，经常尝试新的方法"},
                                   {"Factor": "在多元多变的工作环境中会感到不安"}, {
                                       "Suggest": "避免在没有任何外部支持的情况下要求他/她负责不熟悉的业务,多让他/她承担目标明确，步骤清晰的工作任务,鼓励他/她在完成重复性工作时，总结经验，优化工作方法,在他/她承担灵活变化的工作任务时，与他/她充分沟通，明确工作目标与任务结构，设定具体的执行路线"},
                                   {"Type": "D"}], )
                    elif j == '艺术/文化':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "重视艺术、文学等方面的工作内容，关注审美和创造，倾向于在鼓励创新的环境中工作"},
                                   {"Factor": "关注实践和执行方面的工作，更看重实质内容而非外在表象，对文化艺术不太重视"}, {
                                       "Suggest": "少为他/她安排需要发挥创意和想象力的工作,鼓励他/她多参与具体执行操作的工作任务,为他/她安排工作任务时，明确具体的工作成果要求，不要求他/她在工作成果中体现他/她审美水平,避免通过他/她在工作中体现的创新能力来衡量他/她的工作表现"},
                                   {"Type": "D"}], )
                    elif j == '挑战/成就':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "乐于在工作生活中面对挑战，克服困难，适应竞争激烈的工作环境"},
                                   {"Factor": "寻求适度而非巨大的挑战，不倾向于在充满竞争的环境中工作"}, {
                                       "Suggest": "向他/她提供能够保持专注工作的环境和条件,为他/她安排足够的工作任务，确保有一定的工作量,向他/她提供有一定难度和挑战性的工作,和向他/她提供更多的休假相比，向其提供新领域的工作和学习机会，以及更好的职业发展渠道等激励手段可能会更有效"},
                                   {"Type": "D"}], )
                    elif j == '自主/独立':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "希望按自己的方式、步调或想法去安排工作时间、地点和方式，不倾向于受到太多来自他人的监督和控制"},
                                   {"Factor": "乐于听从指令及接受督导，缺乏明确指示会让其产生不安。"}, {
                                       "Suggest": "在公司内部，制定健全的工作规章制度,给予他/她明确的工作指示，并监督他/她的工作进程，即时给予反馈,避免为他/她安排需要自主管理的工作任务,对于他/她遵守公司规章制度，严格履行公司纪律的行为，给予奖励和认可"},
                                   {"Type": "D"}], )
                    elif j == '专业/技术':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "追求在技术或专业领域的成长和提高，倾向于专业或技术性的工作岗位和内容"},
                                   {"Factor": "工作是否符合自己的经历或专业并不重要，不关心学习新知识或专业技能的机会"}, {
                                       "Suggest": "与他/她沟通，了解他/她对工作内容专业性的期待,避免仅通过他/她在专业性上的进步和发展激励他/她,避免为他/她安排在专业性要求过高的工作任务,鼓励他/她多尝试多探索，找到自己希望发展的职业技能"},
                                   {"Type": "D"}], )
                    elif j == '认可/表现':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "自己的工作需要得到应有的认可和肯定，希望成为人群中的关注焦点"},
                                   {"Factor": "更高的职位并不是那么重要，也不太关心职业发展前景是否良好"}, {
                                       "Suggest": "是否得到充分的支持不会对他/她的工作动力产生太大的影响,尽量避免直接比较他/她和其它人的工作表现,建议他/她周围的人避免经常寻求他/她的协助或支持,避免仅通过对其工作表现的认可和表扬来激励他/她"},
                                   {"Type": "D"}], )
                    elif j == '地位/职位':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "关注工作或职位在的社会地位，希望得到他人的重视与尊敬"},
                                   {"Factor": "不关注外在的职务、地位和身份认可"},
                                   {
                                       "Suggest": "更多突出他/她在业务或技术方面取得的名声而不是职务级别,确保他/她的头衔更多的是关于技术或业务能力而不是管理级别,关注和赞扬他/她工作所得到的具体成果,避免仅用职位上的提升来激励他/她"},
                                   {"Type": "D"}], )
                    elif j == '权力/影响':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "追求领导职位，比起自己处理工作人物更倾向于指导他人工作"},
                                   {"Factor": "不追求工作中的权力、影响力及权威"},
                                   {
                                       "Suggest": "多让他/她担任项目工作中的参与者，而不是组织者或管理者,避免为他/她安排分配和指导他人的工作任务,鼓励他/她通过团队的讨论形成决策,明确他/她的职业成长意愿，为他/她提供合适的上升道路"},
                                   {"Type": "D"}], )
                    elif j == '利他/慈善':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "渴望帮助他人，关心社会福祉，看重在工作中的自我价值实现，主动帮助他人取得成功"},
                                   {"Factor": "不倾向于帮助他人，认为人可以自助，不太能从帮助他人中获得满足"},
                                   {
                                       "Suggest": "倡导个人的独立自主,避免通过他/她对他人的帮助来评价他/她的工作表现,不要求他/她关注公益慈善事业,鼓励他/她专注于自己本职工作又好又快的完成"},
                                   {"Type": "D"}], )
                    elif j == '社交/人际':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "乐于结交朋友，重视建立广泛的社会联系和关系"},
                                   {"Factor": "与他人的沟通互动需求比较低，不倾向于参与交际或应酬"},
                                   {
                                       "Suggest": "避免给予他/她过多交际应酬的工作任务,在他/她参与各类行业内交流活动时，引导他/她专注于专业知识的获取和学习,不强迫他/她参加工作应酬,鼓励他/她从达成工作目标角度出发，与他人相处，建立工作关系"},
                                   {"Type": "D"}], )
                    elif j == '归属/团队':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "关注和谐的工作氛围，倾向于在团队中和他人合作开展工作"},
                                   {"Factor": "希望独自承担任务，不倾向于和他人合作，不关注团队"}, {
                                       "Suggest": "避免过多关心他/她的私人生活多为他/她安排个人可独立完成的工作任务,在他/她参与团队合作工作时，与他/她充分沟通，明确他/她个人承担的工作任务,在他/她参于集体活动时，强调集体活动对团队建设和发展的意义"},
                                   {"Type": "D"}], )

                    elif j == '经济/报酬':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "关注工作所获得的经济报酬和物质回报，自身的额外努力必须得到可见的奖励"},
                                   {"Factor": "较少关注工作带来的金钱利益和其它物质回报"},
                                   {
                                       "Suggest": "与他/她沟通，了解他/她所期望的激励方式确保组织内经济报酬分配的公平合理性,尝试采用多种手段相结合的方式来评价他/她的工作表现,避免只通过薪资福利增长的方式来激励他/她"},
                                   {"Type": "D"}], )
                    elif j == '安全/稳定':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "关注工作生活的安全与稳定，偏好有序的、计划性的、可预测的工作环境，不倾向于承担风险"},
                                   {"Factor": "不介意工作中的风险因素，接受不稳定的职位、工作环境和氛围"}, {
                                       "Suggest": " 向他/她说明组织的发展状态，确保工作环境的变动在他/她可承受的范围内,鼓励他/她在完成自己职责范围内的工作后，自主拓展，承担更多的工作，提升个人能力,为他/她安排工作时，与他/她商讨确定工作目标，让他/她自主确定工作计划与安排,向他/她提供必要保险和福利"},
                                   {"Type": "D"}], )
                    elif j == '舒适/家庭':
                        ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                   {"TargetDesc": "追求舒适、轻松、优越的工作条件和环境，关注工作与生活的平衡"},
                                   {"Factor": "不关注工作与生活的平衡，接受在常规工作时间外执行任务，不介意加班"}, {
                                       "Suggest": "向他/她提供能够保持专注工作的环境和条件为他/她安排足够的工作任务，确保有一定的工作量,向他/她提供有一定难度和挑战性的工作,和向他/她提供更多的休假相比，向其提供新领域的工作和学习机会，以及更好的职业发展渠道等激励手段可能会更有效"},
                                   {"Type": "D"}], )

        analysis = ls

        report07['msg']["StrongIncentiveFactor"] = StrongIncentiveFactor_list
        report07['msg']["GeneralIncentiveFactor"] = GeneralIncentiveFactor_list
        report07['msg']["GeneralNegativeMotivators"] = GeneralNegativeMotivators_list
        report07['msg']["StrongNegativeIncentiveFactors"] = StrongNegativeIncentiveFactors_list
        report07['msg']["analysis"] = analysis
        # res = {"code": 0, 'detail': {'report_data': report_07_data}}
        res = {"code": 0, 'detail': {'report_data': report07}}
        print('发送到word服务的数据:%s' % res)
        return res
    elif report_type_id == "DISC_NEW":
        try:
            report08 = d['detail']['report_data']
        except Exception as e:
            res = {"code": 40400, 'detail': {'report_data': e}}
            return res
        res = {"code": 0, 'detail': {'report_data': report08}}
        print('发送到word服务的数据:%s' % res)
        return res
    elif report_type_id == "HAMeasurePersonal":
        try:
            report03 = d['detail']['report_data']
            print('report03打印：%s' % report03)
        except Exception as e:
            res = {"code": 40400, 'detail': {'report_data': e}}
            return res

        chart_data = report03['msg']['ChartEudaemonia']
        Content_Advantage = []
        Content_Keep = []
        Content_Follow = []
        Content_Improvement = []

        # print(chart_data)
        for i in chart_data:
            if 8 <= i["score"] <= 10:
                Content_Advantage.append(i["name"] + ': ' + str(i["score"]))
            if 4 <= i["score"] <= 7:
                Content_Keep.append(i["name"] + ': ' + str(i["score"]))
            if 2 <= i["score"] <= 3:
                Content_Follow.append(i["name"] + ': ' + str(i["score"]))
            if i["score"] <= 1:
                Content_Improvement.append(i["name"] + ': ' + str(i["score"]))
        report03['msg']['Content_Advantage'] = Content_Advantage
        report03['msg']['Content_Keep'] = Content_Keep
        report03['msg']['Content_Follow'] = Content_Follow
        report03['msg']['Content_Improvement'] = Content_Improvement
        res = {"code": 0, 'detail': {'report_data': report03}}
        print('发送到word服务的数据:%s' % res)
        return res

    elif report_type_id == "HAMeasurePersonal_EN":
        try:
            report09 = d['detail']['report_data']
            print('report09打印：%s' % report09)
        except Exception as e:
            res = {"code": 40400, 'detail': {'report_data': e}}
            return res

        chart_data = report09['msg']['ChartEudaemonia']
        Content_Advantage = []
        Content_Keep = []
        Content_Follow = []
        Content_Improvement = []

        # print(chart_data)

        for i in chart_data:

            if 8 <= i["score"] <= 10:
                Content_Advantage.append(i["en_name"] + ': ' + str(i["score"]))
            if 4 <= i["score"] <= 7:
                Content_Keep.append(i["en_name"] + ': ' + str(i["score"]))
            if 2 <= i["score"] <= 3:
                Content_Follow.append(i["en_name"] + ': ' + str(i["score"]))
            if i["score"] <= 1:
                Content_Improvement.append(i["en_name"] + ': ' + str(i["score"]))

        report09['msg']['Content_Advantage'] = Content_Advantage
        report09['msg']['Content_Keep'] = Content_Keep
        report09['msg']['Content_Follow'] = Content_Follow
        report09['msg']['Content_Improvement'] = Content_Improvement
        res = {"code": 0, 'detail': {'report_data': report09}}
        print('发送到word服务的数据:%s' % res)
        return res

    elif report_type_id == "EmployeeMentalHealth_EN":
        try:
            report10 = d['detail']['report_data']
            print('report10打印：%s' % report10)
        except Exception as e:
            res = {"code": 40400, 'detail': {'report_data': e}}
            return res

        chart_data = report10['msg']['chart']
        v = report10['msg']['Validation']
        v1 = ''
        if v >= 25:
            v1 = v1 + 'Unable to provide you with a true and detailed report, please take time to retake the test, because you are failing to answer according to your own actual situation, there are more decorative, camouflage tendency.'
        else:
            v1 = v1 + 'The answer is true, undisguised, and the results are believable.'
        # print(chart_data)
        # 定义黄、橙、红 指标
        ChartYellowIndex = ""
        ChartOrangeIndex = ""
        ChartRedIndex = ""
        # 定义内容
        # 躯体反应
        ContentSomaticReaction = ""
        # 回避行为
        ContentAvoidanceBehavior = ""
        # 幻想行为
        ContentFantasies = ""
        # 自责行为
        ContentSelfReproach = ""
        # 强迫行为
        ContentCompulsion = ""
        # 偏执心理
        ContentParanoia = ""
        # 嫉妒心理
        ContentJealousy = ""
        # 人际适应
        ContentInterpersonalAdaptation = ""
        # 孤独感受
        ContentLonelyFeeling = ""
        # 依赖心理
        ContentAnaclisis = ""
        # 猜疑心理
        ContentSuspicions = ""
        # 焦虑情绪
        ContentAnxiety = ""
        # 冲动控制
        ContentImpulsiveControl = ""
        # 抑郁倾向
        ContentDepressiveTendency = ""
        # 环境适应
        ContentEnvironmentalAdaptation = ""
        # 恐惧心理
        ContentFear = ""
        # 身心同一

        ContentBodyAndMind = ""
        for i in chart_data:
            if i['score'] >= 16 and i['score'] <= 20:
                # 黄色指标
                ChartYellowIndex = ChartYellowIndex + i['en_name'] + ","
            if i['score'] >= 21 and i['score'] <= 25:
                # 橙色指标
                ChartOrangeIndex = ChartOrangeIndex + i['en_name'] + ","
            if i['score'] >= 26 and i['score'] <= 30:
                # 红色指标
                ChartRedIndex = ChartRedIndex + i['en_name'] + ","

            if i['name'] == "躯体反应":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentSomaticReaction = ContentSomaticReaction + "Generally, you have a good physical condition, possibly:;[1] Energetic, strong work interest and high working efficiency;[2] Rarely have a lasting and intense physical pain feeling;[3] Even if fatigue, can recover quickly by rest"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentSomaticReaction = ContentSomaticReaction + "Generally, you have a quite good physical condition, possibly:;[1] Quite rarely have gastrointestinal symptoms such as abdominal pain, abdominal distension, nausea, vomiting, etc;[2] Quite rarely have a lasting and intense physical pain feeling;[3] Quite rarely have a feeling of physical fatigue"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentSomaticReaction = ContentSomaticReaction + "You have shown some slight somatic syndrome, possibly:;[1] Sometimes have a tired, fatigue feeling;[2] Sometimes have abdominal pain, bloating, nausea or vomiting;[3] Sometimes feel depressed, short of breath;[4] May feel painful in some parts of the body sometimes, the feeling may be persistent and intense"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentSomaticReaction = ContentSomaticReaction + "You have shown significant somatic syndrome, possibly:;[1] Often have gastrointestinal symptoms, such as abdominal pain, nausea, abdominal distension, vomiting, hiccups, stools, etc;[2] Often exhibit respiratory symptoms, such as shortness of breath, chest pain, etc;[3] Often exhibit symptoms of autonomic nervous excitement, such as palpitations,sweating, blushing and tremor;[4] Easily getting tired, Often feel heavy in the limbs or powerless;[5] Pain feeling in the body, sometimes persistent, serious, intense and prominent"
            if i['name'] == "回避行为":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentAvoidanceBehavior = ContentAvoidanceBehavior + "Generally, you are a person who are able to face difficulties and challenges, possibly:;[1] Be able to focus on established goals and actively seek solutions to the task;[2] Able to deal with difficulties, setbacks and failures in a mature way;[3] Try hard to change the status quo, in order to improve the situation;[4] Rarely affected by negative emotions such as disappointment and frustration;[5] Very determined"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentAvoidanceBehavior = ContentAvoidanceBehavior + "Generally, you are a person who are quite able to face difficulties and challenges, possibly:;[1] Be able to focus on the finishing of established goals, and find solutions to it;[2] Able to face difficulties, setbacks and failures, rarely withdraw from them;[3] Less affected by negative emotions such as disappointment and depression than others;[4] Will not overemphasize the difficulty of the task"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentAvoidanceBehavior = ContentAvoidanceBehavior + "Generally, you do not tend to face difficulties and challenges, possibly:;[1] Sometimes cannot face the reality, may complain or escape;[2] In the face of difficulties and challenges, may not want to give effort, may be easy to give up;[3] Prone to disappointment and frustration;[4] Take a wait-and-see attitude towards the problems"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentAvoidanceBehavior = ContentAvoidanceBehavior + "Generally, you clearly prefer to avoid difficulties and challenges, possibly:;[1] Not calm in the face of reality, often complain or escape;[2] Cannot adhere to the established goals, lack of self-confidence, tend to withdraw;[3] Evaluate the potential difficulties more serious than they actually are, often feel frustrating and disappointing;[4] Willing to fall behind, avoid difficulties, and muddle along"
            if i['name'] == "幻想行为":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentFantasies = ContentFantasies + "You are a rational and realistic person, able to face and deal with difficulties properly:;[1] Usually a realist, do not like fantasy, have a sober understanding of reality;[2] Be able to take a positive view and focus on problem solving;[3] Be able to cope with difficulties rationally"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentFantasies = ContentFantasies + "You are quite a rational and realistic person, able to face and deal with difficulties properly:;[1] With only a little fantasy, you have a sober understanding of reality;[2] Focused in problem solving, will not be easily disturbed"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentFantasies = ContentFantasies + "Compared with others, you seem not to be that able to face and deal with difficulties properly:;[1] May have some unrealistic fantasies when face problems;[2] Not very concentrated when dealing with problems, easily disturbed"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentFantasies = ContentFantasies + "Compared with others, you are not able to face and deal with difficulties properly:;[1] Often have some unrealistic fantasies when face problems;[2] Often distracted when dealing with problems"
            if i['name'] == "自责行为":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentSelfReproach = ContentSelfReproach + "You have strong confidence in the face of setbacks and difficulties:;[1] Able to know yourself and be positive about your experiences;[2] Able to objectively evaluate your abilities and deficiencies;[3] Confident with your ability to solve problems, you are not easily moved."
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentSelfReproach = ContentSelfReproach + "You have some confidence in the face of setbacks and difficulties:;[1] Relatively able to know yourself and be positive about your experiences;[2] Relatively able to objectively evaluate your abilities and deficiencies;[3] Confident with your ability to solve problems, you are not easily moved."
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentSelfReproach = ContentSelfReproach + "Compared with others, you tend to blame yourself for setbacks and difficulties:;[1] Cannot accept difficulties and failures, may not have an objective view of yourself;[2] Ignore own advantages, exaggerate defects, negative self-evaluation;[3] May not be able to deal with your own shortcomings correctly, as well as to adjust and correct them"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentSelfReproach = ContentSelfReproach + "Compared with others, you have a clear tendency to blame yourself for setbacks and difficulties:;[1] Cannot accept difficulties and failures, have a completely negative self-evaluation;[2] Give up the efforts to solve the problem because of the negative self-evaluation;[3] Not be able to deal with your own shortcomings correctly, as well as to adjust and correct them."
            if i['name'] == "强迫行为":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentCompulsion = ContentCompulsion + "You are generally very rational, never worry about baseless ideas, nor do you do meaningless things compulsively :;[1] Not full of doubts, you do not always worried about the invasion of bacteria, viruses, and  will not repeatedly check the gas pipeline, power switches and other objects;[2] Can effectively control own thoughts, can put strange, absurd ideas aside at any time;[3] Behave normal, you do not have any habits or hobbies that brings anxiety when not able to repeat them;[4] Have a strong control of life and work, you do not exaggerate the consequences of mistakes and will not be too anxious or upset"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentCompulsion = ContentCompulsion + "You are generally relative rational, rarely worry about baseless ideas or do meaningless things compulsively :;[1] Can Intentionally restrain most of absurd thoughts and excessive actions;[2] Have a trust in yourself, you have enough confidence in what you have done recently, not tend to check them repeatedly;[3] Have an effectively control on your own thoughts, you can get rid of unnecessary imaginations and memories timely;[4] no strange habits and inflexible behavior style;[5] Have a relative strong control of life and work, you rarely exaggerate the consequences of mistakes and will not be too anxious or upset"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentCompulsion = ContentCompulsion + "You are somewhat rational, although sometimes may be worried about unfounded ideas,or repeatedly doing meaningless things:;[1] Knowing that certain ideas are absurd and unreasonable ,or certain behaves are excessive, you may not be able to intentionally restrain them;[2] Sometimes may not have sufficient control on your own thoughts to get rid of unnecessary imaginations and memories timely;[3] Have not enough trust in yourself, you do not have enough confidence in what you have done recently, tend to check them repeatedly;[4] With limited flexibility, you may have some strange habits and inflexible behavior style"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentCompulsion = ContentCompulsion + "You may already have some obvious symptoms of obsessive-compulsive disorder, you may troubled by unnecessary thoughts as well as meaningless behavior problems, even feel painful:;[1] Knowing that certain ideas are absurd and unreasonable, or certain behaves are excessive, you cannot intentionally restrain them;[2] Cannot trust yourself, you do not have confidence in what you have done recently, will check them repeatedly;[3] Do not have sufficient control on your own thoughts to get rid of unnecessary imaginations and memories timely, already affected the daily work and life;[4] Behave in a fixed manner, will strictly follow certain routines, inflexible."
            if i['name'] == "偏执心理":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentParanoia = ContentParanoia + "Reasonable and flexible person as you are:;[1] Willing to trust others, have little doubt about motives and desires;[2] Broad-minded, rarely bear any grudge, able to accept others fault;[3] Having a clear self-awareness, can objectively evaluation your own ability."
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentParanoia = ContentParanoia + "Generally reasonable and flexible person as you are:;[1] Willing to trust others, rarely doubt about motives and desires;[2] Broad-minded, not tend to bear any grudge;[3] Willing to establish good relationship with others;[4] Having a relative clear self-awareness, can objectively evaluation your own ability in most cases."
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentParanoia = ContentParanoia + "You have shown a slight tendency to be paranoid, sometimes sensitive and suspicious, stubborn and willful:;[1] May not trust others so much compared with most people;[2] May misunderstand others friendly behavior;[3] May not be able to analyze the situation objectively, often subjective and one-sided;[4] Have a higher estimate of own ability, very tall."
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentParanoia = ContentParanoia + "You have shown a strong tendency to be paranoid, can be quite sensitive and suspicious, stubborn and willful:;[1] Very sensitive，brood on insults and hurts，stubborn, sensitive, suspicious, narrow-minded in action and thoughts;[2] Over confident，only trust ownself;[3] Excessive vigilance and hostility;[4] Overestimate own ability and often exaggerate in working situations."
            if i['name'] == "嫉妒心理":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentJealousy = ContentJealousy + "Open-minded and calm person as you are:;[1] Have a clear understanding of yourself, can evaluate own ability in an objective and rational way;[2] Be able to see the strengths and virtues of others, and praise them for their achievements and abilities;[3] Often show enthusiasm, joy, vigor and high working efficiency;[4] Outstanding resilience"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentJealousy = ContentJealousy + "Relative open-minded and calm person as you are:;[1] Having an objective understanding of own, rarely overestimate your ability and value;[2] Approve others for their achievements and abilities, will not belittle the ability and value of others;[3] Show enthusiasm, joy, vigor and high working efficiency relative often."
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentJealousy = ContentJealousy + "You have shown a slight tendency of jealousy, not open-minded sometimes:;[1] Over self-estimate, have a relatively high evaluation on own ability and personal value;[2] May not approve others’ achievements and abilities, sometimes belittle the ability and value of others;[3] Sometimes lack of optimism and upward mobility, may affect the efficiency of work."
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentJealousy = ContentJealousy + "You have shown a relative strong tendency of jealousy, narrow-minded with unbalanced mentality:;[1] Over self-estimate, overly evaluation on own ability and personal value;[2] Do not approve others’ achievements and abilities, belittle the ability and value of others;[3] Difficult to restrain when someone else do better in any situation, even if a very small matter;[4] Lack of optimism and upward mobility, the efficiency of work and enthusiasm Obviously decreased."
            if i['name'] == "人际适应":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentInterpersonalAdaptation = ContentInterpersonalAdaptation + "Outgoing, warm and understanding person as you are，you will not be entangled in the details or being self-closed:;[1] broad-minded; [2] Very confident, like to express，able to stand up to others' rejection, neglect and negative evaluation,treat people with kindness and trust others, and will not thinking only from a personal standpoint;[3] Mentally strong and optimistic, able to communicate with others calmly and openly;[4] Often participate in various social activities, willing to deal with others."
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentInterpersonalAdaptation = ContentInterpersonalAdaptation + "Relative outgoing, warm and understanding person as you are, you rarely entangled in the details or being self-closed:;[1] Quite broad-minded;[2] Relative confident, like to express，quite able to stand up to others' rejection, neglect and negative evaluation, can treat people with kindness and trust others, not tend to thinking only from a personal standpoint;[3] Mentally quite strong and optimistic, often able to communicate with others calmly and openly;[4] May participate in various social activities, willing to deal with others in most cases."
                elif i['score'] >= 16 and i['score'] <= 20:
                    ContentInterpersonalAdaptation = ContentInterpersonalAdaptation + "Outgoing, warm and understanding as most peoples do，you sometimes may entangled in the details or being self-closed:;[1] Broad-minded as most others do;[2] Sometimes will think only from a personal standpoint;[3] Although not very mentally strong and optimistic,can still deal with others calmly and openly in situation with no great pressure;[4] May participate in various social activities and deal with others when needed"
                elif i['score'] >= 21 and i['score'] <= 25:
                    ContentInterpersonalAdaptation = ContentInterpersonalAdaptation + "Not as outgoing, warm and understanding as most peoples do，you may entangled in the details or being self-closed:;[1] Not as broad-minded as most others do;[2] Often think only from a personal standpoint;[3] Mentally not strong or optimistic, sometimes cannot deal with others calmly and openly;[4] May avoid participate in various social activities and deal with others."
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentInterpersonalAdaptation = ContentInterpersonalAdaptation + "Sensitive in the interpersonal relationship, you refused to establish close relationship with others, which may cause confusion and distress:;[1] Avoid contact with others;[2] Narrow-minded;[3] Think only from a personal standpoint quite often;[4] Mentally not strong or optimistic at all, cannot deal with others calmly and openly;[5] Avoid participate in various social activities and deal with others"
            if i['name'] == "孤独感受":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentLonelyFeeling = ContentLonelyFeeling + "You have a strong, lasting mental support, such as family, friendship, love, faith, interest and many people care for you:;[1] Spend your leisure time in a pleasant way, without a feeling of loneliness;[2] In the face of difficulties or bad mood，there are always some help and comfort;[3] Good interpersonal relationship, fine social resources and support;[4] Can actively deal with competition and pressure"
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentLonelyFeeling = ContentLonelyFeeling + "You have a relative strong, lasting mental support, such as family, friendship, love, faith, interest and quite many people care for you:;[1] Spend your most leisure time in a pleasant way, without a feeling of loneliness;[2] In the face of difficulties or bad mood，there are often some help and comfort;[3] Good interpersonal relationship, relative fine social resources and support;[4] Can actively deal with competition and pressure in most cases"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentLonelyFeeling = ContentLonelyFeeling + "You have some decent mental support, such as family, friendship, love, faith, interest and some people care for you:;[1] Spend your most leisure time in a pleasant way, although sometimes there is a feeling of loneliness;[2] In the face of difficulties or bad mood，there are sometimes help and comfort;[3] Having an interpersonal relationship like most other people, you have some social resources and support;[4] Can deal with competition and pressure like most people"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentLonelyFeeling = ContentLonelyFeeling + "You are lacking of mental support, such as family, friendship, love, faith, interest and there are very few people care for you:;[1] Spend your most leisure time in a lonely way;[2] In the face of difficulties or bad mood，there are almost no help and comfort;[3] Do not have a good interpersonal relationship, you may find it difficult to get some social resources and support;[4] Sometimes cannot deal with competition and pressure like others"
            if i['name'] == "依赖心理":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentAnaclisis = ContentAnaclisis + "Independent, autonomous and creative person as you are:;[1] Actively take part in discussion and decision-making;[2] Objective self-evaluation and self-recognition;[3] Thinking and decision-making on your own, not dependent;[4] Respect other people's thoughts and will;[5] Maintain independence when contacting with others as well as in social activities. "
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentAnaclisis = ContentAnaclisis + "Relative independent, autonomous and creative person as you are:;[1] Be able to take part in discussion and decision-making;[2] Objective self-evaluation and self-recognition;[3] Respect other people's thoughts and will in most situations;[4] Thinking and decision-making on your own, not dependent. "
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentAnaclisis = ContentAnaclisis + "With an relative incompetent self-evaluation, you are a somewhat dependent and lacking of independent consciousness person:;[1] Not able to take part in discussion and decision-making sometimes;[2] Need a lot of advice and assurance in decision-making;[3] Self-depreciation, think others are better, more attractive and more capable;[4] Somewhat passive;[5] Sometimes have the idea and thought of being abandoned."
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentAnaclisis = ContentAnaclisis + "With an incompetent self-evaluation, you are quite dependent and lacking of independent consciousness person:;[1] Cannot make any decision without a lot of advice and assurance;[2] helplessness, let others make the most important decisions, such as where to live and career;[3] fear of being abandoned, only can achieve something with others help and guide;[4] difficult to plan or do anything alone;[5] Willing to do things to please others even if not want to do;[6] Self-depreciation in order to get help from others;[7] Always pin hope on others."
            if i['name'] == "猜疑心理":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentSuspicions = ContentSuspicions + "Willing to trust others , friendly and cooperative person as you are:;[1] Have a positive attitude towards others, believe in the goodness of human nature, willing to cooperate with others;[2] Willing to establish relationships with others, do not doubt the motives of others without sufficient evidence;[3] Able to control emotions, will rarely attack others with words or behaviors;[4] Frank and open-minded, not tend to hold a grudge, do not bring negative mood into works."
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentSuspicions = ContentSuspicions + "Willing to trust others in most cases, relative friendly and cooperative person as you are:;[1] Have a quite positive attitude towards others, believe in the good side of human nature;[2] Often willing to establish relationships with others, not tend to doubt the motives of others without sufficient evidence;[3] Able to control emotions in most situation, in order to avoid negative influence on work and life;[4] Generally trust others, rarely make groundless accusations;[5] Do not like to argue with others, will communicate calmly to solve misunderstanding or conflict."
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentSuspicions = ContentSuspicions + "Although relatively friendly and cooperative in dealing with others, you do not quite trust them and keep alertness:;[1] Sometimes have a negative view on others, even think most people are indifferent and selfish;[2] May worry about other people will damage your interests, may lead to emotional reactions and take a confrontational approach;[3] Sometimes overly sensitive, may be hostile and suspicious to some certain person and keep this altitude for a period."
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentSuspicions = ContentSuspicions + "Relative difficult to deal with, you are not that friendly, not willing to be close to others, and do not want to cooperate:;[1] Have a negative view on others;, even think that all people are indifferent and selfish;[2] May worry about other people will damage your interests, may lead to emotional reactions and take a confrontational approach;[3] Overly sensitive, feel that others are hostile or even will deliberately hurt you;[4] Always keep alert, have an extreme or even distorted point of view on others' behavior;[5] Cannot control emotions, have done some things like: throwing things, tearing the file and other acts, as well as insult others."
            if i['name'] == "焦虑情绪":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentAnxiety = ContentAnxiety + "A calm, optimistic, open-minded, cheerful person as you are:;[1] Able to deal with all kinds of pressure and solve various problems skillfully and efficiently;[2] Have a good control of the environment, have a precise predict of what is likely to happen;[3] Easy-going, good at communication;[4] Healthy, free from pain, discomfort, weakness;[5] Tolerant, indifferent to fame and wealth;[6] Good time management capability."
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentAnxiety = ContentAnxiety + "A relative calm, optimistic, open-minded, cheerful person as you are:;[1] Able to deal with all kinds of problems, rarely get panic or fear when the problem cannot be solved on your own;[2] Easy-going, treat others well, good at communication;[3] Quite healthy, will not be distressed by slight discomfort or illness;[4] Tolerant, relative indifferent to fame and wealth;[5] Relative good time management capability."
                elif i['score'] >= 16 and i['score'] <= 20:
                    ContentAnxiety = ContentAnxiety + "Your anxiety level is moderate，may sometimes be upset about the trouble in work and life:;[1] Although being able to cope with most of the stress, sometimes still have panic, bad emotions, which may bring trouble;[2] As healthy as most people, some times will worry about disease and illness;[3] Average confidence, doubts about uncertain things, and admires the boss or authority;[4] Value fame and fortune, sometimes will feel stress from competition;[5] Indecisive, shillyshally, may fall into remorse of a lost opportunity;[6] Sometimes cannot finish the work on time, will experience some anxiety when catching up."
                elif i['score'] >= 21 and i['score'] <= 25:
                    ContentAnxiety = ContentAnxiety + "Your anxiety level is relative high，often upset about the trouble in work and life:;[1] Although being able to barely cope with most of the problems, sometimes will still be exceeded, and may choose to delay or avoid problems in the face of stress;[2] Not as healthy as most people, may have dizziness, chest tightness, frequent urination, sweating and other somatic symptoms;[3] Have a feeling of surrounded by uncertain factors;[4] Do not know how to get help in an adequate way from adequate person, may spread anxiety to people around you;[5] Self-demanding, poor grasp of own ability and working progress, sometimes cannot finish the work on time and results in great upset."

                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentAnxiety = ContentAnxiety + "Your anxiety level is high, lacking of security and sense of control, often upset about the trouble in work and life:;[1] Not able to cope with most of the problems, feel exhausted, do not know how to properly deal with;[2] Not at all healthy, may be often troubled by pain and illness;[3] Have a feeling of surrounded by uncertain factors;[4] Very self-demanding, poor grasp of own ability and working progress, difficult to find balance between ideal and reality;[5] Feel nervous for no reason, a little frustration may cause emotional breakdown, can bring great negative impact to work and life;[6] Lack of confidence and sense of security;[7] Cannot properly express and control emotions, poor interpersonal relationships."
            if i['name'] == "冲动控制":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentImpulsiveControl = ContentImpulsiveControl + "Mature, calm, friendly person as you are:;[1] Emotionally stable, rarely have breakout, good at self-control;[2] Careful, tend to avoid risks, take the consequences into accounts, very little impulse;[3] Have a normal language and thinking ability, able to calm down when face problems;[4] Rational, objective."
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentImpulsiveControl = ContentImpulsiveControl + "Relative mature, calm, friendly person as you are:;[1] Emotionally stable, quite good at self-control;[2] Careful, tend to avoid risks, take the consequences into accounts, very little impulse in most situations;[3] Quite rational and objective"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentImpulsiveControl = ContentImpulsiveControl + "Not as calm as most people, somewhat emotional as you are:;[1] Emotionally unstable;[2] Somewhat careless, may not take the consequences into accounts;[3] May be not enough calm when facing problems, lack of emotional control."
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentImpulsiveControl = ContentImpulsiveControl + "With Obvious impulsive symptoms, you may easily lose control because of tiny things:;[1] Sudden rage, usually lack of reason and with blindness;[2] Blame own self after rage, but will still lose control next time, has obvious paroxysmal characteristics;[3] In the impulsive period, the consciousness is narrow, the cognition is one-sided, the judgment decline, difficult to control and adjust the language behavior."
            if i['name'] == "抑郁倾向":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentDepressiveTendency = ContentDepressiveTendency + "Vigor, cheerful and optimistic, you are positive and peaceful in the daily work and life:;[1] rarely depressed or pessimistic, often in high and vigorous spirits and smiling;[2] Feel there are a lot of interesting, worthwhile things in the life, such as friends, hobbies, etc;[3] Thinking and language functions are normal, responsive;[4] Self-acceptance;[5] Healthy, Sleep and eat well, vigor;[6] Eager to communicate with others, good interpersonal relationships;[7] Can accept the reality，even in the face of setbacks and blows."
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentDepressiveTendency = ContentDepressiveTendency + "Relative vigor, cheerful and optimistic, you are quite positive and peaceful in the daily work and life:;[1] Rarely depressed or pessimistic, you are confident and hopeful;[2] Feel there are some interesting, worthwhile things in the life, such as friends, hobbies, etc.;[3] Thinking and language functions are normal, responsive;[4] Self-acceptance;[5] Healthy, Sleep and eat well, vigor;[6] Willing to communicate with others, and can make a reasonable judgment to the environment and events;[7] Can accept the reality，even in the face of setbacks and blows."
                elif i['score'] >= 16 and i['score'] <= 20:
                    ContentDepressiveTendency = ContentDepressiveTendency + "Generally speaking, sometimes you experience mood swings. You will be happy and optimistic when the situation is good and contented, but you may be pessimistic and disappointed when you suffer setbacks and difficulties. The possible performance is:;[1] Easily with affection of environment, sometimes the mood changed because of changes in the environment;[2] You don't want to contacts when you are in a bad mood, and avoid stepping outside your home, you are also dismissive of past hobbies;[3] Thinking and language functions are normal, but it's easy to get confused and distracted when you're depressed;[4] You are not very confident, sometimes you feel lost about your future, and you may feel frustrated about recent situation;[5] Sometimes you suffer the trouble of disease, such as chest tightness, gastrointestinal discomfort, constipation, etc.;[6] Sometimes you can not sleep well, mental fatigue and loss of appetit;[7] General stress resistance, sometimes you may be panic in face of difficulty."
                elif i['score'] >= 21 and i['score'] <= 25:
                    ContentDepressiveTendency = ContentDepressiveTendency + "Generally speaking, you tend to be slightly depressed, sometimes you feel depressed and even pessimistic. The possible performance is:;[1] You may feel depressed, bored, and unfulfilled at work;[2] Sometimes you love sulking. When misunderstanding occurs, you seldom communicate with others and bring negative emotions into your work;[3] When you are in a bad mood, you have little interest in the things around you and lack the will and energy to participate in various activities;[4] Not very confident, sometimes doubt your own value, even feel inferior;[5] The ability of thinking is affected greatly by emotion. When you are depressed, the thinking is slow and the work is lazy;[6] Bad appetite, dropping appetite, bad sleeping, sometimes you wake up in the morning feeling very tired;[7] The ability to resist pressure is relatively weak, setbacks and obstacles make you depressed and helpless, and affect your mood seriously."
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentDepressiveTendency = ContentDepressiveTendency + "Generally speaking, you have shown more obvious symptoms of depression. You are often in a bad mood, and you have pessimistic disappointed feelings, even have the idea of world-weariness. The possible performance is:;[1] Often depressed, no interest in the things around, feeling that life is a burden and one day seems a year;[2] Physical and mental exhaustion, lack of enthusiasm for work, difficulty in concentration, the efficiency of work is seriously affected;[3] You feel hopeless and not confident, and you doubt your own value;[3] You feel hopeless and not confident, and you doubt your own value;[4] Passive in interpersonal communication, lack of willingness to communicate with others;[5] Declined mental ability, declined memory, slower action;[6] Often being ill, poor diet and sleep, sometimes sexual function also suffering exhaustion;[7] Waking up early and not being able to fall asleep, falling into a sad mood and a clear trend of weight loss;[8] You often feel anxious and view yourself critically and negatively. You even have the concept of self-guilt."
            if i['name'] == "环境适应":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentEnvironmentalAdaptation = ContentEnvironmentalAdaptation + "Generally speaking, your social adaptability is very well. You can adjust your personal needs according to the changes of the environment and your own development, and you can face the difficulties in work and live with a positive attitude. The possible performance is:;[1] Good communication skills, ability to quickly build relationships with people around you, being able to achieve success one way or another;[2] Highly rational, practical and easily accepted by others;[3] You can maintain appropriate contact with the environment, but you are not a person who only focus on the immediate interests;[4] You can endure a moment of frustration and pain, and delay gratification;[5] Mostly, your values is same as social mainstream values, and you have the appropriate pursuit of individual needs."
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentEnvironmentalAdaptation = ContentEnvironmentalAdaptation + "Generally speaking, your social adaptability is well, and you can adjust your personal needs according to the changes in the environment and your own development, and you can face the difficulties in work and live with a more positive attitude. The possible performance is:;[1] Good communication skills, able to build a harmonious relationship with people around you;[2] More rational, making reasonable plan, practical and easily accepted by others;[3] You are able to learn from the failure and gradually accumulate experience, and you can endure a temporary setback and pain;[4] Your values is same as social mainstream values, and you have the appropriate pursuit of individual needs."
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentEnvironmentalAdaptation = ContentEnvironmentalAdaptation + "Generally speaking, your social adaptability is not good enough. Sometimes it is difficult to adjust your personal needs according to the changes in the environment or your own development, and your attitude is not positive enough. The possible performance is:;[1] Lack of good communication skills, may take a long time to integrate into the new environment;[2] Sometimes being impulsive and capricious, simple idea, impractical suggestions;[3] Usually you can learn from the failure and accumulate experience gradually, but you lack perseverance and long-term vision, and you may feel confused and depressed;[4] There may be some conflict between your values and the mainstream values of society, sometimes, it seems selfish;[5] The ability to resist setbacks is not well, sometimes, it is difficult to control your negative emotions."
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentEnvironmentalAdaptation = ContentEnvironmentalAdaptation + "Generally speaking, your social adaptability is severely inadequate, and it is difficult to adjust your personal needs according to the changes in the environment and your own development. The possible performance is:;[1] Lack of basic communication skills, and it takes a long time to integrate into the new environment;[2] Impulsive and capricious behavior, simple idea, impractical suggestions;[3] Difficult to learn from failure, lack of perseverance, lack of long-term vision, easy to feel confused and depressed;[4] There is a huge conflict between the values and the social mainstream values, sometimes, you may feel too selfish;[5] The ability to resist setbacks is relatively poor, and it is difficult to control your negative emotions."
            if i['name'] == "恐惧心理":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentFear = ContentFear + "Generally speaking, you are a brave and calm person who is not in a panic. The possible performance is:;[1] You are comfortable in social situations, even if someone is staring at you;[2] You dare to express yourself in public, and you even like to speak or perform in public;[3] There is no place or space to be afraid, and you can go calmly in and out of any situation;[4] There is nothing to be afraid. Even if you are frightened, you will soon recover;[5] Physical health, rarely chest tightness, rarely breathing difficulties or syncope, strong ability to control life and work."
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentFear = ContentFear + "Generally speaking, you are daring, less flustered and calmer. The possible performance is:;[1] There is no mental shadow left by life events or things being seriously frightened;[2] You can be comfortable in social situations and communicate with others easily and happily, but you don't want to be the focus of others' attention, otherwise you may feel uncomfortable;[3] No fear of empty fields, no fear of crowded, enclosed rooms or vehicles;[4] One or two things scare you occasionally, and the emotions dissipate more quickly;[5] Good ability to control life and work, confident relatively."
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentFear = ContentFear + "Generally speaking, you are less daring, sometimes, too sensitive. The uncertain factors in work or life often make you worry and being anxious. The possible performance is:;[1] Having been severely frightened or humiliated that you may be afraid of certain things or situations, but you are able to overcome this fear;[2] Sometimes you feel uncomfortable in social situations, and you feel reluctant to communicate with others;[3] You may be afraid of going to an empty place, and be afraid of crowded, enclosed rooms or vehicles;[4] When in trouble or something you can't control, you may panic"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentFear = ContentFear + "Generally speaking, you have obvious symptoms of phobias, with strong and unnecessary fear of a particular object or scene, and accompanying avoidance and withdrawal behavior. The possible performance is:;[1] You may avoid social situations, feel uncomfortable, and find it difficult to communicate with others naturally;[2] You are often not confident enough to accept yourself, or are too demanding of yourself. Once you feel that you are unable to do your job or cope with some problems, you will be disappointed, painful and afraid.[3] You may be afraid of going to an empty place, and be afraid of crowded, enclosed rooms or vehicles;[4] When the fear hit, you often cannot get rid of, and you may feel despairing, corrupted, chest tightness, pale face, heart palpitations and other symptoms, even fainted on the spot."
            if i['name'] == "身心同一":
                if i['score'] >= 6 and i['score'] <= 10:
                    ContentBodyAndMind = ContentBodyAndMind + "Generally speaking, you are a realist, responsible and trustworthy. The possible performance is:;[1] Cognition, will, movement and other aspects are very normal, there is no disease or non-coordination of the situation;[2] Emotional stability, compassionate, often warm, pay attention to distance;[3] Identify with authority, respect those who are truly learned and capable, and be submissive;[4] Good interpersonal relationships, easy-going and sociable;[5] Care about the success and status of individuals, have a clear understanding of the reality, but when making decisions tend to be conservative;[6] Be interested in participating in some social activities and keep some initiative in work;[7] At times, seems rigid, monotonous and unimaginative."
                elif i['score'] >= 11 and i['score'] <= 15:
                    ContentBodyAndMind = ContentBodyAndMind + "Generally speaking, you pay more attention to reality, have a strong sense of responsibility, and deserve the trust of people around you. The possible performance is:;[1] Cognitive, emotional, volitional, motor, sensory and other functions are relatively normal.[2] There is no obvious disease or concomitant disorder;[3] Have a wide range of interests and hobbies. Be willing to establish close relationships with others and treat others kindly and politely.[4] Like concrete things, also like abstract thinking, sometimes will discuss with others, but often stubborn;[5] With respect to authority, with obedience to superiors, sometimes conservative, lack of competitive awareness;[6] The mood is more stable, sometimes not good expression of emotion, even timid, shy"
                elif i['score'] >= 16 and i['score'] <= 25:
                    ContentBodyAndMind = ContentBodyAndMind + "Generally speaking, you are more idealistic, imaginative and have different views and ideas from others. The possible performance is:;[1] Mental function is basically normal, sometimes temporary mental disorder, abnormal emotion and depression may occur;[2] You have a wide range of interests and hobbies, but your attention is easily distracted and often lack perseverance;[3] Your emotions sometimes fluctuate greatly, and social withdrawal occurs, such as suddenly becoming cold and unwilling to talk with others;[4] You prefer abstract things, such as philosophy, but the content of thinking is often hard for others to understand;[5] People who are not responsible tend to have limited respect and deference to superiors and authorities;[6] In times of adversity, it is possible to escape reality through fantasy or daydreaming"
                elif i['score'] >= 26 and i['score'] <= 30:
                    ContentBodyAndMind = ContentBodyAndMind + "Generally speaking, you have more obvious symptoms of schizophrenia, the mind has been out of the real environment, has appeared various functional disorders in cognitive, emotional, will, movement, feeling, etc. The possible performance is:;[1] Sometimes confusion, lack of logic and purpose, or mind control by others;[2] May also appear some delusion, if you want to feel someone hurt you, strange deformation happened in parts of our body, they have a noble lineage, etc.;[3] May appear some illusion, if see there is no image, or hear someone talking to you in the air;[4] More withdrawn personality, don't want to deal with other people, lazy, the ability to work and life serious decline;[5] The emotion is very cold, often deadpan, no sympathy, can also be difficult to understand other people's feelings;[6] You often do some strange things, even ridiculous."

        report10['msg']["ContentSomaticReaction"] = ContentSomaticReaction
        report10['msg']["ContentAvoidanceBehavior"] = ContentAvoidanceBehavior
        report10['msg']["ContentFantasies"] = ContentFantasies
        report10['msg']["ContentSelfReproach"] = ContentSelfReproach
        report10['msg']["ContentCompulsion"] = ContentCompulsion
        report10['msg']["ContentParanoia"] = ContentParanoia
        report10['msg']["ContentJealousy"] = ContentJealousy
        report10['msg']["ContentInterpersonalAdaptation"] = ContentInterpersonalAdaptation
        report10['msg']["ContentLonelyFeeling"] = ContentLonelyFeeling
        report10['msg']["ContentAnaclisis"] = ContentAnaclisis
        report10['msg']["ContentSuspicions"] = ContentSuspicions
        report10['msg']["ContentAnxiety"] = ContentAnxiety
        report10['msg']["ContentImpulsiveControl"] = ContentImpulsiveControl
        report10['msg']["ContentDepressiveTendency"] = ContentDepressiveTendency
        report10['msg']["ContentEnvironmentalAdaptation"] = ContentEnvironmentalAdaptation
        report10['msg']["ContentFear"] = ContentFear
        report10['msg']["ContentBodyAndMind"] = ContentBodyAndMind
        report10['msg']["ChartYellowIndex"] = ChartYellowIndex
        report10['msg']["ChartOrangeIndex"] = ChartOrangeIndex
        report10['msg']["ChartRedIndex"] = ChartRedIndex
        report10['msg']['Validation'] = v1
        res = {"code": 0, 'detail': {'report_data': report10}}
        print('发送到word服务的数据:%s' % res)
        return res
    elif report_type_id == "HappinessNeeds":
        try:
            report12 = d['detail']['report_data']
            print('report12打印：%s' % report12)
        except Exception as e:
            res = {"code": 40400, 'detail': {'report_data': e}}
            return res
        res = {"code": 0, 'detail': {'report_data': report12}}
        print('发送到word服务的数据:%s' % res)
        return res

    elif report_type_id == "CapacityEvaluation":
        try:
            report13 = d['detail']['report_data']
            print('report13打印：%s' % report13)
        except Exception as e:
            res = {"code": 40400, 'detail': {'report_data': e}}
            return res
        res = {"code": 0, 'detail': {'report_data': report13}}
        print('发送到word服务的数据:%s' % res)
        return res

    elif report_type_id == "C1":
        try:
            report14 = d['detail']['report_data']
            print('report15打印：%s' % report14)
        except Exception as e:
            res = {"code": 40400, 'detail': {'report_data': e}}
            return res
        res = {"code": 0, 'detail': {'report_data': report14}}
        print('发送到word服务的数据:%s' % res)
        return res

    elif report_type_id == "C2":
        try:
            report15 = d['detail']['report_data']
            print('report15打印：%s' % report15)
        except Exception as e:
            res = {"code": 40400, 'detail': {'report_data': e}}
            return res
        res = {"code": 0, 'detail': {'report_data': report15}}
        print('发送到word服务的数据:%s' % res)
        return res
    
    elif report_type_id == "YGZWTS":
        try:
            report16 = d['detail']['report_data']
            print('report16打印：%s' % report16)
        except Exception as e:
            res = {"code": 40400, 'detail': {'report_data': e}}
            return res
        res = {"code": 0, 'detail': {'report_data': report16}}
        print('发送到word服务的数据:%s' % res)
        return res

    elif report_type_id == "ZYDX":
        try:
            report17 = d['detail']['report_data']
            print('report17打印：%s' % report17)
        except Exception as e:
            res = {"code": 40400, 'detail': {'report_data': e}}
            return res
        res = {"code": 0, 'detail': {'report_data': report17}}
        print('发送到word服务的数据:%s' % res)
        return res
    
    elif report_type_id == "ZGC180":
        try:
            report18 = d['detail']['report_data']
            print('report18打印：%s' % report18)
        except Exception as e:
            res = {"code": 40400, 'detail': {'report_data': e}}
            return res
        res = {"code": 0, 'detail': {'report_data': report18}}
        print('发送到word服务的数据:%s' % res)
        return res
    
    elif report_type_id == "ZGC90":
        try:
            report18 = d['detail']['report_data']
            print('report18打印：%s' % report18)
        except Exception as e:
            res = {"code": 40400, 'detail': {'report_data': e}}
            return res
        res = {"code": 0, 'detail': {'report_data': report18}}
        print('发送到word服务的数据:%s' % res)
        return res
    
    else:
        res = {"code": 40400, 'detail': {'report_data': "传参错误请检查参数"}}
        print('发送到word服务的数据:%s' % res)
        return res
