@smoke
@regression

Feature: Login Functionality

  Scenario: Valid Login
    Given user is on login page
    When user enters valid username and password
    And clicks login button
    Then user should navigate to dashboard