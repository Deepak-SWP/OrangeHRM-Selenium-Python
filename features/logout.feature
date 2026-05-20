@smoke
@regression

Feature: Logout Functionality

  Scenario: Logout Successfully

    Given user logged into OrangeHRM
    When user clicks profile menu
    And user clicks logout option
    Then login page should display