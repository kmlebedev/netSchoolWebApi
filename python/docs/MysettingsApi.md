# swagger_client.MysettingsApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mysettings**](MysettingsApi.md#mysettings) | **GET** /mysettings | 
[**yearlist**](MysettingsApi.md#yearlist) | **GET** /mysettings/yearlist | 

# **mysettings**
> MySettings mysettings(at)



returns my settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MysettingsApi(swagger_client.ApiClient(configuration))
at = 'at_example' # str | an authorization header

try:
    api_response = api_instance.mysettings(at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MysettingsApi->mysettings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **at** | **str**| an authorization header | 

### Return type

[**MySettings**](MySettings.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **yearlist**
> MySettingsYears yearlist(at)



returns all years

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MysettingsApi(swagger_client.ApiClient(configuration))
at = 'at_example' # str | an authorization header

try:
    api_response = api_instance.yearlist(at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MysettingsApi->yearlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **at** | **str**| an authorization header | 

### Return type

[**MySettingsYears**](MySettingsYears.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

