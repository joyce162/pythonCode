import os
import csv
from common.recordLog import log
from conf.setting import DIR_PATH

def opratecsv(file_name):
    file_path = os.path.join(DIR_PATH,'data',file_name)
    list =[]
    try:
        with open(file_path,'r',encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                list.append(row)
            return list
    except Exception as e:
        log.error(e)