ANNA PAY – Payroll Notification & Anomaly Alert System

Project Link: https://ctc-negotiable-apg8jd6rs6hzywxmcqkp2y.streamlit.app/

Team: CTC Negotiable

Sprint Duration: 48 Hours

Development Approach: Agile (Sprint 0 + Iterative Build)

Status: Submission Ready

1. Project Overview

This project implements a Notification & Anomaly Alert System for ANNA PAY, a payroll processing platform.
The system monitors payroll activity, evaluates predefined business rules, and automatically triggers alerts when abnormal salary conditions are detected. Every alert is logged to ensure traceability and auditability.
The objective is to transform payroll from a silent transactional system into an observable and accountable process.

2. Problem Statement

Traditional payroll systems:

Process salary

Store payroll records

Generate payslips

However, they do not proactively detect anomalies or communicate unusual salary conditions.

This can result in:

Increased HR workload, 
Delayed issue detection, 
Reduced transparency, 
Lower employee confidence

Our solution introduces an intelligent notification layer to address these gaps.

3. Product Vision

To build a lightweight, event-driven notification system that:
Monitors payroll activity
Detects abnormal salary conditions
Triggers alerts automatically
Maintains a complete audit trail
Scales toward enterprise-level usage

4. Sprint 0 Activities

Before implementation, the team clarified:

Assumptions

Payroll is processed monthly
Payroll execution generates structured salary data
Employees and HR are key stakeholders
Email is the primary notification channel

Identified Risks

Silent payroll errors
Duplicate payroll execution
Alert flooding
Missing anomaly detection
Lack of audit traceability

Initial Backlog

Salary threshold alert
Salary spike detection
Notification logging
Payroll execution workflow
Basic UI for interaction

Sprint 0 ensured requirement clarity before development began.

5. System Design Approach

The system follows an event-driven flow:

Payroll data is persisted
Business rules are evaluated
Alerts are triggered if conditions match
Every alert is logged

This ensures:

Decoupled rule logic
Auditability
Traceability
Scalable design

6. Business Rule Implementation
Rule 1 – Low Salary Alert

If salary < 10,000 → Trigger alert

Purpose: Detect potential payroll processing errors.

Rule 2 – Salary Spike Detection

If salary change > 20% compared to previous month → Trigger alert

Purpose: Identify unusual payroll variations requiring validation.

Rules are modular and extendable for future enhancements.

7. Data Model
Employee

id
name
email

Payroll

id
employee_id
month
salary

NotificationLog

id
employee_id
message
timestamp

Design Principles:

Minimal schema
Historical payroll tracking
Persistent audit logging
Extensibility

8. Architecture Overview

Technology Stack:

Python
Streamlit (UI Layer)
SQLite (Persistence Layer)

Logical Separation:

UI Layer → User interaction
Rule Engine → Business logic
Data Layer → Database operations
Logging Layer → Notification audit tracking

Even within a compact implementation, separation of concerns is maintained.

9. Agile Role Execution
Business Analyst (BA)

Responsibilities:

Defined problem scope
Identified stakeholders
Converted requirements into structured user stories
Framed business rules
Identified operational risks
Prioritized backlog

Impact: Ensured structured requirement understanding before coding.

Developer

Responsibilities:

Designed event-driven payroll flow
Implemented rule engine logic
Designed database schema
Integrated logging mechanism
Built Streamlit UI
Handled edge cases

Impact: Delivered a scalable and logically structured system.

Tester

Responsibilities:

Validated rule trigger accuracy
Tested threshold and spike scenarios
Verified normal payroll runs
Confirmed log persistence
Checked invalid employee handling

Impact: Ensured system reliability and predictable behavior.

10. Testing Strategy
Functional Testing

Correct rule trigger validation
Correct alert message generation
Proper logging behavior
Edge Case Testing
First payroll execution
Consecutive payroll runs
Salary spike from zero base
Invalid employee ID

The system is structured to handle high-volume payroll scenarios.

11. Success Metrics (Target)

99% alert reliability
Alert generation within seconds
Reduction in HR payroll queries

ero silent anomaly scenarios

12. Future Enhancements

Multi-channel notifications (SMS / Push)
User-configurable alert preferences
Retry mechanism with exponential backoff
Analytics dashboard
AI-based anomaly detection
Integration into full ANNA PAY ecosystem

13. How to Run Locally

Install dependencies:

pip install -r requirements.txt

Run application:

streamlit run app.py

Open in browser:

http://localhost:8501

14. Project Philosophy

This project demonstrates:
Requirement-first thinking
Event-driven system design
Risk-aware planning
Structured Agile execution
Observability by design

The focus was not just sending notifications, but building a scalable payroll intelligence layer aligned with enterprise practices.





