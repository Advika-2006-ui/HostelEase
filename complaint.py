# Module 1: Complaint Registration


def register_complaint():

    print("\n~~~~~~~~~~~~ Register Complaint ~~~~~~~~~~~~")

    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")
    block_no = input("Enter your Block no.: ")
    room_no = input("Enter your Wing and Room no.: ")

    # Complaint Category
    print("\nComplaint Category:")
    print("1. Electrical")
    print("2. Plumbing")
    print("3. Cleaning")
    print("4. Wi - Fi")
    print("5. Water Supply")
    print("6. Furniture")
    print("7. Other")

    category_choice = input("Select category: ")

    while category_choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid Category! Please choose between 1 to 7!")
        category_choice = input("Select category: ")

    if category_choice == "1":
        category = "Electrical"

    elif category_choice == "2":
        category = "Plumbing"

    elif category_choice == "3":
        category = "Cleaning"

    elif category_choice == "4":
        category = "Wi - Fi"

    elif category_choice == "5":
        category = "Water Supply"

    elif category_choice == "6":
        category = "Furniture"

    else:
        category = "Other"

    description = input("Enter Complaint Description: ")

    # Priority
    print("\nPriority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    priority_choice = input("Select priority: ")

    while priority_choice not in ["1", "2", "3"]:
        print("Invalid priority! Please choose valid priority!")
        priority_choice = input("Select priority: ")

    if priority_choice == "1":
        priority = "Low"

    elif priority_choice == "2":
        priority = "Medium"

    else:
        priority = "High"

    # Complaint ID
    complaint_id = "C001"

    # Initial status
    status = "Pending"

    # Display complaint
    print("\n================================================")
    print("              COMPLAINT REGISTERED")
    print("================================================")

    print("Complaint ID:", complaint_id)
    print("Student ID:", student_id)
    print("Student Name:", student_name)
    print("Student Block no.:", block_no)
    print("Student Room no.:", room_no)
    print("Your selected Category:", category)
    print("Description of issue:", description)
    print("The priority:", priority)
    print("Status of issue:", status)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # Return complaint information
    complaint = {
        "complaint_id": complaint_id,
        "student_id": student_id,
        "student_name": student_name,
        "block_no": block_no,
        "room_no": room_no,
        "category": category,
        "description": description,
        "priority": priority,
        "status": status
    }

    return complaint