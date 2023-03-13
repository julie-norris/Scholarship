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
187251,
300397,
397888,
391330,
391591,
391831,
324588,
330133,
329887,
390830,
329406,
329894,
358266,
324766,
328664,
328913,
325122,
324331,
328968,
385742,
325267,
329177,
329917,
331361,
330598,
322125,
328199,
350088,
331183,
334994,
318523,
334000,
382960,
324770,
324406,
374890,
335357,
385663,
402527,
335471,
396930,
337157,
379961,
333966,
334228,
3631000232,
334877,
325205,
334477,
395767,
374215,
330086,
329441,
379050,
330911,
334359,
350731,
331988,
327342,
329965,
334524,
352797,
395955,
327711,
324697,
334283,
398213,
334784,
363408,
334120,
334605,
386729,
329392,
337113,
330009
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
	AND ada.calendardate BETWEEN TO_DATE( '08/01/2014', 'mm/dd/yyyy' ) 
	AND TO_DATE( '03/09/2018', 'mm/dd/yyyy' )
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
	att_date BETWEEN TO_DATE( '08/01/2014', 'mm/dd/yyyy' ) 
	AND TO_DATE( '03/09/2018', 'mm/dd/yyyy' )  
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
