"""
Logging Demo 1
Logging Levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""
import logging

# by default it prints anything above and including warning level (info wouldn't have printed)
# so can specify level as debug (lowest level) for everything to be printed
logging.basicConfig(filename="test.log", level=logging.DEBUG)

logging.warning("warning message")
logging.info("info message")
logging.error("error message")