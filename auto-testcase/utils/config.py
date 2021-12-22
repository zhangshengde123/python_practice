import configparser
import os
import codecs

class ReadConfigIni():
    """
    实例化configparser
    """
    def __init__(self,filename):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)

    #读取操作
    def getConfigValue(self,config, name):
        value = self.cf.get(config,name)
        return value

"""测试代码"""
file_path = os.path.split(os.path.realpath(__file__))[0]
print(file_path)

log_path = os.path.dirname(os.getcwd()) + "\config"
print(log_path)
config_path = log_path + "\configdata.ini"
print(config_path)
read_config = ReadConfigIni(config_path)
value = read_config.getConfigValue("url", "verification")
print(value)



"""
class ReadConfigIni():
    def __init__(self, filepath=None):
        if filepath:
            configpath = filepath
        else:
            dir = os.path.dirname(os.path.abspath(""))
            configpath = dir + "\configdata.ini"
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def get_password(self, section,param):
        value = self.cf.get(section, param)
        return value


if __name__ == '__main__':
    readIni = ReadConfigIni("configdata.ini")
    username_loc = readIni.get_password("url", "verification")
    print(username_loc)
"""