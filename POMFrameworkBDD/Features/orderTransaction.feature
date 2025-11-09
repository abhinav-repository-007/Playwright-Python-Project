Feature: Order Transaction
  I want to verify order is placed successfully

  Scenario Outline: Verify Order success message shown in details page
    Given place the order with <Username> and <Password>
    And the user on landing page
    When I login into the portal with <Username> and <Password>
    And navigates to orders page
    And selects the orderId
    Then order message is successfully displayed
    Examples:
    |Username               |Password     |
    |abhinav0007@gmail.com  |Iamking@000  |