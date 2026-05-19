Feature: Search User Functionality

  Scenario: Search Existing User

    Given admin logged into OrangeHRM application
    When admin clicks Admin menu
    And admin enters username in search
    And admin clicks user search button
    Then user records should display