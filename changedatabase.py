#from addnewdatabase import dictdatabase
import changefunction


def functioncall():
	while (1):
		print "1. delete\n2. add attendance\n3. add exam marks\n4. add project marks\n5. add assignment marks\n6. edit attendance\n7. edit assignment marks\n8. To go to previous menu\n"
		changechoiceip=int(raw_input("enter your choice please:\n"))
		if changechoiceip == 1:
			changefunction.databasedelete()
	
		if changechoiceip == 2:
			changefunction.addattendance()
	
		if changechoiceip == 3:
			changefunction.addexammarks()

		if changechoiceip == 4:
			changefunction.addprojectmarks()
	
		if changechoiceip == 5:
			changefunction.addassignmentmarks()
		
		if changechoiceip==6:
			changefunction.editattendance()
	
		if changechoiceip==7:
			changefunction.editassignmentmarks()
		
		if changechoiceip==8:
			break
	return
	
	
