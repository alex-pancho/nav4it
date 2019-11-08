Feature: Test cases in automationpractice site
        
    Scenario Outline: Login to site
        Given open web http://automationpractice.com/index.php
        When click "Sign in" button
        And input <login> in the "Email address" field
        And input <pass> in the "Password" field
        And click "Sign" button
        Then the page url will be http://automationpractice.com/index.php?controller=my-account
        Examples: retail user
        | login | pass |
        | "testqa1@yopmail.com" | "qa123456" |
    
    Scenario: Use search
        When input "Printed Dress" in the "Search" field
        And click "Search" button
        Then count of "result item" has "5" items