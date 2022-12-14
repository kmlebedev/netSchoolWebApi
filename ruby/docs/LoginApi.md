# SwaggerClient::LoginApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getauthdata**](LoginApi.md#getauthdata) | **POST** /auth/getdata | 
[**login**](LoginApi.md#login) | **POST** /login | 
[**logindata**](LoginApi.md#logindata) | **GET** /logindata | 
[**loginform**](LoginApi.md#loginform) | **GET** /loginform | 
[**prepareemloginform**](LoginApi.md#prepareemloginform) | **GET** /prepareemloginform | 
[**prepareloginform**](LoginApi.md#prepareloginform) | **GET** /prepareloginform | 

# **getauthdata**
> GetAuthData getauthdata



returns all login data

### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::LoginApi.new

begin
  result = api_instance.getauthdata
  p result
rescue SwaggerClient::ApiError => e
  puts "Exception when calling LoginApi->getauthdata: #{e}"
end
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAuthData**](GetAuthData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json



# **login**
> Login login(login_typecidsidpidcnsftscidunpwltpw2ver)



returns all login data

### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::LoginApi.new
login_type = 56 # Integer | 
cid = 56 # Integer | 
sid = 56 # Integer | 
pid = 56 # Integer | 
cn = 56 # Integer | 
sft = 56 # Integer | 
scid = 56 # Integer | 
un = 'un_example' # String | 
pw = 'pw_example' # String | 
lt = 56 # Integer | 
pw2 = 'pw2_example' # String | 
ver = 56 # Integer | 


begin
  result = api_instance.login(login_typecidsidpidcnsftscidunpwltpw2ver)
  p result
rescue SwaggerClient::ApiError => e
  puts "Exception when calling LoginApi->login: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_type** | **Integer**|  | 
 **cid** | **Integer**|  | 
 **sid** | **Integer**|  | 
 **pid** | **Integer**|  | 
 **cn** | **Integer**|  | 
 **sft** | **Integer**|  | 
 **scid** | **Integer**|  | 
 **un** | **String**|  | 
 **pw** | **String**|  | 
 **lt** | **Integer**|  | 
 **pw2** | **String**|  | 
 **ver** | **Integer**|  | 

### Return type

[**Login**](Login.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json



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



# **loginform**
> LoginForm loginform(opts)



returns all loginform

### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::LoginApi.new
opts = { 
  cid: 56, # Integer | 
  sid: 56, # Integer | 
  pid: 56, # Integer | 
  cn: 56, # Integer | 
  sft: 56, # Integer | 
  lastname: 'lastname_example', # String | 
  cache_ver: 'cache_ver_example' # String | 
}

begin
  result = api_instance.loginform(opts)
  p result
rescue SwaggerClient::ApiError => e
  puts "Exception when calling LoginApi->loginform: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **Integer**|  | [optional] 
 **sid** | **Integer**|  | [optional] 
 **pid** | **Integer**|  | [optional] 
 **cn** | **Integer**|  | [optional] 
 **sft** | **Integer**|  | [optional] 
 **lastname** | **String**|  | [optional] 
 **cache_ver** | **String**|  | [optional] 

### Return type

[**LoginForm**](LoginForm.md)

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
  cid: 56, # Integer | 
  sid: 56, # Integer | 
  pid: 56, # Integer | 
  cn: 56, # Integer | 
  sft: 56, # Integer | 
  lastname: 'lastname_example', # String | 
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
 **cid** | **Integer**|  | [optional] 
 **sid** | **Integer**|  | [optional] 
 **pid** | **Integer**|  | [optional] 
 **cn** | **Integer**|  | [optional] 
 **sft** | **Integer**|  | [optional] 
 **lastname** | **String**|  | [optional] 
 **cache_ver** | **String**|  | [optional] 

### Return type

[**PrepareLoginForm**](PrepareLoginForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json



