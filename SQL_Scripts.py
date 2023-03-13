sql_studentinfo = '''
SELECT
	S.STUDENT_NUMBER,
	S.CITY,
	S.LAST_NAME,
	S.FIRST_NAME,
	S.SchoolID,
	R.ENTRYDATE,
	R.EXITDATE,
	R.ENTRYCODE,
	R.GRADE_LEVEL
FROM
	STUDENTS S 
LEFT OUTER JOIN REENROLLMENTS R ON S.ID = R.STUDENTID 
WHERE
	R.EXITDATE > R.ENTRYDATE 
	AND S.STUDENT_NUMBER IN (
XXXXlist of student numbersXXX
)
'''

sql_attendance = '''
SELECT
	s.Student_Number,
	s.Last_Name,	
	s.First_Name,
	(
SELECT
	coalesce( sum( ada.membershipvalue ), 0 ) 
FROM
	PS_adaadm_defaults_all ada 
WHERE
	ada.studentid = s.id 
	AND ada.calendardate BETWEEN TO_DATE( '08/01/2021', 'mm/dd/yyyy' ) 
	AND TO_DATE( '03/09/2022', 'mm/dd/yyyy' )
	) Days_Enrolled,
	(
SELECT
	coalesce( sum( ada.attendancevalue ), 0 ) 
FROM
	PS_adaadm_defaults_all ada 
WHERE
	ada.studentid = s.id 
	AND ada.calendardate BETWEEN TO_DATE( '08/01/2014', 'mm/dd/yyyy' ) 
	AND TO_DATE( '03/09/2018', 'mm/dd/yyyy' )
	) Days_Present,
	(
SELECT
	count( att_date ) 
FROM
	(
SELECT
	studentid,
	att_date 
FROM
	ps_attendance_meetinter pm 
WHERE
	att_date BETWEEN TO_DATE( '08/01/2021', 'mm/dd/yyyy' ) 
	AND TO_DATE( '03/09/2022', 'mm/dd/yyyy' )  
	AND att_code IN ( 'U', 'A', 'I', 'M', 'E', 'F', 'K', 'S', 'C' ) 
	AND pm.studentID = s.ID 
GROUP BY
	studentid,
	att_date 
	) 
	) Days_Absent
FROM
	Students s
	WHERE s.student_number IN (
398679,
403553,
396949,
329928,
404221,
317071,
357604,
329183,
323998,
324081,
323756
)
	 '''
