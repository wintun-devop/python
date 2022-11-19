#https://github.com/wintun-devop
#https://www.youtube.com/channel/UCz9ebjc-_3t3p49gGpwyAKA (Please subscribe my channel.Thank You!)
import logging, datetime
from datetime import date


#logging with current date and time on debut level
current_date_time=datetime.datetime.now()
current_date_time_redable=current_date_time.strftime("%Y-%m-%d %H:%M:%S")

logging.basicConfig(filename='devlog.log', encoding='utf-8', level=logging.DEBUG,)
logging.debug("This is debut log at %s." % (current_date_time_redable))
logging.info("This is info log at %s." % (current_date_time_redable))
logging.warning("This is warming log at %s." % (current_date_time_redable))
logging.critical("This is critical log at %s." % (current_date_time_redable))
logging.error("This is error log at %s." % (current_date_time_redable))

#logging without time stamp
""" logging.basicConfig(filename='devlog.log', encoding='utf-8', level=logging.DEBUG,)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö') """


''' 
logging.basicConfig(filename='devlog.log', encoding='utf-8',format='%(asctime)s %(message)s', level=logging.DEBUG,)
logging.debug("This message should go to the log file")
logging.info("So should this")
logging.warning("And this, too")
logging.error("And non-ASCII stuff, too, like Øresund and Malmö") 
'''

