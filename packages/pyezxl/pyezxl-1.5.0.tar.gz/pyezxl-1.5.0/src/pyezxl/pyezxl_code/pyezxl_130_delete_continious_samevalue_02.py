#  -*- coding: utf-8 -*-

import pyezxl
excel = pyezxl.pyezxl("activeworkbook")
activesheet_name = excel.read_activesheet_name()

x_start, y_start, x_end, y_end= excel.read_range_select()

#선택한 영역중 연속된 같은자료 삭제
flag_same = 0
old_data=""
for y in range(y_start, y_end+1):
	for x in range(x_start, x_end+1):
		if flag_same == 0:
			cell_value = excel.read_cell_value(activesheet_name,[x, y])
		cell_value_down = excel.read_cell_value(activesheet_name,[x+1, y])
		if cell_value == cell_value_down:
			excel.write_cell_value(activesheet_name, [x+1, y], "")
			flag_same = 1
		else:
			flag_same = 0
