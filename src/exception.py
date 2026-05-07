import sys
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name= exc_tb.tb_frame.t_code.co_filename
    error_message = "error occured in python Script name[{0}] line number[{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))
    return error_message
    

   
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super._init_(error_message)
        self.error_message =error_message_detail(error_message,error_detail=error_detail)


        
        def _str_(self):
            return self.error_message

         