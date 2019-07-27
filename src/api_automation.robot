*** Settings ***
Library    main_service.py
Resource 	properties.robot

*** Test Cases ***
Get Request Status Code Test
    Given service is up and running   ${mainUrl}
    When get service is called  ${end_point_posts}
    Then status code validated  ${OK_status}

Get Request Schema_Test
    Given service is up and running   ${mainUrl}
    When get service is called  ${end_point_posts}
    Then schema is validated

Get Request Record_Test
    Given service is up and running   ${mainUrl}
    When get service is called  ${end_point_posts}
    Then validate number of records  ${number_of_records_posts}

Get Request Single Record Status Code Test
    Given service is up and running   ${mainUrl}
    When get service is called  ${end_point_posts_1}
    Then status code validated  ${OK_status}

Get Request Single Record Schema Test
    Given service is up and running   ${mainUrl}
    When get service is called  ${end_point_posts_1}
    Then schema is validated

Get Request Single Record Count Test
    Given service is up and running   ${mainUrl}
    When get service is called  ${end_point_posts_1}
    Then validate number of records  ${number_of_records_posts_1}

Get Request Record Test ID Match
    Given service is up and running   ${mainUrl}
    When get service is called  ${end_point_posts_1}
    Then validate id match  ${input_id}

Get Request Invalid Posts Status Code Validated
    Given service is up and running  ${mainUrl}
    When get service is called  ${invalid_url}
    Then status code validated  ${invalid_status}

Get Request Invalid_Posts_logging
    Given service is up and running  ${mainUrl}
    When get service is called  ${invalid_url}
    Then log the response  ${invalid_url}

Post_Request Status Code Validation
    Given service is up and running  ${mainUrl}
    When request is done  post  ${end_point_posts}  ${post_request_body}
    Then status code validated  ${post_status_code}

Post Request Schema Validation
    Given service is up and running  ${mainUrl}
    When request is done  post  ${end_point_posts}  ${post_request_body}
    Then record schema is validated

Post Request Record Validation
    Given service is up and running  ${mainUrl}
    When request is done  post  ${end_point_posts}  ${post_request_body}
    Then record change verified  post

Put Request Status Code Validation
    Given service is up and running  ${mainUrl}
    When request is done  put  ${end_point_posts_1}  ${put_request_body}
    Then status code validated  ${put_status_code}

Put Request Schema Validation
    Given service is up and running  ${mainUrl}
    When request is done  put  ${end_point_posts_1}  ${put_request_body}
    Then record schema is validated

Put Request Record Validation
    Given service is up and running  ${mainUrl}
    When request is done  put  ${end_point_posts_1}  ${put_request_body}
    Then record change verified  put

Delete Service Status Validation
    Given service is up and running  ${mainUrl}
    When request is done  delete  ${end_point_posts_1}
    Then status code validated  ${OK_status}
    And record change verified  delete
