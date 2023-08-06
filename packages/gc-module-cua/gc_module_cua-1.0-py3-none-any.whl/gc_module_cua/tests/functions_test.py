from gc_module_cua import functions
from gc_module_cua.tests.sqlshell_test import sql_shell


def get_all_events_test():
    response = functions.get_all_events(sql_shell, events_table='cm_events_table')
    print("RESPONSE:", response)


get_all_events_test()