import xlrd
import os

import xlwt
# import pyexcel as p
# from pathlib import Path


"""打开工作簿"""

#current_path = os.path.dirname(os.path.abspath(""))
# print(current_path)
#"E:\Program Files\web自动化测试用例\auto-testcase\data\kaop_element.xlsx"


# workbook = xlrd.open_workbook("welfare_element.xls")
#
# # 获取第一个sheet
# table = workbook.sheets()[0]
# print(table)
# # """通过sheet索引获取"""
# table1 = workbook.sheet_by_index(0)
# print(table1)
# # """通过sheet名称获取"""
# table2 = workbook.sheet_by_name("welfare")
# print(table2)
# # """获取所有sheet名称"""
# sheets = workbook.sheet_names()
# print(sheets)
#
# #行、列的获取
# row_name = table.row_values(1)
# print(row_name)
#
# col_name = table.col_values(1)
# print(col_name)
#
# #获取行数、列数
#
# rows_number = table.nrows
# print(rows_number)
#
# cols_number = table.ncols
# print(cols_number)
#
# #获取单元格的数据
# cell = table.cell(2, 2).value
# print(cell)
#
#
# def read():
#     workbook = xlrd.open_workbook("welfare_element.xls")
#     sheet = workbook.sheet_by_name('welfare')
#     nrows = sheet.nrows
#     data = []
#     for i in range(nrows):
#         data.append(sheet.row_values(i))
#     return data
#
# data_1 = read()
# print(data_1)
#
#
class DoExcel():
    def __init__(self, filename, sheetname):
        self.workbook = xlrd.open_workbook(filename)
        self.sheetName = self.workbook.sheet_by_name(sheetname)
    def read_excel(self, rownum, colnum):
        value = self.sheetName.cell(rownum, colnum).value
        return value


# cellvalue = DoExcel("welfare_element.xls",'welfare').read_excel(2, 2)
#
# print(cellvalue)
