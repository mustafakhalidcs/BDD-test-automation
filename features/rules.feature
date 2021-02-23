Feature: showing off behave

  Scenario Outline: run a simple test
     Given launch chrome browser
      When open orange hrm page
      AND Enter username "<username>" and password "<password>"
      AND click on login button
      Then user login successfully
    
      Examples:
      | username  | password  |
      | admin     | admin123  |
      | admin123  | adminabc  |
      | adminabc  | adminabc  |
      | adminxyz  | adminxyz  |

      