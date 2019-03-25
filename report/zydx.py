# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:yhq

def sub(score, chart):
    '''
    传入指标分，指标名，返回最高得分，和第二高分值
    :param score:指标分
    :param chart: 指标名对应指标分
    :return: 指标名
    '''
    d1 = max(score)
    ls2 = []
    for i in score:
        if i < d1:
            ls2.append(i)
    if len(ls2)!= 0:
        d2 = max(ls2)
    else:
        d2 = []
    print(d2)
    ls3 = []
    ls4 = []
    for obj in chart:
        if obj['score'] == d1:
            ls3.append(obj['name'])
        if obj['score'] == d2:
            ls4.append(obj['name'])

    return ls3,ls4

def desc_zydx(v):
    '''
    主导
    传入类型，返回类型，类型描述，以及另外4项描述
    :param v:
    :return: 返回类型，类型描述，以及另外4项描述:工作类型 薪酬福利 工作晋升 最佳认可方式

    '''
    if v == '技术/职能型':

        v1 ='''
            <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>意味着您追求在技术/职能领域的成长和技能的不断提高，希望在工作中实践并应用这种技术/职能。您对自己的认可来自于您的专业水平，您喜欢面对专业领域内的挑战。通常，您不喜欢从事一般的管理工作，因为这意味着您不得不放弃在技术职能领域内的成就。</w:t>
            </w:r>
        </w:p>
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>作为技术/职能型职业锚的一员，您强调实际技术/功能等业务工作，注重个人在专业技能领域的进一步发展，希望有机会实践自己的技术才能，享受作为某方面专家带来的满足、愉悦。本类型的人通常不愿意选择一般管理型的工作，因为这是一种他们难以施展自己技术才能的工种，也意味着他们放弃在技术功能领域的成就。技术职能型的人可能出现在许多领域，例如某些金融分析师专注于解决复杂的投资问题，一个工程师发现他非常擅长设计，一个销售员发现他独特的销售才能。</w:t>
            </w:r>
        </w:p>
        
        
        '''


        v2 = '''您在职业选择时主要考虑工作的内容，即工作是否可以带来自己在专业方面的成功和技能的不断提高。喜欢领域内的挑战和独立开展工作，强烈抵制难以施展自己技术才能的工作。
        '''
        v3 = '''您希望薪酬福利可以反映技术、专业水平的高低。
        '''
        v4 = '''您看重技术或专业等级，而非职位的晋升。
        '''
        v5 = '''
        对您而言，来自本专业领域专家的肯定和认可，以及专业地位的提高，是最有效的激励方式。
        '''

        return v, v1, v2, v3, v4, v5,
    if v == '管理型':
        v1 = '''
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t> 意味着您追求并致力于职位晋升，倾心于全面管理，独立负责一个部分，可以跨部门整合其他人的努力成果。管理型的您希望承担整体的责任，并将公司的成功与否看作衡量自己工作的标准。具体的技术/职能工作仅仅被看作是您通向全面管理层的必经之路。</w:t>
            </w:r>
        </w:p>
        
         <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t> 管理型职业锚的人，强调实际的业务管理与控制，注重个人在一般管理与领导领域的进一步发展，希望有机会和时间展示自己的管理才能；管理型的您不愿意放弃任何在组织内获得更高职位的机会，您也愿意承担您所管理组织或单位的业绩与输出。</w:t>
            </w:r>
        </w:p>
        
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t> 如果您目前还处于技术或者职能工作的领域，您会把这看作是学习的必经过程，也愿意接受本功能组织的管理岗位，但您更愿意接受一般性管理的职位。希望能够依靠个人的分析能力、人际关系、团队领导能力、情商、以及负责任的态度，为本组织或者项目的成功贡献力量。</w:t>
            </w:r>
        </w:p>
        
        '''

        v2 = '''管理型的您希望在工作中能够学习如何行使多项职责；如何综合利用来自多种渠道的信息；如何管理人数不断增加的员工队伍；以及如何运用人际交流技巧。'''
        v3 = '''管理型职业锚的人认为薪酬是由所处职位所决定的，因此，管理型的您在管理职位上的追求，也代表了您对于高薪酬福利的期望。'''
        v4 = '''您拥护组织传统的职业发展道路，追求并致力于工作晋升，倾心于全面管理，独立负责一个部分，可以跨部门整合其他人的努力成果。管理型的您想去承担整体的责任，并将公司的成功与否看成自己的工作。具体的技术/职能工作仅仅被看作是通向更高、更全面管理层的必经之路。'''
        v5 = '''您希望通过获得更高的薪水以及职位的晋升来得到认可，如果让您去管理大项目，或者邀请出席重要会议，或者派您去参加某些研讨会，使您得以提升自身管理技能，也是不错的认可方式。'''

        return v, v1, v2, v3, v4, v5,
    if v == '自主/独立型':
        v1 = '''
            <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t> 意味着您不会放弃任何可以以您的意志或方法定义您职业生涯发展的机会。您追求自主和独立，不愿意受别人约束，也不愿受程序、工作时间、着装方式等规范的制约。不管工作内容是什么，自主/独立型的您都希望能在工作过程中用自己的方式、工作习惯、时间进度和自己的标准来完成工作。</w:t>
            </w:r>
        </w:p>
        
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t> 为了追求自主、独立，您宁愿放弃安逸的工作环境或优厚的薪金待遇。自主/独立型的个体，倾向于从事极具自由的职业，比如自由顾问、教授、独立的商务人士、销售员等等。如果您被局限在一个组织内，您希望职位能够具有灵活与独立性；您有时也会因为希望保留自主的权力而放弃晋升与发展的机会。</w:t>
            </w:r>
        </w:p>
        
        '''
        v2 = '''您喜欢专业领域内职责描述清晰、时间明确的工作。对您而言，承包式或项目式工作，全职、兼职或是临时性的工作都是可以接受的。另外您倾向于为“有明确工作目标，却不限制工作完成方式的组织”效力。您能接受组织强加的工作目标，但希望按照自己喜欢的方式完成工作；'''
        v3 = '''您喜欢基于工作绩效的工资、奖金，希望能当即付清；'''
        v4 = '''您希望基于自己以往的成就获得晋升，希望从新的岗位上获取更多的独立和自主权。如果新的职位赋予了您更高的头衔和更多责任，却剥夺了您自由工作的空间，您会感到难以接受；'''
        v5 = '''您最喜欢直接的表扬或认可，勋章、奖品、证书等奖励方式比晋升、获得头衔甚至是金钱更具吸引力。对您而言，如果能在工作上获取更大的自主空间，这将是最有效的激励方式。'''

        return v, v1, v2, v3, v4, v5,
    if v == '安全/稳定型':
        v1 = '''
            <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t> 安全/稳定型职业锚的主要关注点是争取一份稳定的职业，这种职业锚也显示了对于财务安全性（比如养老金、公积金或医疗保险）、雇佣安全性以及地区选择的重视。</w:t>
            </w:r>
        </w:p>
        
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>作为安全/稳定型中的一员，尽管您也可能因为才干获得在组织内的提升，但是您可能不太在意工作的内容或者是否能够得到职位的提升。安全/稳定型的人总是关注于围绕着安全与稳定构建全部的自我形象。安全/稳定型的人只有在已经获得职位的成功以及确定的稳定性后才能够显得放松。</w:t>
            </w:r>
        </w:p>
        
        '''
        v2 = '''您希望获得一份长期的稳定职业，这些职业能够提供有保障的工作、体面的收入以及可靠的未来生活，这种可靠的未来生活通常是由良好的退休计划和较高的退休金来保证的，有可能的话，您会优先选择政府机关，医疗机构，教育行业，大型的外资或国有企业。'''
        v3 = '''您不追求一份令人羡慕的薪金，而更在意稳定长期的财务安全性。对于您来说，除了固定的薪资，您还在意福利的结构，包括各种保险，公积金，休假，固定投资等等。'''
        v4 = '''对于您来说，追求更为优越的职业或工作的晋升，如果意味着将要在您的生活中注入一种不稳定或保障较差的因素的话，那么您会觉得在一个熟悉的环境中维持一种稳定的、有保障的职业对您来说是更为重要的。'''
        v5 = '''来自组织对于您长期贡献与经验资历的表彰是组织对您最佳的认可方式；而一份长期的或无固定期限的合同，或者组织提供的完善的家庭保障计划，将是对您最好的激励方式。'''

        return v, v1, v2, v3, v4, v5,
    if v == '创造/创业型':
        v1 = '''
            <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>意味着您不会放弃任何可能创建属于您自己的团队或组织或企业的机会。您愿意基于自己的能力与意愿，承担风险并克服障碍。您愿意向其他人证明您能够依靠自己的努力创建一个企业。您可能为了学习与寻找机会而被雇佣，但是您一旦找到机会便会抽身而出。</w:t>
            </w:r>
        </w:p>
        
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t> 您愿意去证明您创建企业的成功，您的需求如此强烈使得您愿意去承受可能的失败直到最终成功。极强烈的创造欲使创业型的人要求标新立异、有所创造、并做好冒险的准备。大多数创业型的人成为了创业者、发明家或艺术家。但需要澄清的是，市场分析人员、研究开发人员、广告策划人员并不能归入这一类别，因为创业型人的主要动机和价值观是“创造”。</w:t>
            </w:r>
        </w:p>
        
        
        '''
        v2 = '''您希望通过自己的努力创造新的公司、产品或服务。您相信自己是天才，并有很高的动力去证明您具有创造力，而且不断地接受新的挑战；'''
        v3 = '''您认为所有权和控制权对您才是最重要的，例如：年薪、股票或期权。您不会在意每月固定的薪资，或者定期的奖金，对您来说，获得与所有权与控制权所对应报酬才是最重要的;您希望得到金钱，但不是出于爱财的缘故，而是因为把金钱当作您完成了某件大事业的有形标志；'''
        v4 = '''您要求一定的权力和自由，可以不断去创造；'''
        v5 = '''您要求很高的自我认可和公众认可。创造完全属于自己的东西，例如：一件产品、服务、公司或反应成就的财富等。对于您来说，最佳的认可方式就是对您创造的“产品”的认可与赞扬，或者在公开场合给予您受之无愧的表扬。'''

        return v, v1, v2, v3, v4, v5,
    if v == '服务/奉献型':
        v1 = '''
            <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>服务型的人一直在追求他们的核心价值，例如：帮助他人，改善人们的安全，通过新的产品消除疾病等。服务型的人一直追寻这种机会，即使变换公司，也不会接受无法实现这种价值的变动或工作提升。</w:t>
            </w:r>
        </w:p>
        
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>作为服务型的一员，意味着您不会放弃任何有可能创造某种价值的机会，比如改变人居环境，解决环境污染的问题，创造和谐的人际关系，帮助他人，改善人群的安全感，通过新产品的研发治疗疾病，以及其他方式。就算您所关注的工作或事宜有可能影响到组织的现状，您也会始终追求您的职业定位及其价值意义。您也会不愿意接受那些有可能使您不能关注于创造价值的职位转移或提升。</w:t>
            </w:r>
        </w:p>
        
        
        '''
        v2 = '''您希望工作能够创造价值，对他人能有所帮助、使生活更美好。您希望能以自己的价值观影响组织乃至社会；'''
        v3 = '''您希望获得基于贡献的、公平的薪资，钱并不是您追求的根本；'''
        v4 = '''您希望通过认可您的贡献，给您更多的权力和自由来体现自己的价值；'''
        v5 = '''来自同事及上司的认可和支持，与他人共享自己的核心价值。通过自己的努力，给别人带来了帮助或促成了某项事业的成功。能给您继续提供为心中的理想打拼的机会，这才是对您的真正认可。'''

        return v, v1, v2, v3, v4, v5,
    if v == '挑战型':
        v1 = '''
            <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>挑战型的人，喜欢解决看上去无法解决的问题，战胜强硬的对手，克服无法克服的障碍等。对挑战型的您而言，参加工作或职业的原因是工作允许您去战胜各种不可能。您需要新奇、变化和困难，如果工作非常容易，您马上就会厌倦这份工作。</w:t>
            </w:r>
        </w:p>
        
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>作为挑战型的一员，意味着您不会放弃任何发掘解决问题的方法，克服他人所不能克服的障碍，或者超越您竞争对手的机会。您认为自己可以征服任何事情或任何人；您将成功定义为“克服不可能的障碍，解决不可能解决的问题，或战胜非常强硬的对手”。随着自己的进步，您喜欢寻找越来越强硬的“挑战”，希望在工作中面临越来越艰巨的任务，并享受由战胜或征服而带来的成就感。</w:t>
            </w:r>
        </w:p>
        
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>需要说明的是，您的职业锚类型与技术/职能型之间存在一定差别，即技术/职能型的人只关注某一专业领域内的挑战并持续为之奋斗；而挑战型的人，一旦达成了成就或征服了困难，再让您去做同一类型的任务，就会感觉无聊之极。还有一些挑战型职业锚的人，将挑战定义成人际间的竞争。例如：一些飞行员唯一的目标就是与敌机来一场决战，以向世界证明他们在战斗中的优势；许多销售人员、职业运动员和管理者将职业定义为在每日的战斗或竞赛中胜出。</w:t>
            </w:r>
        </w:p>
        
        
        '''
        v2 = '''对您而言，一定水平的挑战是至关重要的，不管您的工作内容是什么，都需要有“挑战自我的机会”；'''
        v3 = '''您希望基于所从事的项目或任务的挑战性、难度得到报酬。金钱并不是您的最终追求，您更看重工作中是否有挑战自我或挑战难题的机会；'''
        v4 = '''您希望自己的晋升能使自己的“工作为自己提供更多挑战困难或挑战自我的机会”，因而，如果职位提高了，挑战自我的机会减少了，那么您很快就会厌倦这个职位；'''
        v5 = '''您渴望战胜困难或征服对手后的成就感，因此，战胜挑战后的愉悦感会激励着您不断寻求难度更大的挑战。您对自己的认可基于挑战的成败，而不是外在的奖励，因此，对您来说，挑战即是认可，只要给您布置好下一个工作任务就行了。'''

        return v, v1, v2, v3, v4, v5,
    if v == '生活型':
        v1 = '''
            <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>生活型的人，希望将生活的各个主要方面整合为一个整体，喜欢平衡个人的、家庭的和职业的需要，因此，生活型的您需要一个能够提供“足够弹性”的工作环境来实现这一目标。生活型的人甚至可以牺牲职业的一些方面，例如放弃职位的提升或调动，来换取三者的平衡。相对于具体的工作环境、工作内容，生活型的您更关注自己如何生活、在哪里居住、如何处理家庭事情及怎样自我提升等。</w:t>
            </w:r>
        </w:p>
        
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>生活型职业锚是综合了职业与家庭关系的一种职业定位。生活型职业锚现在变得越来越普遍，因为作为家庭主要成员的两方必须同时关注两个同样重要，但是有可能就是不同的职业选择。如果您在生活型方面的得分相对最高，意味着您不会放弃任何有助于整合或平衡个人的需求，与家庭的需求，或者与您职业的需求的机会。您期望那些与生活工作重要的因素能够相互融合成一体，因此，您也愿意去发展您的职业生涯以提供足够的灵活性满足这种融合。</w:t>
            </w:r>
        </w:p>
        
        '''
        v2 = '''您希望为生活而工作的，而不是为工作而生活，所以在工作上，您不会多做一点点份外之事。您期望您的工作内容是明确的。'''
        v3 = '''您不追求通过加班或参与项目的方式获得额外的收入，您追求属于您的那一份明确工作任务的所得。对于您来说，这份薪酬福利已经能够使您正常快乐的生活，而额外付出的努力获得的收入反而得不偿失。'''
        v4 = '''如果职位的晋升可能会带来对于生活家庭的负面的影响，您会毫不迟疑地拒绝；因为成功对您来说，不仅仅是在工作，而更是在生活与家庭上。'''
        v5 = '''弹性的工作时间安排可能是对您最有效的奖励。您不希望承担超出最低工作要求之外的其他工作，所以您也不会期待除了薪水以外的其他奖励。在您表现出色、工作高效的时候，如果能给您一个最大化非工作时间的机会，这将是对您最大的奖励！'''
        return v, v1, v2, v3, v4, v5,


