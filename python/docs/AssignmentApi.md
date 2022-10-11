# swagger_client.AssignmentApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/4.30.43656*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignment_types**](AssignmentApi.md#assignment_types) | **GET** /grade/assignment/types | 

# **assignment_types**
> AssignmentTypes assignment_types()



returns all assignment types

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssignmentApi()

try:
    api_response = api_instance.assignment_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentApi->assignment_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AssignmentTypes**](AssignmentTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

