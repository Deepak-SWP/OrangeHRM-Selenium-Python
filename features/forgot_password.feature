@smoke
@regression
Feature: Forgot Password Functionality

Scenario: Reset Password Successfully
Given user is on OrangeHRM login page
When user clicks forgot password link
And user enters username
And user clicks reset password button
Then reset password message should display