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
| Postman            | API Testing                 |
| Newman             | Postman CLI Execution       |
| Git & GitHub       | Version Control             |
| GitHub Actions     | CI/CD Pipeline              |
| VS Code            | IDE                         |
| Chrome Browser     | Test Execution              |
| ChromeDriver       | Browser Driver              |
| WebDriver Manager  | Driver Management           |
| CSV                | Data Driven Testing         |
| JSON               | API Validation              |
| Logging Module     | Execution Logging           |
| pytest-xdist       | Parallel Execution Support  |

---

# Framework Design

The framework follows the Page Object Model (POM) design pattern.

## Framework Components

### 1. Feature Files

Feature files are written using Gherkin syntax.

These files contain:

* Scenarios
* Given
* When
* Then steps

Example:

```gherkin
Feature: Login Functionality

Scenario: Valid Login

Given user is on login page
When user enters valid username and password
Then user should navigate to dashboard
```

---

### 2. Step Definition Files

Step definition files contain Python code implementation for feature file steps.

These files connect feature file steps with automation code.

---

### 3. Page Object Model (POM)

Each application page has a separate Python class.

Examples:

* Login Page
* Dashboard Page
* Employee Page
* Leave Page
* Recruitment Page

POM helps in:

* Reusability
* Better maintenance
* Reduced code duplication
* Easy locator management

---

### 4. Utility Files

Utility files contain reusable common functionalities.

Examples:

* Driver setup
* Logging
* Configuration handling

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

## Newman Reports

Newman Reports provide:

* Request Summary
* API Response Validation
* Assertion Results
* Execution Summary

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
├── newman/
├── pages/
├── postman/
│
├── screenshots/
├── testdata/
│   └── login_data.csv
│
├── utils/
│   ├── config.py
│   ├── driver_setup.py
│   └── logger.py
│
├── .gitignore
├── README.md
├── behave.ini
├── requirements.txt
│
└── automation.log
```

---

# How to Install the Project

## Step 1: Clone Repository

```bash
git clone <repository_url>
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

---

# Test Execution Summary

The framework successfully automates:

* 14 Features
* 14 Scenarios
* 61 Steps

---

# Conclusion

This project demonstrates a complete automation testing framework using Selenium Python with BDD framework integration, reporting tools, API testing, reusable framework architecture, logging, CI/CD pipeline, and professional automation practices.

The framework is designed to simulate real-time industry automation testing standards and improve software quality through automated validation.
