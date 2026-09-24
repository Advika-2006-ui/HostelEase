# HostelEase – Hostel Complaint Management System

## 1. Project Overview

HostelEase is a simple hostel complaint management system developed to make the process of registering, tracking, and viewing hostel complaints easier.

The system provides a structured way for students to submit complaints related to hostel facilities and allows complaint information to be tracked and viewed through different modules.

## 2. Problem Statement

In hostels, students may face problems related to electrical facilities, plumbing, cleaning, Wi-Fi, water supply, furniture, and other services.

Managing these complaints manually can make it difficult to keep track of complaint details and their current status.

HostelEase provides a simple computer-based solution for organizing this process.

## 3. Objectives

The main objectives of HostelEase are:

- To provide a simple way to register hostel complaints.
- To allow students to track their complaints.
- To provide an admin login facility.
- To display complaint reports in an organized format.
- To use a modular programming approach for easier maintenance.

## 4. Functional Modules

### Module 1 – Complaint Registration

Allows students to enter complaint details such as:

- Student ID
- Student Name
- Block Number
- Room Number
- Complaint Category
- Complaint Description
- Priority

The system assigns a complaint ID and sets the initial status as Pending.

### Module 2 – Complaint Tracking

Allows the user to enter a complaint ID and view the corresponding complaint details.

The system also handles invalid complaint IDs.

### Module 3 – Admin Login

Provides a basic login facility for the administrator.

The system checks the entered username and password and displays an appropriate message for valid or invalid login attempts.

### Module 4 – View Reports

Displays the registered complaint information in an organized report format.

## 5. Non-Functional Requirements

The system is designed with the following non-functional requirements:

- **Usability:** The system should be simple and easy to use.
- **Reliability:** The system should provide consistent results for valid inputs.
- **Maintainability:** The modular structure should make the code easier to modify.
- **Error Handling:** Invalid inputs should be handled with suitable messages.

## 6. Technologies Used

- Python
- Pydroid 3
- GitHub

## 7. Project Structure

```text
HostelEase/
│
├── main.py
├── complaint.py
├── tracking.py
├── admin.py
└── reports.py