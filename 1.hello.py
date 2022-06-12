import sys

from loguru import logger as lg

# 1.默认输出
lg.info('1. hello loguru')

# 2. 自定义输出, 注:必须清除之前的
lg.remove(handler_id=None)
lg.add(sys.stderr, format='{time} {level} {message}')
lg.info('2. time format')

# 3.文件输出,
lg.remove(handler_id=None)
lg.add('logs/1.log',
       rotation='1 kb',
       format='{time:YYYY-MM-DD HH:mm:ss f} | {level} | {message}')
lg.info('3. file text')
