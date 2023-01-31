def view_data(data, title):
    print(f'{title} = {data}')

def get_value():
    return input()

def input_data():
    print('Введите 1 для работы с комплексными числами или 2 для работы с рациональным числами')
    data_type = get_value()
    if data_type == '1':
        print ('Введите первое число, формат 3+1j: ')
        left_value = get_value()
        print ('Введите второе число, формат 3+1j: ')
        right_value = get_value()
        print ('Выберите операцию: ')
        oper = get_value()
    elif data_type == '2':
        print ('Введите первое число: ')
        left_value = get_value()
        print ('Введите второе число: ')
        right_value = get_value()
        print ('Выберите операцию: ')
        oper = get_value()
    return (data_type, left_value, oper, right_value)
