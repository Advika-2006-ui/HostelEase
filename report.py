# Module 4: View Reports

def view_report(complaint):

    print("\n==================== View Reports ====================")

    if complaint["complaint_id"] != "":
        
        print("\n~~~~~~~~~~~~ Complaint Report ~~~~~~~~~~~~")

        print("Complaint ID :", complaint["complaint_id"])
        print("Student ID   :", complaint["student_id"])
        print("Student Name :", complaint["student_name"])
        print("Block No.    :", complaint["block_no"])
        print("Room No.     :", complaint["room_no"])
        print("Category     :", complaint["category"])
        print("Description  :", complaint["description"])
        print("Priority     :", complaint["priority"])
        print("Status       :", complaint["status"])

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    else:
        print("\nNo complaint registered yet.")