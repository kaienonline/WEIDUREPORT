# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:yhq

import xlrd
import re


excel_path = r'C:\WD\WeiDuReport\report\test_en.xlsx'
# excel_path = 'test_en.xlsx'
data = xlrd.open_workbook(excel_path)
table = data.sheet_by_index(3)
row_count = table.nrows
substandard_name = ""
substandard_comments_map = {}

def hm_template_en():
    for i in range(row_count):
        if i == 0:
            continue
        if i > 48:
            continue
        info = table.row_values(i)
        name = info[1][:4]
        if name:
            substandard_name = name
        if substandard_name not in substandard_comments_map:
            substandard_comments_map[substandard_name] = []
        score_range = info[2]
        comment = info[4]
        score_range = score_range.replace("[", "").replace("]", "")
        if score_range.find(",") > -1:
            score_ranges = score_range.split(",")
        elif score_range.find("，") > -1:
            score_ranges = score_range.split("，")
        else:
            raise Exception("error")
        min_value = int(score_ranges[0].strip())
        max_value = int(score_ranges[1].strip())
        data = {
            "min_value": min_value,
            "max_value": max_value,
            "comment": comment,
            "word_template": ""
        }

        black_template = '''
    <w:r w:rsidRPr="00040D97">
        <w:rPr>
            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
            <w:b/>
            <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>%s</w:t>
    </w:r>
                        '''
        not_black_template = '''
    <w:r w:rsidRPr="00040D97">
        <w:rPr>
            <w:rFonts w:ascii="微软雅黑" w:eastAsia="微软雅黑" w:hAnsi="微软雅黑" w:hint="eastAsia"/>
            <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>%s</w:t>
    </w:r>
        '''
        re_comment = re.findall(r'(.*?)<b>(.*?)</b>', comment, re.S | re.M)
        left_comment = comment.split('</b>')[-1]

        word_template = ''
        for re_c in re_comment:
            not_black_template_comment = re_c[0]
            blank_template_comment = re_c[1]
            word_template += not_black_template % not_black_template_comment
            word_template += black_template % blank_template_comment
        if len(left_comment) > 0:
            word_template += not_black_template % left_comment

        data["word_template"] = word_template
        substandard_comments_map[substandard_name].append(data)
    return substandard_comments_map