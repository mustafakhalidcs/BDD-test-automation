Feature: orange HRM Login

    Background: common steps
        Given launch chrome browser
        When open orange hrm page
        AND Enter validuser and password 
        AND click on login button

    Scenario: Login to Orange HRM
        Then user login successfully

    Scenario: Search user
        When navigate to search page
        Then search page should display
    
      

      