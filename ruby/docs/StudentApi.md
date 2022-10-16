# SwaggerClient::StudentApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**student_diary**](StudentApi.md#student_diary) | **GET** /student/diary | 
[**student_diary_init**](StudentApi.md#student_diary_init) | **GET** /student/diary/init | 

# **student_diary**
> Diary student_diary(student_id, opts)



returns all assignments

### Example
```ruby
# load the gem
require 'swagger_client'
# setup authorization
SwaggerClient.configure do |config|
end

api_instance = SwaggerClient::StudentApi.new
student_id = 56 # Integer | 
opts = { 
  week_start: Date.parse('2013-10-20'), # Date | 
  week_end: Date.parse('2013-10-20'), # Date | 
  with_la_assigns: true, # BOOLEAN | 
  with_past_mandatory: true, # BOOLEAN | 
  year_id: 56 # Integer | 
}

begin
  result = api_instance.student_diary(student_id, opts)
  p result
rescue SwaggerClient::ApiError => e
  puts "Exception when calling StudentApi->student_diary: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **student_id** | **Integer**|  | 
 **week_start** | **Date**|  | [optional] 
 **week_end** | **Date**|  | [optional] 
 **with_la_assigns** | **BOOLEAN**|  | [optional] 
 **with_past_mandatory** | **BOOLEAN**|  | [optional] 
 **year_id** | **Integer**|  | [optional] 

### Return type

[**Diary**](Diary.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json



# **student_diary_init**
> StudentDiaryInit student_diary_init



returns strudent diary init data

### Example
```ruby
# load the gem
require 'swagger_client'
# setup authorization
SwaggerClient.configure do |config|
end

api_instance = SwaggerClient::StudentApi.new

begin
  result = api_instance.student_diary_init
  p result
rescue SwaggerClient::ApiError => e
  puts "Exception when calling StudentApi->student_diary_init: #{e}"
end
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



