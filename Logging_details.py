import logging

logging.basicConfig(filename="E:/Test/test1.log",format="%(asctime)s:%(levelname)s:%(message)s",level=logging.DEBUG)
logging.debug("This is a debug message")
logging.info("This is just a info, execution is going to start")
logging.warning("Please close the other applications")
logging.error("404 not found")
logging.critical("Memory usage is very high")