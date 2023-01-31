from calc import Calc_block as calc
from logger import result_logger as write_log
import data_transformation as d_t
import user_interface as u_i

def button_click():
    e = d_t.data_format(u_i.input_data())
    calc_result = calc(e)
    u_i.view_data(calc_result, 'Ответ:')
    write_log(e, calc_result)
button_click()  