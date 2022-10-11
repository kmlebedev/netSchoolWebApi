# SwaggerClient::LoginApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/4.30.43656*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logindata**](LoginApi.md#logindata) | **GET** /logindata | 
[**prepareemloginform**](LoginApi.md#prepareemloginform) | **GET** /prepareemloginform | 
[**prepareloginform**](LoginApi.md#prepareloginform) | **GET** /prepareloginform | 

# **logindata**
> LoginData logindata



returns all login data

### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::LoginApi.new

begin
  result = api_instance.logindata
  p result
rescue SwaggerClient::ApiError => e
  puts "Exception when calling LoginApi->logindata: #{e}"
end
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LoginData**](LoginData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json



# **prepareemloginform**
> PrepareEmLoginForm prepareemloginform(opts)



returns all prepareemloginform

### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::LoginApi.new
opts = { 
  cache_ver: 'cache_ver_example' # String | 
}

begin
  result = api_instance.prepareemloginform(opts)
  p result
rescue SwaggerClient::ApiError => e
  puts "Exception when calling LoginApi->prepareemloginform: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cache_ver** | **String**|  | [optional] 

### Return type

[**PrepareEmLoginForm**](PrepareEmLoginForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json



# **prepareloginform**
> PrepareLoginForm prepareloginform(opts)



returns all prepareloginform

### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::LoginApi.new
opts = { 
  cache_ver: 'cache_ver_example' # String | 
}

begin
  result = api_instance.prepareloginform(opts)
  p result
rescue SwaggerClient::ApiError => e
  puts "Exception when calling LoginApi->prepareloginform: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cache_ver** | **String**|  | [optional] 

### Return type

[**PrepareLoginForm**](PrepareLoginForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json



