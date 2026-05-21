# OrangeHRM Selenium Python Automation Framework

---

## Project Overview

This project is an end-to-end automation testing framework developed for the OrangeHRM application using Selenium, Python, Behave BDD, Allure Reporting, Postman, Newman, and GitHub Actions.

The framework follows the Page Object Model (POM) design pattern to improve maintainability, scalability, reusability, synchronization handling, and stable automation execution.

---

## Tools & Technologies Used

* Python
* Selenium WebDriver
* Behave BDD
* Allure Reporting
* Postman API Testing
* Newman CLI Reporting
* Git & GitHub
* GitHub Actions
* Visual Studio Code
* Chrome Browser
* ChromeDriver
* Page Object Model (POM)
* Explicit Waits
* Gherkin Syntax
* JSON
* CSV
* Virtual Environment (venv)
* REST API Testing
* Modular Framework Design
* Python Logging Module
* pytest-xdist

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
* Logging Framework Integration
* Try-Catch Exception Handling
* Assertions and Validation Handling
* False Failure & False Pass Reduction
* Data Driven Testing (DDT) using CSV
* Reusable Driver Initialization
* Synchronization Handling using Explicit Waits
* Parallel Execution Support using pytest-xdist
* Basic CI/CD Pipeline using GitHub Actions
* Stable URL-Based Verification
* JavaScript Executor Click Handling
* Professional Logging Strategy
* Dynamic Wait Handling

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
├── .github/
│   └── workflows/
│       └── automation.yml
│
├── drivers/
│   └── chromedriver.exe
│
├── features/
│   ├── steps/
│   ├── environment.py
│   └── *.feature
│
├── logs/
│   └── automation.log
│
├── pages/
│
├── utils/
│   ├── driver_setup.py
│   ├── config.py
│   └── logger.py
│
├── testdata/
│   └── login_data.csv
│
├── allure-results/
├── allure-report/
├── postman/
├── newman/
├── screenshots/
│
├── behave.ini
├── requirements.txt
└── README.md
```
---

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/your-username/OrangeHRM-Selenium-Python.git
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

## Execution Commands

### Run Behave Tests

```bash
behave
```

---

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

## CI/CD Pipeline Setup

### GitHub Actions Workflow

The framework includes a basic CI/CD pipeline using GitHub Actions for automated execution.

Workflow File Path:

```text
.github/workflows/automation.yml
```

The pipeline performs:

* Repository Checkout
* Python Setup
* Dependency Installation
* Behave Test Execution
* Allure Report Generation

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
* Logging and Exception Handling Framework
* Stable Synchronization using Explicit Waits
* False Failure Reduction Mechanism
* Basic Data Driven Testing using CSV
* Reusable Utilities and Modular Components
* Parallel Execution Support using pytest-xdist
* Basic CI/CD Pipeline using GitHub Actions

---

## Screenshots Included

* Allure Overview Dashboard
* Allure Suites Page
* Newman HTML Report
* Postman Login API Success
* VS Code Project Structure
* GitHub Repository Structure
* GitHub Actions Workflow Execution

---

## Test Execution Summary

* Total Features Passed: 14
* Total Scenarios Passed: 14
* Total Steps Passed: 61
* 100% Test Execution Success

---

## Team

PyAutomation Crew