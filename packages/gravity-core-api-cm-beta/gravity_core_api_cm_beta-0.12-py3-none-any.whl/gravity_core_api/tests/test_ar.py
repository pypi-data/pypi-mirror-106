class TestAR:
    def __init__(self, ar_status='Готов'):
        self.ar_status = ar_status

    def get_api_support_methods(self):
        methods = {'get_status': {'method': self.get_status},
                   'start_car_protocol': {'method': self.cic_start_car_protocol},
                   'operate_gate_manual_control': {'method': self.operate_gate_manual_control}}
        return methods

    def get_status(self):
        return self.ar_status

    def cic_start_car_protocol(self, info):
        print('Начало заезда с данными:', info)

    def operate_gate_manual_control(self, info):
        print('Открытие шлагбаума с данными:', info)