import sys
import logging

def error_message_details(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python scripts name[{0}] line number[{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, (error))
    

    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
    logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='error.log',
        filemode='w'

        
        # level=logging.ERROR,
        # filename="error.log"
        # format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        # level=logging.INFO,
        
        )


    

if __name__=="__main__":
    
    
    try:
        a = 1/0
    except Exception as e:
        logging.info("divide by zero")
        # logging.exception(e)
        raise CustomException(e,sys)
    




