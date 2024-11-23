from TimeLogContext import TimeLogContext

import logging
logging.basicConfig(level=logging.DEBUG)

def total():
    with TimeLogContext('context-1') as ctx_name:
        print(f"Running code in {ctx_name}")
        for i in range(10000000):  # Искусственная задержка
            pass
        print("Done!")

total()