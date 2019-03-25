import json, sys, time, requests, simplejson, re
from django.shortcuts import render
from django.http import HttpResponse

from . import models
from .tasks import get_report


# Create your views here.


def index(request):
    """
    维度报告首页视图处理函数
    :param request:
    :return:
    """
    if request.method == "GET":

        return render(request, "report/index.html", {'msg': ''})


    elif request.method == "POST":
        pass
        # res = {'msg': ''}
        # return HttpResponse(json.dumps(res), content_type="application/json")


def user_get_report(request):
    """
    用户获取报告函数
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "report/user_get_report.html", )


def user_get_all_report(request):
    """
    用户获取已做过测评的所有报告函数
    :param request:
    :return:
    """

    user_report_list = models.UserReport.objects.filter()

    return render(request, "report/user_get_all_report.html", {'user_report_list': user_report_list})


def user_get_specific_report(request):
    """
    用户获取指定报告函数
    :param request:
    :return:
    """
    if request.method == "GET":
        res = {"code": 0, "detail": {"msg": "请用post方式获取"}}
        return HttpResponse(json.dumps(res, ensure_ascii=False).encode('utf-8'), content_type="application/json")

    elif request.method == "POST":
        # 获取数据
        try:
            req_list = simplejson.loads(request.body)
            print('测评端拿到的数据：%s' % req_list)
        except Exception as e:
            res = {"code": 2, "detail": {'status': '', "url": '', 'msg': '只接受post请求,请检查参数和请求方式'}}
            return HttpResponse(json.dumps(res, ensure_ascii=False).encode('utf-8'), content_type="application/json")
        new_result = dict()
        for index, req in enumerate(req_list):
            try:
                people_result_id = req['people_result_id']
                report_type_id = req['report_type_id']
                force_recreate = req.get('force_recreate', False)
                # TODO 解析测评端其余数据
            except Exception as e:
                res = {"code": 2, "detail": {'status': '', "url": '', 'msg': '只接受post请求,请检查参数和请求方式'}}
                return HttpResponse(json.dumps(res, ensure_ascii=False).encode('utf-8'),
                                    content_type="application/json")
            try:
                # 从数据库中查询报告
                user_report_list = models.UserReport.objects.filter(
                    people_result_id=people_result_id,
                    report_type_id=report_type_id
                )
                # TODO 增加其他字段
                print(type(user_report_list))
                print(len(user_report_list))
                data = {
                        "people_result_id": people_result_id,
                        "report_type_id": report_type_id
                    }
                if len(user_report_list) == 0 or force_recreate:
                    # 数据库中暂无报告 创建该条报告信息

                    #   TODO 启动任务 生产报告，更新数据库报告状态

                    
                    get_report.delay(data)
                    if data["report_type_id"] == 'HAMeasurePersonal_EN' or data["report_type_id"] == 'EmployeeMentalHealth_EN':
                        new_result[index] = {'status': 0, 'en_url': ""}
                    else:

                        new_result[index] = {'status': 0, 'url': ""}

                else:
                    if data["report_type_id"] == 'HAMeasurePersonal_EN' or data["report_type_id"] == 'EmployeeMentalHealth_EN':
                        new_result[index] = {'status': user_report_list[0].status, "en_url": user_report_list[0].url}
                    else:

                        new_result[index] = {'status': user_report_list[0].status, "url": user_report_list[0].url}
            except Exception as e:
                print(e)
                res = {"code": 0, "detail": {'status': '', "url": '', 'msg': e}}
                return HttpResponse(json.dumps(res, ensure_ascii=False).encode('utf-8'),
                                    content_type="application/json")
        res = {"code": 0, "detail": new_result}
        return HttpResponse(json.dumps(res, ensure_ascii=False).encode('utf-8'), content_type="application/json")


def send_report_data(request):
    """
    word服务 请求报告信息接口
    :param request:
    :return:
    """
    if request.method == "GET":

        res = {"code": 40400, 'detail': {'report_data': "请用post方式请求"}}
        return HttpResponse(json.dumps(res, ensure_ascii=False).encode('utf-8'), content_type="application/json")

    elif request.method == "POST":
        # 获取 word 服务传来的数据 json数据

        try:
            print(request.body)
            print(type(request.body))
            req = simplejson.loads(request.body)

            questionnaire_id = req['questionnaire_id']
            assess_project_id = req['assess_project_id']
            user_id = req['user_id']
            report_type_id = req['report_type_id']
        except Exception as e:
            res = {"code": 40400, 'detail': {'report_data': "请检查传递参数是否有误"}}
            return HttpResponse(json.dumps(res, ensure_ascii=False).encode('utf-8'), content_type="application/json")

        url = "http://assessment.iwedoing.com/api/client/v1/front/report/data/"
        data = {"questionnaire_id": questionnaire_id,
                "assess_project_id": assess_project_id,
                "user_id": user_id,
                "report_type_id": report_type_id
                }
        try:
            res = requests.post(url=url, data=data, timeout=15)
        except Exception as e :
            print('算分服务响应超时')

        d = eval(res.text)
        print('算分服务发来的数据:%s' % d)
        if d["code"] != 0:
            res = {"code": 40400, 'detail': {'report_data': "算分服务无法提供数据,"}}
            return HttpResponse(json.dumps(res, ensure_ascii=False).encode('utf-8'), content_type="application/json")

        try:
            report07 = d['detail']['report_data']
            print('report07%s' % report07)
        except Exception as e:
            print('请求数据暂无')
        try:
            report08 = d['detail']['report_data']
        except Exception as e:
            print('请求数据暂无')
        from .report_templates import report01, report02, report04, report05, report06
        if report_type_id == "LeaderShipStyle":
            # # 对拿到的数据进行整理判断
            chart_data = report02()['msg']['chart']
            ContentTheMain = ""
            ContentLessUsed = ""
            ContentManagementBe = ""
            Content = [{"name": "高压风格",
                        "desc": "不断的给出命令，期望下属立刻服从;密切的监督和控制下属的工作进程;关注发现的问题，经常给出负面的、纠正性的反馈;强调不服从所导致的负面后果来激发团队成员服从;"},
                       {"name": "教练风格",
                        "desc": "鼓励员工确定长期的职业发展目标，帮助制订明确的实施计划;应用倾听技巧和开放性问题来鼓励团队成员解决自己的问题;擅长授权，会布置给员工挑战性的任务;将错误视为学习机会，为了员工的成长愿意接受暂时的失败;"},
                       {"name": "权威风格",
                        "desc": "为团队制定和传达清晰的使命和方向;用清晰的目标激励员工，让他们清楚地认识到本岗位与组织总体愿景之间的联系;会把宏大的愿景分解为个体的目标任务，并围绕组织愿景制定工作标准;允许员工自由创新、尝试各种方法，并愿意承担可衡量的风险;"},
                       {"name": "亲和风格",
                        "desc": "提倡团队成员之间保持友好的关系;关注团队成员的情感需求，而不是工作任务的指引、目标和标准;追求员工的满意以及团队的和谐，通过与员工建立牢固的感情联系，获得员工强烈的忠诚;避免与绩效相关的冲突，创造能带来积极反馈的机会;"},
                       {"name": "民主风格",
                        "desc": "愿意花时间听取集体意见，争取民意;允许员工对自己的任务目标以及工作方式保留发言权;通过组织许多会议来作出决策，希望通过深入讨论最终达成共识;"},
                       {"name": "模范风格",
                        "desc": "相信团队成员有能力为自己和团队确定合适的指引;设定特别高的业绩标准，并且以身作则，亲自示范;强迫自己更高质量、更快速地完成工作，而且要求别人跟他一样;倾向于亲力亲为，独立完成工作任务，只有紧急任务时，才与他人协调;在团队成员遇到问题时，提供详细的工作指引;"},
                       ]
            for i in chart_data:
                if i['score'] >= 60:
                    # 主要使用的领导风格判断
                    ContentTheMain = ContentTheMain + i['name'] + ","
                if i['score'] in [40, 59]:
                    # 较少使用的领导风格判断
                    ContentLessUsed = ContentLessUsed + i['name'] + ","
            # 管理行为判断
            for i in ContentTheMain.split(','):
                for j in Content:
                    if i == j["name"]:
                        ContentManagementBe = ContentManagementBe + j["desc"]
            # print(ContentManagementBe)
            report02()['msg']["ContentTheMain"] = ContentTheMain
            report02()['msg']["ContentLessUsed"] = ContentLessUsed
            report02()['msg']["ContentManagementBe"] = ContentManagementBe
            res = {"code": 0, 'detail': {'report_data': report02()}}
            print('发送到word服务的数据:%s' % res)
            return HttpResponse(json.dumps(res, ensure_ascii=False).encode('utf-8'), content_type="application/json")
        elif report_type_id == "BehavioralStyle":
            chart_data = report01()['msg']['chart']
            # 能量指向
            ContentEnergyPt = ""
            # 信息收集方式
            ContentInfoCol = ""
            # 信息加工方式
            ContentInfoProc = ""
            # 行动方式
            ContentActMethod = ""

            for i in chart_data:
                if i['name'] == "能量指向":
                    if i['score'] >= 17:
                        # 能量指向
                        ContentEnergyPt = ContentEnergyPt + "合群、开放易沟通，坦率随和、好交际，愿意自由地与他人分享与交流，喜欢快节奏行动，对外部环境敏感，易于受到外部环境的影响。"
                    if i['score'] >= 8 and i['score'] <= 16:
                        # 能量指向
                        ContentEnergyPt = ContentEnergyPt + "喜欢接触外界环境，愿意与别人进行沟通，较为喜欢与他人自由地分享与交流，不拘束，喜欢行动，有时会受到外部环境的影响。"

                    if i['score'] >= 0 and i['score'] <= 7:
                        # 能量指向
                        ContentEnergyPt = ContentEnergyPt + "虽能将兴趣和注意力指向外部客观事物，但范围不大，在熟悉情境下能够与人开放沟通、交流分享表现一定的外向特点，有时喜欢独自思考，表现出一定的内倾特点，两者较均衡，特点不太突出。"
                    if i['score'] >= -3 and i['score'] <= -1:
                        # 能量指向
                        ContentEnergyPt = ContentEnergyPt + "相对而言，能够集中于自己内心的思想和体验，倾向于独立思考，也愿意与他人开放沟通与交流，表现出一定的外倾特点。"
                    if i['score'] >= -7 and i['score'] <= -4:
                        # 能量指向
                        ContentEnergyPt = ContentEnergyPt + "喜欢独立思考，做事比较谨慎，相对喜欢独立工作，较为专注，在与人沟通有一定的选择性。"
                    if i['score'] <= -8:
                        # 能量指向
                        ContentEnergyPt = ContentEnergyPt + "喜欢独自深度思考，做事谨慎，先思考后行动，沉静而专注，满足于独立工作，与人沟通有较强的选择性，只在小群体中进行分享。"
                elif i['name'] == "信息收集方式":
                    if i['score'] >= 14:
                        # 信息收集方式
                        ContentInfoCol = ContentInfoCol + "善于通过收集具体的信息了解外在世界，关注具体问题和事务的细节，着眼现实，注重结果，乐于从事具体而明确的工作，做事细心周到。"
                    if i['score'] >= 5 and i['score'] <= 13:
                        # 信息收集方式
                        ContentInfoCol = ContentInfoCol + "喜欢通过收集具体的信息了解外在世界，较为关注具体问题和事务的细节，比较喜欢从事具体而明确的工作，做事往往能从现实出发，注重结果。"
                    if i['score'] >= 0 and i['score'] <= 4:
                        # 信息收集方式
                        ContentInfoCol = ContentInfoCol + "相对而言，通过收集具体的信息了解外在世界，在一定程度上倾向于关注具体细节、做事一般能从现实出发，对具体而明确的工作有一定的偏好表现出一定的直觉型特点，但有时也能关注到事物的整体和发展规律，表现出一定的直觉型特点，两者比较均衡，特点不太突出。"

                    if i['score'] >= -6 and i['score'] <= 1:
                        # 信息收集方式
                        ContentInfoCol = ContentInfoCol + "相对而言，能够关注事物的全貌或整体，会考虑一些事物的意义、联系和可能的变化，但也会关注当前的现实以及事务的细节，表现出一些感觉型的特点。"
                    if i['score'] >= -10 and i['score'] <= -7:
                        # 信息收集方式
                        ContentInfoCol = ContentInfoCol + "较为关注事物的全貌或整体，能够把握事物的意义、联系和发展的可能性，表现出思维跳跃、追求变化的特点，不太喜欢一成不变、细节性的事情。"
                    if i['score'] <= -11:
                        # 信息收集方式
                        ContentInfoCol = ContentInfoCol + "关注事物的全貌或整体，善于把握事物的意义、联系和发展的可能性，表现出思维跳跃、追求变化的特点，但可能忽略现实，不关心细节，不喜欢一成不变的环境。"
                elif i['name'] == "信息加工方式":
                    if i['score'] >= 12:
                        # 信息加工方式
                        ContentInfoProc = ContentInfoProc + "严格按照客观理性、逻辑推理进行客观分析和决策，重视客观事实、公正原则、现实规则；在决策时不考虑决策对他人的影响，也不喜欢他人感情用事。"
                    if i['score'] >= 3 and i['score'] <= 11:
                        # 信息加工方式
                        ContentInfoProc = ContentInfoProc + "能够按照客观理性、逻辑推理进行决策，能以客观事实、公正原则、现实规则解决问题；有时不太考虑决策对他人的影响。"
                    if i['score'] >= 0 and i['score'] <= 2:
                        # 信息加工方式
                        ContentInfoProc = ContentInfoProc + "相对而言，在分析问题或作判断时，一般能以事物的逻辑性和事实为依据表现出一定的思考型特点；但也会考虑决策对他人的影响，表现出一定的情感型的特点，两者较均衡，特点不太突出。"
                    if i['score'] >= -8 and i['score'] <= -1:
                        # 信息加工方式
                        ContentInfoProc = ContentInfoProc + "相对而言，能够权衡问题的相对价值和利益进行决策，有时也会考虑客观理性，依据逻辑进行分析判断，表现出思考型的特点。"
                    if i['score'] >= -11 and i['score'] <= -9:
                        # 信息加工方式
                        ContentInfoProc = ContentInfoProc + "做决定时倾向于以主观因素为依据，通过权衡问题的相对价值和利益进行决策，会考虑对他人的影响以及他人的感受。"
                    if i['score'] <= -12:
                        # 信息加工方式
                        ContentInfoProc = ContentInfoProc + "常常喜欢以主观因素为依据来做决定，主要是通过权衡问题的相对价值和利益进行决策，关注对他人的影响，有时会过于考虑他人的感受。"
                elif i['name'] == "行动方式":
                    if i['score'] >= 13:
                        # 行动方式
                        ContentActMethod = ContentActMethod + "具有很强的计划性、条理性，善于组织、决断和控制，关注结果的达成，但有时缺乏弹性与灵活。"
                    if i['score'] >= 5 and i['score'] <= 12:
                        # 行动方式
                        ContentActMethod = ContentActMethod + "具有较强的计划性和条理性，能够对行动进行组织和控制，关注任务完成。"
                    if i['score'] >= 0 and i['score'] <= 4:
                        # 行动方式
                        ContentActMethod = ContentActMethod + "相对而言，有一定的计划性和条理性，有时也表现出一定的灵活性，表现出一定的知觉型特点和判断型特点，两者较均衡，特点不太突出。"
                    if i['score'] >= -4 and i['score'] <= -1:
                        # 行动方式
                        ContentActMethod = ContentActMethod + "相对而言，有一定好奇、灵活适应的特征，做事情也会有一定的计划性和条理性，表现出一定的判断型特征。"
                    if i['score'] >= -8 and i['score'] <= -5:
                        # 行动方式
                        ContentActMethod = ContentActMethod + "具有较强的开放、好奇的特征，由较强的灵活性和适应性，相对于结果更注重过程，不愿意受到约束，不太注重计划性。"
                    if i['score'] <= -9:
                        # 行动方式
                        ContentActMethod = ContentActMethod + "具有很强的开放、好奇的特征，灵活性和适应性强，思考多于行动，注重过程而不是结果，对规则和约束反感，有时会欠缺计划性和坚持性。"

            report01()['msg']["ContentEnergyPt"] = ContentEnergyPt
            report01()['msg']["ContentInfoCol"] = ContentInfoCol
            report01()['msg']["ContentInfoProc"] = ContentInfoProc
            report01()['msg']["ContentActMethod"] = ContentActMethod

            res = {"code": 0, 'detail': {'report_data': report01()}}
            print('发送到word服务的数据:%s' % res)
            return HttpResponse(json.dumps(res, ensure_ascii=False).encode('utf-8'), content_type="application/json")
        elif report_type_id == "EmployeeMentalHealth":
            chart_data = report04()['msg']['chart']
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
                        ContentSomaticReaction = ContentSomaticReaction + "一般来说，您具有良好的身体状态，可能的表现为：精力充沛，具有较强的工作兴趣和较高的工作效率；极少产生持久而强烈的身体疼痛感；即使产生身体疲劳感，也能够通过休息很快恢复。"
                    elif i['score'] >= 11 and i['score'] <= 15:
                        ContentSomaticReaction = ContentSomaticReaction + "一般来说，您基本具有较好的身体状态，可能的表现为：较少表现出明显的胃肠道症状，比如腹痛、腹胀、恶心、呕吐等；较少表现出持久、严重且强烈的身体疼痛感；较少表现出明显的身体疲劳感。"
                    elif i['score'] >= 16 and i['score'] <= 25:
                        ContentSomaticReaction = ContentSomaticReaction + "一般来说，您已经呈现出轻微的躯体症状，可能的表现为：有时感到身体疲劳，浑身乏力；有时感到腹痛、腹胀或感到恶心、呕吐；有时郁郁寡欢，感到胸闷、气短；身体的某些部位有时会有疼痛感，有时持久且强烈。"
                    elif i['score'] >= 26 and i['score'] <= 30:
                        ContentSomaticReaction = ContentSomaticReaction + "一般来说，您已经呈现比较明显的躯体症状，可能的表现为：常表现出胃肠道症状，比如腹痛、恶心、腹胀、呕吐、打嗝、稀便等；常表现出呼吸系统症状，比如气短、胸痛等；常表现出自主神经兴奋症状，比如心悸、出汗、脸红、震颤等；极易过度疲劳，常感到手脚沉重或无力感；感觉到身体的疼痛感，有时持续、严重、强烈且突出。"
                if i['name'] == "回避行为":
                    if i['score'] >= 6 and i['score'] <= 10:
                        ContentAvoidanceBehavior = ContentAvoidanceBehavior + "一般来说，您是一个能积极面对困难和挑战的人。可能的表现为：能坚定地专注于既定的目标，积极寻求解决任务的办法,能够用成熟的态度面对困难、挫折和失败,努力去改变现状,使情况向好的一面转化,极少受到失望、沮丧等负面情绪的影响,具有锲而不舍、不达目的决不罢休的决心。"
                    elif i['score'] >= 11 and i['score'] <= 15:
                        ContentAvoidanceBehavior = ContentAvoidanceBehavior + "一般来说，您能够积极面对困难。可能的表现为：能够关注既定目标的完成，寻求解决办法,能够面对困难、挫折和失败，少有回避倾向,较少受到失望、沮丧等负面情绪的影响,不会过分强调任务的困难和不可完成性。"
                    elif i['score'] >= 16 and i['score'] <= 25:
                        ContentAvoidanceBehavior = ContentAvoidanceBehavior + "一般来说，您不太愿意直面困难和挑战。可能的表现为：有时不能坦然面对现实环境，而是选择抱怨或逃避。在困难和挑战面前，不愿付出努力，容易放弃容易受到失望、沮丧的情绪影响面对问题采取等待观望的态度"
                    elif i['score'] >= 26 and i['score'] <= 30:
                        ContentAvoidanceBehavior = ContentAvoidanceBehavior + "一般来说，您具有明显的回避困难、挫折和失败的倾向。可能的表现为：不能坦然面对现实环境，经常报怨或逃避。不能坚守既定的目标，缺乏自信，消极退缩,常常将潜在困难看得比实际上更严重，往往感到沮丧和失望,自甘落后，回避困难，得过且过"
                if i['name'] == "幻想行为":
                    if i['score'] >= 6 and i['score'] <= 10:
                        ContentFantasies = ContentFantasies + "一般说来，您是一位理性的、现实的人，能够正确的面对和应付困难。可能的表现为：通常是现实主义者，不喜欢幻想，对现实持有清醒的认识；能够正面的看待问题，并专注于问题解决,能理智地应付困难."
                    elif i['score'] >= 11 and i['score'] <= 15:
                        ContentFantasies = ContentFantasies + "一般说来，您比较理性，能够正确看待问题。可能的表现为：很少幻想，对现实持有比较清醒的认识。解决问题比较专注，不易受外部打扰"
                    elif i['score'] >= 16 and i['score'] <= 25:
                        ContentFantasies = ContentFantasies + "一般说来，您不太能够正确的面对问题和困难. 可能的表现为：面对问题会产生一些不切实际的幻想;在处理问题时注意力不能集中，容易受外部干扰"
                    elif i['score'] >= 26 and i['score'] <= 30:
                        ContentFantasies = ContentFantasies + "一般说来，您在应对问题的方式不太成熟。可能的表现为：不愿意正视问题的存在，经常沉迷于幻想而逃避现实的压力;在处理问题时经常性的分散注意力"
                if i['name'] == "自责行为":
                    if i['score'] >= 6 and i['score'] <= 10:
                        ContentSelfReproach = ContentSelfReproach + "一般来说，您在遇到挫折和困难时有较强的信心。可能的表现为：能正确地认识自己，正面对待自己的经历,能够客观的评估自己的能力与不足,信任自己解决问题的能力，不轻易动摇"
                    elif i['score'] >= 11 and i['score'] <= 15:
                        ContentSelfReproach = ContentSelfReproach + "一般来说，您在遇到挫折和困难时比较有信心，可能的表现为：比较能正确地认识自己，正面对待自己的经历,基本上能够客观的评估自己的能力，比较自信,信任自己解决问题的能力，不轻易动摇"
                    elif i['score'] >= 16 and i['score'] <= 25:
                        ContentSelfReproach = ContentSelfReproach + "一般来说，您在遇到挫折和困难时有责怪自己的倾向。可能的表现为：对自己的困难和失败不能坦然接受，对自己的认识不够客观。忽略自己的优势，夸大自己的缺陷，产生消极的自我评价。难以正确对待自己的不足、并进行调整和修正。"
                    elif i['score'] >= 26 and i['score'] <= 30:
                        ContentSelfReproach = ContentSelfReproach + "一般来说，您在遇到挫折和失败时有明显的自责倾向。可能的表现为：对自己的困难和失败不能坦然接受，完全否定自己。认为自己能力不足而放弃解决问题的努力。不能正确面对自己的不足，放弃进行调整和修正。"
                if i['name'] == "强迫行为":
                    if i['score'] >= 6 and i['score'] <= 10:
                        ContentCompulsion = ContentCompulsion + "一般说来，您非常理性，从不为毫无根据的想法而烦恼，也不会反复去做毫无意义的事情。可能的表现为：不是充满疑虑的人，不会时刻担心细菌、病毒的侵入，也不会反复检查煤气管道、电源开关等物件；可以有效地控制自己的思维活动，随时可以把那些奇怪的、荒谬的念头抛开；行为举止很正常，没有任何需要反复进行否则就会感到焦虑的行为习惯或癖好;对生活和工作的掌控能力比较强，不会夸大犯错的后果，也不会因此惴惴不安。"
                    elif i['score'] >= 11 and i['score'] <= 15:
                        ContentCompulsion = ContentCompulsion + "一般说来，您比较理性，很少为毫无根据的想法而烦恼，也很少反复去做毫无意义的事情。可能的表现为：如果明知某些念头是荒谬的、不合理的，或者觉得某些行为是过分的、无关紧要的，会有意压抑这些念头、克制这些行为；相信自己，对刚刚做完的事情比较放心，很少反复去检查；可以有效地控制自己的思维活动，适时摆脱不必要的联想或回忆；没有比较奇怪的生活习惯，也没有顽固而难以变通的行为风格；对生活和工作的掌控能力比较强，很少会夸大犯错后果，也很少会因此惴惴不安。"
                    elif i['score'] >= 16 and i['score'] <= 25:
                        ContentCompulsion = ContentCompulsion + "一般说来，您相对理性，但有时可能为毫无根据的想法而烦恼，或者反复去做毫无意义的事情。可能的表现为：明知某些念头是荒谬的、不合理的，或者觉得某些行为是过分的、无关紧要的，有时却无法压抑这些念头、克制这些行为；可以比较有效地控制自己的思维活动，但有时摆脱不了某些不良的念头，也难以制止某些不必要的联想或回忆；对自己信心不足，对那些刚刚做完的事情不够放心，经常去反复检查；做事的方式比较固定，很少变通，可能存在比较奇怪的生活习惯。"
                    elif i['score'] >= 26 and i['score'] <= 30:
                        ContentCompulsion = ContentCompulsion + "一般说来，您已出现比较明显的强迫症症状，被某些不必要的念头、毫无意义的行为习惯所困扰，甚至痛苦万分。可能的表现为：明知某些念头是荒谬的、不合理的，或者觉得某些行为是过分的、无关紧要的，却无法压抑这些念头或者克制这些行为；缺乏自信，对自己做过的事情总是持怀疑态度，而需要反复检查才能安心；难以有效地控制自己的思维活动，往往摆脱不了某些不良的念头，也难以制止某些不必要的联想或回忆，因此不仅很苦恼，而且严重影响了日常的工作与生活；为人处世有固定的行为方式，会严格遵循某些套路，不知变通."
                if i['name'] == "偏执心理":
                    if i['score'] >= 6 and i['score'] <= 10:
                        ContentParanoia = ContentParanoia + "一般来说，您是一位通情达理、灵活变通的人，有可能的表现为：乐于信任别人，极少怀疑别人的动机和愿望；心胸宽广，很少记恨别人，能够坦然宽容接受别人的过错；对自己有清晰的认识，能客观评估自己的能力"
                    elif i['score'] >= 11 and i['score'] <= 15:
                        ContentParanoia = ContentParanoia + "一般来说，您通情达理，通常情况下也愿意信任别人。可能的表现为：通常能够信任别人，较少对别人的动机产生疑虑；心胸较为宽广，一般不会记恨别人；多数情况下，能够积极正面的认识别人的行为和态度，乐于与别人建立良好关系；对自己的认识比较清晰，很少高估自己的能力"
                    elif i['score'] >= 16 and i['score'] <= 25:
                        ContentParanoia = ContentParanoia + "一般来说，您已经表现出轻微的偏执倾向，有时敏感多疑、固执任性，可能的表现为：有时敏感多疑，较多的信任自己，不轻易信任别人；有时不能开放坦然的正确理解和认识别人友好的行为；有时不能正确、客观地分析形势，有问题易从个人感情出发，主观片面性大；对自己的能力有较高估计，自视甚高。"
                    elif i['score'] >= 26 and i['score'] <= 30:
                        ContentParanoia = ContentParanoia + "一般来说，您已经呈现比较明显的偏执倾向，敏感多疑、固执己见，甚至极易记恨，可能的表现为：极度感觉过敏，对侮辱和伤害耿耿于怀，思想行为固执死板，敏感多疑、心胸狭隘;过度的自信，且只信任自己，不信任别人；过分警惕和抱有敌意，常将别人无意的、非恶意的甚至友好的行为误解为敌意或歧视，或无足够根据的怀疑会被人利用或伤害；对自己的能力估计过高，在工作上往往言过其实."
                if i['name'] == "嫉妒心理":
                    if i['score'] >= 6 and i['score'] <= 10:
                        ContentJealousy = ContentJealousy + "一般来说，您是一位心胸豁达，心态平和的人。可能的表现为：对自己有清晰的认识，客观理性的评估自己的能力；能够正确看待别人的长处和优点，并能由衷赞美别人的成绩和能力;往往表现出热情、喜悦、生活充满动力，具有较高的工作效率；极好的适应能力，能够坦然面对现实环境，以客观的态度面对现实，冷静地判断事实，理性地处理问题，并形成积极应变的心态。"
                    elif i['score'] >= 11 and i['score'] <= 15:
                        ContentJealousy = ContentJealousy + "一般来说，您的心胸较为豁达，心态较为平和。可能的表现为：对自己的认识较为客观，很少高估自己的能力和价值；一般能够认可别人的成绩和荣誉，不会贬低别人的能力和价值;通常情况下，工作充满热情和动力，效率较高；"
                    elif i['score'] >= 16 and i['score'] <= 25:
                        ContentJealousy = ContentJealousy + "一般来说，您表现出轻微的嫉妒倾向，有时心胸不够豁达，心态不够平和。可能的表现为:自我感觉良好，对自己能力和价值的评价较高；有时不太认可别人的成绩和荣誉，不能客观的认识别人的能力和价值；有时缺乏乐观向上的进取心，以致影响工作效率；"
                    elif i['score'] >= 26 and i['score'] <= 30:
                        ContentJealousy = ContentJealousy + "一般来说，您已经表现出明显的嫉妒倾向，心胸较为狭隘，心态不平衡。可能的表现为：自我感觉非常好，过度高估自我价值和能力；习惯否定别人的成绩和荣誉，同时贬低别人的能力和价值；遇到他人优于自己的情境时，产生难以克制的痛苦感，即使是一点小事；有时缺乏信心，丧失动力，工作积极性和效率明显降低。"
                if i['name'] == "人际适应":
                    if i['score'] >= 6 and i['score'] <= 10:
                        ContentInterpersonalAdaptation = ContentInterpersonalAdaptation + "一般说来，您是一个外向、热情、善解人意的人，不会在细节上纠缠不清，也不会自我封闭。可能的表现为：心胸宽广，能够分辨别人说话的意图，对无心之言、玩笑话不会放在心上，更不会生气、愤恨；非常自信，喜欢表达和展现自己，能够坦然面对别人的拒绝、冷落和负面评价；您待人宽厚，信任他人，不会仅仅从个人立场出发考虑问题；心理能量很强大，乐观大方，能够从容、坦荡地与他人交往；经常参加各种社交活动，乐意和别人打交道，并能以淡定的心态处理人际冲突或矛盾。"
                    elif i['score'] >= 11 and i['score'] <= 15:
                        ContentInterpersonalAdaptation = ContentInterpersonalAdaptation + "一般说来，您是一个比较外向、热情、善解人意的人，很少在细节上纠缠不清，也很少在社交活动上退缩。可能的表现为：为人宽厚，通常能够分辨别人说话的意图，对无心之言、玩笑话不会放在心上，更不会生气、愤恨；比较自信，往往喜欢表达和展现自己，能够坦然面对别人的拒绝、冷落和负面评价；比较乐观大方，能顾及他人的感受，通常能够从容、坦荡地与他人交往；乐于参加各种社交活动，愿意和别人打交道，通常情况下能以淡定的心态处理人际冲突或矛盾。"
                    elif i['score'] >= 16 and i['score'] <= 25:
                        ContentInterpersonalAdaptation = ContentInterpersonalAdaptation + "一般说来，您不够大度、宽容和善解人意，有时会在细节上纠缠不清，或者刻意回避与他人的交往。可能的表现为：心胸不够宽广，有时分辨不清别人说话的意图，因而把无心之言、玩笑话放在心上，甚至生气、愤恨；比较感性，有时会把自己的想法投射到现实中，或者仅仅从个人立场出发考虑问题，情绪波动较大；心理能量相对弱小，缺乏自信心，有时难以从容、坦荡地与他人交往；对参加社交活动缺乏积极性，也很少主动和别人搭话，有时无法用平常的心态处理人际冲突或矛盾。"
                    elif i['score'] >= 26 and i['score'] <= 30:
                        ContentInterpersonalAdaptation = ContentInterpersonalAdaptation + "一般说来，您在人际关系方面比较敏感，拒绝与别人建立亲密的关系，因而带来种种困惑和苦恼。可能的表现为：常常在细节上纠缠不清，或者刻意回避与他人的交往；常常分辨不清别人说话的意图， 把无心之言、玩笑话放在心上，甚至生气、愤恨；十分感性，经常会把自己的想法投射到现实中，或者把细微的东西过度放大，情绪容易波动；心理能量比较弱小，骨子里比较自卑，常常难以从容、坦荡地与他人交往；不愿意参加社交活动，极少主动和别人搭话，常常无法用平常的心态处理人际冲突或矛盾。"
                if i['name'] == "孤独感受":
                    if i['score'] >= 6 and i['score'] <= 10:
                        ContentLonelyFeeling = ContentLonelyFeeling + "一般说来，您具有强大的、持久的精神支持，如亲情、友谊、爱情、信仰、兴趣等，关心与爱护您的人很多。可能的表现为：能够以愉悦的方式消磨自己的空闲时间，而不会有寂寞、无所事事的感受；在遇到困难或者心情不好的时候，总是会有人帮助和安慰，有温暖、安心的感受；通常具备良好的人际关系，可以得到较多社会资源和支持；一个成熟、乐观的人,能积极应对竞争和压力、忍受拥挤和忙碌，以平和、恬淡的心态面对生活和工作。"
                    elif i['score'] >= 11 and i['score'] <= 15:
                        ContentLonelyFeeling = ContentLonelyFeeling + "一般说来，您具有稳固的、持久的精神支持，如亲情、友谊、爱情、信仰、兴趣等，关心与爱护您的人比较多。可能的表现为：通常能够以愉悦的方式消磨自己的空闲时间，而很少有寂寞、无所事事的感受；在遇到困难或者心情不好的时候，经常会有人帮助和安慰您，有温暖、安心感；通常具备和谐的人际关系，可以得到一定的社会资源和支持；往往是一个成熟、乐观的人，能以积极的态度应对竞争和压力、忍受拥挤和忙碌，并能较好地控制自己的情绪。"
                    elif i['score'] >= 16 and i['score'] <= 25:
                        ContentLonelyFeeling = ContentLonelyFeeling + "一般说来，您具有比较稳固的、持久的精神支持，如亲情、友谊、爱情、信仰、兴趣等，有一些关心与爱护您的人。可能的表现为：往往能够以愉悦的方式消磨自己的空闲时间，但有时可能会产生寂寞、无聊、烦闷的感觉；在遇到困难或者心情不好的时候，您往往可以找到合适的人帮助和安慰自己；通常具备比较和谐的人际关系，可以得到一定的社会资源和支持；比较成熟与乐观，基本上能以积极的态度应对竞争和压力、忍受拥挤和忙碌，并能合理地控制自己的情绪。"
                    elif i['score'] >= 26 and i['score'] <= 30:
                        ContentLonelyFeeling = ContentLonelyFeeling + "一般说来，您欠缺比较稳固的、持久的精神支持，如亲情、友谊、爱情、信仰、兴趣等，几乎没有关心与爱护您的人。可能的表现为：往往以一个人独处的方式来消磨空闲时间，常常有寂寞、无聊、烦闷的感觉；在遇到困难或者心情不好的时候，往往找不到合适的人来帮助和安慰自己，总觉得自己被周围人忽视或遗忘；往往缺乏安全感，人际关系不是很好，难以得到充分的社会资源和支持；容易悲观、情绪低落，经常以消极的态度应对竞争和压力、忍受拥挤和忙碌，有时无法适当地控制自己的情绪。"
                if i['name'] == "依赖心理":
                    if i['score'] >= 6 and i['score'] <= 10:
                        ContentAnaclisis = ContentAnaclisis + "一般来说，您具有较好的独立性、自主性和创造性，可能的表现为：具有较强的理性思维，情绪控制能力较强，积极参与决策的讨论和制定；客观理性的评价自己，积极肯定认可自我价值和优势；以自己的价值取向和思维方式进行决策，不依附别人，也不受别人摆布；尊重别人的思想和意志，不以自己的利益去驾驭别人的事，不以自己的意志束缚任何人；在与别人交往中保持自身的独立性，并以个体的独立价值积极参与社会活动。"
                    elif i['score'] >= 11 and i['score'] <= 15:
                        ContentAnaclisis = ContentAnaclisis + "一般来说，您基本认可自我价值，具有一定的自主进取精神和独立意识。可能的表现为：偏理性，能够控制自我情绪，并参与决策讨论和制定；积极认可自我能力和自我价值；不会对别人提出过多不合理的要求和期望；不依附别人，对事物能够独立的进行判断和作出决策。"
                    elif i['score'] >= 16 and i['score'] <= 25:
                        ContentAnaclisis = ContentAnaclisis + "一般来说，您呈现出轻微的依赖倾向，有时缺乏独立意识，甚至自感无能。可能的表现为：有时敏感多思，依恋别人，不太注意自己参与决策的能力；有时缺乏自主性和创造性，需要作出决策时，需要征求大量的建议和保证；有时自我贬低，认为别人比自己优秀，比自己有吸引力，比自己能干；主动精神较弱，有时被动服从别人的愿望和要求，即使不够合理；有时产生被人遗弃的想法和念头。"
                    elif i['score'] >= 26 and i['score'] <= 30:
                        ContentAnaclisis = ContentAnaclisis + "一般来说，您已呈现比较明显的依赖症状，缺乏活力，缺乏独立意识，甚至自感无能，可能的表现为：在没有从别人处得到大量的建议和保证之前，对日常事物不能作出决策；无助感，让别人为自己作大多数的重要决定，如在何处生活，该选择什么职业等；深怕被人遗弃，一些基本目标常常只能在别人予以协助之下才能达到；无独立性，很难单独展开计划或做事；过度容忍，为讨好别人甘愿做低下的或自己不愿做的事；缺乏自尊自重，把自己看作是毫无能力的、必须依附别人的人，经常通过自我贬低以求获得别人的帮助；往往对别人有过多的不易被人理解的要求，在各方面总是寄希望于得到帮助和依靠。"
                if i['name'] == "猜疑心理":
                    if i['score'] >= 6 and i['score'] <= 10:
                        ContentSuspicions = ContentSuspicions + "一般说来，您是一位友善、合作的人，愿意相信别人。可能的表现为：对他人的看法比较正面、积极，相信人性的善良，愿与他人协作；信任别人，愿意和别人建立关系，没有充分的证据，极少怀疑别人的动机。即使遇到不快，也能控制自己的情绪，而极少在语言和行为上攻击他人；比较坦率和豁达，很少记仇，不会将负面情绪带入以后的工作中；"
                    elif i['score'] >= 11 and i['score'] <= 15:
                        ContentSuspicions = ContentSuspicions + "一般说来，您待人友好，具备较强合作性，通常情况下也愿意相信别人。可能的表现为：对他人的看法相对积极和正面，相信别人有“善”的一面；不大喜欢与别人争论，有了误解或矛盾，愿意心平气和地进行沟通；多数时候能控制自己的情绪，以避免给工作和生活带来不良影响；一般不会选择对抗，大体上信赖他人，很少捕风捉影，鲜有过度敏感之时；通常愿意与别人建立友好的关系，很少对别人的动机心存疑虑。"
                    elif i['score'] >= 16 and i['score'] <= 25:
                        ContentSuspicions = ContentSuspicions + "一般说来，您待人相对友好，具备一定的合作性，但不大相信别人，有较强的戒备心。可能的表现为：对他人的看法有时是消极和负面的，甚至认为多数时候人是冷漠自私的；担心别人损害您的利益，可能出现过激情绪反应，并采取对抗排斥的应对方式；有时过度敏感，并可能对某些人持有敌意和怀疑，并将这种态度保持一段时间。"
                    elif i['score'] >= 26 and i['score'] <= 30:
                        ContentSuspicions = ContentSuspicions + "一般说来，您是一位比较难相处的人，待人不够友善，不大愿意和别人亲近，合作性也比较差。可能的表现为：对别人的看法往往是负面的和消极的，觉得人都是自私冷漠的,时刻保持警惕，对别人的言行举止的想法往往是过激的、甚至扭曲的；常常难以控制自己的情绪，有过摔东西、撕文件等行为，并对别人恶言相向；过于敏感，认为别人对自己存在敌意，甚至要故意伤害自己；采取敌对的方式处理问题，给工作和人际交往制造了巨大的障碍。"
                if i['name'] == "焦虑情绪":
                    if i['score'] >= 6 and i['score'] <= 10:
                        ContentAnxiety = ContentAnxiety + "一般说来，您是一位从容镇定、乐观豁达、心情愉悦的人。可能的表现为：能坦然面对各种压力，并能巧妙地、高效地解决各种问题；对周围环境的掌控能力很强，对可能发生的事情有着准确的预期；性格比较随和，擅长交际，并可能喜欢在公众场合表现自己；身体健康，没有受到疾病、疼痛、不适、衰弱的困扰；心态很好，淡泊名利，极少有偏激的想法或看法，对人对事都比较宽容；往往按照惯常的方式做事，遵循既有的规则，时间管理能力也比较好，很少拖沓。"
                    elif i['score'] >= 11 and i['score'] <= 15:
                        ContentAnxiety = ContentAnxiety + "一般说来，您的焦虑水平较低，很少因为工作和生活方面的事情而烦躁不安，常常给人从容淡定的感觉。可能的表现为：能冷静地面对各种问题，即使自己无法解决，也很少慌乱或害怕；身体比较健康，即使稍有不适或病痛，也不会因此而苦恼；自信心比较强，对自己内在价值的认同比较高，很少在上司或权威面前惊慌失措；为人宽厚，善待别人，很少卷入名利之争，也很少有偏激的、扭曲的想法；时间管理能力比较强，较少拖沓，即使没有及时完成工作任务，也会因开朗、豁达的性格而保持表面的镇静。"
                    elif i['score'] >= 16 and i['score'] <= 25:
                        ContentAnxiety = ContentAnxiety + "一般说来，您的焦虑水平中等，有时为工作和生活中的麻烦事而烦躁。可能的表现为：尚能适当地应付各种压力，但有时可能惊慌失措，产生不良情绪，带来困扰；身体相对健康，有时可能会担心身体的疾患与病痛；自信水平一般，对不确定的事情心存疑虑，对上司或权威心存敬畏；比较看重名利，有时会因为攀比、竞争而苦恼和担忧；有时瞻前顾后，做事顾虑太多、犹豫不决，并可能陷入痛失良机的懊悔之中；有时会延期完成任务，导致突击赶进度，并体验到一定程度的焦虑。"
                    elif i['score'] >= 26 and i['score'] <= 30:
                        ContentAnxiety = ContentAnxiety + "一般说来，您的焦虑水平较高，经常为工作和生活中的事情而烦恼，甚至担心受怕。可能的表现为：能勉强应付各种问题，但有时力不从心，在压力面前你可能心情烦躁，采用拖拉、回避等消极方式来应对问题；可能出现负面情绪，还可能出现头晕、胸闷、尿频、出汗等躯体症状，会因为身体的疾病、疼痛而苦恼不已；往往不知道如何以确切的方式向合适的人寻求帮助，如果您是那种情绪外露的人，则可能向周围人散播焦虑的气氛；可能觉得周围充满了不确定的因素，为了增强安全感，可能竭力争夺；自我要求比较严格，有时对自身的能力、工作的进度把握不好，造成拖延，并因此体验到强烈的不安。"
                if i['name'] == "冲动控制":
                    if i['score'] >= 6 and i['score'] <= 10:
                        ContentImpulsiveControl = ContentImpulsiveControl + "一般来说，您是一位成熟理智而沉着冷静的人，待人比较友善。可能的表现为：情绪状态非常稳定，极少出现突然的暴怒，情绪控制能力也较强；行为比较慎重，倾向于规避风险，做事情顾及后果，很少冲动；语言和思维能力正常，遇事能够冷静对待，并能很好的控制和调节语言举止；头脑冷静，能够平心静气、毫无偏见地分析道理而不感情用事。"
                    elif i['score'] >= 11 and i['score'] <= 15:
                        ContentImpulsiveControl = ContentImpulsiveControl + "一般来说，您比较成熟理智，为人处世相对沉着冷静。可能的表现为：情绪状态比较稳定，很少暴躁、发火；通常情况下，行为较为谨慎，较少冲动，采取行动之前会考虑行为的后果；一般遇事较为冷静，较好控制协调语言举止。"
                    elif i['score'] >= 16 and i['score'] <= 25:
                        ContentImpulsiveControl = ContentImpulsiveControl + "一般来说，您已经表现出轻微的冲动症状，情绪波动较大。可能的表现为：有时情绪不够稳定，因一件小事而大发雷霆、大动干戈；有时比较冲动，做事也常常忽略后果；有时遇事不够冷静，意识狭隘，贸然行事，不能较好控制自己的语言举止。"
                    elif i['score'] >= 26 and i['score'] <= 30:
                        ContentImpulsiveControl = ContentImpulsiveControl + "一般来说，您已经表现出明显的冲动症状，常因微小刺激爆发强烈而难以控制的愤怒情绪，可能的表现为：情绪控制不够稳定，往往突然暴怒，通常缺乏理智且带有盲目性；稍不如意就怒火直冒、行为冲动，且不计后果和难以遏制；事后对发作时的所作所为感到后悔，甚至自责，但不能防止失控冲动的再次发生，具有明显的阵发性特点；在强烈的感情冲动期间，意识明显狭隘，认知片面、判断力下降、注意范围缩小，难以控制和调节语言举止。"
                if i['name'] == "抑郁倾向":
                    if i['score'] >= 6 and i['score'] <= 10:
                        ContentDepressiveTendency = ContentDepressiveTendency + "一般说来，您是一位开朗、愉悦、乐观的人，精神比较饱满，能以积极、平和的心态面对日常的工作与生活。可能的表现为：极少情绪低落、悲观失望，而往往意气风发、笑容满面；觉得生活很充实，有很多有趣的、值得做的事情，如交友、培养兴趣爱好等；思维和语言功能正常，反应灵敏；自信，并在一定程度上悦纳自己，觉得自己是一个有用的、有价值的人；身体健康，饮食睡眠状况良好，精力也比较充沛；喜欢与别人交往，人际关系良好，态度宽容、随和，经常给人阳光、活泼的感觉；能坦然接受社会现实，即使遭遇挫折和打击，也能勇敢地面对。"
                    elif i['score'] >= 11 and i['score'] <= 15:
                        ContentDepressiveTendency = ContentDepressiveTendency + "一般说来，您是一位比较积极乐观、活泼开朗的人，能以适当的方式应对工作与生活中的各种问题。可能的表现为：往往情绪状态良好，待人接物乐观积极，给别人愉悦、舒适的感觉；愿意与别人交往，并得到别人的理解和帮助；对身边的事物持有一定的兴趣，并有精力和体力参与各项活动；很少悲观，对前途保有一些期望，对自己也比较有信心；身体状况比较良好，没有遭受严重疾病、疼痛的侵袭，饮食睡眠也相对正常；思维和意志功能比较正常，能够对环境和事件做出合理的判断；受挫能力比较强，能坦然面对一般的压力，并妥善处理身边的问题。"
                    elif i['score'] >= 16 and i['score'] <= 25:
                        ContentDepressiveTendency = ContentDepressiveTendency + "一般说来，您的情绪有一定的波动，在处境顺利、心满意足时愉快、乐观，但在遭受挫折、面对困难时则可能悲观失望。可能的表现为：易受环境的影响，有时会因为环境的变化而心情大变；心情不好的时候不愿交往，甚至闭门不出，对既往的爱好也不屑一顾；思维和意志功能比较正常，但沮丧的时候容易犯糊涂和走神；不是非常自信，有时对前途感到迷惘，对近况感到失落；有时会受到疾病、疼痛的困扰，如胸闷、肠胃不适、便秘等，有时食欲不振，睡眠不佳，精神疲惫；抗压能力一般，有时会在困难面前惊慌失措。"
                    elif i['score'] >= 26 and i['score'] <= 30:
                        ContentDepressiveTendency = ContentDepressiveTendency + "一般说来，您已呈现比较明显的抑郁症状，经常情绪低落、悲观失望，甚至产生厌世轻生的念头。可能的表现为：常郁郁寡欢，对周围事物毫无兴趣，觉得生活是一种负担，有度日如年的感觉；常身心疲惫，对工作缺乏热情，注意力难以集中，严重影响了工作效率；觉得没有前途和希望，很不自信，怀疑自己的价值；在人际交往方面消极被动，缺乏与人沟通的意愿；思维能力有所下降，记忆力减退，行动也比较迟缓；经常生病，饮食和睡眠状况比较差，有时性功能也遭到衰竭；经常早醒，然后无法入睡，陷入悲哀的情绪之中，体重也有明显下降的趋势；常感到焦虑，以批判、否定的态度看待自己，甚至有自罪观念。"
                if i['name'] == "环境适应":
                    if i['score'] >= 6 and i['score'] <= 10:
                        ContentEnvironmentalAdaptation = ContentEnvironmentalAdaptation + "一般说来，您的社会适应能力很强，能根据环境的变化、自身的发展来调整个人的需求，以积极的态度面对工作和生活中的困难。可能的表现为：具备良好沟通技巧，能迅速和周围的人建立关系，甚至左右逢源、讨人喜欢；非常理性，制定的计划切合实际，操作性强，容易被别人接受；与环境保持适宜的接触，但不是只注重眼前利益的人；能够忍受一时的挫折和痛苦，能延迟满足；价值观与社会主流价值观趋同或者兼容，能对个人需求做适当的追求。"
                    elif i['score'] >= 11 and i['score'] <= 15:
                        ContentEnvironmentalAdaptation = ContentEnvironmentalAdaptation + "一般说来，您的社会适应能力较强，通常能根据环境的变化、自身的发展来调整个人的需求，以比较积极的态度面对工作和生活中的困难。可能的表现为：具备较好的沟通技巧，能与周围人建立和谐的关系；比较理性，制定的计划通常切合实际，操作性较强，容易被别人接受；能够从失败中吸取教训，逐渐积累经验，做事比较坚持，能忍受一时挫折和痛苦；价值观与社会主流价值观基本趋同或者兼容，能对个人需求做适当的追求。"
                    elif i['score'] >= 16 and i['score'] <= 25:
                        ContentEnvironmentalAdaptation = ContentEnvironmentalAdaptation + "一般说来，您的社会适应能力欠佳，有时难以根据环境的变化、自身的发展来调整个人的需求，态度也不够积极。可能的表现为：欠缺较好的沟通技巧，不善与人交往，可能需要花很长时间才能融入新的环境；有时冲动任性，想法过于单纯，提出的建议不切实际；通常能够从失败中吸取教训，逐渐积累经验，但做事缺乏毅力，缺乏长远的眼光，比较容易感到困惑和苦闷；价值观与社会主流价值观可能存在一些冲突，有时显得有些自私；抗挫折能力不是很强，有时难以克制自己的负面情绪。"
                    elif i['score'] >= 26 and i['score'] <= 30:
                        ContentEnvironmentalAdaptation = ContentEnvironmentalAdaptation + "一般说来，您的社会适应能力严重不足，难以根据环境的变化、自身的发展来调整个人的需求，为人处世的态度也比较消极。可能的表现为：欠缺基本的沟通技巧，不善与人交往，需要花很长时间才能融入新的环境；往往冲动任性，想法过于单纯，提出的建议不切实际；难以从失败中吸取教训，缺乏毅力，缺乏长远眼光，容易感到困惑和苦闷；价值观与社会主流价值观存在较大的冲突，有时过于自私；抗挫折能力比较差，经常难以克制自己的负面情绪。"
                if i['name'] == "恐惧心理":
                    if i['score'] >= 6 and i['score'] <= 10:
                        ContentFear = ContentFear + "一般说来，您是一位胆大的、泰然自若的人，遇事不慌不乱。可能的表现为：在社交场合表现自如，即使有人盯着你看，也不会觉得不自在；敢于在公众场合表达，甚至喜欢在大庭广众之下演讲或者表演；没有什么场所或空间让您觉得害怕，可以镇定地出入各种场合；没有任何“怕得要命”的东西，即使受了惊吓，也会很快恢复过来；身体健康，极少出现胸闷、呼吸困难、晕厥，对生活和工作的把控能力很强。"
                    elif i['score'] >= 11 and i['score'] <= 15:
                        ContentFear = ContentFear + "一般说来，您的胆子比较大，遇事很少慌乱，比较镇定自若。可能的表现为：没有因什么生活事件或事物受到严重惊吓而留下心理阴影；可以在社交场合表现自如，比较轻松、愉快地和别人交流，但不大希望自己成为别人关注的焦点，否则您可能觉得浑身不自在；对空旷的场地没有任何恐惧，对拥挤的、密闭的房间或交通工具也毫不害怕；偶尔有一两样事物让您感到害怕，但程度并不深，恐惧的情绪消散得也比较快；"
                    elif i['score'] >= 16 and i['score'] <= 25:
                        ContentFear = ContentFear + "一般说来，您的胆子比较大，遇事很少慌乱，比较镇定自若。可能的表现为：没有因什么生活事件或事物受到严重惊吓而留下心理阴影；可以在社交场合表现自如，比较轻松、愉快地和别人交流，但不大希望自己成为别人关注的焦点，否则您可能觉得浑身不自在；对空旷的场地没有任何恐惧，对拥挤的、密闭的房间或交通工具也毫不害怕；偶尔有一两样事物让您感到害怕，但程度并不深，恐惧的情绪消散得也比较快；"
                    elif i['score'] >= 26 and i['score'] <= 30:
                        ContentFear = ContentFear + "一般说来，您已经出现比较明显的恐惧症症状，对特定的事物或场景有着强烈的、不必要的恐惧，并伴随回避、退缩行为。可能的表现为：可能对社交场合避而远之，觉得浑身不自在，难以和别人自然地交流；往往不够自信，没有悦纳自己，或者对自己的要求过高，一旦觉得自己无法胜任工作或者应付某些问题，就会失望、痛苦和害怕；可能害怕一个人去空旷的地方，或者对拥挤的、密闭的房间或交通工具心怀畏惧；当恐惧袭来的时候，往往无法摆脱,感到绝望、崩溃，出现胸闷、脸色苍白、心悸等症状，甚至当场昏厥。"
                if i['name'] == "身心同一":
                    if i['score'] >= 6 and i['score'] <= 10:
                        ContentBodyAndMind = ContentBodyAndMind + "一般说来，您是一位胆大的、泰然自若的人，遇事不慌不乱。可能的表现为：在社交场合表现自如，即使有人盯着你看，也不会觉得不自在；敢于在公众场合表达，甚至喜欢在大庭广众之下演讲或者表演；没有什么场所或空间让您觉得害怕，可以镇定地出入各种场合；没有任何“怕得要命”的东西，即使受了惊吓，也会很快恢复过来；身体健康，极少出现胸闷、呼吸困难、晕厥，对生活和工作的把控能力很强。"
                    elif i['score'] >= 11 and i['score'] <= 15:
                        ContentBodyAndMind = ContentBodyAndMind + "一般说来，您的胆子比较大，遇事很少慌乱，比较镇定自若。可能的表现为：没有因什么生活事件或事物受到严重惊吓而留下心理阴影；可以在社交场合表现自如，比较轻松、愉快地和别人交流，但不大希望自己成为别人关注的焦点，否则您可能觉得浑身不自在；对空旷的场地没有任何恐惧，对拥挤的、密闭的房间或交通工具也毫不害怕；偶尔有一两样事物让您感到害怕，但程度并不深，恐惧的情绪消散得也比较快；对生活和工作的把控能力比较强，相对自信一些。"
                    elif i['score'] >= 16 and i['score'] <= 25:
                        ContentBodyAndMind = ContentBodyAndMind + "一般说来，您的胆子比较小，有时过于敏感，工作与生活中那些不确定的因素往往让您忧心和焦虑。可能的表现为：曾经受到比较严重的惊吓或羞辱，以致对某些事物或场合心有余悸，但尚能克服这种恐惧感；在社交场合有时会觉得别扭、不舒服，与别人的交流也显得比较勉强；可能害怕一个人去空旷的地方，或者对拥挤的、密闭的房间或交通工具心怀畏惧；遇到困难的、自己无法掌控的事情时，有时会惊慌失措，甚至惊恐。"
                    elif i['score'] >= 26 and i['score'] <= 30:
                        ContentBodyAndMind = ContentBodyAndMind + "一般说来，您已出现比较明显的精神分裂症症状，思想已经脱离现实环境，在认知、情绪、意志、运动、感觉等方面存在种种功能障碍。可能的表现为：有时思维混乱、缺乏逻辑与目的性，或者觉得思维被别人控制了；还可能出现一些妄想，如觉得有人想伤害您、身体某部分发生了奇异的变形、自己有高贵的血统等；可能出现一些幻觉，如看到不存在的图像，或听到空气中有人对你说话；性格比较孤僻，不愿和别人打交道，懒散，工作与生活的能力严重下降；情感非常冷淡，经常面无表情，没有同情心，也难以理解别人的感受；在别人看来，您经常做些奇怪的事情，甚至荒谬可笑。"

            report04()['msg']["ContentSomaticReaction"] = ContentSomaticReaction
            report04()['msg']["ContentAvoidanceBehavior"] = ContentAvoidanceBehavior
            report04()['msg']["ContentFantasies"] = ContentFantasies
            report04()['msg']["ContentSelfReproach"] = ContentSelfReproach
            report04()['msg']["ContentCompulsion"] = ContentCompulsion
            report04()['msg']["ContentParanoia"] = ContentParanoia
            report04()['msg']["ContentJealousy"] = ContentJealousy
            report04()['msg']["ContentInterpersonalAdaptation"] = ContentInterpersonalAdaptation
            report04()['msg']["ContentLonelyFeeling"] = ContentLonelyFeeling
            report04()['msg']["ContentAnaclisis"] = ContentAnaclisis
            report04()['msg']["ContentSuspicions"] = ContentSuspicions
            report04()['msg']["ContentAnxiety"] = ContentAnxiety
            report04()['msg']["ContentImpulsiveControl"] = ContentImpulsiveControl
            report04()['msg']["ContentDepressiveTendency"] = ContentDepressiveTendency
            report04()['msg']["ContentEnvironmentalAdaptation"] = ContentEnvironmentalAdaptation
            report04()['msg']["ContentFear"] = ContentFear
            report04()['msg']["ContentBodyAndMind"] = ContentBodyAndMind
            report04()['msg']["ChartYellowIndex"] = ChartYellowIndex
            report04()['msg']["ChartOrangeIndex"] = ChartOrangeIndex
            report04()['msg']["ChartRedIndex"] = ChartRedIndex
            res = {"code": 0, 'detail': {'report_data': report04()}}
            print('发送到word服务的数据:%s' % res)
            return HttpResponse(json.dumps(res, ensure_ascii=False).encode('utf-8'), content_type="application/json")
        elif report_type_id == "PsychologicalCapital":
            res = {"code": 0, 'detail': {'report_data': report05()}}
            print('发送到word服务的数据:%s' % res)
            return HttpResponse(json.dumps(res, ensure_ascii=False).encode('utf-8'), content_type="application/json")
        elif report_type_id == "WorkValueQuestionnaire":
            print(report07)
            chart_data = report07['msg']['ChartDataModel']
            char = report07['msg']['char']

            StrongIncentiveFactor = ""
            GeneralIncentiveFactor = ""
            GeneralNegativeMotivators = ""
            StrongNegativeIncentiveFactors = ""
            analysis = ""
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

            StrongIncentiveFactor_list = StrongIncentiveFactor.split(',')
            GeneralIncentiveFactor_list = GeneralIncentiveFactor.split(',')
            GeneralNegativeMotivators_list = GeneralNegativeMotivators.split(',')
            StrongNegativeIncentiveFactors_list = StrongNegativeIncentiveFactors.split(',')
            # j 指标名
            # [4,5]
            for i in char:
                for j in StrongIncentiveFactor_list:
                    if i['name'] == j:
                        if j == '变化/探索':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "希望每天都能处理全新的事务，适应变化的环境，经常尝试新的方法"},
                                       {"Factor": "希望以自己的方式工作，过度的监督会影响工作表现"}, {
                                           "Suggest": "· 在确保工作任务能够保质保量完成的基础上，允许他/她自行安排工作方式，如：在家办公等在确保工作结果的基础上，鼓励他/她在工作中尝试新的方式方法优化工作流程为他/她安排工作任务时，共同商讨确定工作目标和时间节点，允许他/她自主安排工作进度,在能力范围内，为他/她提供自由、宽松的工作氛围"},
                                       {"Type": "A"}], )
                        elif j == '艺术/文化':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "重视艺术、文学等方面的工作内容，关注审美和创造，倾向于在鼓励创新的环境中工作"},
                                       {"Factor": "认为和艺术或文化有关的工作非常理想，重视创作和自我表达的机会"}, {
                                           "Suggest": " 有意识多为他/她安排与艺术相关联的工作任务在确保工作结果的基础上，鼓励他/她发挥自己的创新能力，对工作流程进行优化鼓励他/她不断提高自己的审美水平，在工作成果中体现他/她的审美能力，如PPT的制作等在团队中，营造鼓励创新的氛围"},
                                       {"Type": "A"}], )
                        elif j == '挑战/成就':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "乐于在工作生活中面对挑战，克服困难，适应竞争激烈的工作环境"},
                                       {"Factor": "乐于克服各种困难及挑战，总是试图做得比别人更好，与他人之间的竞争关系会激发更好的工作表现"}, {
                                           "Suggest": " 工作时间外，只在工作任务非常紧急的时候才联系他/她,在可调整的范围内，尽量为他/她提供舒适的工作环境,避免为他/她安排过多的工作任务，尽量不要占用他/她的私人时间,向他/她说明组织需要的是完成工作任务以及绩效，而不是工作的时间长度,鼓励并帮助他/她做好工作生活两方面的时间安排"},
                                       {"Type": "A"}], )
                        elif j == '自主/独立':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "希望按自己的方式、步调或想法去安排工作时间、地点和方式，不倾向于受到太多来自他人的监督和控制"},
                                       {"Factor": "希望以自己的方式工作，过度的监督会影响工作表现"}, {
                                           "Suggest": " · 在确保工作任务能够保质保量完成的基础上，允许他/她自行安排工作方式，如：在家办公等,在确保工作结果的基础上，鼓励他/她在工作中尝试新的方式方法优化工作流程为他/她安排工作任务时，共同商讨确定工作目标和时间节点，允许他/她自主安排工作进度,在能力范围内，为他/她提供自由、宽松的工作氛围"},
                                       {"Type": "A"}], )
                        elif j == '专业/技术':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "追求在技术或专业领域的成长和提高，倾向于专业或技术性的工作岗位和内容"},
                                       {"Factor": "对专业或技术导向的工作感兴趣，关注工作中提供的学习新知识或技能的机会"}, {
                                           "Suggest": " 关注他/她工作内容的专业性，多为他/她安排专业性上有挑战的工作任务,为他/她专业性的提高提供平台和资源支持,通过他/她完成任务是否符合专业标准来评价他/她的工作表现,重视专业人才，鼓励他/她在专业领域上精益求精，不断进步"},
                                       {"Type": "A"}], )
                        elif j == '认可/表现':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "自己的工作需要得到应有的认可和肯定，希望成为人群中的关注焦点"},
                                       {"Factor": "希望在工作中得到肯定，失去同事的认可和关注可能会是一个打击"}, {
                                           "Suggest": " 鼓励他/她在自己擅长的领域培训和支持其他同事确保他/她的优异工作表现得到同事和领导的认可和赞扬,每当他/她的工作最终被证明有效，不管用了什么方式和手段，都要强调其所具有的实用价值,鼓励他/她表达自己的观点，对于他/她提出的有建设性的观点，及时的给予支持和认可,不要过多赞扬他/她，会降低赞扬的效果"},
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
                                           "Suggest": "· 适当放权，给予他/她担任项目负责人的工作机会，并在过程中不断的给予指导与支持,鼓励他/她勇敢表达自己的观点，采用一定的方法和策略说服和影响他人,重视他/她的合理建议，鼓励他/她参与决策并承担相应职责,确保他/她每隔一段时间都会有机会承担新的职责,明确他/她所期望的管理权限和职责范围"},
                                       {"Type": "A"}], )
                        elif j == '利他/慈善':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "渴望帮助他人，关心社会福祉，看重在工作中的自我价值实现，主动帮助他人取得成功"},
                                       {"Factor": "渴望帮助他人，关心社会福祉，重视在工作中的自我价值实现，乐意帮助他人取得成功"},
                                       {
                                           "Suggest": " 强调整个组织的工作最终能使整个世界变得更好,对于他/她帮助他人的行为，及时的给予认可和奖励,帮助他/她意识到自己的工作任务对他人和社会的积极影响,鼓励他/她多参与社会公益活动，并为他/她提供公益活动的相关资源和信息"},
                                       {"Type": "A"}], )
                        elif j == '社交/人际':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "乐于结交朋友，重视建立广泛的社会联系和关系"},
                                       {"Factor": "愿意主动与他人沟通，和各种人交往，建立比较广泛的社会联系和关系"},
                                       {
                                           "Suggest": " 多给予他/她一些需要跨部门沟通的工作任务，并鼓励他/她在过程中不断提高自己沟通交流的能力,向他/她提供参加行业展会、外出交流的机会,为他/她提供机会，与行业内有影响的人交流沟通,鼓励他/她参加工作应酬，建立良好的工作人脉"},
                                       {"Type": "A"}], )
                        elif j == '归属/团队':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "关注和谐的工作氛围，倾向于在团队中和他人合作开展工作"},
                                       {"Factor": "希望独自承担任务，不倾向于和他人合作，不关注团队"}, {
                                           "Suggest": " · 避免过多关心他/她的私人生活多为他/她安排个人可独立完成的工作任务,在他/她参与团队合作工作时，与他/她充分沟通，明确他/她个人承担的工作任务,在他/她参于集体活动时，强调集体活动对团队建设和发展的意义"},
                                       {"Type": "A"}], )

                        elif j == '经济/报酬':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "关注工作所获得的经济报酬和物质回报，自身的额外努力必须得到可见的奖励"},
                                       {"Factor": "看重物质上的实际利益，很难接受自己的工作得不到足够的物质回报"},
                                       {
                                           "Suggest": " 为他/她提供行业内具有竞争力的薪资,在激励他/她时，多考虑采用物质奖励的方式,当他/她工作表现优异时，确保他/她能够得到丰厚的奖金,注意在他/她加班或担负了额外的工作任务后向其提供相应的额外报酬"},
                                       {"Type": "A"}], )
                        elif j == '安全/稳定':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "关注工作生活的安全与稳定，偏好有序的、计划性的、可预测的工作环境，不倾向于承担风险"},
                                       {"Factor": "工作和职位具有安全感会提升工作热情"}, {
                                           "Suggest": "  在组织发生变动时，及时与他/她沟通，确保他/她了解具体情况，说明组织变动对组织发展的重要性建立完善的保险和福利制度，保障他/她收入的稳定,明确他/她的工作内容以及相应的职责范围,在给他/她安排工作任务时，及时与他/她进行沟通并尽可能提供明确具体的任务及计划安排"},
                                       {"Type": "A"}], )
                        elif j == '舒适/家庭':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "追求舒适、轻松、优越的工作条件和环境，关注工作与生活的平衡"},
                                       {"Factor": "认为工作不应该影响生活，轻松、舒适工作条件以及工作与家庭的平衡能够提升满意度"}, {
                                           "Suggest": " 工作时间外，只在工作任务非常紧急的时候才联系他/她,在可调整的范围内，尽量为他/她提供舒适的工作环境,避免为他/她安排过多的工作任务，尽量不要占用他/她的私人时间,向他/她说明组织需要的是完成工作任务以及绩效，而不是工作的时间长度,鼓励并帮助他/她做好工作生活两方面的时间安排"},
                                       {"Type": "A"}], )

            # [2,3]
            for i in char:
                for j in GeneralIncentiveFactor_list:
                    if i['name'] == j:
                        if j == '变化/探索':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "希望每天都能处理全新的事务，适应变化的环境，经常尝试新的方法"},
                                       {"Factor": "希望每一天的工作都是在解决全新的问题，对枯燥重复的工作内容感到厌倦"}, {
                                           "Suggest": "·为他/她安排需要多部门合作的工作任务,避免让他/她承担过多重复性、枯燥的工作,在必须执行的重复性工作时鼓励他/她探索总结新的工作方式方法，提高工作效率,鼓励他/她在工作中，多方面拓展，了解行业内最前沿的信息和发展趋势"},
                                       {"Type": "B"}], )
                        elif j == '艺术/文化':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "重视艺术、文学等方面的工作内容，关注审美和创造，倾向于在鼓励创新的环境中工作"},
                                       {"Factor": "认为和艺术或文化有关的工作非常理想，重视创作和自我表达的机会"}, {
                                           "Suggest": "  少为他/她安排需要发挥创意和想象力的工作,鼓励他/她多参与具体执行操作的工作任务,为他/她安排工作任务时，明确具体的工作成果要求，不要求他/她在工作成果中体现他/她审美水平,避免通过他/她在工作中体现的创新能力来衡量他/她的工作表现"},
                                       {"Type": "B"}], )
                        elif j == '挑战/成就':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "乐于在工作生活中面对挑战，克服困难，适应竞争激烈的工作环境"},
                                       {"Factor": "乐于克服各种困难及挑战，总是试图做得比别人更好，与他人之间的竞争关系会激发更好的工作表现"}, {
                                           "Suggest": " 工作时间外，只在工作任务非常紧急的时候才联系他/她,在可调整的范围内，尽量为他/她提供舒适的工作环境, 避免为他/她安排过多的工作任务，尽量不要占用他/她的私人时间,向他/她说明组织需要的是完成工作任务以及绩效，而不是工作的时间长度,鼓励并帮助他/她做好工作生活两方面的时间安排"},
                                       {"Type": "B"}], )
                        elif j == '自主/独立':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "希望按自己的方式、步调或想法去安排工作时间、地点和方式，不倾向于受到太多来自他人的监督和控制"},
                                       {"Factor": "希望以自己的方式工作，过度的监督会影响工作表现"}, {
                                           "Suggest": " 在确保工作任务能够保质保量完成的基础上，允许他/她自行安排工作方式，如：在家办公等,在确保工作结果的基础上，鼓励他/她在工作中尝试新的方式方法优化工作流程,为他/她安排工作任务时，共同商讨确定工作目标和时间节点，允许他/她自主安排工作进度,在能力范围内，为他/她提供自由、宽松的工作氛围"},
                                       {"Type": "B"}], )
                        elif j == '专业/技术':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "追求在技术或专业领域的成长和提高，倾向于专业或技术性的工作岗位和内容"},
                                       {"Factor": "对专业或技术导向的工作感兴趣，关注工作中提供的学习新知识或技能的机会"}, {
                                           "Suggest": " 关注他/她工作内容的专业性，多为他/她安排专业性上有挑战的工作任务,为他/她专业性的提高提供平台和资源支持,通过他/她完成任务是否符合专业标准来评价他/她的工作表现,重视专业人才，鼓励他/她在专业领域上精益求精，不断进步"},
                                       {"Type": "B"}], )
                        elif j == '认可/表现':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "自己的工作需要得到应有的认可和肯定，希望成为人群中的关注焦点"},
                                       {"Factor": "希望在工作中得到肯定，失去同事的认可和关注可能会是一个打击"}, {
                                           "Suggest": " 鼓励他/她在自己擅长的领域培训和支持其他同事,确保他/她的优异工作表现得到同事和领导的认可和赞扬,每当他/她的工作最终被证明有效，不管用了什么方式和手段，都要强调其所具有的实用价值,鼓励他/她表达自己的观点，对于他/她提出的有建设性的观点，及时的给予支持和认可,不要过多赞扬他/她，会降低赞扬的效果"},
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
                                           "Suggest": "· 适当放权，给予他/她担任项目负责人的工作机会，并在过程中不断的给予指导与支持,鼓励他/她勇敢表达自己的观点，采用一定的方法和策略说服和影响他人,重视他/她的合理建议，鼓励他/她参与决策并承担相应职责,确保他/她每隔一段时间都会有机会承担新的职责,明确他/她所期望的管理权限和职责范围"},
                                       {"Type": "B"}], )
                        elif j == '利他/慈善':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "渴望帮助他人，关心社会福祉，看重在工作中的自我价值实现，主动帮助他人取得成功"},
                                       {"Factor": "渴望帮助他人，关心社会福祉，重视在工作中的自我价值实现，乐意帮助他人取得成功"},
                                       {
                                           "Suggest": " 强调整个组织的工作最终能使整个世界变得更好,对于他/她帮助他人的行为，及时的给予认可和奖励,帮助他/她意识到自己的工作任务对他人和社会的积极影响,鼓励他/她多参与社会公益活动，并为他/她提供公益活动的相关资源和信息"},
                                       {"Type": "B"}], )
                        elif j == '社交/人际':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "乐于结交朋友，重视建立广泛的社会联系和关系"},
                                       {"Factor": "愿意主动与他人沟通，和各种人交往，建立比较广泛的社会联系和关系"},
                                       {
                                           "Suggest": " 多给予他/她一些需要跨部门沟通的工作任务，并鼓励他/她在过程中不断提高自己沟通交流的能力,向他/她提供参加行业展会、外出交流的机会,为他/她提供机会，与行业内有影响的人交流沟通,鼓励他/她参加工作应酬，建立良好的工作人脉"},
                                       {"Type": "B"}], )
                        elif j == '归属/团队':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "关注和谐的工作氛围，倾向于在团队中和他人合作开展工作"},
                                       {"Factor": "希望独自承担任务，不倾向于和他人合作，不关注团队"}, {
                                           "Suggest": " 避免过多关心他/她的私人生活多为他/她安排个人可独立完成的工作任务,在他/她参与团队合作工作时，与他/她充分沟通，明确他/她个人承担的工作任务,在他/她参于集体活动时，强调集体活动对团队建设和发展的意义"},
                                       {"Type": "B"}], )

                        elif j == '经济/报酬':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "关注工作所获得的经济报酬和物质回报，自身的额外努力必须得到可见的奖励"},
                                       {"Factor": "看重物质上的实际利益，很难接受自己的工作得不到足够的物质回报"},
                                       {
                                           "Suggest": " · 与他/她沟通，了解他/她所期望的激励方式确保组织内经济报酬分配的公平合理性,尝试采用多种手段相结合的方式来评价他/她的工作表现,避免只通过薪资福利增长的方式来激励他/她"},
                                       {"Type": "B"}], )
                        elif j == '安全/稳定':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "关注工作生活的安全与稳定，偏好有序的、计划性的、可预测的工作环境，不倾向于承担风险"},
                                       {"Factor": "工作和职位具有安全感会提升工作热情"}, {
                                           "Suggest": "  在组织发生变动时，及时与他/她沟通，确保他/她了解具体情况，说明组织变动对组织发展的重要性建立完善的保险和福利制度，保障他/她收入的稳定,明确他/她的工作内容以及相应的职责范围,在给他/她安排工作任务时，及时与他/她进行沟通并尽可能提供明确具体的任务及计划安排"},
                                       {"Type": "B"}], )
                        elif j == '舒适/家庭':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "追求舒适、轻松、优越的工作条件和环境，关注工作与生活的平衡"},
                                       {"Factor": "不关注工作与生活的平衡，接受在常规工作时间外执行任务，不介意加班"}, {
                                           "Suggest": " · 向他/她提供能够保持专注工作的环境和条件为他/她安排足够的工作任务，确保有一定的工作量,向他/她提供有一定难度和挑战性的工作,和向他/她提供更多的休假相比，向其提供新领域的工作和学习机会，以及更好的职业发展渠道等激励手段可能会更有效"},
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
                                           "Suggest": " 在公司内部，制定健全的工作规章制度,给予他/她明确的工作指示，并监督他/她的工作进程，即时给予反馈,避免为他/她安排需要自主管理的工作任务,对于他/她遵守公司规章制度，严格履行公司纪律的行为，给予奖励和认可"},
                                       {"Type": "C"}], )
                        elif j == '专业/技术':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "追求在技术或专业领域的成长和提高，倾向于专业或技术性的工作岗位和内容"},
                                       {"Factor": "工作是否符合自己的经历或专业并不重要，不关心学习新知识或专业技能的机会"}, {
                                           "Suggest": " 与他/她沟通，了解他/她对工作内容专业性的期待,避免仅通过他/她在专业性上的进步和发展激励他/她,避免为他/她安排在专业性要求过高的工作任务,鼓励他/她多尝试多探索，找到自己希望发展的职业技能"},
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
                                       {"Factor": "不关注外在的职务、地位和身份认可 "},
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
                                           "Suggest": " 避免过多关心他/她的私人生活,多为他/她安排个人可独立完成的工作任务,在他/她参与团队合作工作时，与他/她充分沟通，明确他/她个人承担的工作任务,在他/她参于集体活动时，强调集体活动对团队建设和发展的意义"},
                                       {"Type": "C"}], )

                        elif j == '经济/报酬':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "关注工作所获得的经济报酬和物质回报，自身的额外努力必须得到可见的奖励"},
                                       {"Factor": "较少关注工作带来的金钱利益和其它物质回报"},
                                       {
                                           "Suggest": " · 与他/她沟通，了解他/她所期望的激励方式确保组织内经济报酬分配的公平合理性,尝试采用多种手段相结合的方式来评价他/她的工作表现,避免只通过薪资福利增长的方式来激励他/她"},
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
                                           "Suggest": " · 向他/她提供能够保持专注工作的环境和条件为他/她安排足够的工作任务，确保有一定的工作量,向他/她提供有一定难度和挑战性的工作,和向他/她提供更多的休假相比，向其提供新领域的工作和学习机会，以及更好的职业发展渠道等激励手段可能会更有效"},
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
                                           "Suggest": " 在公司内部，制定健全的工作规章制度,给予他/她明确的工作指示，并监督他/她的工作进程，即时给予反馈,避免为他/她安排需要自主管理的工作任务,对于他/她遵守公司规章制度，严格履行公司纪律的行为，给予奖励和认可"},
                                       {"Type": "D"}], )
                        elif j == '专业/技术':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "追求在技术或专业领域的成长和提高，倾向于专业或技术性的工作岗位和内容"},
                                       {"Factor": "工作是否符合自己的经历或专业并不重要，不关心学习新知识或专业技能的机会"}, {
                                           "Suggest": " 与他/她沟通，了解他/她对工作内容专业性的期待,避免仅通过他/她在专业性上的进步和发展激励他/她,避免为他/她安排在专业性要求过高的工作任务,鼓励他/她多尝试多探索，找到自己希望发展的职业技能"},
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
                                       {"Factor": "不关注外在的职务、地位和身份认可 "},
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
                                           "Suggest": " 避免过多关心他/她的私人生活,多为他/她安排个人可独立完成的工作任务,在他/她参与团队合作工作时，与他/她充分沟通，明确他/她个人承担的工作任务,在他/她参于集体活动时，强调集体活动对团队建设和发展的意义"},
                                       {"Type": "D"}], )

                        elif j == '经济/报酬':
                            ls.append([{"Dimension": i['Dimension']}, {"Target": i['name']},
                                       {"TargetDesc": "关注工作所获得的经济报酬和物质回报，自身的额外努力必须得到可见的奖励"},
                                       {"Factor": "较少关注工作带来的金钱利益和其它物质回报"},
                                       {
                                           "Suggest": " · 与他/她沟通，了解他/她所期望的激励方式确保组织内经济报酬分配的公平合理性,尝试采用多种手段相结合的方式来评价他/她的工作表现,避免只通过薪资福利增长的方式来激励他/她"},
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
                                           "Suggest": " · 向他/她提供能够保持专注工作的环境和条件为他/她安排足够的工作任务，确保有一定的工作量,向他/她提供有一定难度和挑战性的工作,和向他/她提供更多的休假相比，向其提供新领域的工作和学习机会，以及更好的职业发展渠道等激励手段可能会更有效"},
                                       {"Type": "D"}], )

            analysis = ls
            StrongIncentiveFactor = (re.sub(',', '', StrongIncentiveFactor))
            GeneralIncentiveFactor = (re.sub(',', '', GeneralIncentiveFactor))
            GeneralNegativeMotivators = (re.sub(',', '', GeneralNegativeMotivators))
            StrongNegativeIncentiveFactors = (re.sub(',', '', StrongNegativeIncentiveFactors))

            report07['msg']["StrongIncentiveFactor"] = StrongIncentiveFactor
            report07['msg']["GeneralIncentiveFactor"] = GeneralIncentiveFactor
            report07['msg']["GeneralNegativeMotivators"] = GeneralNegativeMotivators
            report07['msg']["StrongNegativeIncentiveFactors"] = StrongNegativeIncentiveFactors
            report07['msg']["analysis"] = analysis
            res = {"code": 0, 'detail': {'report_data': report07}}
            print('发送到word服务的数据:%s' % res)
            return HttpResponse(json.dumps(res, ensure_ascii=False).encode('utf-8'), content_type="application/json")
        elif report_type_id == "ProfessionalPpersonalit":
            ContentDBCofSelfImage = ""
            ContentBehavioralCharacte = ""
            ContentAdvantagesAndWeaknesses = ""
            ContentCommunicationStyle = ""
            report08['msg']["ContentDBCofSelfImage"] = ContentDBCofSelfImage
            report08['msg']["ContentBehavioralCharacte"] = ContentBehavioralCharacte
            report08['msg']["ContentAdvantagesAndWeaknesses"] = ContentAdvantagesAndWeaknesses
            report08['msg']["ContentCommunicationStyle"] = ContentCommunicationStyle

            res = {"code": 0, 'detail': {'report_data': report08}}
            print('发送到word服务的数据:%s' % res)
            return HttpResponse(json.dumps(res, ensure_ascii=False).encode('utf-8'), content_type="application/json")
        else:
            res = {"code": 40400, 'detail': {'report_data': "传参错误请检查参数"}}
            print('发送到word服务的数据:%s' % res)
            return HttpResponse(json.dumps(res, ensure_ascii=False).encode('utf-8'), content_type="application/json")

def admin_get_report(request):
    """
    管理员获取报告函数
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "report/admin_get_report.html", )

def admin_get_specific_report(request):
    """
    管理员获取报告函数
    管理员获取指定报告
    :param request:
    :return:
    """
    if request.method == "GET":

        return render(request, "report/admin_get_specific_report.html", )

    elif request.method == "POST":
        # 获取数据
        req = simplejson.loads(request.body)
        questionnaire_id = req['questionnaire_id']
        assess_project_id = req['assess_project_id']
        user_id = req['user_id']
        report_type_id = req['report_type_id']

        user_report_list = models.UserReport.objects.filter(
            questionnaire_id=questionnaire_id,
            assess_project_id=assess_project_id,
            user_id=user_id,
            report_type_id=report_type_id)
        report_list = []
        for i in user_report_list:
            report_list.append(i)
        res = {"code": 0, "detail": {'status': user_report_list[0].status, "url": user_report_list[0].url}}


def admin_get_all_report(request):
    """
    管理员获取报告函数
    管理员获取所有用户报告
    :param request:
    :return:
    """
    if request.method == "GET":
        user_report_list = models.AdminUserReport.objects.filter()
        return render(request, "report/admin_get_all_report.html", {'user_report_list': user_report_list})

