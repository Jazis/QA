# import sys
# sys.path.append('../../imports/')

# from connect import *
# from waiter import *
# from waiter import waitResponse
# import pytest
# import logging
# import allure

# @allure.step('Try to disable one record')
# def routineMaintenanceCheck(ws):
#     ws.send('[48,5932123028902192,{"receive_progress":false},"api.konfigd.get",["fd226a26-34a6-19b7-fc6b-5a6b4369a117","exec maintenance.pl disable \'{\"id\\\":2}\' --json"],{}]')
#     message = waitResponse(ws)
#     # assert "fd226a26-34a6-19b7-fc6b-5a6b4369a117" in message, "Something wrong with take routine maintenance list"
#     # ws.swnd(r'[48,5396004881188620,{"receive_progress":false},"api.konfigd.get",["a356236d-7f05-7c50-4c02-0520fdc65b9d","exec maintenance.pl dump \'{\"user_id\":\"root\",\"disabled\":true,\"extensions\":[{\"name\":\"target_info\",\"tags\":[\"target-type\",\"device\"],\"display_path\":true},{\"name\":\"user_info\",\"tags\":[\"displayName\"]},\"is_active\",\"last_change\"]}\' --json"],{}]')
#     # message = waitResponse(ws)
#     # assert ""

# @allure.title('Routine maintenance')
# def test_alerts(seal):
#     seal1 = seal.replace("qweDelimqwe", "|")
#     data = auth(seal1)
#     ws = data[0]
#     routineMaintenanceCheck(ws)