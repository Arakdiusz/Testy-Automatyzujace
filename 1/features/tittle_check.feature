Feature: Title Check on Sauce Demo page

  Scenario: Verify the title of Sauce Demo page
    Given I launch Chrome browser
    When I open Sauce Demo homepage
    Then The title should be "Swag Labs"
