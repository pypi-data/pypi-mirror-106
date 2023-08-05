from gravity_core_api.operate_user_commands.functions import *

BASE_METHOD = 'user_command'

all_keys = {'get_status':
                {'execute_function': get_status},
            'install_user_config':
                {'execute_function': install_user_cfg},
            'start_car_protocol':
                {'execute_function': start_car_protocol},
            'operate_gate_manual_control':
                {'execute_function': operate_gate_manual},
            'change_opened_record':
                {'execute_function': change_opened_record}
            }