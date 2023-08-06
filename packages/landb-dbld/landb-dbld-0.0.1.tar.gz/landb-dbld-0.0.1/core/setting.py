from hashlib import md5
from core.log import logger
from core.log import startLogger

class Setting(object):
    dbname = 'pynodb'
    username = None
    password = None
    store_snapshot = None

    def __init__(self, db, name, password, store_snapshot=None):
        '''
        读取配置文件里面的信息
        '''
        self.dbname = db
        self.username = name
        self.password = password
        if self.store_snapshot is None:
            self.store_snapshot = {
                "60": "1"
            }
        else:
            self.store_snapshot = store_snapshot
        startLogger.info("数据库配置信息初始化：db-name:%s, username:%s, password: %s, store_snapshot：%s "
                    % (self.dbname, self.username, self.password, self.store_snapshot))
        self.__md_identity_info()

    def __md_identity_info(self):
        res_info = self.dbname + self.username + self.password
        self.md_identity = md5(res_info.encode('utf-8')).hexdigest()
        startLogger.info("加密的MD %s" % self.md_identity)
