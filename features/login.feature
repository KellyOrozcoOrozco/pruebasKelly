Feature: SwagLabs login
 Scenario Outline: Login to SwagLab with correct parameters
    Given User launch Chrome browser
    When User open SwagLabs Login
    And User enter username "<username>" and password "<password>"
    And User click on login button
    And Select products to add it to the shopping cart
    And User clicks on the shopping cart
    And User clicks on checkout button
    And User enter "<name>" and "<lastname>" and "<postalcode>"
    And User clicks on Continue button
    And User clicks on finish button
    And User clicks on menu logout
    Then User clicks on logout button

   Examples:
   |username|password|name|lastname|postalcode|
   |standard_user|secret_sauce|Julieta|Garcia|31123|
   |problem_user|secret_sauce|Dario|Duque|5436|
   |performance_glitch_user|secret_sauce|Manuel|Salazar|4567|







