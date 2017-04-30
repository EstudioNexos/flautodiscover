import multiprocessing
from ConfigParser import SafeConfigParser
conf = SafeConfigParser()
conf.read('sample_conf.ini')

bind = "%s:%s" % (conf.get('general', 'host'),conf.get('general', 'port'))
workers = multiprocessing.cpu_count() * 2 + 1
