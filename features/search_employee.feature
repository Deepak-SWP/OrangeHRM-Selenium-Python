Feature: Search Employee Functionality

  Scenario: Search Added Employee

    Given admin logged into OrangeHRM
    When admin opens PIM module
    And admin searches employee name
    And admin clicks search button
    Then employee details should display