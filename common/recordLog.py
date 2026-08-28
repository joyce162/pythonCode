import os
import logging
import time
from common.readYaml import ReadYaml
from conf import setting
from logging.handlers import RotatingFileHandler

log_path = setting.FILE_PATH['log']
if not os.path.exists(log_path):
    os.mkdir(log_path)

logfile_name = log_path + r'\test.{}.log'.format(time.strftime("%Y%m%d"))

log_level = setting.LOG_LEVEL


class RecordLog(object):

    def output_logging(self):
        # 获取log对象
        logger = logging.getLogger(__name__)

        if not logger.handlers:
            logger.setLevel(log_level)
            log_format = logging.Formatter(
                fmt="%(asctime)s %(levelname)s %(filename)s [%(lineno)d] %(funcName)s - %(message)s"
            )

            rf_handler = RotatingFileHandler(
                filename=logfile_name,
                mode='a',
                maxBytes=5 * 1024 * 1024,
                backupCount=3,
                encoding="utf‑8"
            )

            # 日志输出到日志文件
            rf_handler.setLevel(log_level)
            rf_handler.setFormatter(log_format)
            logger.addHandler(rf_handler)

            # 日志输出到console 控制台
            streamHandler = logging.StreamHandler()
            streamHandler.setLevel(setting.STREAM_LOG_LEVEL)
            streamHandler.setFormatter(log_format)
            logger.addHandler(streamHandler)

        return logger

apilog = RecordLog()
log = apilog.output_logging()



