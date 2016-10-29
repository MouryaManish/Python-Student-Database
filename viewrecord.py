import addnewdatabase
import totalgrade

def viewattendance():
	totalgrade.statattendance()
	return

def viewexammarks():
	totalgrade.statexammarks()
	return

def viewassignmentmarks():
	totalgrade.statassignmentmarks()
	return

def viewprojectmarks():
	totalgrade.statprojectmarks()
	return
	
def viewtotalrecord():
	global dictdatabase
	viewstring1=raw_input("enter the student id\n")
	if addnewdatabase.dictdatabase.has_key(viewstring1):
		viewlist1 = addnewdatabase.dictdatabase[viewstring1]["personalinformation"]
		viewlist2 = addnewdatabase.dictdatabase[viewstring1]["attendance"]
		viewlist3 = addnewdatabase.dictdatabase[viewstring1]["exammarks"]
		viewlist4 =  addnewdatabase.dictdatabase[viewstring1]["assignmentmarks"]
		viewlist5 = addnewdatabase.dictdatabase[viewstring1]["projectmarks"]

		print "name: ",viewlist1[0],"		","DOB: ",viewlist1[1],"		","Student ID: ",viewlist1[2]

		print "Student's Attendance "
		for i in range(0,len(viewlist2),1):
			print "Attendance ",(i+1),":",viewlist2[i],"		",
			if ((i%4)==0):
				print
		templist1=totalgrade.totalgrade(viewlist2)
		print "Total Attendance percentage: ",templist1[0],"		","scaled down Attendance percentage is:",templist1[1]

		print "Student's Exam marks "
		for i in range(0,len(viewlist3),1):
			print "Exam marks ",(i+1),":",viewlist3[i],"		",
			if ((i%4)==0):
				print
		templist1=totalgrade.totalgrade(viewlist3)
		print "Total Exam percentage: ",templist1[0],"		","scaled down Exam percentage is:",templist1[1]
		
		print "Student's Assignment marks"
		for i in range(0,len(viewlist4),1):
			print "Assignment marks ",(i+1),":",viewlist4[i],"		",
			if ((i%4)==0):
				print
		templist1=totalgrade.totalgrade(viewlist4)
		print "Total Assignment percentage: ",templist1[0],"		","scaled down Assignment percentage is:",templist1[1]
		
		
		print "Student's Project marks "
		for i in range(0,len(viewlist5),1):
			print "Project marks ",(i+1),":",viewlist5[i],"		",		
			if ((i%4)==0):
				print
		templist1=totalgrade.totalgrade(viewlist5)
		print "Total Project percentage: ",templist1[0],"		","scaled down project percentage is:",templist1[1]
		
	else:
		print "The student ID entered is not present in the record\n"
		return
	return

