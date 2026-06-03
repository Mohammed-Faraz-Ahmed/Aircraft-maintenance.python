# ✈️ Aircraft Maintenance Tracking System

A Python-based Aircraft Maintenance Tracking System designed to simulate flight-hour-based maintenance planning and tracking for aircraft. This project demonstrates how aviation maintenance schedules can be monitored, forecasted, and managed using object-oriented programming principles.

---

## 📌 Overview

Aircraft maintenance planning is a critical part of Continuing Airworthiness Management (CAMO). This project models a simplified maintenance tracking system that:

* Tracks aircraft flight hours
* Monitors maintenance intervals
* Identifies due and overdue maintenance tasks
* Records completed maintenance actions
* Forecasts upcoming maintenance events
* Generates maintenance reports

The goal of this project is to bridge aviation maintenance concepts with software development using Python.

---

## 🚀 Features

### Aircraft Management

* Create aircraft records
* Store aircraft identification and model information
* Track current flight hours

### Maintenance Scheduling

* Add maintenance intervals based on flight hours
* Define last performed maintenance hours
* Automatically calculate next due maintenance

### Due & Overdue Tracking

* Detect maintenance that is due
* Highlight overdue maintenance tasks
* Calculate overdue flight hours

### Maintenance Forecasting

* Display upcoming maintenance events
* Sort maintenance tasks by urgency
* Show remaining hours until maintenance is required

### Maintenance History

* Log completed maintenance actions
* Store maintenance completion date and flight hours
* Maintain maintenance records for future reference

### Reporting

* Generate aircraft maintenance reports
* Display maintenance status summaries
* Provide maintenance planning information

---

## 🛠 Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Datetime Module
* Type Hints
* Dictionaries & Lists

---

## 📂 Project Structure

```text
Aircraft Maintenance Tracking System
│
├── MaintenanceRecord Class
│   ├── Maintenance Type
│   ├── Due Hours
│   ├── Last Performed Hours
│   └── Next Due Hours
│
├── Aircraft Class
│   ├── Aircraft Information
│   ├── Maintenance Schedules
│   ├── Maintenance History
│   ├── Due Maintenance Checks
│   ├── Maintenance Reporting
│   └── Maintenance Status Display
│
└── Main Program
    ├── Create Aircraft
    ├── Add Maintenance Tasks
    ├── Simulate Flight Operations
    ├── Perform Maintenance
    └── Generate Reports
```

---

## 🔧 Example Maintenance Tasks

The system can track maintenance activities such as:

* Oil Change
* Tire Inspection
* Hydraulic System Check
* Avionics Update
* Engine Overhaul

Additional maintenance tasks can easily be added by defining new maintenance schedules.

---

## 📊 Sample Workflow

```text
Aircraft Created
        ↓
Add Maintenance Schedules
        ↓
Update Flight Hours
        ↓
Check Due Maintenance
        ↓
Perform Maintenance
        ↓
Update Next Due Hours
        ↓
Generate Maintenance Report
```

---

## 🎯 Learning Objectives

This project was developed to:

* Understand Python Object-Oriented Programming
* Explore aviation maintenance planning concepts
* Simulate CAMO-related maintenance tracking workflows
* Learn how maintenance data can be structured programmatically
* Practice building industry-relevant software projects

---

## 🔮 Future Improvements

Planned enhancements include:

* CSV Export Functionality
* Excel Report Generation
* Fleet Management for Multiple Aircraft
* Aircraft Registration Database
* GUI Dashboard
* Maintenance Calendar View
* Aircraft Utilization Forecasting
* Maintenance Cost Tracking
* A-Check / C-Check Monitoring
* SQLite Database Integration

---

## ✈ Aviation Relevance

This project is inspired by real-world maintenance planning activities performed within:

* CAMO (Continuing Airworthiness Management Organisation)
* MRO (Maintenance, Repair & Overhaul)
* Airline Engineering Departments
* Aircraft Maintenance Planning Teams

While simplified for educational purposes, the project demonstrates fundamental concepts used in aircraft maintenance scheduling and airworthiness management.

---

## 🤖 AI Assistance Disclosure

This project was developed using **Python with GitHub Copilot assistance**. The objective was not only to build the system but also to study and understand how aviation maintenance planning concepts can be implemented programmatically.

---

## 📚 Author

**Mohammed Faraz Ahmed**
Aeronautical Engineering Student
Aspiring CAMO / Continuing Airworthiness Professional
---

### ⭐ If you found this project interesting, consider giving it a star! ✈️
