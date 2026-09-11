import copy
import xlrd
import xlwt
from xlutils.copy import copy

from conf.setting import FILE_PATH

class HandleExcel(object):
    def __init__(self,file_path=None,sheet_index=None):
        if file_path is not None:
            self.file_path = file_path
        else:
            self.file_path = FILE_PATH['EXCEL']

        if sheet_index is not None:
            self.sheetData = self.excel_read(sheet_index)
        else:
            self.sheetData = self.excel_read()

    def excel_read(self,sheetIndex=0):
        """
        读excel文件
        :param sheetIndex: sheet 索引，从0开始
        :return: 返回sheet对象
        """
        table = xlrd.open_workbook(self.file_path,formatting_info=True)
        worksheet = table.sheets()[sheetIndex]
        return worksheet

    def get_cell_value(self,rowIndex,colIndex):
        data = self.sheetData.cell_value(rowIndex,colIndex)
        return data

    def excel_write(self,rowIndex,colIndex,value,sheetIndex=0):
        """
        excel写入数据方法
        :param rowIndex:行索引，从0开始
        :param colIndex:列索引，从0开始
        :param value: 写入数据
        :param sheetIndex: 表名
        """
        init_table = xlrd.open_workbook(self.file_path,formatting_info=True)
        copy_table = copy(init_table)
        copy_sheet = copy_table.get_sheet(sheetIndex)
        copy_sheet.write(rowIndex,colIndex,value)
        copy_table.save(self.file_path)

    def get_sheet_total_col(self,sheetIndex=0):
        """
        获取sheet总列数
        :param sheetIndex:
        :return:
        """
        return self.sheetData.ncols

    def get_sheet_total_row(self, sheetIndex=0):
        """
        获取sheet总行数
        :param sheetIndex:
        :return:
        """
        return self.sheetData.nrows

if __name__ == '__main__':
    excel = HandleExcel()