def desc_fu(v):
    '''
    辅助
    传入类型，返回类型，类型描述，以及另外4项描述
    :param v:
    :return: 返回类型，类型描述，以及另外4项描述:工作类型 薪酬福利 工作晋升 最佳认可方式

    '''
    if v == '技术/职能型':        
        v1 = '''
            <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>意味着您追求在技术/职能领域的成长和技能的不断提高，希望在工作中实践并应用这种技术/职能。您对自己的认可来自于您的专业水平，您喜欢面对专业领域内的挑战。通常，您不喜欢从事一般的管理工作，因为这意味着您不得不放弃在技术职能领域内的成就。</w:t>
            </w:r>
        </w:p>
        
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>作为技术/职能型职业锚的一员，您强调实际技术/功能等业务工作，注重个人在专业技能领域的进一步发展，希望有机会实践自己的技术才能，享受作为某方面专家带来的满足、愉悦。本类型的人通常不愿意选择一般管理型的工作，因为这是一种他们难以施展自己技术才能的工种，也意味着他们放弃在技术功能领域的成就。技术职能型的人可能出现在许多领域，例如某些金融分析师专注于解决复杂的投资问题，一个工程师发现他非常擅长设计，一个销售员发现他独特的销售才能。</w:t>
            </w:r>
        </w:p>
        
        
        '''

        v2 = '''您在职业选择时主要考虑工作的内容，即工作是否可以带来自己在专业方面的成功和技能的不断提高。喜欢领域内的挑战和独立开展工作，强烈抵制难以施展自己技术才能的工作。'''
        v3 = '''您希望薪酬福利可以反映技术、专业水平的高低。'''
        v4 = '''您看重技术或专业等级，而非职位的晋升。'''
        v5 = '''对您而言，来自本专业领域专家的肯定和认可，以及专业地位的提高，是最有效的激励方式。'''

        return v, v1, v2, v3, v4, v5,
    if v == '管理型':
        v1 = '''
            <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>意味着您追求并致力于职位晋升，倾心于全面管理，独立负责一个部分，可以跨部门整合其他人的努力成果。管理型的您希望承担整体的责任，并将公司的成功与否看作衡量自己工作的标准。具体的技术/职能工作仅仅被看作是您通向全面管理层的必经之路。</w:t>
            </w:r>
        </w:p>
        
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>管理型职业锚的人，强调实际的业务管理与控制，注重个人在一般管理与领导领域的进一步发展，希望有机会和时间展示自己的管理才能；管理型的您不愿意放弃任何在组织内获得更高职位的机会，您也愿意承担您所管理组织或单位的业绩与输出。</w:t>
            </w:r>
        </w:p>
        
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>如果您目前还处于技术或者职能工作的领域，您会把这看作是学习的必经过程，也愿意接受本功能组织的管理岗位，但您更愿意接受一般性管理的职位。希望能够依靠个人的分析能力、人际关系、团队领导能力、情商、以及负责任的态度，为本组织或者项目的成功贡献力量。</w:t>
            </w:r>
        </w:p>
        
        
        '''
        v2 = '''管理型的您希望在工作中能够学习如何行使多项职责；如何综合利用来自多种渠道的信息；如何管理人数不断增加的员工队伍；以及如何运用人际交流技巧。'''
        v3 = '''管理型职业锚的人认为薪酬是由所处职位所决定的，因此，管理型的您在管理职位上的追求，也代表了您对于高薪酬福利的期望。'''
        v4 = '''您拥护组织传统的职业发展道路，追求并致力于工作晋升，倾心于全面管理，独立负责一个部分，可以跨部门整合其他人的努力成果。管理型的您想去承担整体的责任，并将公司的成功与否看成自己的工作。具体的技术/职能工作仅仅被看作是通向更高、更全面管理层的必经之路。'''
        v5 = '''您希望通过获得更高的薪水以及职位的晋升来得到认可，如果让您去管理大项目，或者邀请出席重要会议，或者派您去参加某些研讨会，使您得以提升自身管理技能，也是不错的认可方式。'''
        return v, v1, v2, v3, v4, v5,
    if v == '自主/独立型':
        v1 = '''
            <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t> 意味着您不会放弃任何可以以您的意志或方法定义您职业生涯发展的机会。您追求自主和独立，不愿意受别人约束，也不愿受程序、工作时间、着装方式等规范的制约。不管工作内容是什么，自主/独立型的您都希望能在工作过程中用自己的方式、工作习惯、时间进度和自己的标准来完成工作。</w:t>
            </w:r>
        </w:p>
        
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t> 为了追求自主、独立，您宁愿放弃安逸的工作环境或优厚的薪金待遇。自主/独立型的个体，倾向于从事极具自由的职业，比如自由顾问、教授、独立的商务人士、销售员等等。如果您被局限在一个组织内，您希望职位能够具有灵活与独立性；您有时也会因为希望保留自主的权力而放弃晋升与发展的机会。</w:t>
            </w:r>
        </w:p>
        
        
        '''
        v2 = '''您喜欢专业领域内职责描述清晰、时间明确的工作。对您而言，承包式或项目式工作，全职、兼职或是临时性的工作都是可以接受的。另外您倾向于为“有明确工作目标，却不限制工作完成方式的组织”效力。您能接受组织强加的工作目标，但希望按照自己喜欢的方式完成工作；'''
        v3 = '''您喜欢基于工作绩效的工资、奖金，希望能当即付清；'''
        v4 = '''您希望基于自己以往的成就获得晋升，希望从新的岗位上获取更多的独立和自主权。如果新的职位赋予了您更高的头衔和更多责任，却剥夺了您自由工作的空间，您会感到难以接受；'''
        v5 = '''您最喜欢直接的表扬或认可，勋章、奖品、证书等奖励方式比晋升、获得头衔甚至是金钱更具吸引力。对您而言，如果能在工作上获取更大的自主空间，这将是最有效的激励方式。'''
        return v, v1, v2, v3, v4, v5,
    if v == '安全/稳定型':
        v1 = '''
             <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>安全/稳定型职业锚的主要关注点是争取一份稳定的职业，这种职业锚也显示了对于财务安全性（比如养老金、公积金或医疗保险）、雇佣安全性以及地区选择的重视。</w:t>
            </w:r>
        </w:p>
        
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>作为安全/稳定型中的一员，尽管您也可能因为才干获得在组织内的提升，但是您可能不太在意工作的内容或者是否能够得到职位的提升。安全/稳定型的人总是关注于围绕着安全与稳定构建全部的自我形象。安全/稳定型的人只有在已经获得职位的成功以及确定的稳定性后才能够显得放松。</w:t>
            </w:r>
        </w:p>
        
        
        
        '''
        v2 = '''您希望获得一份长期的稳定职业，这些职业能够提供有保障的工作、体面的收入以及可靠的未来生活，这种可靠的未来生活通常是由良好的退休计划和较高的退休金来保证的，有可能的话，您会优先选择政府机关，医疗机构，教育行业，大型的外资或国有企业。'''
        v3 = '''您不追求一份令人羡慕的薪金，而更在意稳定长期的财务安全性。对于您来说，除了固定的薪资，您还在意福利的结构，包括各种保险，公积金，休假，固定投资等等。'''
        v4 = '''对于您来说，追求更为优越的职业或工作的晋升，如果意味着将要在您的生活中注入一种不稳定或保障较差的因素的话，那么您会觉得在一个熟悉的环境中维持一种稳定的、有保障的职业对您来说是更为重要的。'''
        v5 = '''来自组织对于您长期贡献与经验资历的表彰是组织对您最佳的认可方式；而一份长期的或无固定期限的合同，或者组织提供的完善的家庭保障计划，将是对您最好的激励方式。'''
        return v, v1, v2, v3, v4, v5,
    if v == '创造/创业型':
        v1 = '''
             <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>意味着您不会放弃任何可能创建属于您自己的团队或组织或企业的机会。您愿意基于自己的能力与意愿，承担风险并克服障碍。您愿意向其他人证明您能够依靠自己的努力创建一个企业。您可能为了学习与寻找机会而被雇佣，但是您一旦找到机会便会抽身而出。</w:t>
            </w:r>
        </w:p>
        
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>您愿意去证明您创建企业的成功，您的需求如此强烈使得您愿意去承受可能的失败直到最终成功。极强烈的创造欲使创业型的人要求标新立异、有所创造、并做好冒险的准备。大多数创业型的人成为了创业者、发明家或艺术家。但需要澄清的是，市场分析人员、研究开发人员、广告策划人员并不能归入这一类别，因为创业型人的主要动机和价值观是“创造”。</w:t>
            </w:r>
        </w:p>
        
        
        
        
        '''
        v2 = '''您希望通过自己的努力创造新的公司、产品或服务。您相信自己是天才，并有很高的动力去证明您具有创造力，而且不断地接受新的挑战；'''
        v3 = '''您认为所有权和控制权对您才是最重要的，例如：年薪、股票或期权。您不会在意每月固定的薪资，或者定期的奖金，对您来说，获得与所有权与控制权所对应报酬才是最重要的；您希望得到金钱，但不是出于爱财的缘故，而是因为把金钱当作您完成了某件大事业的有形标志；'''
        v4 = '''您要求一定的权力和自由，可以不断去创造；'''
        v5 = '''您要求很高的自我认可和公众认可。创造完全属于自己的东西，例如：一件产品、服务、公司或反应成就的财富等。对于您来说，最佳的认可方式就是对您创造的“产品”的认可与赞扬，或者在公开场合给予您受之无愧的表扬。'''
        return v, v1, v2, v3, v4, v5,
    if v == '服务/奉献型':
        v1 = '''
            <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>服务型的人一直在追求他们的核心价值，例如：帮助他人，改善人们的安全，通过新的产品消除疾病等。服务型的人一直追寻这种机会，即使变换公司，也不会接受无法实现这种价值的变动或工作提升。</w:t>
            </w:r>
        </w:p>
        
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>作为服务型的一员，意味着您不会放弃任何有可能创造某种价值的机会，比如改变人居环境，解决环境污染的问题，创造和谐的人际关系，帮助他人，改善人群的安全感，通过新产品的研发治疗疾病，以及其他方式。就算您所关注的工作或事宜有可能影响到组织的现状，您也会始终追求您的职业定位及其价值意义。您也会不愿意接受那些有可能使您不能关注于创造价值的职位转移或提升。</w:t>
            </w:r>
        </w:p>
        
        
        
        '''
        v2 = '''您希望工作能够创造价值，对他人能有所帮助、使生活更美好。您希望能以自己的价值观影响组织乃至社会；'''
        v3 = '''您希望获得基于贡献的、公平的薪资，钱并不是您追求的根本；'''
        v4 = '''您希望通过认可您的贡献，给您更多的权力和自由来体现自己的价值；'''
        v5 = '''来自同事及上司的认可和支持，与他人共享自己的核心价值。通过自己的努力，给别人带来了帮助或促成了某项事业的成功。能给您继续提供为心中的理想打拼的机会，这才是对您的真正认可。'''
        return v, v1, v2, v3, v4, v5,
    if v == '挑战型':
        v1 = '''
            <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>挑战型的人，喜欢解决看上去无法解决的问题，战胜强硬的对手，克服无法克服的障碍等。对挑战型的您而言，参加工作或职业的原因是工作允许您去战胜各种不可能。您需要新奇、变化和困难，如果工作非常容易，您马上就会厌倦这份工作。</w:t>
            </w:r>
        </w:p>
        
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>作为挑战型的一员，意味着您不会放弃任何发掘解决问题的方法，克服他人所不能克服的障碍，或者超越您竞争对手的机会。您认为自己可以征服任何事情或任何人；您将成功定义为“克服不可能的障碍，解决不可能解决的问题，或战胜非常强硬的对手”。随着自己的进步，您喜欢寻找越来越强硬的“挑战”，希望在工作中面临越来越艰巨的任务，并享受由战胜或征服而带来的成就感。</w:t>
            </w:r>
        </w:p>
        
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>需要说明的是，您的职业锚类型与技术/职能型之间存在一定差别，即技术/职能型的人只关注某一专业领域内的挑战并持续为之奋斗；而挑战型的人，一旦达成了成就或征服了困难，再让您去做同一类型的任务，就会感觉无聊之极。还有一些挑战型职业锚的人，将挑战定义成人际间的竞争。例如：一些飞行员唯一的目标就是与敌机来一场决战，以向世界证明他们在战斗中的优势；许多销售人员、职业运动员和管理者将职业定义为在每日的战斗或竞赛中胜出。</w:t>
            </w:r>
        </w:p>
        
        '''
        v2 = '''对您而言，一定水平的挑战是至关重要的，不管您的工作内容是什么，都需要有“挑战自我的机会”；'''
        v3 = '''您希望基于所从事的项目或任务的挑战性、难度得到报酬。金钱并不是您的最终追求，您更看重工作中是否有挑战自我或挑战难题的机会；'''
        v4 = '''您希望自己的晋升能使自己的“工作为自己提供更多挑战困难或挑战自我的机会”，因而，如果职位提高了，挑战自我的机会减少了，那么您很快就会厌倦这个职位；'''
        v5 = '''您渴望战胜困难或征服对手后的成就感，因此，战胜挑战后的愉悦感会激励着您不断寻求难度更大的挑战。您对自己的认可基于挑战的成败，而不是外在的奖励，因此，对您来说，挑战即是认可，只要给您布置好下一个工作任务就行了。'''
        return v, v1, v2, v3, v4, v5,
    if v == '生活型':        
        v1 = '''
            <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>生活型的人，希望将生活的各个主要方面整合为一个整体，喜欢平衡个人的、家庭的和职业的需要，因此，生活型的您需要一个能够提供“足够弹性”的工作环境来实现这一目标。生活型的人甚至可以牺牲职业的一些方面，例如放弃职位的提升或调动，来换取三者的平衡。相对于具体的工作环境、工作内容，生活型的您更关注自己如何生活、在哪里居住、如何处理家庭事情及怎样自我提升等。</w:t>
            </w:r>
        </w:p>
        
        <w:p w14:paraId="020E4E27" w14:textId="32AEF2DE" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>生活型职业锚是综合了职业与家庭关系的一种职业定位。生活型职业锚现在变得越来越普遍，因为作为家庭主要成员的两方必须同时关注两个同样重要，但是有可能就是不同的职业选择。如果您在生活型方面的得分相对最高，意味着您不会放弃任何有助于整合或平衡个人的需求，与家庭的需求，或者与您职业的需求的机会。您期望那些与生活工作重要的因素能够相互融合成一体，因此，您也愿意去发展您的职业生涯以提供足够的灵活性满足这种融合。</w:t>
            </w:r>
        </w:p>
        
        '''
        v2 = '''您希望为生活而工作的，而不是为工作而生活，所以在工作上，您不会多做一点点份外之事。您期望您的工作内容是明确的。'''
        v3 = '''您不追求通过加班或参与项目的方式获得额外的收入，您追求属于您的那一份明确工作任务的所得。对于您来说，这份薪酬福利已经能够使您正常快乐的生活，而额外付出的努力获得的收入反而得不偿失。 '''
        v4 = '''如果职位的晋升可能会带来对于生活家庭的负面的影响，您会毫不迟疑地拒绝；因为成功对您来说，不仅仅是在工作，而更是在生活与家庭上。'''
        v5 = '''弹性的工作时间安排可能是对您最有效的奖励。您不希望承担超出最低工作要求之外的其他工作，所以您也不会期待除了薪水以外的其他奖励。在您表现出色、工作高效的时候，如果能给您一个最大化非工作时间的机会，这将是对您最大的奖励！'''
        return v, v1, v2, v3, v4, v5,





