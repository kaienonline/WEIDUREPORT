# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:yhq

import os
import time

from win32com.client import Dispatch

def word_to_pdf(folder):
    w = Dispatch('Word.Application')
    t4 = time.time()
    files = os.listdir(folder)
    # 获取word类型的文件放到一个列表里面
    wdfiles = [f for f in files if f.endswith((".doc", ".docx"))]
    pdffiles = [f for f in files if f.endswith((".pdf"))]
    t5 = time.time()
    print('获取所有docx文件用时%s' % (t5 - t4))
    for wdfile in wdfiles:
        if wdfile != wdfiles[-1]:
            continue
        p = wdfile + ".pdf"
        if p in pdffiles:
            continue
        t6 = time.time()
        print("%s开始转换" % wdfile)
        # 将word文件放到指定的路径下面
        wdPath = os.path.join(folder, wdfile)
        print(wdPath)
        # 设置将要存放pdf文件的路径
        pdfPath = wdPath

        # 判断是否已经存在对应的pdf文件，如果不存在就加入到存放pdf的路径内
        if pdfPath[-3:] != 'pdf':
            pdfPath = pdfPath + ".pdf"

        doc = w.Documents.Open(wdPath, ReadOnly=1)

        try:
            doc.SaveAs(pdfPath, 17)
            
        except Exception as e:
            print(e)
            
        finally:
            print('转换过程结束')
            doc.Close(-1)

        return wdPath