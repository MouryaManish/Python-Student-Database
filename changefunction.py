import addnewdatabase

def databasedelete():
	global dictdatabase
	deletestring1=raw_input("enter the student ID\n")
	if (addnewdatabase.dictdatabase.has_key(deletestring1)):
		addnewdatabase.dictdatabase.pop(deletestring1)
	else:
		print "Student ID is not present"
	return

def addattendance():
	global dictdatabase
	addattendancestring1=raw_input("enter the student ID\n")
	if (addnewdatabase.dictdatabase.has_key(addattendancestring1)):
		l=addnewdatabase.dictdatabase[addattendancestring1]['attendance']
	else:
		print "Student ID is not present please register"
		return
	addattendancebool=1
	while(addattendancebool):
		addstring1=raw_input("enter p if present and a if absent\n")
		l.append(addstring1)
		addattendancetemp1=raw_input("do you want to enter more press y for yes and n for no\n")
		if addattendancetemp1== 'y':
			continue
		else:
			addnewdatabase.dictdatabase[addattendancestring1]['attendance']=l
			break
	return

def addexammarks():
	global dictdatabase
	addattendancestring1=raw_input("enter the student ID \n")
	if (addnewdatabase.dictdatabase.has_key(addattendancestring1)):
		l=addnewdatabase.dictdatabase[addattendancestring1]['exammarks']
	else:
		print "Student ID is not present"
		return
	addattendancebool=1
	while(addattendancebool):
		addstring1=raw_input("enter exam marks\n")
	#	if '.' in addattendancestring1:
		l.append(float(addstring1))
	#	else:
	#		l.append(int(addattendancestring1))
		addattendancetemp1=raw_input("do you want to enter more press y for yes and n for no\n")
		if addattendancetemp1== 'y':
			continue
		else:
			addnewdatabase.dictdatabase[addattendancestring1]['exammarks']=l
			break
	return

	
def addprojectmarks():
	global dictdatabase
	addattendancestring1=raw_input("enter the student ID \n")
	if (addnewdatabase.dictdatabase.has_key(addattendancestring1)):
		l=addnewdatabase.dictdatabase[addattendancestring1]['projectmarks']	
	else:
		print "Student ID is not present"
		return
	addattendancebool=1
	while(addattendancebool):
		addstring1=raw_input("enter project marks\n")
	#	if '.' in addattendancestring1:
		l.append(float(addstring1))
	#	else:
	#		l.append(int(addattendancestring1))
		addattendancetemp1=raw_input("do you want to enter more press y for yes and n for no\n")
		if addattendancetemp1 == 'y':
			continue
		else:
			addnewdatabase.dictdatabase[addattendancestring1]['projectmarks']=l
			break
	return
		
def addassignmentmarks():
	global dictdatabase
	addattendancestring1=raw_input("enter the student ID \n")
	if (addnewdatabase.dictdatabase.has_key(addattendancestring1)):
		l=addnewdatabase.dictdatabase[addattendancestring1]['assignmentmarks']	
	else:
		print "Student ID is not present"
		return
	addattendancebool=1
	while(addattendancebool):
		addstring1=raw_input("enter project marks\n")
#		if '.' in addattendancestring1:
		l.append(float(addstring1))
#		else:
#			l.append(int(addattendancestring1))
		addattendancetemp1=raw_input("do you want to enter more press y for yes and n for no\n")
		if addattendancetemp1 == 'y':
			continue
		else:
			addnewdatabase.dictdatabase[addattendancestring1]['assignmentmarks']=l
			break
	return


def editattendance():
	global dictdatabase
	addattendancestring1=raw_input("enter the student ID\n")
	if (addnewdatabase.dictdatabase.has_key(addattendancestring1)):
		l=addnewdatabase.dictdatabase[addattendancestring1]['attendance']
	else:
		print "Student ID is not present"
		return
	x=int(raw_input("enter the class no. you want to change\n"))
	addstring1=raw_input("enter p if present and a if absent\n")
	l[x-1]=addstring1
#	addattendancetemp1=raw_input("do you want to enter more press y for yes and n for no\n")
#	"""if addattendancetemp1== 'y':
#		continue
#	else:
	addnewdatabase.dictdatabase[addattendancestring1]['attendance']=l
#		break"""
	return


def editassignmentmarks():
	global dictdatabase
	addattendancestring1=raw_input("enter the student ID\n")
	if (addnewdatabase.dictdatabase.has_key(addattendancestring1)):
		l=addnewdatabase.dictdatabase[addattendancestring1]['assignmentmarks']	
	else:
		print "Student ID is not present"
		return
	x=int(raw_input("enter the assignment no. of which you want to change the marks\n"))
	addstring1=float(raw_input("enter assignment marks\n"))
	#if '.' in addattendancestring1:
	l[x-1]=addstring1
	#else:
	#	l[x-1]=(int(addattendancestring1))
#	addattendancetemp1=raw_input("do you want to enter more press y for yes and n for no\n")
#	if addattendancetemp1 == 'y':
#		continue
#	else:
	addnewdatabase.dictdatabase[addattendancestring1]['assignmentmarks']=l
#		break
	return	
