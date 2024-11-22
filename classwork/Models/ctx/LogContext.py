import logging


class InterruptContext(Exception): pass


class LogContext(object):

    def __init__(self, context_name):
        self.__context_name = context_name
        
    def __enter__(self):
        logging.debug(f'Entering context {self.__context_name}')
        return self.__context_name
        
    def __exit__(self, exc_type, exc_val, traceback):
        if exc_val is not None:
            if isinstance(exc_val, InterruptContext):
                logging.debug(f'Context {self.__context_name} interrupted')
                return True
            logging.warning('Exception raised')
        logging.debug(f'Leaving context {self.__context_name}')
        return False
        
        