def zd_desc(ls1):
    '''
    传入类型，返回职业定向描述
    :param ls1: 主导类型
    :return: 职业定向描述
    '''
    s1 = ''
    if len(ls1) == 1:
        a = '''
         <w:p w14:paraId="57EC3546" w14:textId="77777777" w:rsidR="00520E7F" w:rsidRDefault="00520E7F"
             w:rsidP="00142614">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
        </w:p>
         <w:p w14:paraId="57EC3546" w14:textId="77777777" w:rsidR="00520E7F" w:rsidRDefault="00520E7F"
             w:rsidP="00142614">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
        </w:p>
        <w:p w14:paraId="4AF0FCEF" w14:textId="6E2B511A" w:rsidR="00142614" w:rsidRDefault="005E386E"
             w:rsidP="005E386E">
            <w:pPr>
                <w:pStyle w:val="a4"/>
                <w:numPr>
                    <w:ilvl w:val="0"/>
                    <w:numId w:val="8"/>
                </w:numPr>
                <w:snapToGrid w:val="0"/>
                <w:ind w:firstLineChars="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>主导职业锚：</w:t>
            </w:r>
            <w:r w:rsidR="003B3998">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
        </w:p>
        
         <w:p w14:paraId="57EC3546" w14:textId="77777777" w:rsidR="00520E7F" w:rsidRDefault="00520E7F"
             w:rsidP="00142614">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
        </w:p>
        
        <w:p w14:paraId="4D691D4F" w14:textId="7E5761B6" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="005E386E">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:noProof/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <mc:AlternateContent>
                    <mc:Choice Requires="wps">
                        <w:drawing>
                            <wp:anchor distT="0" distB="0" distL="114300" distR="114300" simplePos="0"
                                       relativeHeight="251675648" behindDoc="0" locked="0" layoutInCell="1"
                                       allowOverlap="1" wp14:anchorId="6FDDADD8" wp14:editId="0F7F2B3E">
                                <wp:simplePos x="0" y="0"/>
                                <wp:positionH relativeFrom="column">
                                    <wp:posOffset>4312</wp:posOffset>
                                </wp:positionH>
                                <wp:positionV relativeFrom="paragraph">
                                    <wp:posOffset>27964</wp:posOffset>
                                </wp:positionV>
                                <wp:extent cx="5296619" cy="0"/>
                                <wp:effectExtent l="0" t="0" r="0" b="0"/>
                                <wp:wrapNone/>
                                <wp:docPr id="13" name="直接连接符 13"/>
                                <wp:cNvGraphicFramePr/>
                                <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
                                    <a:graphicData
                                            uri="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
                                        <wps:wsp>
                                            <wps:cNvCnPr/>
                                            <wps:spPr>
                                                <a:xfrm>
                                                    <a:off x="0" y="0"/>
                                                    <a:ext cx="5296619" cy="0"/>
                                                </a:xfrm>
                                                <a:prstGeom prst="line">
                                                    <a:avLst/>
                                                </a:prstGeom>
                                                <a:ln w="12700">
                                                    <a:solidFill>
                                                        <a:schemeClr val="bg2">
                                                            <a:lumMod val="50000"/>
                                                        </a:schemeClr>
                                                    </a:solidFill>
                                                </a:ln>
                                            </wps:spPr>
                                            <wps:style>
                                                <a:lnRef idx="1">
                                                    <a:schemeClr val="accent1"/>
                                                </a:lnRef>
                                                <a:fillRef idx="0">
                                                    <a:schemeClr val="accent1"/>
                                                </a:fillRef>
                                                <a:effectRef idx="0">
                                                    <a:schemeClr val="accent1"/>
                                                </a:effectRef>
                                                <a:fontRef idx="minor">
                                                    <a:schemeClr val="tx1"/>
                                                </a:fontRef>
                                            </wps:style>
                                            <wps:bodyPr/>
                                        </wps:wsp>
                                    </a:graphicData>
                                </a:graphic>
                            </wp:anchor>
                        </w:drawing>
                    </mc:Choice>
                    <mc:Fallback>
                        <w:pict>
                            <v:line w14:anchorId="42E2299B" id="直接连接符 13" o:spid="_x0000_s1026"
                                    style="position:absolute;left:0;text-align:left;z-index:251675648;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text"
                                    from=".35pt,2.2pt" to="417.4pt,2.2pt"
                                    o:gfxdata="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&#xA;"
                                    strokecolor="#747070 [1614]" strokeweight="1pt">
                                <v:stroke joinstyle="miter"/>
                            </v:line>
                        </w:pict>
                    </mc:Fallback>
                </mc:AlternateContent>
            </w:r>
        </w:p>
        <w:p w14:paraId="020E4E27" w14:textId="275D75F3" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
        </w:p>
       
       
        <w:p w14:paraId="06DCE1F9" w14:textId="1B757E76" w:rsidR="00F968E2" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="005E386E">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>工作类型</w:t>
            </w:r>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>:%s</w:t>
            </w:r>
            
            
        </w:p>
        
        <w:p w14:paraId="45B5540F" w14:textId="6A41CF20" w:rsidR="00F968E2" w:rsidRPr="00DF5704"
             w:rsidRDefault="005E386E" w:rsidP="005E386E">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>薪酬福利</w:t>
            </w:r>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>:%s</w:t>
            </w:r>
            
        </w:p>
        <w:p w14:paraId="66923C5D" w14:textId="274B4461" w:rsidR="00BF60AD" w:rsidRPr="00DF5704"
             w:rsidRDefault="005E386E" w:rsidP="005E386E">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>工作晋升</w:t>
            </w:r>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r w:rsidR="00031A2A">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
        </w:p>
        <w:p w14:paraId="3F7C0DD7" w14:textId="7F02724E" w:rsidR="008515B4" w:rsidRDefault="005E386E"
             w:rsidP="00142614">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>最佳认可方式</w:t>
            </w:r>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r w:rsidR="00031A2A">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
           
        </w:p>
         <w:p w14:paraId="57EC3546" w14:textId="77777777" w:rsidR="00520E7F" w:rsidRDefault="00520E7F"
             w:rsidP="00142614">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
        </w:p>
        ''' % (ls1[0],desc_zydx(ls1[0])[1],desc_zydx(ls1[0])[2],desc_zydx(ls1[0])[3],desc_zydx(ls1[0])[4],desc_zydx(ls1[0])[5])
        s1 = s1 + a

    elif len(ls1) == 2:
        a = '''
         <w:p w14:paraId="57EC3546" w14:textId="77777777" w:rsidR="00520E7F" w:rsidRDefault="00520E7F"
             w:rsidP="00142614">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
        </w:p>
        <w:p w14:paraId="4AF0FCEF" w14:textId="6E2B511A" w:rsidR="00142614" w:rsidRDefault="005E386E"
             w:rsidP="005E386E">
            <w:pPr>
                <w:pStyle w:val="a4"/>
                <w:numPr>
                    <w:ilvl w:val="0"/>
                    <w:numId w:val="8"/>
                </w:numPr>
                <w:snapToGrid w:val="0"/>
                <w:ind w:firstLineChars="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>主导职业锚：</w:t>
            </w:r>
            <w:r w:rsidR="003B3998">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
        </w:p>
        <w:p w14:paraId="4D691D4F" w14:textId="7E5761B6" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="005E386E">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:noProof/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <mc:AlternateContent>
                    <mc:Choice Requires="wps">
                        <w:drawing>
                            <wp:anchor distT="0" distB="0" distL="114300" distR="114300" simplePos="0"
                                       relativeHeight="251675648" behindDoc="0" locked="0" layoutInCell="1"
                                       allowOverlap="1" wp14:anchorId="6FDDADD8" wp14:editId="0F7F2B3E">
                                <wp:simplePos x="0" y="0"/>
                                <wp:positionH relativeFrom="column">
                                    <wp:posOffset>4312</wp:posOffset>
                                </wp:positionH>
                                <wp:positionV relativeFrom="paragraph">
                                    <wp:posOffset>27964</wp:posOffset>
                                </wp:positionV>
                                <wp:extent cx="5296619" cy="0"/>
                                <wp:effectExtent l="0" t="0" r="0" b="0"/>
                                <wp:wrapNone/>
                                <wp:docPr id="13" name="直接连接符 13"/>
                                <wp:cNvGraphicFramePr/>
                                <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
                                    <a:graphicData
                                            uri="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
                                        <wps:wsp>
                                            <wps:cNvCnPr/>
                                            <wps:spPr>
                                                <a:xfrm>
                                                    <a:off x="0" y="0"/>
                                                    <a:ext cx="5296619" cy="0"/>
                                                </a:xfrm>
                                                <a:prstGeom prst="line">
                                                    <a:avLst/>
                                                </a:prstGeom>
                                                <a:ln w="12700">
                                                    <a:solidFill>
                                                        <a:schemeClr val="bg2">
                                                            <a:lumMod val="50000"/>
                                                        </a:schemeClr>
                                                    </a:solidFill>
                                                </a:ln>
                                            </wps:spPr>
                                            <wps:style>
                                                <a:lnRef idx="1">
                                                    <a:schemeClr val="accent1"/>
                                                </a:lnRef>
                                                <a:fillRef idx="0">
                                                    <a:schemeClr val="accent1"/>
                                                </a:fillRef>
                                                <a:effectRef idx="0">
                                                    <a:schemeClr val="accent1"/>
                                                </a:effectRef>
                                                <a:fontRef idx="minor">
                                                    <a:schemeClr val="tx1"/>
                                                </a:fontRef>
                                            </wps:style>
                                            <wps:bodyPr/>
                                        </wps:wsp>
                                    </a:graphicData>
                                </a:graphic>
                            </wp:anchor>
                        </w:drawing>
                    </mc:Choice>
                    <mc:Fallback>
                        <w:pict>
                            <v:line w14:anchorId="42E2299B" id="直接连接符 13" o:spid="_x0000_s1026"
                                    style="position:absolute;left:0;text-align:left;z-index:251675648;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text"
                                    from=".35pt,2.2pt" to="417.4pt,2.2pt"
                                    o:gfxdata="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&#xA;"
                                    strokecolor="#747070 [1614]" strokeweight="1pt">
                                <v:stroke joinstyle="miter"/>
                            </v:line>
                        </w:pict>
                    </mc:Fallback>
                </mc:AlternateContent>
            </w:r>
        </w:p>
        <w:p w14:paraId="020E4E27" w14:textId="275D75F3" w:rsidR="005E386E" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="003A4C48">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
        </w:p>


        <w:p w14:paraId="06DCE1F9" w14:textId="1B757E76" w:rsidR="00F968E2" w:rsidRPr="005E386E"
             w:rsidRDefault="005E386E" w:rsidP="005E386E">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>工作类型</w:t>
            </w:r>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>:%s</w:t>
            </w:r>


        </w:p>

        <w:p w14:paraId="45B5540F" w14:textId="6A41CF20" w:rsidR="00F968E2" w:rsidRPr="00DF5704"
             w:rsidRDefault="005E386E" w:rsidP="005E386E">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>薪酬福利</w:t>
            </w:r>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>:%s</w:t>
            </w:r>

        </w:p>
        <w:p w14:paraId="66923C5D" w14:textId="274B4461" w:rsidR="00BF60AD" w:rsidRPr="00DF5704"
             w:rsidRDefault="005E386E" w:rsidP="005E386E">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>工作晋升</w:t>
            </w:r>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r w:rsidR="00031A2A">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
        </w:p>
        <w:p w14:paraId="3F7C0DD7" w14:textId="7F02724E" w:rsidR="008515B4" w:rsidRDefault="005E386E"
             w:rsidP="00142614">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>最佳认可方式</w:t>
            </w:r>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r w:rsidR="00031A2A">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>

        </w:p>
        ''' % (ls1[0], desc_zydx(ls1[0])[1], desc_zydx(ls1[0])[2], desc_zydx(ls1[0])[3], desc_zydx(ls1[0])[4],
               desc_zydx(ls1[0])[5])

        b = '''<w:p w14:paraId="3B235633" w14:textId="5BFF7D16" w:rsidR="00406AA1" w:rsidRDefault="00406AA1"
             w:rsidP="00406AA1">
            <w:pPr>
                <w:pStyle w:val="a4"/>
                <w:numPr>
                    <w:ilvl w:val="0"/>
                    <w:numId w:val="8"/>
                </w:numPr>
                <w:snapToGrid w:val="0"/>
                <w:ind w:firstLineChars="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>主导职业锚：</w:t>
            </w:r>
            <w:r w:rsidR="003B3998">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
        </w:p>
        <w:p w14:paraId="55AEAF84" w14:textId="77777777" w:rsidR="00406AA1" w:rsidRPr="005E386E"
             w:rsidRDefault="00406AA1" w:rsidP="00406AA1">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:noProof/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <mc:AlternateContent>
                    <mc:Choice Requires="wps">
                        <w:drawing>
                            <wp:anchor distT="0" distB="0" distL="114300" distR="114300" simplePos="0"
                                       relativeHeight="251684864" behindDoc="0" locked="0" layoutInCell="1"
                                       allowOverlap="1" wp14:anchorId="2539BF30" wp14:editId="33685E65">
                                <wp:simplePos x="0" y="0"/>
                                <wp:positionH relativeFrom="column">
                                    <wp:posOffset>4312</wp:posOffset>
                                </wp:positionH>
                                <wp:positionV relativeFrom="paragraph">
                                    <wp:posOffset>27964</wp:posOffset>
                                </wp:positionV>
                                <wp:extent cx="5296619" cy="0"/>
                                <wp:effectExtent l="0" t="0" r="0" b="0"/>
                                <wp:wrapNone/>
                                <wp:docPr id="19" name="直接连接符 19"/>
                                <wp:cNvGraphicFramePr/>
                                <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
                                    <a:graphicData
                                            uri="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
                                        <wps:wsp>
                                            <wps:cNvCnPr/>
                                            <wps:spPr>
                                                <a:xfrm>
                                                    <a:off x="0" y="0"/>
                                                    <a:ext cx="5296619" cy="0"/>
                                                </a:xfrm>
                                                <a:prstGeom prst="line">
                                                    <a:avLst/>
                                                </a:prstGeom>
                                                <a:ln w="12700">
                                                    <a:solidFill>
                                                        <a:schemeClr val="bg2">
                                                            <a:lumMod val="50000"/>
                                                        </a:schemeClr>
                                                    </a:solidFill>
                                                </a:ln>
                                            </wps:spPr>
                                            <wps:style>
                                                <a:lnRef idx="1">
                                                    <a:schemeClr val="accent1"/>
                                                </a:lnRef>
                                                <a:fillRef idx="0">
                                                    <a:schemeClr val="accent1"/>
                                                </a:fillRef>
                                                <a:effectRef idx="0">
                                                    <a:schemeClr val="accent1"/>
                                                </a:effectRef>
                                                <a:fontRef idx="minor">
                                                    <a:schemeClr val="tx1"/>
                                                </a:fontRef>
                                            </wps:style>
                                            <wps:bodyPr/>
                                        </wps:wsp>
                                    </a:graphicData>
                                </a:graphic>
                            </wp:anchor>
                        </w:drawing>
                    </mc:Choice>
                    <mc:Fallback>
                        <w:pict>
                            <v:line w14:anchorId="1DF71DED" id="直接连接符 19" o:spid="_x0000_s1026"
                                    style="position:absolute;left:0;text-align:left;z-index:251684864;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text"
                                    from=".35pt,2.2pt" to="417.4pt,2.2pt"
                                    o:gfxdata="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&#xA;"
                                    strokecolor="#747070 [1614]" strokeweight="1pt">
                                <v:stroke joinstyle="miter"/>
                            </v:line>
                        </w:pict>
                    </mc:Fallback>
                </mc:AlternateContent>
            </w:r>
        </w:p>
        <w:p w14:paraId="299039F7" w14:textId="77777777" w:rsidR="00406AA1" w:rsidRPr="005E386E"
             w:rsidRDefault="00406AA1" w:rsidP="00406AA1">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
           
        </w:p>
       
        <w:p w14:paraId="3A1F798E" w14:textId="77777777" w:rsidR="00406AA1" w:rsidRPr="005E386E"
             w:rsidRDefault="00406AA1" w:rsidP="00406AA1">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>工作类型</w:t>
            </w:r>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>:%s</w:t>
            </w:r>
            
        </w:p>
        <w:p w14:paraId="648721E4" w14:textId="77777777" w:rsidR="00406AA1" w:rsidRPr="00DF5704"
             w:rsidRDefault="00406AA1" w:rsidP="00406AA1">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>薪酬福利</w:t>
            </w:r>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>:%s</w:t>
            </w:r>
           
        </w:p>
        <w:p w14:paraId="2F2C087D" w14:textId="77777777" w:rsidR="00406AA1" w:rsidRPr="00DF5704"
             w:rsidRDefault="00406AA1" w:rsidP="00406AA1">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>工作晋升</w:t>
            </w:r>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
            
        </w:p>
        <w:p w14:paraId="72AE804C" w14:textId="77777777" w:rsidR="00F50CE2" w:rsidRDefault="00406AA1"
             w:rsidP="00406AA1">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>最佳认可方式</w:t>
            </w:r>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
          
        </w:p>''' % (ls1[1], desc_zydx(ls1[1])[1], desc_zydx(ls1[1])[2], desc_zydx(ls1[1])[3], desc_zydx(ls1[1])[4],
               desc_zydx(ls1[1])[5])
        s1 = s1 + a + b
    else:
        a = '''
         <w:p w14:paraId="57EC3546" w14:textId="77777777" w:rsidR="00520E7F" w:rsidRDefault="00520E7F"
             w:rsidP="00142614">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
        </w:p>
        <w:p w14:paraId="4AF0FCEF" w14:textId="6E2B511A" w:rsidR="00142614" w:rsidRDefault="005E386E"
                     w:rsidP="005E386E">
                    <w:pPr>
                        <w:pStyle w:val="a4"/>
                        <w:numPr>
                            <w:ilvl w:val="0"/>
                            <w:numId w:val="8"/>
                        </w:numPr>
                        <w:snapToGrid w:val="0"/>
                        <w:ind w:firstLineChars="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>主导职业锚：</w:t>
                    </w:r>
                    <w:r w:rsidR="003B3998">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>
                </w:p>
                <w:p w14:paraId="4D691D4F" w14:textId="7E5761B6" w:rsidR="005E386E" w:rsidRPr="005E386E"
                     w:rsidRDefault="005E386E" w:rsidP="005E386E">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:noProof/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <mc:AlternateContent>
                            <mc:Choice Requires="wps">
                                <w:drawing>
                                    <wp:anchor distT="0" distB="0" distL="114300" distR="114300" simplePos="0"
                                               relativeHeight="251675648" behindDoc="0" locked="0" layoutInCell="1"
                                               allowOverlap="1" wp14:anchorId="6FDDADD8" wp14:editId="0F7F2B3E">
                                        <wp:simplePos x="0" y="0"/>
                                        <wp:positionH relativeFrom="column">
                                            <wp:posOffset>4312</wp:posOffset>
                                        </wp:positionH>
                                        <wp:positionV relativeFrom="paragraph">
                                            <wp:posOffset>27964</wp:posOffset>
                                        </wp:positionV>
                                        <wp:extent cx="5296619" cy="0"/>
                                        <wp:effectExtent l="0" t="0" r="0" b="0"/>
                                        <wp:wrapNone/>
                                        <wp:docPr id="13" name="直接连接符 13"/>
                                        <wp:cNvGraphicFramePr/>
                                        <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
                                            <a:graphicData
                                                    uri="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
                                                <wps:wsp>
                                                    <wps:cNvCnPr/>
                                                    <wps:spPr>
                                                        <a:xfrm>
                                                            <a:off x="0" y="0"/>
                                                            <a:ext cx="5296619" cy="0"/>
                                                        </a:xfrm>
                                                        <a:prstGeom prst="line">
                                                            <a:avLst/>
                                                        </a:prstGeom>
                                                        <a:ln w="12700">
                                                            <a:solidFill>
                                                                <a:schemeClr val="bg2">
                                                                    <a:lumMod val="50000"/>
                                                                </a:schemeClr>
                                                            </a:solidFill>
                                                        </a:ln>
                                                    </wps:spPr>
                                                    <wps:style>
                                                        <a:lnRef idx="1">
                                                            <a:schemeClr val="accent1"/>
                                                        </a:lnRef>
                                                        <a:fillRef idx="0">
                                                            <a:schemeClr val="accent1"/>
                                                        </a:fillRef>
                                                        <a:effectRef idx="0">
                                                            <a:schemeClr val="accent1"/>
                                                        </a:effectRef>
                                                        <a:fontRef idx="minor">
                                                            <a:schemeClr val="tx1"/>
                                                        </a:fontRef>
                                                    </wps:style>
                                                    <wps:bodyPr/>
                                                </wps:wsp>
                                            </a:graphicData>
                                        </a:graphic>
                                    </wp:anchor>
                                </w:drawing>
                            </mc:Choice>
                            <mc:Fallback>
                                <w:pict>
                                    <v:line w14:anchorId="42E2299B" id="直接连接符 13" o:spid="_x0000_s1026"
                                            style="position:absolute;left:0;text-align:left;z-index:251675648;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text"
                                            from=".35pt,2.2pt" to="417.4pt,2.2pt"
                                            o:gfxdata="UEsDBBQABgAIAAAAIQC2gziS/gAAAOEBAAATAAAAW0NvbnRlbnRfVHlwZXNdLnhtbJSRQU7DMBBF&#xA;90jcwfIWJU67QAgl6YK0S0CoHGBkTxKLZGx5TGhvj5O2G0SRWNoz/78nu9wcxkFMGNg6quQqL6RA&#xA;0s5Y6ir5vt9lD1JwBDIwOMJKHpHlpr69KfdHjyxSmriSfYz+USnWPY7AufNIadK6MEJMx9ApD/oD&#xA;OlTrorhX2lFEilmcO2RdNtjC5xDF9pCuTyYBB5bi6bQ4syoJ3g9WQ0ymaiLzg5KdCXlKLjvcW893&#xA;SUOqXwnz5DrgnHtJTxOsQfEKIT7DmDSUCaxw7Rqn8787ZsmRM9e2VmPeBN4uqYvTtW7jvijg9N/y&#xA;JsXecLq0q+WD6m8AAAD//wMAUEsDBBQABgAIAAAAIQA4/SH/1gAAAJQBAAALAAAAX3JlbHMvLnJl&#xA;bHOkkMFqwzAMhu+DvYPRfXGawxijTi+j0GvpHsDYimMaW0Yy2fr2M4PBMnrbUb/Q94l/f/hMi1qR&#xA;JVI2sOt6UJgd+ZiDgffL8ekFlFSbvV0oo4EbChzGx4f9GRdb25HMsYhqlCwG5lrLq9biZkxWOiqY&#xA;22YiTra2kYMu1l1tQD30/bPm3wwYN0x18gb45AdQl1tp5j/sFB2T0FQ7R0nTNEV3j6o9feQzro1i&#xA;OWA14Fm+Q8a1a8+Bvu/d/dMb2JY5uiPbhG/ktn4cqGU/er3pcvwCAAD//wMAUEsDBBQABgAIAAAA&#xA;IQAfKe3k+QEAADAEAAAOAAAAZHJzL2Uyb0RvYy54bWysU8uO0zAU3SPxD5b3NGnRFCZqOosZDRse&#xA;FTAf4DrXjSW/ZHua9Cf4ASR2sGLJnr9h+AyunTQdAUICkYVj3+c5x9eri14rsgcfpDU1nc9KSsBw&#xA;20izq+nN2+tHTykJkZmGKWugpgcI9GL98MGqcxUsbGtVA55gEROqztW0jdFVRRF4C5qFmXVg0Cms&#xA;1yzi0e+KxrMOq2tVLMpyWXTWN85bDiGg9Wpw0nWuLwTw+EqIAJGomiK2mFef121ai/WKVTvPXCv5&#xA;CIP9AwrNpMGmU6krFhm59fKXUlpyb4MVccatLqwQkkPmgGzm5U9s3rTMQeaC4gQ3yRT+X1n+cr/x&#xA;RDZ4d48pMUzjHd29//Lt3cfvXz/gevf5E0EPytS5UGH0pdn48RTcxifOvfA6/ZEN6bO0h0la6CPh&#xA;aDxbnC+X83NK+NFXnBKdD/EZWE3SpqZKmsSaVWz/PERshqHHkGRWhnSId/GkLHNYsEo211Kp5MyT&#xA;A5fKkz3DO9/uFjlG3eoXthlsZyV+iRLWncKH06kS+pRBY6I9EM27eFAwYHgNAnVDavMBRJrYU1/G&#xA;OZg4H7sog9EpTSDKKXFE/6fEMT6lQp7mv0meMnJna+KUrKWx/newY3+ELIb4owID7yTB1jaHPAJZ&#xA;GhzLrNz4hNLc3z/n9NNDX/8AAAD//wMAUEsDBBQABgAIAAAAIQCxJ3xP2gAAAAQBAAAPAAAAZHJz&#xA;L2Rvd25yZXYueG1sTI/BbsIwEETvlfgHa5G4FYc2CiiNg1ArDqg9tLQfYOIlCcTryDYh/ftueynH&#xA;0Yxm3hTr0XZiQB9aRwoW8wQEUuVMS7WCr8/t/QpEiJqM7hyhgm8MsC4nd4XOjbvSBw77WAsuoZBr&#xA;BU2MfS5lqBq0Osxdj8Te0XmrI0tfS+P1lcttJx+SJJNWt8QLje7xucHqvL9YBdniZE9DX7+/Vdvd&#xA;q8mOPsSXpVKz6bh5AhFxjP9h+MVndCiZ6eAuZILoFCw5pyBNQbC5ekz5x+FPy7KQt/DlDwAAAP//&#xA;AwBQSwECLQAUAAYACAAAACEAtoM4kv4AAADhAQAAEwAAAAAAAAAAAAAAAAAAAAAAW0NvbnRlbnRf&#xA;VHlwZXNdLnhtbFBLAQItABQABgAIAAAAIQA4/SH/1gAAAJQBAAALAAAAAAAAAAAAAAAAAC8BAABf&#xA;cmVscy8ucmVsc1BLAQItABQABgAIAAAAIQAfKe3k+QEAADAEAAAOAAAAAAAAAAAAAAAAAC4CAABk&#xA;cnMvZTJvRG9jLnhtbFBLAQItABQABgAIAAAAIQCxJ3xP2gAAAAQBAAAPAAAAAAAAAAAAAAAAAFME&#xA;AABkcnMvZG93bnJldi54bWxQSwUGAAAAAAQABADzAAAAWgUAAAAA&#xA;"
                                            strokecolor="#747070 [1614]" strokeweight="1pt">
                                        <v:stroke joinstyle="miter"/>
                                    </v:line>
                                </w:pict>
                            </mc:Fallback>
                        </mc:AlternateContent>
                    </w:r>
                </w:p>
                <w:p w14:paraId="020E4E27" w14:textId="275D75F3" w:rsidR="005E386E" w:rsidRPr="005E386E"
                     w:rsidRDefault="005E386E" w:rsidP="003A4C48">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:spacing w:afterLines="50" w:after="156"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>
                </w:p>


                <w:p w14:paraId="06DCE1F9" w14:textId="1B757E76" w:rsidR="00F968E2" w:rsidRPr="005E386E"
                     w:rsidRDefault="005E386E" w:rsidP="005E386E">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>工作类型</w:t>
                    </w:r>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>:%s</w:t>
                    </w:r>


                </w:p>

                <w:p w14:paraId="45B5540F" w14:textId="6A41CF20" w:rsidR="00F968E2" w:rsidRPr="00DF5704"
                     w:rsidRDefault="005E386E" w:rsidP="005E386E">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>薪酬福利</w:t>
                    </w:r>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>:%s</w:t>
                    </w:r>

                </w:p>
                <w:p w14:paraId="66923C5D" w14:textId="274B4461" w:rsidR="00BF60AD" w:rsidRPr="00DF5704"
                     w:rsidRDefault="005E386E" w:rsidP="005E386E">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>工作晋升</w:t>
                    </w:r>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>：</w:t>
                    </w:r>
                    <w:r w:rsidR="00031A2A">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>
                </w:p>
                <w:p w14:paraId="3F7C0DD7" w14:textId="7F02724E" w:rsidR="008515B4" w:rsidRDefault="005E386E"
                     w:rsidP="00142614">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>最佳认可方式</w:t>
                    </w:r>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>：</w:t>
                    </w:r>
                    <w:r w:rsidR="00031A2A">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>

                </w:p>
                ''' % (ls1[0], desc_zydx(ls1[0])[1], desc_zydx(ls1[0])[2], desc_zydx(ls1[0])[3], desc_zydx(ls1[0])[4],
                       desc_zydx(ls1[0])[5])

        b = '''<w:p w14:paraId="3B235633" w14:textId="5BFF7D16" w:rsidR="00406AA1" w:rsidRDefault="00406AA1"
                     w:rsidP="00406AA1">
                    <w:pPr>
                        <w:pStyle w:val="a4"/>
                        <w:numPr>
                            <w:ilvl w:val="0"/>
                            <w:numId w:val="8"/>
                        </w:numPr>
                        <w:snapToGrid w:val="0"/>
                        <w:ind w:firstLineChars="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>主导职业锚：</w:t>
                    </w:r>
                    <w:r w:rsidR="003B3998">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>
                </w:p>
                <w:p w14:paraId="55AEAF84" w14:textId="77777777" w:rsidR="00406AA1" w:rsidRPr="005E386E"
                     w:rsidRDefault="00406AA1" w:rsidP="00406AA1">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:noProof/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <mc:AlternateContent>
                            <mc:Choice Requires="wps">
                                <w:drawing>
                                    <wp:anchor distT="0" distB="0" distL="114300" distR="114300" simplePos="0"
                                               relativeHeight="251684864" behindDoc="0" locked="0" layoutInCell="1"
                                               allowOverlap="1" wp14:anchorId="2539BF30" wp14:editId="33685E65">
                                        <wp:simplePos x="0" y="0"/>
                                        <wp:positionH relativeFrom="column">
                                            <wp:posOffset>4312</wp:posOffset>
                                        </wp:positionH>
                                        <wp:positionV relativeFrom="paragraph">
                                            <wp:posOffset>27964</wp:posOffset>
                                        </wp:positionV>
                                        <wp:extent cx="5296619" cy="0"/>
                                        <wp:effectExtent l="0" t="0" r="0" b="0"/>
                                        <wp:wrapNone/>
                                        <wp:docPr id="19" name="直接连接符 19"/>
                                        <wp:cNvGraphicFramePr/>
                                        <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
                                            <a:graphicData
                                                    uri="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
                                                <wps:wsp>
                                                    <wps:cNvCnPr/>
                                                    <wps:spPr>
                                                        <a:xfrm>
                                                            <a:off x="0" y="0"/>
                                                            <a:ext cx="5296619" cy="0"/>
                                                        </a:xfrm>
                                                        <a:prstGeom prst="line">
                                                            <a:avLst/>
                                                        </a:prstGeom>
                                                        <a:ln w="12700">
                                                            <a:solidFill>
                                                                <a:schemeClr val="bg2">
                                                                    <a:lumMod val="50000"/>
                                                                </a:schemeClr>
                                                            </a:solidFill>
                                                        </a:ln>
                                                    </wps:spPr>
                                                    <wps:style>
                                                        <a:lnRef idx="1">
                                                            <a:schemeClr val="accent1"/>
                                                        </a:lnRef>
                                                        <a:fillRef idx="0">
                                                            <a:schemeClr val="accent1"/>
                                                        </a:fillRef>
                                                        <a:effectRef idx="0">
                                                            <a:schemeClr val="accent1"/>
                                                        </a:effectRef>
                                                        <a:fontRef idx="minor">
                                                            <a:schemeClr val="tx1"/>
                                                        </a:fontRef>
                                                    </wps:style>
                                                    <wps:bodyPr/>
                                                </wps:wsp>
                                            </a:graphicData>
                                        </a:graphic>
                                    </wp:anchor>
                                </w:drawing>
                            </mc:Choice>
                            <mc:Fallback>
                                <w:pict>
                                    <v:line w14:anchorId="1DF71DED" id="直接连接符 19" o:spid="_x0000_s1026"
                                            style="position:absolute;left:0;text-align:left;z-index:251684864;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text"
                                            from=".35pt,2.2pt" to="417.4pt,2.2pt"
                                            o:gfxdata="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&#xA;"
                                            strokecolor="#747070 [1614]" strokeweight="1pt">
                                        <v:stroke joinstyle="miter"/>
                                    </v:line>
                                </w:pict>
                            </mc:Fallback>
                        </mc:AlternateContent>
                    </w:r>
                </w:p>
                <w:p w14:paraId="299039F7" w14:textId="77777777" w:rsidR="00406AA1" w:rsidRPr="005E386E"
                     w:rsidRDefault="00406AA1" w:rsidP="00406AA1">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:spacing w:afterLines="50" w:after="156"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>

                </w:p>

                <w:p w14:paraId="3A1F798E" w14:textId="77777777" w:rsidR="00406AA1" w:rsidRPr="005E386E"
                     w:rsidRDefault="00406AA1" w:rsidP="00406AA1">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>工作类型</w:t>
                    </w:r>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>:%s</w:t>
                    </w:r>

                </w:p>
                <w:p w14:paraId="648721E4" w14:textId="77777777" w:rsidR="00406AA1" w:rsidRPr="00DF5704"
                     w:rsidRDefault="00406AA1" w:rsidP="00406AA1">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>薪酬福利</w:t>
                    </w:r>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>:%s</w:t>
                    </w:r>

                </w:p>
                <w:p w14:paraId="2F2C087D" w14:textId="77777777" w:rsidR="00406AA1" w:rsidRPr="00DF5704"
                     w:rsidRDefault="00406AA1" w:rsidP="00406AA1">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>工作晋升</w:t>
                    </w:r>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>：</w:t>
                    </w:r>
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>

                </w:p>
                <w:p w14:paraId="72AE804C" w14:textId="77777777" w:rsidR="00F50CE2" w:rsidRDefault="00406AA1"
                     w:rsidP="00406AA1">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>最佳认可方式</w:t>
                    </w:r>
                    <w:r w:rsidRPr="005E386E">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>：</w:t>
                    </w:r>
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>

                </w:p>''' % (ls1[1], desc_zydx(ls1[1])[1], desc_zydx(ls1[1])[2], desc_zydx(ls1[1])[3], desc_zydx(ls1[1])[4],
               desc_zydx(ls1[1])[5])
        c = '''<w:p w14:paraId="2B7CE35D" w14:textId="0DA919E4" w:rsidR="00F50CE2" w:rsidRDefault="00F50CE2"
             w:rsidP="00F50CE2">
            <w:pPr>
                <w:pStyle w:val="a4"/>
                <w:numPr>
                    <w:ilvl w:val="0"/>
                    <w:numId w:val="8"/>
                </w:numPr>
                <w:snapToGrid w:val="0"/>
                <w:ind w:firstLineChars="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>主导职业锚：</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
        </w:p>
        <w:p w14:paraId="712B3515" w14:textId="77777777" w:rsidR="00F50CE2" w:rsidRPr="005E386E"
             w:rsidRDefault="00F50CE2" w:rsidP="00F50CE2">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:noProof/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <mc:AlternateContent>
                    <mc:Choice Requires="wps">
                        <w:drawing>
                            <wp:anchor distT="0" distB="0" distL="114300" distR="114300" simplePos="0"
                                       relativeHeight="251730944" behindDoc="0" locked="0" layoutInCell="1"
                                       allowOverlap="1" wp14:anchorId="48832C2F" wp14:editId="6B42E196">
                                <wp:simplePos x="0" y="0"/>
                                <wp:positionH relativeFrom="column">
                                    <wp:posOffset>4312</wp:posOffset>
                                </wp:positionH>
                                <wp:positionV relativeFrom="paragraph">
                                    <wp:posOffset>27964</wp:posOffset>
                                </wp:positionV>
                                <wp:extent cx="5296619" cy="0"/>
                                <wp:effectExtent l="0" t="0" r="0" b="0"/>
                                <wp:wrapNone/>
                                <wp:docPr id="15" name="直接连接符 15"/>
                                <wp:cNvGraphicFramePr/>
                                <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
                                    <a:graphicData
                                            uri="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
                                        <wps:wsp>
                                            <wps:cNvCnPr/>
                                            <wps:spPr>
                                                <a:xfrm>
                                                    <a:off x="0" y="0"/>
                                                    <a:ext cx="5296619" cy="0"/>
                                                </a:xfrm>
                                                <a:prstGeom prst="line">
                                                    <a:avLst/>
                                                </a:prstGeom>
                                                <a:ln w="12700">
                                                    <a:solidFill>
                                                        <a:schemeClr val="bg2">
                                                            <a:lumMod val="50000"/>
                                                        </a:schemeClr>
                                                    </a:solidFill>
                                                </a:ln>
                                            </wps:spPr>
                                            <wps:style>
                                                <a:lnRef idx="1">
                                                    <a:schemeClr val="accent1"/>
                                                </a:lnRef>
                                                <a:fillRef idx="0">
                                                    <a:schemeClr val="accent1"/>
                                                </a:fillRef>
                                                <a:effectRef idx="0">
                                                    <a:schemeClr val="accent1"/>
                                                </a:effectRef>
                                                <a:fontRef idx="minor">
                                                    <a:schemeClr val="tx1"/>
                                                </a:fontRef>
                                            </wps:style>
                                            <wps:bodyPr/>
                                        </wps:wsp>
                                    </a:graphicData>
                                </a:graphic>
                            </wp:anchor>
                        </w:drawing>
                    </mc:Choice>
                    <mc:Fallback>
                        <w:pict>
                            <v:line w14:anchorId="09291D50" id="直接连接符 15" o:spid="_x0000_s1026"
                                    style="position:absolute;left:0;text-align:left;z-index:251730944;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text"
                                    from=".35pt,2.2pt" to="417.4pt,2.2pt"
                                    o:gfxdata="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&#xA;"
                                    strokecolor="#747070 [1614]" strokeweight="1pt">
                                <v:stroke joinstyle="miter"/>
                            </v:line>
                        </w:pict>
                    </mc:Fallback>
                </mc:AlternateContent>
            </w:r>
        </w:p>
        <w:p w14:paraId="21A05FB7" w14:textId="77777777" w:rsidR="00F50CE2" w:rsidRPr="005E386E"
             w:rsidRDefault="00F50CE2" w:rsidP="00F50CE2">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
            
        </w:p>
     
        <w:p w14:paraId="52E2E27F" w14:textId="77777777" w:rsidR="00F50CE2" w:rsidRPr="005E386E"
             w:rsidRDefault="00F50CE2" w:rsidP="00F50CE2">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>工作类型</w:t>
            </w:r>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>:%s</w:t>
            </w:r>
            
        </w:p>
        <w:p w14:paraId="65180989" w14:textId="77777777" w:rsidR="00F50CE2" w:rsidRPr="00DF5704"
             w:rsidRDefault="00F50CE2" w:rsidP="00F50CE2">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>薪酬福利</w:t>
            </w:r>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>:%s</w:t>
            </w:r>
           
        </w:p>
        <w:p w14:paraId="6632C015" w14:textId="77777777" w:rsidR="00F50CE2" w:rsidRPr="00DF5704"
             w:rsidRDefault="00F50CE2" w:rsidP="00F50CE2">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>工作晋升</w:t>
            </w:r>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
            
        </w:p>
        <w:p w14:paraId="43FFD45F" w14:textId="77777777" w:rsidR="00F50CE2" w:rsidRDefault="00F50CE2"
             w:rsidP="00F50CE2">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>最佳认可方式</w:t>
            </w:r>
            <w:r w:rsidRPr="005E386E">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
           
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:br w:type="page"/>
            </w:r>
        </w:p>
''' % (ls1[2], desc_zydx(ls1[2])[1], desc_zydx(ls1[2])[2], desc_zydx(ls1[2])[3], desc_zydx(ls1[2])[4],
               desc_zydx(ls1[2])[5])
        s1 = s1 + a + b + c
    return s1


