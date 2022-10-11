# SwaggerClient::DiaryApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/4.30.43656*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diary_assignn_details**](DiaryApi.md#diary_assignn_details) | **GET** /student/diary/assigns/{assignId} | 

# **diary_assignn_details**
> DiaryAssignDetails diary_assignn_details(assign_id, student_id)



returns assign information

### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::DiaryApi.new
assign_id = 56 # Integer | 
student_id = 56 # Integer | 


begin
  result = api_instance.diary_assignn_details(assign_id, student_id)
  p result
rescue SwaggerClient::ApiError => e
  puts "Exception when calling DiaryApi->diary_assignn_details: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assign_id** | **Integer**|  | 
 **student_id** | **Integer**|  | 

### Return type

[**DiaryAssignDetails**](DiaryAssignDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json



