

Feature: Leap Year

  Write a function that returns true or false depending on whether its input integer is a leap year or not.

  #Rule: A leap year is divisible by 4
  Scenario: Typical Common Year
    When the user asks whether 2001 is a leap year
    Then it should respond with "false"

  Scenario: Typical Leap Year
    When the user asks whether 1996 is a leap year
    Then it should respond with "true"

  #Rule: It's not a leap year if it's divisible by 100
  Scenario: Typical Common Year
    When the user asks whether 1900 is a leap year
    Then it should respond with "false"

  #Rule: It is a leap year if it's divisible by 400
  Scenario: Typical Leap Year
    When the user asks whether 2000 is a leap year
    Then it should respond with "true"