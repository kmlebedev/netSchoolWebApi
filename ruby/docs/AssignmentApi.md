# SwaggerClient::AssignmentApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/4.30.43656*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignment_types**](AssignmentApi.md#assignment_types) | **GET** /grade/assignment/types | 

# **assignment_types**
> AssignmentTypes assignment_types



returns all assignment types

### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::AssignmentApi.new

begin
  result = api_instance.assignment_types
  p result
rescue SwaggerClient::ApiError => e
  puts "Exception when calling AssignmentApi->assignment_types: #{e}"
end
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



