import cx_Oracle
# I put all the sql queries into a different file to clean it up a little bit
from  SQL_Scripts import sql_attendance

conn_str = 'usrnm/pswrd@###'
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
		return {'Student_Number': self.student_number, 'Attendance%': (self.days_present/self.days_enrolled)}
	
attendance = positive_attendance(sql_attendance)

		
df3=pd.DataFrame([a.calculate_attendance() for a in attendance.values()])
print (df3)
#df3.to_excel("AttendanceRP1.xlsx", index=False)



