dictdatabase={} 
def addnewdatabase():
	while True:
# personal information
		print "\nenter personal information\n"
		newstring1=raw_input("enter the name\n")
		newstring2=raw_input("enter the date of birth\n")
		newstring4=raw_input("enter the ID no.\n")
		newpersonalinfo=[newstring1,newstring2,newstring4]
# attendance input
		print "\nenter attendence database\n"	
		newattendance=[]
		newstring3=raw_input("enter p for present and a for abscent\n")
		if newstring3=='p':
			newattendance.append(newstring3)
		else:
			newattendance.append(newstring3)
# exam marks
		newexammarks=[]
		newstring3=raw_input("\nenter the exam marks scored\n")
	#	if '.' in newstring3:
		newexammarks.append(float(newstring3))
		#else:
		#	newexammarks.append(int(newstring3))
# assignment marks
		newassignmentmarks=[]
		newstring3=raw_input("\nenter the assignment marks scored\n")
		#if '.' in newstring3:
		newassignmentmarks.append(float(newstring3))
		#else:
		#	newassignmentmarks.append(int(newstring3))
# project marks
		newprojectmarks=[]
		newstring3=raw_input("\nenter the project marks scored\n")
		#if '.' in newstring3:
		newprojectmarks.append(float(newstring3))
		#else:
		#	newprojectmarks.append(int(newstring3))
# adding all the list to dictionary with student id as key for whole record of his
		global dictdatabase
		dictdatabase[newstring4]={"personalinformation":newpersonalinfo,"attendance":newattendance,"exammarks":newexammarks,"assignmentmarks":newassignmentmarks,"projectmarks":newprojectmarks}	
		print dictdatabase
		newdatachoice= raw_input("\ndo you want to add more press y for yes and n for no\n")
		if (newdatachoice== "Y" or newdatachoice == "y"):
			continue
		else:
			break
	return

		
	


