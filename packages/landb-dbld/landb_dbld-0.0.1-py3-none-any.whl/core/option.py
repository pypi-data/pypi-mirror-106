from core.pynodb import PyNoDDB
from core.log import logger, callbacklogger


class Option:
    write_count = 0
    option_cont = 0
    core = None

    def __init__(self):
        self.core = PyNoDDB()

    def add(self, key, value):
        logger.info("插入数据 %s %s" % (key,value))
        callbacklogger.info("add %s %s" %(key, value))
        self.core.set(key, value)
        self.write_count += 1
        self.option_cont += 1

    def delete(self, key):
        logger.info("删除数据 %s" % key)
        callbacklogger.info("delete %s" % key)
        self.core.delete(key)
        self.write_count += 1
        self.option_cont += 1

    def update(self, key, value):
        logger.info("更新数据 %s %s" % (key, value))
        callbacklogger.info("update %s %s" % (key, value))
        self.core.update(key, value)
        self.write_count += 1
        self.option_cont += 1

    def select(self, key):
        logger.info("查询数据key： %s" % (key))
        value = self.core.get(key)
        self.option_cont += 1
        logger.info("查询数据的value: %s" % value)
        return value
