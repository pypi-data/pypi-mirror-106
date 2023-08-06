# -*- coding: utf-8 -*-

import time
import string

class pyezxl_time:
	def __init__(self):
		self.web_site = "www.halmoney.com"

	def read_time_day(self, time_char=time.localtime(time.time())):
		#일 -----> ['05', '095']
		return [time.strftime('%d',time_char),time.strftime('%j',time_char)]

	def read_time_hour(self, time_char=time.localtime(time.time())):
		#시 -----> ['10', '22', 'PM']
		return [time.strftime('%I',time_char),time.strftime('%H',time_char),time.strftime('%P',time_char)]

	def read_time_minute(self, time_char=time.localtime(time.time())):
		#분 -----> ['07']
		return [time.strftime('%M',time_char)]

	def read_time_month(self, time_char=time.localtime(time.time())):
		#월 -----> ['04', 'Apr', 'April']
		return [time.strftime('%m',time_char),time.strftime('%b',time_char),time.strftime('%B', time_char)]

	def read_time_second(self, time_char=time.localtime(time.time())):
		#초 -----> ['48']
		return [time.strftime('%S',time_char)]

	def read_time_today(self, time_char=time.localtime(time.time())):
		#종합 -----> ['04/05/02', '22:07:48', '04/05/02 22:07:48','2002-04-05']
		aaa = string.split(time.strftime('%c',time_char))
		total_dash = time.strftime('%Y', time_char)+"-"+time.strftime('%m',time_char)+"-"+time.strftime('%d',time_char)
		return [aaa[0], aaa[1], time.strftime('%c',time_char), total_dash]

	def read_time_week(self, time_char=time.localtime(time.time())):
		#주 -----> ['5', '13', 'Fri', 'Friday']
		return [time.strftime('%w',time_char),time.strftime('%W',time_char),time.strftime('%a',time_char),time.strftime('%A',time_char)]

	def read_time_year(self, time_char=time.localtime(time.time())):
		#년 -----> ['02', '2002']
		return [time.strftime('%y', time_char), time.strftime('%Y', time_char)]

	def sort_datas_on (self, input_datas):
		#aa = [[111, 'abc'], [222, 222],['333', 333], ['777', 'sjpark'], ['aaa', 123],['zzz', 'sang'], ['jjj', 987], ['ppp', 'park']]
		#정렬하는 방법입니다
		temp_result=[]
		for one_data in input_datas:
			for one in one_data:
				temp_resultappend(one.sort())
		return result



	def delete_same_data (self, input_data):
	#리스트데이터중 같은 자료만 삭제
		return "assa"

	def set_unique_data (self, input_data):
	#리스트데이터중 고유한 자료만 남김
		return "assa"



