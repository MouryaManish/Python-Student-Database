import addnewdatabase

def statattendance():
	global dictdatabase
	statattendancestring1=raw_input("enter the student ID\n")
	if (addnewdatabase.dictdatabase.has_key(statattendancestring1)):
		l=addnewdatabase.dictdatabase[statattendancestring1]['attendance']
	else:
		print "Student ID is not present"
		return
	length=len(l)
	count=l.count("p")
	attendancestat=0.0
	attendancestat=round((count/float(length))*100)
	print "the attendance statistic is:",attendancestat,"%"
	return

def statexammarks():
	global dictdatabase
	statattendancestring1=raw_input("enter the student ID\n")
	if (addnewdatabase.dictdatabase.has_key(statattendancestring1)):
		l=addnewdatabase.dictdatabase[statattendancestring1]['exammarks']
	else:
		print "Student ID is not present"
		return
	length=len(l)
	sum=0.0
	for item in range(0,length,1):
		sum=sum+l[item]
	examstat=0.0
	length=length*100
	examstat=round(sum/length*100)
	print "the exam statistic is:",examstat,"%"
	return

def statprojectmarks():
	global dictdatabase
	statattendancestring1=raw_input("enter the student ID\n")
	if (addnewdatabase.dictdatabase.has_key(statattendancestring1)):
		l=addnewdatabase.dictdatabase[statattendancestring1]['projectmarks']	
	else:
		print "Student ID is not present"
		return
	length=len(l)
	sum=0.0
	for item in range(0,length,1):
		sum=sum+l[item]
	projectstat=0.0
	length=length*100
	projectstat=round(sum/length*100)
	print "the project statistic is:",projectstat,"%"
	return
		
def statassignmentmarks():
	global dictdatabase
	statattendancestring1=raw_input("enter the student ID\n")
	if (addnewdatabase.dictdatabase.has_key(statattendancestring1)):
		l=addnewdatabase.dictdatabase[statattendancestring1]['assignmentmarks']	
	else:
		print "Student ID is not present"
		return
	length=len(l)
	sum=0.0
	for item in range(0,length,1):
		sum=sum+l[item]
	assignmentstat=0.0
	length=length*100
	assignmentstat=round(sum/length*100)
	print "the assignment statistic is:",assignmentstat,"%"
	return

def totalgrade(l):
	if (type(l[0])==str) :
		length=len(l)
		count=l.count("p")
		attendancestat=0.0
		attendancestat=round((count/float(length))*100)
		resultlist=[]
		resultlist.append(attendancestat)
		attendancestat=attendancestat/100*25
		resultlist.append(attendancestat)
		return resultlist

	else :
		length=len(l)
		sum=0.0
		for item in range(0,length,1):
			sum=sum+l[item]
		length=length*100
		commonmarks=0.0
		commonmarks=round(sum/length*100)
		resultlist=[]
		resultlist.append(commonmarks)
		commonmarks=commonmarks/100*25
		resultlist.append(commonmarks)
		return resultlist
