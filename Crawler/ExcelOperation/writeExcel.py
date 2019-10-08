# -*- coding: utf-8 -*-
__author__ = 'miaoyan'


import xlsxwriter
import datetime


# #创建Excel文件
# workBook = xlsxwriter.Workbook('E:/miaoyan.xlsx')
#
# #创建sheet
# sheetName = workBook.add_worksheet('txls')
#
# #特定单元格写入
#
# cell_A1 = sheetName.write('A1','userName')
# cell_B1 = sheetName.write(0,1,'passWord')
#
# #写入数字
#
# cell_A2 = sheetName.write('A2',45)
#
# #设置行属性
# cell_B2 = sheetName.set_row(0,50)
#
#
# #写入日期
# # cell_B3 = sheetName.write('B3',datetime.datetime.strptime('2018-01-16','%Y-%m-%d'))
#
# #批量行写入数据
# # rows= sheetName.write_row('A6','[1,2,4,5,6]')
# rows = sheetName.write_row('A7',[5,6,7,8])