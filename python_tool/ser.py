# -*- coding:UTF-8 -*-
import string
import json
import serial.tools.list_ports
ports=list(serial.tools.list_ports.comports())

print("ports----",ports)

'''
<serial.tools.list_ports_common.ListPortInfo object at 0x10ad9f610>
<serial.tools.list_ports_common.ListPortInfo object at 0x10ad9f9a0>
'''

def get_pid(str):
	pid_vid = str.split(' ')[1]
	pid_str = pid_vid.split('=')[1]
	pid = pid_str.split(":")[1]
	return '0x'+pid

def get_vid(str):
	pid_vid = str.split(' ')[1]
	vid_str = pid_vid.split("=")[1]
	vid = vid_str.split(":")[0]
	return "0x"+vid

def get_location_id(str):

	print("get_location_id input ---", str)
    	
	location_str = str.split(' ')[-1]

	print("location_str split ---", location_str)

	# location_id = location_str.split('=')[-1].replace('.','')
	location_id = location_str.split('=')[-1]

	print("location_id split ---", location_id)

	location_first_str = location_id.split('-')[0]

	print("location_first_str split ---", location_first_str)
	location_num = int(location_first_str.upper())
	print("location_num upper ---", location_num)
	location_hex_str = hex(location_num)
	print("location_hex_str ---", location_hex_str)

	location_last_str = location_id.split('-')[1]
	print("location_last_str ---", location_last_str)

	last_str = ""
	arr = location_last_str.split('.')
	for item in arr:
		item_num = int(item.upper())
		item_hex = hex(item_num)
		item_hex = item_hex.replace("0x","")
		last_str = last_str+item_hex
	
	id_str = location_hex_str+last_str
	length = len(id_str)
	for i in range(0, 10-length):
		id_str = id_str + "0"
	return id_str

array = []
for port in ports:
	port_list=list(port)

	print('port_list ---- ',port_list)

	lastObject = port_list[-1]

	print('lastObject ---- ',lastObject)

	if lastObject != 'n/a':
		pid = get_pid(lastObject)
		vid = get_vid(lastObject)
		location_id = get_location_id(lastObject)
		name = port_list[0]	
		product = port_list[1]
		dict = {"name": name, "product": product, "location_id": location_id, "pid": pid, "vid": vid}
		array.append(dict)
print(json.dumps(array))
