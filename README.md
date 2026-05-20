# OrangeHRM Selenium Python Automation Framework

## Project Overview

This project is an end-to-end automation testing framework developed for the OrangeHRM application using Selenium, Python, Behave BDD, Allure Reporting, Postman, and Newman.

The framework follows the Page Object Model (POM) design pattern to improve maintainability, scalability, reusability, and stable automation execution.

---

## Tools & Technologies Used

* Python
* Selenium WebDriver
* Behave BDD
* Allure Reporting
* Postman API Testing
* Newman CLI Reporting
* Git & GitHub
* Visual Studio Code
* Chrome Browser
* ChromeDriver
* WebDriver Manager
* Page Object Model (POM)
* Explicit Waits
* Gherkin Syntax
* JSON
* Virtual Environment (venv)
* REST API Testing
* Modular Framework Design

---

## Features Automated

### UI Automation

* Login Validation
* Invalid Login Validation
* Logout Functionality
* Dashboard Validation
* Add Employee
* Update Employee
* Delete Employee
* Employee List Validation
* Search Employee
* Search User
* Leave Module Validation
* Leave Search Validation
* Recruitment Module Validation
* Forgot Password Functionality

---

## API Testing

* GET API Validation
* POST API Validation
* Login API Validation
* Status Code Validation
* Response Validation
* Newman Report Generation

---

## Framework Design

* Page Object Model (POM)
* Reusable Methods
* Explicit Waits
* Modular Framework Structure
* Feature Files using Gherkin Syntax
* Step Definitions using Behave
* Smoke & Regression Tags
* Allure Reporting Integration
* API Testing using Postman
* Newman CLI Execution

---

## Reporting Features

### Allure Report

* Overview
* Suites
* Behaviors
* Packages
* Categories
* Environment
* Executors
* Timeline
* Graphs

### Newman Report

* Total Requests
* Assertions Summary
* Response Time Analysis
* Failed Test Summary
* API Execution Dashboard

---

## Project Structure

```text
OrangeHRM-Selenium-Python/
│
├── features/
│   └── steps/
├── pages/
├── utils/
├── allure-results/
├── allure-report/
├── postman/
├── newman/
├── screenshots/
├── behave.ini
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/Deepak-SWP/OrangeHRM-Selenium-Python.git
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

---

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

---

### Install Required Packages

```bash
pip install -r requirements.txt
```

---

## Run Automation Tests

### Run Behave Tests

```bash
behave
```

---

## Allure Report Setup

### Generate Allure Report

```bash
allure generate allure-results --clean -o allure-report
```

---

### Open Allure Report

```bash
allure open allure-report
```

---

## API Testing Setup

### Newman Installation

```bash
npm install -g newman
npm install -g newman-reporter-htmlextra
```

---

### Run Newman Collection

```bash
newman run "OrangeHRM API Testing.postman_collection.json"
```

---

## Framework Highlights

* End-to-End Test Automation
* UI + API Automation
* BDD Framework Design
* Enterprise-Level Reporting
* Reusable Automation Components
* Stable Synchronization Handling
* Scalable Framework Architecture
* Git Branching & Merge Workflow
* Smoke & Regression Test Execution
* API Automation with Newman Reporting

---

## Screenshots Included

* Allure Overview Dashboard
* Allure Suites Page
* Newman HTML Report
* Postman Login API Success
* VS Code Project Structure
* GitHub Repository Structure

---

## Test Execution Summary

* Total Features Passed: 14
* Total Scenarios Passed: 14
* Total Steps Passed: 61
* 100% Test Execution Success

---

## Team

PyAutomation Crew
