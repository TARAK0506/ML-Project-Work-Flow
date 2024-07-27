import logging
import os
from datetime import datetime
LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d')}.log"
logs_path=os.path.join(os.getcwd(),LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE,
    format= '%(asctime)s %(levelname)s: %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

'''if __name__ == "__main__":
    logging.info("This is a test log message")
    logging.error("This is an error log message")
    logging.warning("This is a warning log message")
    logging.debug("This is a debug log message")
    logging.critical("This is a critical log message")
    logging.exception("This is an exception log message")'''

