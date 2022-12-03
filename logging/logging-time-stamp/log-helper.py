import logging
import sys
from logging.handlers import TimedRotatingFileHandler
FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = "my_app.log"

def get_console_handler():
   console_handler = logging.StreamHandler(sys.stdout)
   console_handler.setFormatter(FORMATTER)
   return console_handler
def get_file_handler():
   file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
   file_handler.setFormatter(FORMATTER)
   return file_handler
def get_logger(logger_name):
   logger = logging.getLogger(logger_name)
   logger.setLevel(logging.DEBUG) # better to have too much log than not enough
   logger.addHandler(get_console_handler())
   logger.addHandler(get_file_handler())
   # with this pattern, it's rarely necessary to propagate the error up to parent
   logger.propagate = False
   return logger



def module_1(test_debug):
    my_logger = get_logger("Testing %s message."%(test_debug))
    my_logger.debug("This is debug message.")
    return test_debug

def module_2(test_info):
    my_logger = get_logger("Testing %s message."%(test_info))
    my_logger.info("This is info message.")
    return test_info

def module_3(test_warning):
    my_logger = get_logger("Testing %s message."%(test_warning))
    my_logger.warning("This is warning message.")
    return test_warning

def module_4(test_error):
    my_logger = get_logger("Testing %s message."%(test_error))
    my_logger.error("This is error message.")
    return test_error

def module_5(test_critical):
    my_logger = get_logger("Testing %s message."%(test_critical))
    my_logger.critical("This is critical message.")
    return test_critical


module_1("Debuging")
module_2("Info")
module_3("Warning")
module_4("Error")
module_5("Critical")
