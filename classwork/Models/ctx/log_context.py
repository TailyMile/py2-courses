from contextlib import contextmanager
import logging


@contextmanager
def log_context(ctx_name):
    logging.debug(f'ENTERING: {ctx_name}')
    try:
        yield ctx_name
    finally:
        logging.debug(f'LEAVING: {ctx_name}')
        