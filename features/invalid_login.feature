@smoke
@regression

Feature: Invalid Login Functionality

Scenario: Invalid Login Validation
Given user opens OrangeHRM login page
When user enters invalid username and password
And user clicks login button
Then invalid credentials message should display