import logging
import logging.handlers
import datetime


logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', encoding='utf8', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('error.log', encoding='utf8')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
logger.addHandler(rf_handler)
logger.addHandler(f_handler)
logger.addHandler(ch)




callbacklogger = logging.getLogger("callbacklogger")
callbacklogger.setLevel(logging.DEBUG)
callback_handler = logging.FileHandler('callback.log', encoding='utf8')
callback_handler.setFormatter(logging.Formatter("%(created)d-%(message)s"))
callbacklogger.addHandler(callback_handler)



startLogger = logging.getLogger("startLogger")
startLogger.setLevel(logging.DEBUG)
start_handler = logging.FileHandler('start.log', encoding='utf8')
start_handler.setFormatter(logging.Formatter("%(asctime)s-%(message)s"))
startLogger.addHandler(start_handler)
startLogger.addHandler(ch)






