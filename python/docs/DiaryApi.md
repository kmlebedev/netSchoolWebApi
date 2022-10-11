# swagger_client.DiaryApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/4.30.43656*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diary_assignn_details**](DiaryApi.md#diary_assignn_details) | **GET** /student/diary/assigns/{assignId} | 

# **diary_assignn_details**
> DiaryAssignDetails diary_assignn_details(assign_id, student_id)



returns assign information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiaryApi()
assign_id = 56 # int | 
student_id = 56 # int | 

try:
    api_response = api_instance.diary_assignn_details(assign_id, student_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiaryApi->diary_assignn_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assign_id** | **int**|  | 
 **student_id** | **int**|  | 

### Return type

[**DiaryAssignDetails**](DiaryAssignDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

