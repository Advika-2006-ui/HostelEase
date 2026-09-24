# HOSTELEASE
# Module 2: Track Complaint

def track_complaint(complaint):

    print("\n~~~~~~~~~~~~ Track Complaint ~~~~~~~~~~~~")

    track_id = input("Enter Complaint ID: ")

    if track_id == complaint.get("complaint_id"):

        print("\n---------- Complaint Details ----------")

        print("Complaint ID :", complaint["complaint_id"])
        print("Student ID   :", complaint["student_id"])
        print("Student Name :", complaint["student_name"])
        print("Block No.    :", complaint["block_no"])
        print("Room No.     :", complaint["room_no"])
        print("Category     :", complaint["category"])
        print("Description  :", complaint["description"])
        print("Priority     :", complaint["priority"])
        print("Status       :", complaint["status"])

    else:
        print("\nComplaint ID not found!")