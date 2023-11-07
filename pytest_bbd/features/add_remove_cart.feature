Feature: Add and remove items from the shopping cart

  Scenario: User can add and remove items from the cart after logging in
    Given the user has logged in to the "saucedemo" website
    When the user adds an item to the cart
    And the user removes the item from the cart
    Then the cart should be empty
