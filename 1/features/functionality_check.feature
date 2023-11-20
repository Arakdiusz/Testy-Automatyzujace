Feature: Functionality Check on Sauce Demo page after login

  Scenario: Verify functionality after login
    Given I launch Chrome browser
    When I open Sauce Demo homepage
    And I enter username and password
    Then I should be able to add an item to the cart
    And I should be able to open the cart
    And I should be able to remove the item from the cart