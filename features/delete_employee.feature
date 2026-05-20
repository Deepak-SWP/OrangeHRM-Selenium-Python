@regression

Feature: Delete Employee Functionality

  Scenario: Delete Employee Record

    Given admin logged into OrangeHRM portal
    When admin opens PIM module for delete
    And admin selects employee record
    And admin clicks delete button
    And admin confirms delete action
    Then employee record should delete successfully