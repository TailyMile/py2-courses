import logging
import time


class TimeLogContext(object):
    def __init__(self, context_name):
        self.context_name = context_name
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        logging.debug(f"Entering context {self.context_name}")
        return self.context_name

    def __exit__(self, exc_type, exc_val, traceback):
        total_time = time.time() - self.start_time
        if exc_val is not None:
            logging.warning(f"Exception in context {self.context_name}")
        logging.debug(f"Leaving context {self.context_name}, total time is: {total_time:.2f} seconds")
        return False