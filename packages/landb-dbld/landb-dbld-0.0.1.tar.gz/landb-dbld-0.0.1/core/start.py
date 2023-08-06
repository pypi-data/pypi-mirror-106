from core.pynodb import PyNoDDB
from core.setting import Setting
from core.option import Option
from core.store import Store, ReLoadSnapshot
from core.log import startLogger

class Build:
    setting = None
    option = None
    core = None

    def __init__(self, setting):
        self.setting = setting
        self.core = PyNoDDB(setting)
        self.option = Option()

    def build(self):
        reload = ReLoadSnapshot()
        reload.reload_snapshot()
        store_demo = Store(store_setting=self.setting.store_snapshot)
        startLogger.info("快照监听线程启动")
        store_demo.start()
        startLogger.info("初始化完成，返回操作接口")
        return self.option