def fz_desc(ls1):
    '''
    传入类型，返回职业定向描述
    :param ls1: 辅助类型
    :return: 职业定向描述
    '''
    s1 = ''
    if len(ls1) == 1:
        a = '''
         <w:p w14:paraId="57EC3546" w14:textId="77777777" w:rsidR="00520E7F" w:rsidRDefault="00520E7F"
             w:rsidP="00142614">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
        </w:p>
        <w:p w14:paraId="353FBE79" w14:textId="6CB0202D" w:rsidR="003B3998" w:rsidRPr="00E0412D"
             w:rsidRDefault="003B3998" w:rsidP="003B3998">
            <w:pPr>
                <w:pStyle w:val="a4"/>
                <w:numPr>
                    <w:ilvl w:val="0"/>
                    <w:numId w:val="8"/>
                </w:numPr>
                <w:snapToGrid w:val="0"/>
                <w:ind w:firstLineChars="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="00E0412D">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>辅助职业锚：</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
        </w:p>
        <w:p w14:paraId="697AEFE3" w14:textId="77777777" w:rsidR="003B3998" w:rsidRDefault="003B3998"
             w:rsidP="003B3998">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:noProof/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <mc:AlternateContent>
                    <mc:Choice Requires="wps">
                        <w:drawing>
                            <wp:anchor distT="0" distB="0" distL="114300" distR="114300" simplePos="0"
                                       relativeHeight="251705344" behindDoc="0" locked="0" layoutInCell="1"
                                       allowOverlap="1" wp14:anchorId="231C7C0B" wp14:editId="16CF7B34">
                                <wp:simplePos x="0" y="0"/>
                                <wp:positionH relativeFrom="column">
                                    <wp:posOffset>0</wp:posOffset>
                                </wp:positionH>
                                <wp:positionV relativeFrom="paragraph">
                                    <wp:posOffset>16246</wp:posOffset>
                                </wp:positionV>
                                <wp:extent cx="5296619" cy="0"/>
                                <wp:effectExtent l="0" t="0" r="0" b="0"/>
                                <wp:wrapNone/>
                                <wp:docPr id="31" name="直接连接符 31"/>
                                <wp:cNvGraphicFramePr/>
                                <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
                                    <a:graphicData
                                            uri="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
                                        <wps:wsp>
                                            <wps:cNvCnPr/>
                                            <wps:spPr>
                                                <a:xfrm>
                                                    <a:off x="0" y="0"/>
                                                    <a:ext cx="5296619" cy="0"/>
                                                </a:xfrm>
                                                <a:prstGeom prst="line">
                                                    <a:avLst/>
                                                </a:prstGeom>
                                                <a:ln w="12700">
                                                    <a:solidFill>
                                                        <a:schemeClr val="bg2">
                                                            <a:lumMod val="50000"/>
                                                        </a:schemeClr>
                                                    </a:solidFill>
                                                </a:ln>
                                            </wps:spPr>
                                            <wps:style>
                                                <a:lnRef idx="1">
                                                    <a:schemeClr val="accent1"/>
                                                </a:lnRef>
                                                <a:fillRef idx="0">
                                                    <a:schemeClr val="accent1"/>
                                                </a:fillRef>
                                                <a:effectRef idx="0">
                                                    <a:schemeClr val="accent1"/>
                                                </a:effectRef>
                                                <a:fontRef idx="minor">
                                                    <a:schemeClr val="tx1"/>
                                                </a:fontRef>
                                            </wps:style>
                                            <wps:bodyPr/>
                                        </wps:wsp>
                                    </a:graphicData>
                                </a:graphic>
                            </wp:anchor>
                        </w:drawing>
                    </mc:Choice>
                    <mc:Fallback>
                        <w:pict>
                            <v:line w14:anchorId="1E8961D6" id="直接连接符 31" o:spid="_x0000_s1026"
                                    style="position:absolute;left:0;text-align:left;z-index:251705344;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text"
                                    from="0,1.3pt" to="417.05pt,1.3pt"
                                    o:gfxdata="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&#xA;"
                                    strokecolor="#747070 [1614]" strokeweight="1pt">
                                <v:stroke joinstyle="miter"/>
                            </v:line>
                        </w:pict>
                    </mc:Fallback>
                </mc:AlternateContent>
            </w:r>
        </w:p>
        <w:p w14:paraId="2C51BFB1" w14:textId="77777777" w:rsidR="003B3998" w:rsidRPr="004E5ED4"
             w:rsidRDefault="003B3998" w:rsidP="003B3998">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
           
        </w:p>
        
        <w:p w14:paraId="75E0C41F" w14:textId="77777777" w:rsidR="003B3998" w:rsidRPr="004E5ED4"
             w:rsidRDefault="003B3998" w:rsidP="003B3998">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>工作类型</w:t>
            </w:r>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
            
        </w:p>
        <w:p w14:paraId="5C984D07" w14:textId="77777777" w:rsidR="003A1099" w:rsidRDefault="003B3998"
             w:rsidP="003B3998">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>薪酬福利</w:t>
            </w:r>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
           
        </w:p>
        <w:p w14:paraId="46BDF839" w14:textId="7EDF6E52" w:rsidR="003B3998" w:rsidRPr="004E5ED4"
             w:rsidRDefault="003B3998" w:rsidP="003B3998">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>工作晋升</w:t>
            </w:r>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
            
           
        </w:p>
        <w:p w14:paraId="74F2D684" w14:textId="2B530810" w:rsidR="003B3998" w:rsidRPr="003B3998"
             w:rsidRDefault="003B3998" w:rsidP="00F50CE2">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>最佳认可方式</w:t>
            </w:r>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
            
            
        </w:p>''' % (ls1[0], desc_fu(ls1[0])[1], desc_fu(ls1[0])[2], desc_fu(ls1[0])[3], desc_fu(ls1[0])[4],
                     desc_fu(ls1[0])[5])
        s1 = s1 + a

    elif len(ls1) == 2:
        a = '''
         <w:p w14:paraId="57EC3546" w14:textId="77777777" w:rsidR="00520E7F" w:rsidRDefault="00520E7F"
             w:rsidP="00142614">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
        </w:p>
        <w:p w14:paraId="353FBE79" w14:textId="6CB0202D" w:rsidR="003B3998" w:rsidRPr="00E0412D"
                     w:rsidRDefault="003B3998" w:rsidP="003B3998">
                    <w:pPr>
                        <w:pStyle w:val="a4"/>
                        <w:numPr>
                            <w:ilvl w:val="0"/>
                            <w:numId w:val="8"/>
                        </w:numPr>
                        <w:snapToGrid w:val="0"/>
                        <w:ind w:firstLineChars="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="00E0412D">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>辅助职业锚：</w:t>
                    </w:r>
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>
                </w:p>
                <w:p w14:paraId="697AEFE3" w14:textId="77777777" w:rsidR="003B3998" w:rsidRDefault="003B3998"
                     w:rsidP="003B3998">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:noProof/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <mc:AlternateContent>
                            <mc:Choice Requires="wps">
                                <w:drawing>
                                    <wp:anchor distT="0" distB="0" distL="114300" distR="114300" simplePos="0"
                                               relativeHeight="251705344" behindDoc="0" locked="0" layoutInCell="1"
                                               allowOverlap="1" wp14:anchorId="231C7C0B" wp14:editId="16CF7B34">
                                        <wp:simplePos x="0" y="0"/>
                                        <wp:positionH relativeFrom="column">
                                            <wp:posOffset>0</wp:posOffset>
                                        </wp:positionH>
                                        <wp:positionV relativeFrom="paragraph">
                                            <wp:posOffset>16246</wp:posOffset>
                                        </wp:positionV>
                                        <wp:extent cx="5296619" cy="0"/>
                                        <wp:effectExtent l="0" t="0" r="0" b="0"/>
                                        <wp:wrapNone/>
                                        <wp:docPr id="31" name="直接连接符 31"/>
                                        <wp:cNvGraphicFramePr/>
                                        <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
                                            <a:graphicData
                                                    uri="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
                                                <wps:wsp>
                                                    <wps:cNvCnPr/>
                                                    <wps:spPr>
                                                        <a:xfrm>
                                                            <a:off x="0" y="0"/>
                                                            <a:ext cx="5296619" cy="0"/>
                                                        </a:xfrm>
                                                        <a:prstGeom prst="line">
                                                            <a:avLst/>
                                                        </a:prstGeom>
                                                        <a:ln w="12700">
                                                            <a:solidFill>
                                                                <a:schemeClr val="bg2">
                                                                    <a:lumMod val="50000"/>
                                                                </a:schemeClr>
                                                            </a:solidFill>
                                                        </a:ln>
                                                    </wps:spPr>
                                                    <wps:style>
                                                        <a:lnRef idx="1">
                                                            <a:schemeClr val="accent1"/>
                                                        </a:lnRef>
                                                        <a:fillRef idx="0">
                                                            <a:schemeClr val="accent1"/>
                                                        </a:fillRef>
                                                        <a:effectRef idx="0">
                                                            <a:schemeClr val="accent1"/>
                                                        </a:effectRef>
                                                        <a:fontRef idx="minor">
                                                            <a:schemeClr val="tx1"/>
                                                        </a:fontRef>
                                                    </wps:style>
                                                    <wps:bodyPr/>
                                                </wps:wsp>
                                            </a:graphicData>
                                        </a:graphic>
                                    </wp:anchor>
                                </w:drawing>
                            </mc:Choice>
                            <mc:Fallback>
                                <w:pict>
                                    <v:line w14:anchorId="1E8961D6" id="直接连接符 31" o:spid="_x0000_s1026"
                                            style="position:absolute;left:0;text-align:left;z-index:251705344;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text"
                                            from="0,1.3pt" to="417.05pt,1.3pt"
                                            o:gfxdata="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&#xA;"
                                            strokecolor="#747070 [1614]" strokeweight="1pt">
                                        <v:stroke joinstyle="miter"/>
                                    </v:line>
                                </w:pict>
                            </mc:Fallback>
                        </mc:AlternateContent>
                    </w:r>
                </w:p>
                <w:p w14:paraId="2C51BFB1" w14:textId="77777777" w:rsidR="003B3998" w:rsidRPr="004E5ED4"
                     w:rsidRDefault="003B3998" w:rsidP="003B3998">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:spacing w:afterLines="50" w:after="156"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="004E5ED4">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>

                </w:p>

                <w:p w14:paraId="75E0C41F" w14:textId="77777777" w:rsidR="003B3998" w:rsidRPr="004E5ED4"
                     w:rsidRDefault="003B3998" w:rsidP="003B3998">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="004E5ED4">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>工作类型</w:t>
                    </w:r>
                    <w:r w:rsidRPr="004E5ED4">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>：</w:t>
                    </w:r>
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>

                </w:p>
                <w:p w14:paraId="5C984D07" w14:textId="77777777" w:rsidR="003A1099" w:rsidRDefault="003B3998"
                     w:rsidP="003B3998">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="004E5ED4">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>薪酬福利</w:t>
                    </w:r>
                    <w:r w:rsidRPr="004E5ED4">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>：</w:t>
                    </w:r>
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>

                </w:p>
                <w:p w14:paraId="46BDF839" w14:textId="7EDF6E52" w:rsidR="003B3998" w:rsidRPr="004E5ED4"
                     w:rsidRDefault="003B3998" w:rsidP="003B3998">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="004E5ED4">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>工作晋升</w:t>
                    </w:r>
                    <w:r w:rsidRPr="004E5ED4">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>：</w:t>
                    </w:r>
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>


                </w:p>
                <w:p w14:paraId="74F2D684" w14:textId="2B530810" w:rsidR="003B3998" w:rsidRPr="003B3998"
                     w:rsidRDefault="003B3998" w:rsidP="00F50CE2">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="004E5ED4">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>最佳认可方式</w:t>
                    </w:r>
                    <w:r w:rsidRPr="004E5ED4">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>：</w:t>
                    </w:r>
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>


                </w:p>''' % (ls1[0], desc_fu(ls1[0])[1], desc_fu(ls1[0])[2], desc_fu(ls1[0])[3], desc_fu(ls1[0])[4],
                     desc_fu(ls1[0])[5])
        b = '''
         <w:p w14:paraId="57EC3546" w14:textId="77777777" w:rsidR="00520E7F" w:rsidRDefault="00520E7F"
             w:rsidP="00142614">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
        </w:p>
        
        <w:p w14:paraId="7EF78CE3" w14:textId="4DBE7179" w:rsidR="003B3998" w:rsidRPr="00E0412D"
             w:rsidRDefault="003B3998" w:rsidP="003B3998">
            <w:pPr>
                <w:pStyle w:val="a4"/>
                <w:numPr>
                    <w:ilvl w:val="0"/>
                    <w:numId w:val="8"/>
                </w:numPr>
                <w:snapToGrid w:val="0"/>
                <w:ind w:firstLineChars="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="00E0412D">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>辅助职业锚：</w:t>
            </w:r>
            <w:r w:rsidR="003A1099">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
        </w:p>
        <w:p w14:paraId="79E4EDDA" w14:textId="77777777" w:rsidR="003B3998" w:rsidRDefault="003B3998"
             w:rsidP="003B3998">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:noProof/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <mc:AlternateContent>
                    <mc:Choice Requires="wps">
                        <w:drawing>
                            <wp:anchor distT="0" distB="0" distL="114300" distR="114300" simplePos="0"
                                       relativeHeight="251708416" behindDoc="0" locked="0" layoutInCell="1"
                                       allowOverlap="1" wp14:anchorId="0E4E11BE" wp14:editId="640B6DCE">
                                <wp:simplePos x="0" y="0"/>
                                <wp:positionH relativeFrom="column">
                                    <wp:posOffset>0</wp:posOffset>
                                </wp:positionH>
                                <wp:positionV relativeFrom="paragraph">
                                    <wp:posOffset>16246</wp:posOffset>
                                </wp:positionV>
                                <wp:extent cx="5296619" cy="0"/>
                                <wp:effectExtent l="0" t="0" r="0" b="0"/>
                                <wp:wrapNone/>
                                <wp:docPr id="193" name="直接连接符 193"/>
                                <wp:cNvGraphicFramePr/>
                                <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
                                    <a:graphicData
                                            uri="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
                                        <wps:wsp>
                                            <wps:cNvCnPr/>
                                            <wps:spPr>
                                                <a:xfrm>
                                                    <a:off x="0" y="0"/>
                                                    <a:ext cx="5296619" cy="0"/>
                                                </a:xfrm>
                                                <a:prstGeom prst="line">
                                                    <a:avLst/>
                                                </a:prstGeom>
                                                <a:ln w="12700">
                                                    <a:solidFill>
                                                        <a:schemeClr val="bg2">
                                                            <a:lumMod val="50000"/>
                                                        </a:schemeClr>
                                                    </a:solidFill>
                                                </a:ln>
                                            </wps:spPr>
                                            <wps:style>
                                                <a:lnRef idx="1">
                                                    <a:schemeClr val="accent1"/>
                                                </a:lnRef>
                                                <a:fillRef idx="0">
                                                    <a:schemeClr val="accent1"/>
                                                </a:fillRef>
                                                <a:effectRef idx="0">
                                                    <a:schemeClr val="accent1"/>
                                                </a:effectRef>
                                                <a:fontRef idx="minor">
                                                    <a:schemeClr val="tx1"/>
                                                </a:fontRef>
                                            </wps:style>
                                            <wps:bodyPr/>
                                        </wps:wsp>
                                    </a:graphicData>
                                </a:graphic>
                            </wp:anchor>
                        </w:drawing>
                    </mc:Choice>
                    <mc:Fallback>
                        <w:pict>
                            <v:line w14:anchorId="6B81E660" id="直接连接符 193" o:spid="_x0000_s1026"
                                    style="position:absolute;left:0;text-align:left;z-index:251708416;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text"
                                    from="0,1.3pt" to="417.05pt,1.3pt"
                                    o:gfxdata="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&#xA;"
                                    strokecolor="#747070 [1614]" strokeweight="1pt">
                                <v:stroke joinstyle="miter"/>
                            </v:line>
                        </w:pict>
                    </mc:Fallback>
                </mc:AlternateContent>
            </w:r>
        </w:p>
        <w:p w14:paraId="5E85BB1B" w14:textId="77777777" w:rsidR="003B3998" w:rsidRPr="004E5ED4"
             w:rsidRDefault="003B3998" w:rsidP="003B3998">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
            
        </w:p>
        
        <w:p w14:paraId="6ADCA463" w14:textId="77777777" w:rsidR="003B3998" w:rsidRPr="004E5ED4"
             w:rsidRDefault="003B3998" w:rsidP="003B3998">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>工作类型</w:t>
            </w:r>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
            
        </w:p>
        <w:p w14:paraId="2D9B5257" w14:textId="77777777" w:rsidR="003B3998" w:rsidRPr="00DF5704"
             w:rsidRDefault="003B3998" w:rsidP="003B3998">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>薪酬福利</w:t>
            </w:r>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
           
        </w:p>
        <w:p w14:paraId="3AB2AE7E" w14:textId="77777777" w:rsidR="003B3998" w:rsidRPr="004E5ED4"
             w:rsidRDefault="003B3998" w:rsidP="003B3998">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>工作晋升</w:t>
            </w:r>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
            
        </w:p>
        <w:p w14:paraId="64C2D9F3" w14:textId="77777777" w:rsidR="00F50CE2" w:rsidRDefault="003B3998"
             w:rsidP="003A1099">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>最佳认可方式</w:t>
            </w:r>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
            
        </w:p>''' % (ls1[1], desc_fu(ls1[1])[1], desc_fu(ls1[1])[2], desc_fu(ls1[1])[3], desc_fu(ls1[1])[4],
                     desc_fu(ls1[1])[5])
        s1 = s1 + a + b
    else:
        a = '''
         <w:p w14:paraId="57EC3546" w14:textId="77777777" w:rsidR="00520E7F" w:rsidRDefault="00520E7F"
             w:rsidP="00142614">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
        </w:p>
        <w:p w14:paraId="353FBE79" w14:textId="6CB0202D" w:rsidR="003B3998" w:rsidRPr="00E0412D"
                             w:rsidRDefault="003B3998" w:rsidP="003B3998">
                            <w:pPr>
                                <w:pStyle w:val="a4"/>
                                <w:numPr>
                                    <w:ilvl w:val="0"/>
                                    <w:numId w:val="8"/>
                                </w:numPr>
                                <w:snapToGrid w:val="0"/>
                                <w:ind w:firstLineChars="0"/>
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                            </w:pPr>
                            <w:r w:rsidRPr="00E0412D">
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                                    <w:b/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                                <w:t>辅助职业锚：</w:t>
                            </w:r>
                            <w:r>
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                                    <w:b/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                                <w:t>%s</w:t>
                            </w:r>
                        </w:p>
                        <w:p w14:paraId="697AEFE3" w14:textId="77777777" w:rsidR="003B3998" w:rsidRDefault="003B3998"
                             w:rsidP="003B3998">
                            <w:pPr>
                                <w:snapToGrid w:val="0"/>
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                            </w:pPr>
                            <w:r>
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                                    <w:b/>
                                    <w:noProof/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                                <mc:AlternateContent>
                                    <mc:Choice Requires="wps">
                                        <w:drawing>
                                            <wp:anchor distT="0" distB="0" distL="114300" distR="114300" simplePos="0"
                                                       relativeHeight="251705344" behindDoc="0" locked="0" layoutInCell="1"
                                                       allowOverlap="1" wp14:anchorId="231C7C0B" wp14:editId="16CF7B34">
                                                <wp:simplePos x="0" y="0"/>
                                                <wp:positionH relativeFrom="column">
                                                    <wp:posOffset>0</wp:posOffset>
                                                </wp:positionH>
                                                <wp:positionV relativeFrom="paragraph">
                                                    <wp:posOffset>16246</wp:posOffset>
                                                </wp:positionV>
                                                <wp:extent cx="5296619" cy="0"/>
                                                <wp:effectExtent l="0" t="0" r="0" b="0"/>
                                                <wp:wrapNone/>
                                                <wp:docPr id="31" name="直接连接符 31"/>
                                                <wp:cNvGraphicFramePr/>
                                                <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
                                                    <a:graphicData
                                                            uri="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
                                                        <wps:wsp>
                                                            <wps:cNvCnPr/>
                                                            <wps:spPr>
                                                                <a:xfrm>
                                                                    <a:off x="0" y="0"/>
                                                                    <a:ext cx="5296619" cy="0"/>
                                                                </a:xfrm>
                                                                <a:prstGeom prst="line">
                                                                    <a:avLst/>
                                                                </a:prstGeom>
                                                                <a:ln w="12700">
                                                                    <a:solidFill>
                                                                        <a:schemeClr val="bg2">
                                                                            <a:lumMod val="50000"/>
                                                                        </a:schemeClr>
                                                                    </a:solidFill>
                                                                </a:ln>
                                                            </wps:spPr>
                                                            <wps:style>
                                                                <a:lnRef idx="1">
                                                                    <a:schemeClr val="accent1"/>
                                                                </a:lnRef>
                                                                <a:fillRef idx="0">
                                                                    <a:schemeClr val="accent1"/>
                                                                </a:fillRef>
                                                                <a:effectRef idx="0">
                                                                    <a:schemeClr val="accent1"/>
                                                                </a:effectRef>
                                                                <a:fontRef idx="minor">
                                                                    <a:schemeClr val="tx1"/>
                                                                </a:fontRef>
                                                            </wps:style>
                                                            <wps:bodyPr/>
                                                        </wps:wsp>
                                                    </a:graphicData>
                                                </a:graphic>
                                            </wp:anchor>
                                        </w:drawing>
                                    </mc:Choice>
                                    <mc:Fallback>
                                        <w:pict>
                                            <v:line w14:anchorId="1E8961D6" id="直接连接符 31" o:spid="_x0000_s1026"
                                                    style="position:absolute;left:0;text-align:left;z-index:251705344;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text"
                                                    from="0,1.3pt" to="417.05pt,1.3pt"
                                                    o:gfxdata="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&#xA;"
                                                    strokecolor="#747070 [1614]" strokeweight="1pt">
                                                <v:stroke joinstyle="miter"/>
                                            </v:line>
                                        </w:pict>
                                    </mc:Fallback>
                                </mc:AlternateContent>
                            </w:r>
                        </w:p>
                        <w:p w14:paraId="2C51BFB1" w14:textId="77777777" w:rsidR="003B3998" w:rsidRPr="004E5ED4"
                             w:rsidRDefault="003B3998" w:rsidP="003B3998">
                            <w:pPr>
                                <w:snapToGrid w:val="0"/>
                                <w:spacing w:afterLines="50" w:after="156"/>
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                            </w:pPr>
                            <w:r w:rsidRPr="004E5ED4">
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                                <w:t>%s</w:t>
                            </w:r>

                        </w:p>

                        <w:p w14:paraId="75E0C41F" w14:textId="77777777" w:rsidR="003B3998" w:rsidRPr="004E5ED4"
                             w:rsidRDefault="003B3998" w:rsidP="003B3998">
                            <w:pPr>
                                <w:snapToGrid w:val="0"/>
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                            </w:pPr>
                            <w:r w:rsidRPr="004E5ED4">
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                                    <w:b/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                                <w:t>工作类型</w:t>
                            </w:r>
                            <w:r w:rsidRPr="004E5ED4">
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                                <w:t>：</w:t>
                            </w:r>
                            <w:r>
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                                <w:t>%s</w:t>
                            </w:r>

                        </w:p>
                        <w:p w14:paraId="5C984D07" w14:textId="77777777" w:rsidR="003A1099" w:rsidRDefault="003B3998"
                             w:rsidP="003B3998">
                            <w:pPr>
                                <w:snapToGrid w:val="0"/>
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                            </w:pPr>
                            <w:r w:rsidRPr="004E5ED4">
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                                    <w:b/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                                <w:t>薪酬福利</w:t>
                            </w:r>
                            <w:r w:rsidRPr="004E5ED4">
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                                <w:t>：</w:t>
                            </w:r>
                            <w:r>
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                                <w:t>%s</w:t>
                            </w:r>

                        </w:p>
                        <w:p w14:paraId="46BDF839" w14:textId="7EDF6E52" w:rsidR="003B3998" w:rsidRPr="004E5ED4"
                             w:rsidRDefault="003B3998" w:rsidP="003B3998">
                            <w:pPr>
                                <w:snapToGrid w:val="0"/>
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                            </w:pPr>
                            <w:r w:rsidRPr="004E5ED4">
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                                    <w:b/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                                <w:t>工作晋升</w:t>
                            </w:r>
                            <w:r w:rsidRPr="004E5ED4">
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                                <w:t>：</w:t>
                            </w:r>
                            <w:r>
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                                <w:t>%s</w:t>
                            </w:r>


                        </w:p>
                        <w:p w14:paraId="74F2D684" w14:textId="2B530810" w:rsidR="003B3998" w:rsidRPr="003B3998"
                             w:rsidRDefault="003B3998" w:rsidP="00F50CE2">
                            <w:pPr>
                                <w:snapToGrid w:val="0"/>
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                            </w:pPr>
                            <w:r w:rsidRPr="004E5ED4">
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                                    <w:b/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                                <w:t>最佳认可方式</w:t>
                            </w:r>
                            <w:r w:rsidRPr="004E5ED4">
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                                <w:t>：</w:t>
                            </w:r>
                            <w:r>
                                <w:rPr>
                                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                                    <w:sz w:val="24"/>
                                    <w:szCs w:val="24"/>
                                </w:rPr>
                                <w:t>%s</w:t>
                            </w:r>


                        </w:p>''' % (ls1[0], desc_fu(ls1[0])[1], desc_fu(ls1[0])[2], desc_fu(ls1[0])[3], desc_fu(ls1[0])[4],
                     desc_fu(ls1[0])[5])
        b = '''
         <w:p w14:paraId="57EC3546" w14:textId="77777777" w:rsidR="00520E7F" w:rsidRDefault="00520E7F"
             w:rsidP="00142614">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
        </w:p>
        <w:p w14:paraId="7EF78CE3" w14:textId="4DBE7179" w:rsidR="003B3998" w:rsidRPr="00E0412D"
                     w:rsidRDefault="003B3998" w:rsidP="003B3998">
                    <w:pPr>
                        <w:pStyle w:val="a4"/>
                        <w:numPr>
                            <w:ilvl w:val="0"/>
                            <w:numId w:val="8"/>
                        </w:numPr>
                        <w:snapToGrid w:val="0"/>
                        <w:ind w:firstLineChars="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="00E0412D">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>辅助职业锚：</w:t>
                    </w:r>
                    <w:r w:rsidR="003A1099">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>
                </w:p>
                <w:p w14:paraId="79E4EDDA" w14:textId="77777777" w:rsidR="003B3998" w:rsidRDefault="003B3998"
                     w:rsidP="003B3998">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:noProof/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <mc:AlternateContent>
                            <mc:Choice Requires="wps">
                                <w:drawing>
                                    <wp:anchor distT="0" distB="0" distL="114300" distR="114300" simplePos="0"
                                               relativeHeight="251708416" behindDoc="0" locked="0" layoutInCell="1"
                                               allowOverlap="1" wp14:anchorId="0E4E11BE" wp14:editId="640B6DCE">
                                        <wp:simplePos x="0" y="0"/>
                                        <wp:positionH relativeFrom="column">
                                            <wp:posOffset>0</wp:posOffset>
                                        </wp:positionH>
                                        <wp:positionV relativeFrom="paragraph">
                                            <wp:posOffset>16246</wp:posOffset>
                                        </wp:positionV>
                                        <wp:extent cx="5296619" cy="0"/>
                                        <wp:effectExtent l="0" t="0" r="0" b="0"/>
                                        <wp:wrapNone/>
                                        <wp:docPr id="193" name="直接连接符 193"/>
                                        <wp:cNvGraphicFramePr/>
                                        <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
                                            <a:graphicData
                                                    uri="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
                                                <wps:wsp>
                                                    <wps:cNvCnPr/>
                                                    <wps:spPr>
                                                        <a:xfrm>
                                                            <a:off x="0" y="0"/>
                                                            <a:ext cx="5296619" cy="0"/>
                                                        </a:xfrm>
                                                        <a:prstGeom prst="line">
                                                            <a:avLst/>
                                                        </a:prstGeom>
                                                        <a:ln w="12700">
                                                            <a:solidFill>
                                                                <a:schemeClr val="bg2">
                                                                    <a:lumMod val="50000"/>
                                                                </a:schemeClr>
                                                            </a:solidFill>
                                                        </a:ln>
                                                    </wps:spPr>
                                                    <wps:style>
                                                        <a:lnRef idx="1">
                                                            <a:schemeClr val="accent1"/>
                                                        </a:lnRef>
                                                        <a:fillRef idx="0">
                                                            <a:schemeClr val="accent1"/>
                                                        </a:fillRef>
                                                        <a:effectRef idx="0">
                                                            <a:schemeClr val="accent1"/>
                                                        </a:effectRef>
                                                        <a:fontRef idx="minor">
                                                            <a:schemeClr val="tx1"/>
                                                        </a:fontRef>
                                                    </wps:style>
                                                    <wps:bodyPr/>
                                                </wps:wsp>
                                            </a:graphicData>
                                        </a:graphic>
                                    </wp:anchor>
                                </w:drawing>
                            </mc:Choice>
                            <mc:Fallback>
                                <w:pict>
                                    <v:line w14:anchorId="6B81E660" id="直接连接符 193" o:spid="_x0000_s1026"
                                            style="position:absolute;left:0;text-align:left;z-index:251708416;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text"
                                            from="0,1.3pt" to="417.05pt,1.3pt"
                                            o:gfxdata="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&#xA;"
                                            strokecolor="#747070 [1614]" strokeweight="1pt">
                                        <v:stroke joinstyle="miter"/>
                                    </v:line>
                                </w:pict>
                            </mc:Fallback>
                        </mc:AlternateContent>
                    </w:r>
                </w:p>
                <w:p w14:paraId="5E85BB1B" w14:textId="77777777" w:rsidR="003B3998" w:rsidRPr="004E5ED4"
                     w:rsidRDefault="003B3998" w:rsidP="003B3998">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:spacing w:afterLines="50" w:after="156"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="004E5ED4">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>

                </w:p>

                <w:p w14:paraId="6ADCA463" w14:textId="77777777" w:rsidR="003B3998" w:rsidRPr="004E5ED4"
                     w:rsidRDefault="003B3998" w:rsidP="003B3998">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="004E5ED4">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>工作类型</w:t>
                    </w:r>
                    <w:r w:rsidRPr="004E5ED4">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>：</w:t>
                    </w:r>
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>

                </w:p>
                <w:p w14:paraId="2D9B5257" w14:textId="77777777" w:rsidR="003B3998" w:rsidRPr="00DF5704"
                     w:rsidRDefault="003B3998" w:rsidP="003B3998">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="004E5ED4">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>薪酬福利</w:t>
                    </w:r>
                    <w:r w:rsidRPr="004E5ED4">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>：</w:t>
                    </w:r>
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>

                </w:p>
                <w:p w14:paraId="3AB2AE7E" w14:textId="77777777" w:rsidR="003B3998" w:rsidRPr="004E5ED4"
                     w:rsidRDefault="003B3998" w:rsidP="003B3998">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="004E5ED4">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>工作晋升</w:t>
                    </w:r>
                    <w:r w:rsidRPr="004E5ED4">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>：</w:t>
                    </w:r>
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>

                </w:p>
                <w:p w14:paraId="64C2D9F3" w14:textId="77777777" w:rsidR="00F50CE2" w:rsidRDefault="003B3998"
                     w:rsidP="003A1099">
                    <w:pPr>
                        <w:snapToGrid w:val="0"/>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                    </w:pPr>
                    <w:r w:rsidRPr="004E5ED4">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:b/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>最佳认可方式</w:t>
                    </w:r>
                    <w:r w:rsidRPr="004E5ED4">
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>：</w:t>
                    </w:r>
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                            <w:sz w:val="24"/>
                            <w:szCs w:val="24"/>
                        </w:rPr>
                        <w:t>%s</w:t>
                    </w:r>

                </w:p>''' % (ls1[1], desc_fu(ls1[1])[1], desc_fu(ls1[1])[2], desc_fu(ls1[1])[3], desc_fu(ls1[1])[4],
                     desc_fu(ls1[1])[5])
        c = '''
         <w:p w14:paraId="57EC3546" w14:textId="77777777" w:rsidR="00520E7F" w:rsidRDefault="00520E7F"
             w:rsidP="00142614">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
        </w:p>
        <w:p w14:paraId="2230251B" w14:textId="73E06D45" w:rsidR="00F50CE2" w:rsidRPr="00E0412D"
             w:rsidRDefault="00F50CE2" w:rsidP="00F50CE2">
            <w:pPr>
                <w:pStyle w:val="a4"/>
                <w:numPr>
                    <w:ilvl w:val="0"/>
                    <w:numId w:val="8"/>
                </w:numPr>
                <w:snapToGrid w:val="0"/>
                <w:ind w:firstLineChars="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="00E0412D">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>辅助职业锚：</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
        </w:p>
        <w:p w14:paraId="2C0C50E1" w14:textId="77777777" w:rsidR="00F50CE2" w:rsidRDefault="00F50CE2"
             w:rsidP="00F50CE2">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:noProof/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <mc:AlternateContent>
                    <mc:Choice Requires="wps">
                        <w:drawing>
                            <wp:anchor distT="0" distB="0" distL="114300" distR="114300" simplePos="0"
                                       relativeHeight="251732992" behindDoc="0" locked="0" layoutInCell="1"
                                       allowOverlap="1" wp14:anchorId="1AF97FF2" wp14:editId="70AE3463">
                                <wp:simplePos x="0" y="0"/>
                                <wp:positionH relativeFrom="column">
                                    <wp:posOffset>0</wp:posOffset>
                                </wp:positionH>
                                <wp:positionV relativeFrom="paragraph">
                                    <wp:posOffset>16246</wp:posOffset>
                                </wp:positionV>
                                <wp:extent cx="5296619" cy="0"/>
                                <wp:effectExtent l="0" t="0" r="0" b="0"/>
                                <wp:wrapNone/>
                                <wp:docPr id="17" name="直接连接符 17"/>
                                <wp:cNvGraphicFramePr/>
                                <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
                                    <a:graphicData
                                            uri="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
                                        <wps:wsp>
                                            <wps:cNvCnPr/>
                                            <wps:spPr>
                                                <a:xfrm>
                                                    <a:off x="0" y="0"/>
                                                    <a:ext cx="5296619" cy="0"/>
                                                </a:xfrm>
                                                <a:prstGeom prst="line">
                                                    <a:avLst/>
                                                </a:prstGeom>
                                                <a:ln w="12700">
                                                    <a:solidFill>
                                                        <a:schemeClr val="bg2">
                                                            <a:lumMod val="50000"/>
                                                        </a:schemeClr>
                                                    </a:solidFill>
                                                </a:ln>
                                            </wps:spPr>
                                            <wps:style>
                                                <a:lnRef idx="1">
                                                    <a:schemeClr val="accent1"/>
                                                </a:lnRef>
                                                <a:fillRef idx="0">
                                                    <a:schemeClr val="accent1"/>
                                                </a:fillRef>
                                                <a:effectRef idx="0">
                                                    <a:schemeClr val="accent1"/>
                                                </a:effectRef>
                                                <a:fontRef idx="minor">
                                                    <a:schemeClr val="tx1"/>
                                                </a:fontRef>
                                            </wps:style>
                                            <wps:bodyPr/>
                                        </wps:wsp>
                                    </a:graphicData>
                                </a:graphic>
                            </wp:anchor>
                        </w:drawing>
                    </mc:Choice>
                    <mc:Fallback>
                        <w:pict>
                            <v:line w14:anchorId="4F4042AA" id="直接连接符 17" o:spid="_x0000_s1026"
                                    style="position:absolute;left:0;text-align:left;z-index:251732992;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text"
                                    from="0,1.3pt" to="417.05pt,1.3pt"
                                    o:gfxdata="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&#xA;"
                                    strokecolor="#747070 [1614]" strokeweight="1pt">
                                <v:stroke joinstyle="miter"/>
                            </v:line>
                        </w:pict>
                    </mc:Fallback>
                </mc:AlternateContent>
            </w:r>
        </w:p>
        <w:p w14:paraId="6F8799EF" w14:textId="77777777" w:rsidR="00F50CE2" w:rsidRPr="004E5ED4"
             w:rsidRDefault="00F50CE2" w:rsidP="00F50CE2">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:spacing w:afterLines="50" w:after="156"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
           
        </w:p>
       
        
        <w:p w14:paraId="0AFA7D3C" w14:textId="77777777" w:rsidR="00F50CE2" w:rsidRPr="004E5ED4"
             w:rsidRDefault="00F50CE2" w:rsidP="00F50CE2">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>工作类型</w:t>
            </w:r>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
          
        </w:p>
        <w:p w14:paraId="46A30ECF" w14:textId="77777777" w:rsidR="00F50CE2" w:rsidRPr="00DF5704"
             w:rsidRDefault="00F50CE2" w:rsidP="00F50CE2">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>薪酬福利</w:t>
            </w:r>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
           
        </w:p>
        <w:p w14:paraId="787BF4E3" w14:textId="77777777" w:rsidR="00F50CE2" w:rsidRPr="004E5ED4"
             w:rsidRDefault="00F50CE2" w:rsidP="00F50CE2">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>工作晋升</w:t>
            </w:r>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
           
            
        </w:p>
        <w:p w14:paraId="0013AFDB" w14:textId="466E9290" w:rsidR="003B3998" w:rsidRPr="003B3998"
             w:rsidRDefault="00F50CE2" w:rsidP="00F50CE2">
            <w:pPr>
                <w:snapToGrid w:val="0"/>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
            </w:pPr>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:b/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>最佳认可方式</w:t>
            </w:r>
            <w:r w:rsidRPr="004E5ED4">
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>：</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
                    <w:sz w:val="24"/>
                    <w:szCs w:val="24"/>
                </w:rPr>
                <w:t>%s</w:t>
            </w:r>
          
            <w:r w:rsidR="003B3998">
                <w:rPr>
                    <w:noProof/>
                </w:rPr>
                <mc:AlternateContent>
                    <mc:Choice Requires="wps">
                        <w:drawing>
                            <wp:anchor distT="0" distB="0" distL="114300" distR="114300" simplePos="0"
                                       relativeHeight="251707392" behindDoc="0" locked="0" layoutInCell="1"
                                       allowOverlap="1" wp14:anchorId="25805FC8" wp14:editId="48E74B28">
                                <wp:simplePos x="0" y="0"/>
                                <wp:positionH relativeFrom="margin">
                                    <wp:posOffset>1341120</wp:posOffset>
                                </wp:positionH>
                                <wp:positionV relativeFrom="paragraph">
                                    <wp:posOffset>-9018270</wp:posOffset>
                                </wp:positionV>
                                <wp:extent cx="2705100" cy="742950"/>
                                <wp:effectExtent l="0" t="0" r="0" b="0"/>
                                <wp:wrapNone/>
                                <wp:docPr id="194" name="矩形 194"/>
                                <wp:cNvGraphicFramePr/>
                                <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
                                    <a:graphicData
                                            uri="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
                                        <wps:wsp>
                                            <wps:cNvSpPr/>
                                            <wps:spPr>
                                                <a:xfrm>
                                                    <a:off x="0" y="0"/>
                                                    <a:ext cx="2705100" cy="742950"/>
                                                </a:xfrm>
                                                <a:prstGeom prst="rect">
                                                    <a:avLst/>
                                                </a:prstGeom>
                                                <a:solidFill>
                                                    <a:schemeClr val="accent5">
                                                        <a:lumMod val="75000"/>
                                                    </a:schemeClr>
                                                </a:solidFill>
                                                <a:ln>
                                                    <a:noFill/>
                                                </a:ln>
                                            </wps:spPr>
                                            <wps:style>
                                                <a:lnRef idx="2">
                                                    <a:schemeClr val="accent1">
                                                        <a:shade val="50000"/>
                                                    </a:schemeClr>
                                                </a:lnRef>
                                                <a:fillRef idx="1">
                                                    <a:schemeClr val="accent1"/>
                                                </a:fillRef>
                                                <a:effectRef idx="0">
                                                    <a:schemeClr val="accent1"/>
                                                </a:effectRef>
                                                <a:fontRef idx="minor">
                                                    <a:schemeClr val="lt1"/>
                                                </a:fontRef>
                                            </wps:style>
                                            <wps:txbx>
                                                <w:txbxContent>
                                                    <w:p w14:paraId="5AAE99C4" w14:textId="77777777" w:rsidR="003B3998"
                                                         w:rsidRPr="00E30B06" w:rsidRDefault="003B3998"
                                                         w:rsidP="003B3998">
                                                        <w:pPr>
                                                            <w:jc w:val="center"/>
                                                            <w:rPr>
                                                                <w:rFonts w:ascii="宋体" w:eastAsia="宋体" w:hAnsi="宋体"/>
                                                                <w:b/>
                                                                <w:sz w:val="72"/>
                                                                <w:szCs w:val="72"/>
                                                            </w:rPr>
                                                        </w:pPr>
                                                        <w:r>
                                                            <w:rPr>
                                                                <w:rFonts w:ascii="宋体" w:eastAsia="宋体" w:hAnsi="宋体"
                                                                          w:hint="eastAsia"/>
                                                                <w:b/>
                                                                <w:sz w:val="72"/>
                                                                <w:szCs w:val="72"/>
                                                            </w:rPr>
                                                            <w:t>测评结果</w:t>
                                                        </w:r>
                                                    </w:p>
                                                </w:txbxContent>
                                            </wps:txbx>
                                            <wps:bodyPr rot="0" spcFirstLastPara="0" vertOverflow="overflow"
                                                        horzOverflow="overflow" vert="horz" wrap="square" lIns="91440"
                                                        tIns="45720" rIns="91440" bIns="45720" numCol="1" spcCol="0"
                                                        rtlCol="0" fromWordArt="0" anchor="ctr" anchorCtr="0"
                                                        forceAA="0" compatLnSpc="1">
                                                <a:prstTxWarp prst="textNoShape">
                                                    <a:avLst/>
                                                </a:prstTxWarp>
                                                <a:noAutofit/>
                                            </wps:bodyPr>
                                        </wps:wsp>
                                    </a:graphicData>
                                </a:graphic>
                            </wp:anchor>
                        </w:drawing>
                    </mc:Choice>
                    <mc:Fallback>
                        <w:pict>
                            <v:rect w14:anchorId="25805FC8" id="矩形 194" o:spid="_x0000_s1034"
                                    style="position:absolute;left:0;text-align:left;margin-left:105.6pt;margin-top:-710.1pt;width:213pt;height:58.5pt;z-index:251707392;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:margin;mso-position-vertical:absolute;mso-position-vertical-relative:text;v-text-anchor:middle"
                                    o:gfxdata="UEsDBBQABgAIAAAAIQC2gziS/gAAAOEBAAATAAAAW0NvbnRlbnRfVHlwZXNdLnhtbJSRQU7DMBBF&#xA;90jcwfIWJU67QAgl6YK0S0CoHGBkTxKLZGx5TGhvj5O2G0SRWNoz/78nu9wcxkFMGNg6quQqL6RA&#xA;0s5Y6ir5vt9lD1JwBDIwOMJKHpHlpr69KfdHjyxSmriSfYz+USnWPY7AufNIadK6MEJMx9ApD/oD&#xA;OlTrorhX2lFEilmcO2RdNtjC5xDF9pCuTyYBB5bi6bQ4syoJ3g9WQ0ymaiLzg5KdCXlKLjvcW893&#xA;SUOqXwnz5DrgnHtJTxOsQfEKIT7DmDSUCaxw7Rqn8787ZsmRM9e2VmPeBN4uqYvTtW7jvijg9N/y&#xA;JsXecLq0q+WD6m8AAAD//wMAUEsDBBQABgAIAAAAIQA4/SH/1gAAAJQBAAALAAAAX3JlbHMvLnJl&#xA;bHOkkMFqwzAMhu+DvYPRfXGawxijTi+j0GvpHsDYimMaW0Yy2fr2M4PBMnrbUb/Q94l/f/hMi1qR&#xA;JVI2sOt6UJgd+ZiDgffL8ekFlFSbvV0oo4EbChzGx4f9GRdb25HMsYhqlCwG5lrLq9biZkxWOiqY&#xA;22YiTra2kYMu1l1tQD30/bPm3wwYN0x18gb45AdQl1tp5j/sFB2T0FQ7R0nTNEV3j6o9feQzro1i&#xA;OWA14Fm+Q8a1a8+Bvu/d/dMb2JY5uiPbhG/ktn4cqGU/er3pcvwCAAD//wMAUEsDBBQABgAIAAAA&#xA;IQBvKS+8sQIAAL8FAAAOAAAAZHJzL2Uyb0RvYy54bWysVMFu2zAMvQ/YPwi6r7aDZGmDOkXQosOA&#xA;ri3WDj0rslQbkERNUhJnPzNgt37EPmfYb4ySHTfrgh2GXWxRJB/JJ5KnZ61WZC2cb8CUtDjKKRGG&#xA;Q9WYx5J+ur98c0yJD8xUTIERJd0KT8/mr1+dbuxMjKAGVQlHEMT42caWtA7BzrLM81po5o/ACoNK&#xA;CU6zgKJ7zCrHNoiuVTbK87fZBlxlHXDhPd5edEo6T/hSCh5upPQiEFVSzC2kr0vfZfxm81M2e3TM&#xA;1g3v02D/kIVmjcGgA9QFC4ysXPMHlG64Aw8yHHHQGUjZcJFqwGqK/EU1dzWzItWC5Hg70OT/Hyy/&#xA;Xt860lT4didjSgzT+Eg/vz79+P6NxBvkZ2P9DM3u7K3rJY/HWGwrnY5/LIO0idPtwKloA+F4OZrm&#xA;kyJH6jnqpuPRySSRnj17W+fDOwGaxENJHb5ZopKtr3zAiGi6M4nBPKimumyUSkLsE3GuHFkzfGHG&#xA;uTBhktzVSn+AqrufTnJMocNKrRVdEvJvaMpETAMRvTOON1kkoCs5ncJWiWinzEchkbpYZIo4IO8n&#xA;U3SqmlWiu46pHM4lAUZkifEH7B7gUKFFX1JvH11F6vnBOf9bYl2Jg0eKDCYMzrox4A4BqDBE7ux3&#xA;JHXURJZCu2xTWx3vWmgJ1RZbzUE3g97yywYf/Ir5cMscDh32CC6ScIMfqWBTUuhPlNTgvhy6j/Y4&#xA;C6ilZINDXFL/ecWcoES9NzglJ8V4HKc+CePJdISC29cs9zVmpc8Bu6jAlWV5Okb7oHZH6UA/4L5Z&#xA;xKioYoZj7JLy4HbCeeiWC24sLhaLZIaTblm4MneWR/DIc2zo+/aBOdt3fcB5uYbdwLPZi+bvbKOn&#xA;gcUqgGzSZESmO177F8Atkdq632hxDe3Lyep5785/AQAA//8DAFBLAwQUAAYACAAAACEAFiaXqeQA&#xA;AAAPAQAADwAAAGRycy9kb3ducmV2LnhtbEyPS0/DMBCE70j8B2uRuFStHafqI8SpChIXJFRRkHp1&#xA;YpNE+KXYbQK/nu0JbrM7o9lvy91kDbnoIfbeCcgWDIh2jVe9awV8vD/PN0Bikk5J450W8K0j7Krb&#xA;m1IWyo/uTV+OqSVY4mIhBXQphYLS2HTayrjwQTv0Pv1gZcJxaKka5Ijl1lDO2Ipa2Tu80Mmgnzrd&#xA;fB3PVsDL4xjCXh5m9c9pOaPbTVqb+CrE/d20fwCS9JT+wnDFR3SokKn2Z6ciMQJ4lnGMCphnS85Q&#xA;YmaVr1HU113Ocg60Kun/P6pfAAAA//8DAFBLAQItABQABgAIAAAAIQC2gziS/gAAAOEBAAATAAAA&#xA;AAAAAAAAAAAAAAAAAABbQ29udGVudF9UeXBlc10ueG1sUEsBAi0AFAAGAAgAAAAhADj9If/WAAAA&#xA;lAEAAAsAAAAAAAAAAAAAAAAALwEAAF9yZWxzLy5yZWxzUEsBAi0AFAAGAAgAAAAhAG8pL7yxAgAA&#xA;vwUAAA4AAAAAAAAAAAAAAAAALgIAAGRycy9lMm9Eb2MueG1sUEsBAi0AFAAGAAgAAAAhABYml6nk&#xA;AAAADwEAAA8AAAAAAAAAAAAAAAAACwUAAGRycy9kb3ducmV2LnhtbFBLBQYAAAAABAAEAPMAAAAc&#xA;BgAAAAA=&#xA;"
                                    fillcolor="#2e74b5 [2408]" stroked="f" strokeweight="1pt">
                                <v:textbox>
                                    <w:txbxContent>
                                        <w:p w14:paraId="5AAE99C4" w14:textId="77777777" w:rsidR="003B3998"
                                             w:rsidRPr="00E30B06" w:rsidRDefault="003B3998" w:rsidP="003B3998">
                                            <w:pPr>
                                                <w:jc w:val="center"/>
                                                <w:rPr>
                                                    <w:rFonts w:ascii="宋体" w:eastAsia="宋体" w:hAnsi="宋体"/>
                                                    <w:b/>
                                                    <w:sz w:val="72"/>
                                                    <w:szCs w:val="72"/>
                                                </w:rPr>
                                            </w:pPr>
                                            <w:r>
                                                <w:rPr>
                                                    <w:rFonts w:ascii="宋体" w:eastAsia="宋体" w:hAnsi="宋体"
                                                              w:hint="eastAsia"/>
                                                    <w:b/>
                                                    <w:sz w:val="72"/>
                                                    <w:szCs w:val="72"/>
                                                </w:rPr>
                                                <w:t>测评结果</w:t>
                                            </w:r>
                                        </w:p>
                                    </w:txbxContent>
                                </v:textbox>
                                <w10:wrap anchorx="margin"/>
                            </v:rect>
                        </w:pict>
                    </mc:Fallback>
                </mc:AlternateContent>
            </w:r>
        </w:p>''' % (ls1[2], desc_fu(ls1[2])[1], desc_fu(ls1[2])[2], desc_fu(ls1[2])[3], desc_fu(ls1[2])[4],
                     desc_fu(ls1[2])[5])
        s1 = s1 + a + b + c
    return s1

