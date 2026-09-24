from complaint import register_complaint
from tracking import track_complaint
from admin import admin_login
from reports import view_report

print("=====================================================")
print("         Hostel Complaint Management System  ")
print("=====================================================")

complaint_id = " "
student_id = " "
student_name = " "
block_no = " "
room_no = " "
category = " "
description = " "
priority = " "
status = " "
complaint = { }

while True:
    print(" \n1. Register Complaint")
    print("2. Track Complaint")
    print("3. Admin Login")
    print("4. View Reports")
    print("5. Exit")

    Register = "1. Register Complaint"
    Track = "2. Track Complaint"
    Admin = "3. Admin Login"
    View = "4. View Reports"

    choice = input("Select your purpose:  ")

    #Module 1: Register Complaint
    if choice == "1":

        complaint = register_complaint()

        complaint_id = complaint["complaint_id"]
        student_id = complaint["student_id"]
        student_name = complaint["student_name"]
        block_no = complaint["block_no"]
        room_no = complaint["room_no"]
        category = complaint["category"]
        description = complaint["description"]
        priority = complaint["priority"]
        status = complaint["status"]
        
        
        
    
    #Module 2: Track Complaint    
    elif choice == "2":
        
        track_complaint(complaint)
            
        
    #Module 3: Admin Login
    elif choice == "3":
        admin_login( )       
        
        
    #Module 4: View Reports
    elif choice == "4":
            view_report(complaint)
            
              
    #Exit
    elif choice == "5":
        print("Thank you for using 'Complaint Ease!' ")
        break
        
    
    #Invalid Choice
    else:
        print("Invalid choice. Please, choose again!")
     

