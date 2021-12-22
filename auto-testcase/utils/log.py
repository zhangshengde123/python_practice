import logging
import os
import time
import datetime
from pathlib import Path



# def today():
#     now = datetime.datetime.now()
#     return now
# #
def get_cwd():
    log_path = os.path.dirname(os.getcwd()) + "/log/"  #os.getcwd()
    return log_path
log_path = get_cwd()
#
#
# log_name = f'{today}.log'
# path = get_cwd()
# print(path)



  # 日志类1

class Logger():
    def __init__(self, logger, LogFile,CmdLevel, FileLevel):

        #创建一个logger
        #LogFile = f'{today}.log'
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)


        fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        #设置日志文件的名称
        self.LogFileName = os.path.join(log_path, "{0}.log".format(time.strftime("%Y-%m-%d")))

        #设置控制台日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(CmdLevel)

        #设置文件日志

        fh = logging.FileHandler(self.LogFileName, encoding='utf_8')
        fh.setFormatter(fmt)
        fh.setLevel(FileLevel)

        #给logger添加Handler
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)

    def debug(self,message):
        self.logger.debug(message)

    def info(self,message):
        self.logger.info(message)

    def warn(self,message):
        self.logger.warn(message)

    def error(self,message):
        self.logger.error(message)

    def cri(self,message):
        self.logger.critical(message)


# if __name__ == "__main__":
#     logger = Logger(LogFile= 'logging.log', CmdLevel=logging.DEBUG, FileLevel=logging.ERROR)
#     logger.debug("debug message!")
#     logger.info("info message!")
#     logger.warn("warn message!")
#     logger.error("error message!")
#     logger.cri("critical message!")




