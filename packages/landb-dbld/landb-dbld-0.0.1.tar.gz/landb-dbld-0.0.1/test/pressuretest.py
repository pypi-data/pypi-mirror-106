import time

import logging
from core.pynodb import PyNoDDB
from core.setting import Setting
from core.start import Build

def init_db():
    setting = Setting('my-db','root','123456')
    db = Build(setting)
    option = db.build()
    return option

def add_test():
    for i in range(100000):
        option.add('keu-%s' % i, i)
        logging.info("查询数据为： %s" % option.select('keu-%s' % i))


def update():
    option.add('test1','ming')
    print(option.select('test1'))
    option.update('test1',19)
    print(option.select('test1'))



if __name__ == '__main__':
    option = init_db()
    start_time = time.time()
    add_test()
    end_time = time.time()
    print("10000条数据所用的时间 %s" % (end_time - start_time))
