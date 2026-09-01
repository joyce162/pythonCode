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
    'log': os.path.join(DIR_PATH, 'log')
}

print(FILE_PATH['extract'])