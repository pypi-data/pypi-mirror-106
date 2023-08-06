
from core.pynodb import PyNoDDB
from core.setting import Setting
from core.start import Build

def init_db():
    setting = Setting('my-db','root','123456')
    db = Build(setting)
    option = db.build()
    return option

def add_test():
    option.add('keu',1999)
    print(option.select('keu'))

def delete():
    option.delete('keu')

def update():
    option.add('test1','ming')
    print(option.select('test1'))
    option.update('test1',19)
    print(option.select('test1'))



if __name__ == '__main__':
    option = init_db()
    add_test()
    delete()
    update()
