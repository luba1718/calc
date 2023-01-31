from datetime import datetime as dt
from time import time

import logging

# logging.basicConfig(
#     level = logging.DEBUG,
#     filename="my_log.log",
#     format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s - %(message)s",
#     datefmt='%d-%m-%Y %H:%M:%S',
#     )


def result_logger(data, result):
    left_value, oper, right_value = data
    data_str = f'{str(left_value)} {oper} {str(right_value)}'
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='UTF-8') as file:
        file.write('{}; операция : {} результат : {}\n'.format(
            time, data_str, result))