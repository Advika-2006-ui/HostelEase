# HostelEase – Hostel Complaint Management System Project

# 1. Project Title

HostelEase – Hostel Complaint Management System




# 2. Problem Statement

• Hostel students regularly face issues related to electrical facilities, plumbing, cleaning, Wi-Fi, water supply, furniture, and other hostel services.

• When complaints are handled manually, it can become difficult to organize complaint details and track them properly.

• HostelEase is developed as a simple Python-based system to provide a structured way to register, track, and view hostel complaints.




# 3. Objective

• The main objective of HostelEase is to develop a simple complaint management system that helps organize hostel complaints through a structured digital process.

• The project aims to:

- Register hostel complaints.
- Record important complaint details.
- Track complaints using a complaint ID.
- Provide basic administrator authentication.
- Display complaint information in a report format.
- Demonstrate modular Python programming.




# 4. Functional Requirements

(i) Complaint Registration:

• The system should allow a student to enter:

- Student ID
- Student Name
- Block Number
- Room Number
- Complaint Category
- Complaint Description
- Priority

• The system should assign a complaint ID and set its initial status to Pending.

(ii) Complaint Tracking:

• The system should allow the user to enter a complaint ID and view the corresponding complaint details.
• The system should display an appropriate message when an invalid complaint ID is entered.

(iii) Admin Login:

• The system should provide a basic administrator login facility.
• The system should verify the entered username and password and display an appropriate result.

(iv) View Reports:

The system should display the registered complaint details in an organized report format.




# 5. Non-Functional Requirements

(i) Usability:

The system should have a simple menu-driven interface that is easy for users to understand.

(ii) Reliability:

The system should provide consistent results for valid inputs and handle invalid inputs appropriately.

(iii) Maintainability:

The system should use separate modules so that individual parts can be modified more easily.

(iv) Error Handling:

The system should identify invalid inputs and display suitable error messages.




# 6. Technologies and Tools

- Python
- Pydroid 3
- GitHub




# 7. Major Python Concepts Used

The project uses:

- Variables
- Input and output
- Conditional statements
- Loops
- Functions
- Dictionaries
- Lists
- Input validation
- Modular programming




# 8. Expected Outcome

• The completed system should provide a simple workflow for managing hostel complaints.

• A user should be able to register a complaint, track a complaint, access the admin login module, and view a complaint report through the main menu.




# 9. Project Modules

The project is divided into the following modules:

1. Complaint Registration – complaint.py
2. Complaint Tracking – tracking.py
3. Admin Login – admin.py
4. View Reports – reports.py
5. Main Controller – main.py




# 10. Future Enhancements

The system can be enhanced in the future by adding:

- Automatic unique complaint ID generation.
- Permanent data storage.
- Multiple complaint management.
- Complaint status updates.
- Student and administrator dashboards.
- Search and filtering facilities.