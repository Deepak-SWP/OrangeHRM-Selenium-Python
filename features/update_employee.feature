Feature: Update Employee Functionality

    Scenario: Update Employee Details

        Given admin logged into OrangeHRM system
        When admin opens PIM module for update
        And admin opens employee record
        And admin updates employee details
        And admin clicks save button
        Then employee details should update successfully