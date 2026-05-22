````md
![CI](https://github.com/Deepak-SWP/OrangeHRM-Selenium-Python/actions/workflows/automation.yml/badge.svg)

# OrangeHRM Selenium Python Automation Framework

## Project Overview

This project is a complete end-to-end automation testing framework developed for the OrangeHRM application using Selenium with Python.

The framework is designed using the Page Object Model (POM) design pattern to improve code reusability, maintainability, scalability, synchronization handling, and stable test execution.

The project covers both UI Automation Testing and API Testing using modern automation tools and frameworks.

---

# Objectives of the Project

* Automate OrangeHRM web application functionalities
* Perform end-to-end UI testing
* Validate application workflows using BDD approach
* Generate professional automation reports
* Perform API testing using Postman and Newman
* Implement reusable and modular automation framework
* Integrate CI/CD using GitHub Actions

---

# Tools & Technologies Used

| Tool / Technology  | Purpose                     |
| ------------------ | --------------------------- |
| Python             | Programming Language        |
| Selenium WebDriver | UI Automation               |
| Behave BDD         | Behavior Driven Development |
| Allure Reports     | Reporting                   |
| HTML Reports       | Execution Reporting         |
| Postman            | API Testing                 |
| Newman             | Postman CLI Execution       |
| Git & GitHub       | Version Control             |
| GitHub Actions     | CI/CD Pipeline              |
| VS Code            | IDE                         |
| Chrome Browser     | Test Execution              |
| WebDriver Manager  | Driver Management           |
| CSV                | Data Driven Testing         |
| JSON               | API Validation              |
| Logging Module     | Execution Logging           |
| pytest-xdist       | Parallel Execution Support  |

---

# Framework Architecture

```text
PyAutomation Crew
       │
       ▼
Feature Files (BDD - Gherkin)
       │
       ▼
Step Definitions (Behave)
       │
       ▼
Page Object Model (POM)
       │
       ▼
Reusable Utilities
(driver setup, logger, config)
       │
       ▼
Selenium WebDriver
       │
       ▼
OrangeHRM Application
       │
       ▼
Allure Reports / HTML Reports / Logs / Screenshots
       │
       ▼
GitHub Actions CI/CD
````

## Architecture Explanation

* Feature files contain business scenarios using Given-When-Then syntax.
* Step definition files implement automation logic for feature steps.
* Page Object Model (POM) handles web elements and reusable page actions.
* Utility files manage reusable configurations like browser setup, logging, and credentials.
* Selenium WebDriver performs browser automation.
* Allure Reports and HTML Reports generate execution insights and graphical reports.
* GitHub Actions provides CI/CD pipeline automation.

---

# Features Automated

## UI Automation

### Authentication Module

* Valid Login
* Invalid Login
* Logout Functionality
* Forgot Password

### Dashboard Module

* Dashboard Validation

### PIM Module

* Add Employee
* Update Employee
* Delete Employee
* Search Employee
* Employee List Validation

### Leave Module

* Open Leave Module
* Search Leave Records

### Admin Module

* Search User Records

### Recruitment Module

* Recruitment Page Validation

---

# API Testing

API testing is performed using Postman and Newman.

## API Validations

* GET Request Validation
* POST Request Validation
* Login API Validation
* Status Code Validation
* Response Validation

---

# Reporting

## Allure Reports

Allure Reports provide:

* Test Execution Summary
* Passed and Failed Tests
* Graphical Representation
* Timeline Reports
* Behaviors
* Suites
* Packages

## HTML Reports

HTML reports provide:

* Scenario Execution Details
* Pass/Fail Status
* Step Execution Summary
* Clean Professional UI

Report Location:

```text
html-report/report.html
```

---

# Logging

Python Logging module is used to track automation execution.

Logs help in:

* Debugging
* Failure Analysis
* Execution Tracking

Log file:

```text
logs/automation.log
```

---

# Data Driven Testing (DDT)

CSV file is used for Data Driven Testing.

Example:

```text
testdata/login_data.csv
```

The framework reads login credentials from CSV files and executes tests dynamically.

---

# CI/CD Integration

GitHub Actions is used for CI/CD pipeline integration.

Whenever code is pushed to GitHub:

* Workflow starts automatically
* Dependencies are installed
* Automation tests execute automatically

Workflow file location:

```text
.github/workflows/automation.yml
```

---

# Defect Handling

The framework includes sample defect reporting documentation to demonstrate defect identification, severity classification, and reporting workflow followed in real-time QA processes.

Defect report file:

```text
defect_report.md
```

---

# Project Structure

```text
OrangeHRM-Selenium-Python/
│
├── .github/
│   └── workflows/
│       └── automation.yml
│
├── allure-report/
├── allure-results/
│
├── features/
│   ├── steps/
│   ├── environment.py
│   └── *.feature
│
├── html-report/
│   └── report.html
│
├── logs/
│   └── automation.log
│
├── newman/
├── pages/
├── postman/
├── screenshots/
│
├── testdata/
│   └── login_data.csv
│
├── utils/
│   ├── config.py
│   ├── driver_setup.py
│   └── logger.py
│
├── defect_report.md
├── README.md
├── requirements.txt
├── behave.ini
└── .gitignore
```

---

# How to Install the Project

## Step 1: Clone Repository

```bash
git clone https://github.com/Deepak-SWP/OrangeHRM-Selenium-Python.git
```

---

## Step 2: Open Project

Open project in VS Code.

---

## Step 3: Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 4: Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# How to Execute Tests

## Run Complete Framework

```bash
behave
```

---

## Run Specific Feature

```bash
behave features/login.feature
```

---

# Generate HTML Report

```bash
behave -f behave_html_pretty_formatter:PrettyHTMLFormatter -o html-report/report.html
```

---

# Open HTML Report

```text
html-report/report.html
```

---

# Generate Allure Report

## Generate Report

```bash
allure generate allure-results --clean -o allure-report
```

---

## Open Report

```bash
allure open allure-report
```

---

# GitHub Actions Execution

After pushing code to GitHub:

* GitHub Actions automatically executes tests
* CI/CD pipeline validates framework execution

---

# Advantages of This Framework

* Reusable Framework
* Scalable Design
* Easy Maintenance
* Better Synchronization Handling
* Reduced Code Duplication
* Professional Reporting
* API + UI Automation
* CI/CD Integration
* Logging Support
* Parallel Execution Support
* Smoke & Regression Execution Support

---

# Test Execution Summary

The framework successfully automates:

* 14 Features
* 14 Scenarios
* 61 Steps
* Smoke & Regression Execution Supported
* CI/CD Workflow Execution Successful

---

# Conclusion

This project demonstrates a complete automation testing framework using Selenium Python with BDD framework integration, reporting tools, API testing, reusable framework architecture, logging, CI/CD pipeline, and professional automation practices.

The framework is designed to simulate real-time industry automation testing standards and improve software quality through automated validation.

```
```
