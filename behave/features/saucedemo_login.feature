Feature: Saucedemo login functionality

  Scenario Outline: Check login functionality with incorrect credentials
    Given The saucedemo login page is open
    When I enter username "<username>" and password "<password>"
    Then I should see an error message "<error_message>"

    Examples:
      | username     | password     | error_message                    |
      | locked_out_user | secret_sauce | Sorry, this user has been locked out. |
      | problem_user | secret | Username and password do not match any user in this service |
      | performance_glitch_user | secret |  Username and password do not match any user in this service |
      | incorrect_user | secret_sauce |  Username and password do not match any user in this service |
      | standard_user | wrong_password |  Username and password do not match any user in this service |
      | standard_user | secret_sauce |""|