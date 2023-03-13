""" This requirement was removed from criteria"""

import cx_Oracle
# I put all the sql queries into a different file to clean it up a little bit
from  SQL_Scripts import sql_attendance

conn_str = 'XXXX/XXXX@XXXX/XXX'
conn = cx_Oracle.connect(conn_str)
c = conn.cursor()

import pandas as pd
import numpy as np
import sys


import os

cwd=os.getcwd()
os.chdir("C:\\Oracle\\RichmondPromise")


def positive_attendance(query):
	'''creates an object of student attendance data'''
	results = c.execute(query)
	attendance= {}
	for row in results:
		student_number =int(row[0])
		attendance[student_number]=StudentAttendance(student_number, int(row[3]), int(row[4]), int(row[5]) )		
	return (attendance)
	
class StudentAttendance:
	'''creates record for the attendance of a student'''
	
	def __init__(self, student_number, days_enrolled, days_present, days_absent):
		self.student_number = student_number
		self.days_enrolled = days_enrolled
		self.days_present = days_present
		self.days_absent = days_absent
		
				
	def calculate_attendance(self):
    		#return float(self.days_present/self.days_enrolled )
		return {'Student_Number': self.student_number, 'Attendance%': (self.days_present/self.days_enrolled)}
	
attendance = positive_attendance(sql_attendance)

#for student_number, StudentAttendance in attendance.items():
	#	results =  ('%s %s' % (StudentAttendance.student_number, StudentAttendance.calculate_attendance()))
		#print (results)
		
df=pd.DataFrame([a.calculate_attendance() for a in attendance.values()])
#, index=index, columns=['Student_Number', 'AttendancePercentage'])
writer=pd.ExcelWriter('AttendanceYR.xlsx')

#writes the new df to excel
df.to_excel(writer, engine=engine)

