#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zhangjiao


# 导入系统库
import sys
import importlib
# 对importlib做处理,让其加载sys
importlib.reload(sys)


from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter# 解释器
from pdfminer.converter import PDFPageAggregator# 转换器
from pdfminer.layout import LTTextBoxHorizontal,LAParams # 布局
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed # 是否允许pdf和text转换


'''
此函数只能转换纯文本
'''


# 将path文件中的内容读取到topath文件中
def readPDF(path, toPath):
    # 以二进制的形式打开pdf文件
    f = open(path, 'rb')
    # 创建一个pdf文档分析器
    parser = PDFParser(f)
    # 创建pdf文档
    pdfFile = PDFDocument()
    # 获取连接分析器
    parser.set_document(pdfFile)
    # 获取文档对象
    pdfFile.initialize()
    # 检测文档是否提供txt转换
    if not pdfFile.is_extractable:
        #不允许转换
        raise PDFTextExtractionNotAllowed
    else:
        # 解析数据
        # 数据管理器
        manager = PDFResourceManager()
        # 参数分析器
        laparams = LAParams()
        # 创建一个PDF设备对象
        device = PDFPageAggregator(manager,laparams=laparams)
        # 解释器对象
        interpreter = PDFPageInterpreter(manager,device)
        # 开始循环处理,每次处理一页
        for page in pdfFile.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if(isinstance(x, LTTextBoxHorizontal)):
                    with open(toPath, 'a') as f:
                        str = x.get_text()
                        # print(str)
                        f.write(str + "\n")


path = r"/home/wayne/PythonCode/Python1805/day15/abc.pdf"
toPath = r"/home/wayne/PythonCode/Python1805/day15/abc_new.pdf"
readPDF(path,toPath)
