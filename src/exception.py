import sys
import logging
from datetime import datetime
from src.logger import logging

def error_message_details(error):
    print(f"Error: {error}")
    exc_type, exc_obj, exc_tb = sys.exc_info()
    error_message = "Error occurred in python script name: " + exc_tb.tb_frame.f_code.co_filename
    error_message += "\nError occurred in line number: " + str(exc_tb.tb_lineno)
    error_message += "\nError occurred in function name: " + exc_tb.tb_frame.f_code.co_name
    print(error_message)
    return error_message

class CustomError(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.message = error_message
        self.error_message = error_message_details(self.message)
        print(self.error_message)

    def __str__(self) -> str:
        return self.error_message
    
if __name__ == "__main__":
    try:
        a=1/0
    except:
        logging.info("Divide by zero error")
        raise CustomError(sys.exc_info())