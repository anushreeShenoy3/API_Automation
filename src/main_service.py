import requests
import json

actual_status_code = 0
actual_response_json = ''


def update_status(status_code_value,response_json):
    '''
    Method to update global parameters as per current test case
    :param status_code_value: status_code from response json
    :param response_json: response json text/body returned by request
    :return:
    '''
    global actual_status_code,actual_response_json
    actual_status_code = status_code_value
    actual_response_json = json.loads(response_json)

def get_request(url):
    '''
    method to create a get request
    :param url: API to be tested
    :return: response from get request
    '''
    header = {'Content-Type': "application/json",
              'Accept-Charset': "UTF-8"}
    response = requests.request("GET", url, headers=header)
    return response

def service_is_up_and_running(url):
    '''
    method to verify API to be tested is up and running
    :param url: main url to be tested
    :return: None
    '''
    service_response = get_request(url)
    print("Service response code for base url " + url + " is "
          + str(service_response.status_code))
    assert int(service_response.status_code) == 200

def get_service_is_called(endPoint):
    '''
    method to call get_request() to create a get request to API
    This also updates global parameters which will be used in current test scenario
    :param endPoint:
    :return: None
    '''
    print("Get service is made to API " + endPoint)
    service_status_code =get_request(endPoint)
    update_status(service_status_code.status_code,service_status_code.text)

def status_code_validated(statusCode):
    '''
    Method to validate actual status code with expected status code
    :param statusCode: expected status code
    :return: None
    '''
    print("Actual status code is " + str(actual_status_code))
    print("Expected status code is " + str(statusCode))
    assert actual_status_code == int(statusCode)


def assert_check(data):
    '''
    Method to check each key in json schema
    :param data: data to be tested
    :return: None
    '''
    assert 'userId' in data.keys()
    assert 'id' in data.keys()
    assert 'title' in data.keys()
    assert 'body' in data.keys()

def schema_is_validated():
    '''
    method to validate schema
    :return: None
    '''
    print("**************")
    print(type(actual_response_json))
    print(isinstance(actual_response_json, list))
    if isinstance(actual_response_json, list):
        for val in actual_response_json:
            print(val)
            print(type(val))
            assert_check(val)
    else:
        assert_check(actual_response_json)

def validate_number_of_records(recordCount):
    '''
    Method to compare actual and expected number of records
    :param recordCount: expected number of records
    :return:
    '''
    print("Expected record count is " + str(recordCount))
    if isinstance(actual_response_json,list):
        assert len(actual_response_json) == int(recordCount)
    else:
        assert isinstance(actual_response_json,dict) == True

def validate_id_match(inputId):
    '''
    Method to validate id value in response
    :param inputId: expected value of 'id'
    :return: None
    '''
    print("Actual ID: " +str(actual_response_json.get('id')))
    print("Expected ID: " +str(inputId))
    assert actual_response_json.get('id') == int(inputId)

def log_the_response(invalidUrl):
    '''
    Method to print detailed log of invalid url
    :param invalidUrl: invalid url which is invoked
    :return: None
    '''
    print("Service is down")
    print("Request URL is " + invalidUrl)
    print("Status code is " + str(actual_status_code))
    print("Response body is " + str(actual_response_json))

def record_schema_is_validated():
    '''
    Validate the schema
    :return: None
    '''
    assert "id" in actual_response_json.keys()

def request_is_done(type,url,body=''):
      '''
      create requests based on input and update status and response json
      :param type: request type for example: post, put, delete
      :param url: API to be tested
      :param body: body of the request
      :return: None
      '''
      print("Request type is " + type)
      print("Request URL is " + url)
      if type == 'post':
          header = {'Accept-Charset': "UTF-8",
                    'Content-Type': "text/plain"}
      else:
          header = {
              'Accept-Charset': "UTF-8",
              'Content-Type': "application/json",
          }
      if type == "post":
          response = requests.post(url, data=body, headers=header)
      elif type == 'put':
          response = requests.put(url=url, data=body)
      else:
          response = requests.delete(url=url)
      update_status(response.status_code, response.text)

def record_change_verified(type):
      '''
      verify the change in records due to API requests
      :param type: type of input, for example: put, post
      :return: None
      '''
      print("Requested service that has altered record is " +type)
      if type == 'post':
        assert actual_response_json.get('id') != ''
      elif type == 'put':
        assert actual_response_json.get('userId') != ''
        assert actual_response_json.get('id') != ''
        assert actual_response_json.get('title') != ''
        assert actual_response_json.get('body') != ''
      else:
        assert bool(actual_response_json) == False
