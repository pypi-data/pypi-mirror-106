from gravity_core_api.tests.test_ar import TestAR


test_ar = TestAR()

all_test_commands = {'get_status':
                         {'test_command':
                              {'user_command': {'get_status': {}}}
                          },

                     'operate_gate_manual_control': {'test_command':
                                                         {'user_command': {'operate_gate_manual_control': {'operation': 'close',
                                                                                                           'gate_name': 'entry'}}}},
                     'change_opened_record': {'test_command':
                                                  {'user_command': {'change_opened_record': {'record_id': 2,
                                                                                             'car_number': 'А333АА333',
                                                                                             'carrier': 1,
                                                                                             'trash_cat': 5,
                                                                                             'trash_type': 4,
                                                                                             'comment': 'CHANGED FROM UT',}
                                                                    }}}
                     }