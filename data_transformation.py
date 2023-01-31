import user_interface as ui
from fractions import Fraction
import cmath
from calc import Calc_block as calc
import data_transformation as d_t

def data_format(data):
    data_type, left_value, oper, right_value = data

    if data_type == '1':
        left_value = complex(left_value)
        right_value = complex(right_value)
    elif data_type == '2':
        a = left_value
        left_value = Fraction(a)
        b = right_value
        right_value = Fraction(b)
    return (left_value, oper, right_value)