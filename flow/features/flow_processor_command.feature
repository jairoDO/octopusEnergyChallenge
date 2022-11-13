Feature: Process flow using command line
  Background: define a couple a files for testing
    Given I have a file csv with valid data called "valid_file.csv"
    And I have a file csv with invalid data called "invalid_nm13.csv"
    And I have a file csv with valid data called "valid_file_2.csv"

  Scenario: Process nem13 with valid file should show info of the data processed
    Given I call command 'process_nem13' with parameter "valid_file.csv"
    Then I should see the message "valid_file.csv process successfully "

  Scenario: Process nem13 with invalid file should show info of the data processed
    Given I call command "process_nem13" with parameter "invalid_nm13.csv"
    Then I should see the message "invalid_file.csv process unsuccessfully"


  Scenario: Process multiple files
    Given I call command "process_nem13" with parameters "valid_file.csv valid_file_2.csv invalid_nm13.csv"
    Then I should see the message:
      """
      process valid_file.csv successfully
      process valid_file_2.csv successfully
      process invalid_nm13.csv unsuccessfully
      """