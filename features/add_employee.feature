@regression

Feature: Add Employee Functionality

  Scenario: Add Employee Successfully

    Given admin is logged into OrangeHRM
    When admin clicks PIM menu
    And admin clicks Add Employee button
    And admin enters firstname and lastname
    And admin clicks Save
    Then employee added successfully