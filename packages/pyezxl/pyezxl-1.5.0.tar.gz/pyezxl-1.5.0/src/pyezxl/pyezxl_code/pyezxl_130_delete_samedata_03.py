#  -*- coding: utf-8 -*-

import pyezxl
excel = pyezxl.pyezxl("")
sheet_name = excel.read_activesheet_name()
[x1, y1, x2, y2] = excel.read_range_select()

#선택한 영역에서 2번이상 반복된것만 색칠하기
py_dic = {}
for x in range(x1, x2+1):
	for y in range(y1, y2+1):
		current_data = excel.read_cell_value(sheet_name,[x, y])
		if current_data != "" and  current_data != None:
			if not py_dic[current_data]:
				py_dic[current_data] = 1
			else:
				py_dic[current_data] = py_dic[current_data] +1

			if py_dic[current_data] >= 2:
				excel.set_cell_color(sheet_name, [x, y], 4)
