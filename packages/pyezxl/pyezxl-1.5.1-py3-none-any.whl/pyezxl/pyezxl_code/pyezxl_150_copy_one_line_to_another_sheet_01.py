#  -*- coding: utf-8 -*-

import pyezxl
excel = pyezxl.pyezxl("")
sheet_name = excel.read_activesheet_name()
activecell = excel.read_activecell_range()

# 다른시트에 현재 위치한 한줄을 특정 위치에 복사하기
# 이것은 사용자가 코드를 넣어서 사용하기위한 자료인 것이다

excel.copy_x_line(sheet_name, "paste_sheet", activecell[0], 1)

