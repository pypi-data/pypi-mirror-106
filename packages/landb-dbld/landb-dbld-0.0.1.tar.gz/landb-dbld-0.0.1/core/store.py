import time
import core.option
import threading
from core.log import logger, startLogger
from core.pynodb import PyNoDDB
import pickle
import os

class Store(threading.Thread):
    snapshot_time = time.time()
    write_count = 0
    store_setting = None

    # dd = {}
    # keys = dd.keys()
    def __init__(self, store_setting):
        threading.Thread.__init__(self)
        logger.info("快照监听模块启动，入参%s" % store_setting)
        self.store_setting = store_setting
        self.keys = self.store_setting.keys()

    def run(self):
        logger.info("快照监听线程启动....")
        self.listen_snapshot()

    def listen_snapshot(self):
        try:
            while True:
                for key in self.keys:
                    count = self.store_setting.get(key)
                    if time.time() - self.snapshot_time >= key and core.Option.write_count - self.write_count >= count:
                        self.snapshot_time = time.time()
                        self.write_count = core.Option.write_count
                        self.snapshot()

        except Exception:
            logger.error("快照监听线程报错! %s" % Exception)

    def snapshot(self):

        logger.info("开始生成快照")
        copy_db = PyNoDDB.db
        with open('data.db', 'wb') as f:
            pickle.dump(copy_db, f, pickle.HIGHEST_PROTOCOL)
        logger.info("快照生成完成")


class ReLoadSnapshot:

    def valid_snapshot(self):
        startLogger.info("检查快照是否存在")
        file = os.access('./data.db',os.F_OK)
        if file is False:
            startLogger.info("不存在数据文件！")
            return False
        else:
            return True


    def reload_snapshot(self):
        file = self.valid_snapshot()
        if file is False:
            startLogger.info("不存在数据文件，不需要载入快照")
            return
        startLogger.info("载入存在的快照")
        with open('data.db', 'rb') as f:
            try:
                data = pickle.load(f)
                PyNoDDB.db = data
            except Exception:
                logger.error("数据载入出错 %s" % Exception)

        startLogger.info("快照载入完成")
