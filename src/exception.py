import sys


def error_msg_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() #give info  abouut, in which file and which line no the exception has occured
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_msg = "Error occured in python script name [{0}] at line no. [{1}] and error message is [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_msg

class CustomException(Exception):
    def __init__(self,error_msg,error_detail:sys):
        super.__init__(error_msg)
        self.error_msg = error_msg_details(error,error_detail=error_detail)

    def __str__(self):
        return self.error_msg