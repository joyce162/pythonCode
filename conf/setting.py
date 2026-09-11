import os
import sys
import logging

DIR_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(DIR_PATH)

LOG_LEVEL = logging.DEBUG
STREAM_LOG_LEVEL = logging.DEBUG

FILE_PATH = {
    'extract': os.path.join(DIR_PATH, 'extract.yml'),
    'conf': os.path.join(DIR_PATH, 'conf','conf.ini'),
    'log': os.path.join(DIR_PATH, 'log'),
    'EXCEL': os.path.join(DIR_PATH, 'data/接口信息.xls')
}

print(FILE_PATH['extract'])
print(DIR_PATH)