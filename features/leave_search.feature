@regression

Feature: Leave Search Functionality

  Scenario: Search Leave Records

    Given admin logged into OrangeHRM for leave search
    When admin clicks Leave menu
    And admin searches leave records
    Then leave records should display successfully