Feature: Login Check on Sauce Demo page

  Scenario Outline: Login with various credentials
    Given I launch Chrome browser
    When I open Sauce Demo homepage
    And I enter wrong username "<username>" and password "<password>"
    Then I should see the error message "<error_message>"

    Examples:
      | username     | password     | error_message                      |
      | wrong_user   | wrong_pass   | Username and password do not match |
      | locked_out_user   | secret_sauce  | Sorry, this user has been locked out. |
      | wrong_user   | secret_sauce   | Username and password do not match |
      | standard_user  | wrong_pass   | Username and password do not match any user in this service|