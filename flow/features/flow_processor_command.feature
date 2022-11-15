Feature: Process flow using command line

  Scenario: Process nem13 with valid file should show info of the data processed
    Given I call command process_nem13 with parameter "-f valid_nm13.csv"
    Then I should see the message:
      """
      Total process successful 1: valid_nm13.csv
      """

  Scenario: Process nem13 with invalid file should show info of the data processed
    Given I call command process_nem13 with parameter "-f invalid_nm13.csv"
    Then I should see the message:
      """
      Total invalid files 1: invalid_nm13.csv
      """
  Scenario: Process multiple files
    Given I call command process_nem13 with parameters "-f valid_nm13.csv valid_nm13_2.csv invalid_nm13.csv"
    Then I should see the message:
      """
      Total invalid files 1: invalid_nm13.csv
      Total process successful 2: valid_nm13.csv,valid_nm13_2.csv
      """
    And I should see the message:
      """
      Upload 8 AccumulationMeterData new instances
      """

  Scenario: Process multiple files one with b2b_details
    Given I call command process_nem13 with parameters "-f valid_nm13.csv valid_nm13_2.csv file_nm13_with_b2b_details.csv"
    Then I should see the message:
      """
      Total process successful 3: valid_nm13.csv,valid_nm13_2.csv,file_nm13_with_b2b_details.csv
      """
    And I should see the message:
      """
      Upload 1 B2BDetails new instances
      """