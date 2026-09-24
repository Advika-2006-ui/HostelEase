# Design Decisions

1. Modular Design:

    • The project is divided into separate Python files based on their functions:
        - main.py controls the main menu.
        - complaint.py handles complaint registration.
        - tracking.py handles complaint tracking.
        - admin.py handles admin login.
        - report.py handles complaint reports.

    • This makes the program easier to understand, test, and maintain.
    
    

 2. Menu-Driven Interface:

    • A menu-driven interface is used so that the user can easily select the required operation.

    • The main menu provides options for registering, tracking, and viewing complaints, along with admin login and exit.



3. Dictionary for Complaint Data:

    • A dictionary is used to store the details of a complaint.

    • It stores information such as:

        - Complaint ID
        - Student ID
        - Student Name
        - Block and Room Number
        - Category
        - Description
        - Priority
        - Status

    • Using a dictionary makes it easier to access individual complaint details.



4. Input Validation:

    • Input validation is used for important choices such as complaint category and priority.
    
    • Invalid inputs are rejected and the user is asked to enter a valid choice.



5. Function-Based Programming:

    • Functions are used to perform individual tasks in each module.
    
    • This keeps the code organized and reduces unnecessary repetition.



6. In-Memory Data Storage:

    • The current version stores complaint information temporarily while the program is running.

    • Permanent storage using a file or database can be added in a future version.



7. Simple User Interface:

    • The system uses a simple text-based interface because the project is designed as a beginner-level Python application.

    • The interface provides clear menus, input prompts, and result messages.