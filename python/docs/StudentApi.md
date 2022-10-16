# swagger_client.StudentApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**student_diary**](StudentApi.md#student_diary) | **GET** /student/diary | 
[**student_diary_init**](StudentApi.md#student_diary_init) | **GET** /student/diary/init | 

# **student_diary**
> Diary student_diary(student_id, week_start=week_start, week_end=week_end, with_la_assigns=with_la_assigns, with_past_mandatory=with_past_mandatory, year_id=year_id)



returns all assignments

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.StudentApi(swagger_client.ApiClient(configuration))
student_id = 56 # int | 
week_start = '2013-10-20' # date |  (optional)
week_end = '2013-10-20' # date |  (optional)
with_la_assigns = true # bool |  (optional)
with_past_mandatory = true # bool |  (optional)
year_id = 56 # int |  (optional)

try:
    api_response = api_instance.student_diary(student_id, week_start=week_start, week_end=week_end, with_la_assigns=with_la_assigns, with_past_mandatory=with_past_mandatory, year_id=year_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StudentApi->student_diary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **student_id** | **int**|  | 
 **week_start** | **date**|  | [optional] 
 **week_end** | **date**|  | [optional] 
 **with_la_assigns** | **bool**|  | [optional] 
 **with_past_mandatory** | **bool**|  | [optional] 
 **year_id** | **int**|  | [optional] 

### Return type

[**Diary**](Diary.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **student_diary_init**
> StudentDiaryInit student_diary_init()



returns strudent diary init data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.StudentApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.student_diary_init()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StudentApi->student_diary_init: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StudentDiaryInit**](StudentDiaryInit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

