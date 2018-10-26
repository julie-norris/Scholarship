#import os
#from jinja2 import StrictUndefined
# import requests, pprint, json
#from flask import Flask, request, jsonify, render_template, flash, session, redirect


import cx_Oracle
# I put all the sql queries into a different file to clean it up a little bit
from  SQL_Scripts import sql_studentinfo

conn_str = 'usrnm/pssword'
conn = cx_Oracle.connect(conn_str)
c = conn.cursor()

def grades_enrolled(query):
		' ' 'creates dictionary of student numbers as key and all grades enrolled as values' ' '
		query_results = c.execute(query)
		students = {}							
		for row in query_results:
			student_number =int(row[0])
			if student_number in students:
				students[student_number].add_grade(row[8])
			else:
				students[student_number]= Student(student_number, row[2], row[3], row[4], row[8] )
		return students


class  Student:
		'''Represents a student applicant for the Richmond Promise Scholarship'''
		WCCUSDESONLY={5,6}
		WCCUSDESMS={5,6,7,8}
		ES_grades={ 5 }
		ESMS_grades={4, 5, 6, 7, 8}
		MS_grades={ 8, 9, 10, 11} 
		HS_grades={9, 10, 11}
		
		def __init__ (self, student_number, lastname, firstname,  schoolid, grade):
			self.student_number = student_number
			self.lastname= lastname
			self.firstname = firstname
			self.schoolid = schoolid
			self.grades = {grade}
		
			
		def add_grade(self, grade):
			self.grades.add(grade)
		
		""" Determines if student went to wccusd for ES, MS and HS"""
		
		def isEligibleForESMSHS(self):
			if self.ES_grades.issubset(self.grades):
				return True
			else:
				return False
				
		""" The following two functions are only for use with students currently enrolled in charter or private school. They will return true for
		the tier attended within wccusd before transferring to charter/private school '"""
		
		#def isEligibleForES(self):
		#	if self.ES_grades.issubset(self.grades):
		#		return True
		#	else:
		#		return False	
		
	
		#def isEligibleForESMS(self):
		#	if self.ESMS_grades.issubset(self.grades):
		#		return True
		#	else:
		#		return False
		
		""" Determines if the student went to wccusd for MS and HS """
		
		def isEligibleForMSHS(self):	
			if self.MS_grades.issubset(self.grades):
				return True
			else:
				return False
		
		""" Determines if the student went to wccusd for HS"""
						
		def isEligibleForHS(self):
			if self.HS_grades.issubset(self.grades):
				return True
			else:
				return False 
				
		"""Returns the code for the consecutive enrollment tier determined by previous series of functions """
		
		def Tier(self):
			if self.isEligibleForESMSHS():
				return 'ESMSHS'
            
			if self.isEligibleForMSHS():
			   return 'MSHS'
				
			if self.isEligibleForHS():
				return 'HS'
			
			""" The following two are specific to students no longer in wccusd (at charter or private)"""	
			#if self.isEligibleForES():
			#	return 'ES'
				
			#if self.isEligibleForESMS():
			#	return 'ESMS'
		
			
def __str__(self):
	return 'Student'

students = grades_enrolled(sql_studentinfo)

for student_number, student  in students.items():
	results =  ('%s %s	%s %s'  %  (student.student_number, student.lastname, student.schoolid, student.Tier()))
	print (results)
	
