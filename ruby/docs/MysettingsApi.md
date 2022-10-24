# SwaggerClient::MysettingsApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mysettings**](MysettingsApi.md#mysettings) | **GET** /mysettings | 
[**yearlist**](MysettingsApi.md#yearlist) | **GET** /mysettings/yearlist | 

# **mysettings**
> MySettings mysettings(at)



returns my settings

### Example
```ruby
# load the gem
require 'swagger_client'
# setup authorization
SwaggerClient.configure do |config|
end

api_instance = SwaggerClient::MysettingsApi.new
at = 'at_example' # String | an authorization header


begin
  result = api_instance.mysettings(at)
  p result
rescue SwaggerClient::ApiError => e
  puts "Exception when calling MysettingsApi->mysettings: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **at** | **String**| an authorization header | 

### Return type

[**MySettings**](MySettings.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json



# **yearlist**
> MySettingsYears yearlist(at)



returns all years

### Example
```ruby
# load the gem
require 'swagger_client'
# setup authorization
SwaggerClient.configure do |config|
end

api_instance = SwaggerClient::MysettingsApi.new
at = 'at_example' # String | an authorization header


begin
  result = api_instance.yearlist(at)
  p result
rescue SwaggerClient::ApiError => e
  puts "Exception when calling MysettingsApi->yearlist: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **at** | **String**| an authorization header | 

### Return type

[**MySettingsYears**](MySettingsYears.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json



