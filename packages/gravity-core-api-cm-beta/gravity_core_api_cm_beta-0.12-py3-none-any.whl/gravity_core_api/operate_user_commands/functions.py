def get_status(sqlshell, ar_method, *args, **kwargs):
    """ Обращается к методу get_status экземпляра ar_engine для извлеченеия статуса """
    status = ar_method(**kwargs)
    return status

def start_car_protocol(sqlshell, ar_method, *args, **kwargs):
    """ Начать проткол заезда """
    ar_method(kwargs)
    return get_success_response(info='Протокол заезда начат')

def operate_gate_manual(sqlshell, ar_method, *args, **kwargs):
    """ Команда на ручное управление шлагбаумами """
    ar_method(kwargs)
    return get_success_response(info='Команда на ручное управление шлагбаумами успешно выполнена')


def add_record_comm(sqlshell, ar_method, record_id, comment, *args, **kwargs):
    """ Добавить комментарий к существующей записи """
    ar_method(record_id, comment)

def change_opened_record(ar_method, *args, **kwargs):
    ar_method(**kwargs)

def if_method_supported(ar_support_methods, command):
    for method_name, method_values in ar_support_methods.items():
            if command == method_name:
                return method_values['method']


def add_ar_method_to_data(data, ar_method):
    for command, info in data.items():
        info['ar_method'] = ar_method
    return data


def get_success_response(status='success', info=None):
    response = {'status': status, 'info': info}
    return response