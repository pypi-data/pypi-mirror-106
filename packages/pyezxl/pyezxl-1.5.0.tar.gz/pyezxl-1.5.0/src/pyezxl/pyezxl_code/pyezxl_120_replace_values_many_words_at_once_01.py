#  -*- coding: cp949 -*-

import pyezxl
excel = pyezxl.pyezxl("activeworkbook")
sheet_name = excel.read_activesheet_name()
[x1, y1, x2, y2] = excel.read_range_select()

# �ٲٱ�
# �ѹ��� �����ܾ� �ٲٱ�
# �̰��� �޼����� �Է¹ޱ�� ����� ���� �ڵ忡 �ٲ� ���ڵ��� �Է¹ٶ��ϴ�

words=[
["����","�ٶ�"],
["¥���","�����"],
["ȿ��","ȿ��"],
]

for x in range(x1, x2+1):
	for y in range(y1, y2+1):
		current_data = str(excel.read_cell_value(sheet_name,[x, y]))
		for one_list in words:
			current_data = current_data.replace(one_list[0], one_list[1])
		excel.write_cell_value(sheet_name,[x, y+1], current_data)