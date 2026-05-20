@regression

Feature: Employee List Functionality

  Scenario: View Employee List

    Given admin logged into OrangeHRM for employee list
    When admin clicks PIM menu for employee list
    And admin opens employee list page
    Then employee records should display successfully