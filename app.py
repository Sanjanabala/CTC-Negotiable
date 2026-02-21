
import streamlit as st
import sqlite3
from datetime import datetime
import os
st.write("APP STARTED")

# ---------------- DATABASE SETUP ----------------

DB_NAME = "database.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS payroll (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER,
            month TEXT,
            salary REAL
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS notification_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER,
            message TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()

init_db()

# ---------------- UI ----------------

st.title("Payroll Notification & Anomaly Alert System")
st.markdown("### ANNA PAY")

menu = st.sidebar.selectbox(
    "Select Option",
    ["Add Employee", "Run Payroll", "View Logs"]
)

# ---------------- ADD EMPLOYEE ----------------

if menu == "Add Employee":
    st.subheader("Add New Employee")

    name = st.text_input("Employee Name")
    email = st.text_input("Employee Email")

    if st.button("Add Employee"):
        if name and email:
            conn = get_connection()
            c = conn.cursor()
            c.execute("INSERT INTO employee (name, email) VALUES (?, ?)", (name, email))
            conn.commit()
            new_id = c.lastrowid
            conn.close()

            st.success(f"Employee Added Successfully! ID: {new_id}")
        else:
            st.error("Please fill all fields")

# ---------------- RUN PAYROLL ----------------

elif menu == "Run Payroll":
    st.subheader("Run Payroll")

    employee_id = st.number_input("Employee ID", min_value=1, step=1)
    month = st.text_input("Month")
    salary = st.number_input("Salary", min_value=0.0)

    if st.button("Process Payroll"):

        conn = get_connection()
        c = conn.cursor()

        # Check employee
        c.execute("SELECT name, email FROM employee WHERE id = ?", (employee_id,))
        employee = c.fetchone()

        if not employee:
            st.error("Employee ID not found!")
            conn.close()
        else:
            # Insert payroll
            c.execute("INSERT INTO payroll (employee_id, month, salary) VALUES (?, ?, ?)",
                      (employee_id, month, salary))
            conn.commit()

            # Fetch last 2 salaries
            c.execute("""
                SELECT salary FROM payroll
                WHERE employee_id = ?
                ORDER BY id DESC LIMIT 2
            """, (employee_id,))
            salaries = c.fetchall()

            message = None

            # Rule 1: Low salary
            if salary < 10000:
                message = f"Low Salary Alert: {salary}"

            # Rule 2: >20% change
            elif len(salaries) > 1:
                previous_salary = salaries[1][0]
                if previous_salary != 0:
                    change = abs(salary - previous_salary) / previous_salary
                    if change > 0.2:
                        message = f"Salary changed >20%. Previous: {previous_salary}, Current: {salary}"

            if message:
                # Simulate email
                print("Sending email to:", employee[1])
                print("Message:", message)

                c.execute("INSERT INTO notification_log (employee_id, message, timestamp) VALUES (?, ?, ?)",
                          (employee_id, message, str(datetime.now())))
                conn.commit()

                st.warning("⚠️ Alert Triggered!")
                st.write(message)
            else:
                st.success("Payroll Processed Successfully — No Alerts")

            conn.close()

# ---------------- VIEW LOGS ----------------

elif menu == "View Logs":
    st.subheader("Notification Logs")

    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM notification_log")
    logs = c.fetchall()
    conn.close()

    if logs:
        for log in logs:
            st.write(f"Employee ID: {log[1]}")
            st.write(f"Message: {log[2]}")
            st.write(f"Time: {log[3]}")
            st.markdown("---")
    else:
        st.info("No notifications yet.")