Feature: Saucedemo shopping cart functionality

  Background:
    Given I am logged in with valid credentials

  Scenario: Add a single item to the shopping cart
    When I add a single item to the cart
    Then the cart should display one item

  Scenario: Add multiple items to the shopping cart
    When I add multiple items to the cart


  Scenario: Remove an item from the shopping cart
    Given I have items in my shopping cart
    When I remove an item from the cart