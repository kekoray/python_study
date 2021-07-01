# -*- coding: utf-8 -*-

from pyhive import hive
# from TCLIService.ttypes import TOperationState

import pyhive
print(dir(pyhive))

hive_host = '1.15.55.232'
hive_port = '7001'
hive_username = 'root'
hive_password = 'FyTOSDYPcp42esn7'
hive_database = 'lazada_dw'

hive_confign = {
    'mapreduce.job.queuename': 'my_hive',
    'hive.execution.engine': 'tez',
    'hive.tez.container.max.java.heap.fraction': '0.9',
    'tez.am.max.app.attempts': '5',
    'tez.am.max.app.task.failed.attempts': '10',
    'hive.tez.exec.print.summary': 'true',
    'hive.merge.tezfiles': 'true',
}
#
# conn = hive.Connection(host=hive_host, port=hive_port, username=hive_username, database=hive_database, auth='LDAP',
#                        password=hive_password)
#
# cursor = conn.cursor()
