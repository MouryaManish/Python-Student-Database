import addnewdatabase
import changedatabase
import viewrecord

print "		Students Rack		"
while(1):
	print "1. Add New Record\n2. Modify Record\n3.View Complete Statistic\n4. Quit"
	mainchoice=int(raw_input("Enter Your Choice\n"))
	if mainchoice == 1:
		addnewdatabase.addnewdatabase()
	if mainchoice == 2:
		changedatabase.functioncall()
	if mainchoice== 3:
		while(1):
			print "1. Complete Record\n2. Attendance Status\n3. Exam Marks Status\n4. Project Marks Status\n 5. Assignment Marks Status\n6. Quit\n"
			mainchoice2=int(raw_input("Enter Your Choice\n"))
			if mainchoice2==1:
				viewrecord.viewtotalrecord()
			
			if mainchoice2==2:
				viewrecord.viewattendance()
			
			if mainchoice2==3:
				viewrecord.viewexammarks()
		
			if mainchoice2==4:
				viewrecord.viewprojectmarks()
			
			if mainchoice2==5:
				viewrecord.viewassignmentmarks()
			if mainchoice2==6:
				break
			
	if mainchoice == 4:
		break
exit()




