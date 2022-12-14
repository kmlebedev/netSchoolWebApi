# {{classname}}

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Getauthdata**](LoginApi.md#Getauthdata) | **Post** /auth/getdata | 
[**Login**](LoginApi.md#Login) | **Post** /login | 
[**Logindata**](LoginApi.md#Logindata) | **Get** /logindata | 
[**Loginform**](LoginApi.md#Loginform) | **Get** /loginform | 
[**Prepareemloginform**](LoginApi.md#Prepareemloginform) | **Get** /prepareemloginform | 
[**Prepareloginform**](LoginApi.md#Prepareloginform) | **Get** /prepareloginform | 

# **Getauthdata**
> GetAuthData Getauthdata(ctx, )


returns all login data

### Required Parameters
This endpoint does not need any parameter.

### Return type

[**GetAuthData**](GetAuthData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Login**
> Login Login(ctx, loginType, cid, sid, pid, cn, sft, scid, uN, pW, lt, pw2, ver)


returns all login data

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **loginType** | **int32**|  | 
  **cid** | **int32**|  | 
  **sid** | **int32**|  | 
  **pid** | **int32**|  | 
  **cn** | **int32**|  | 
  **sft** | **int32**|  | 
  **scid** | **int32**|  | 
  **uN** | **string**|  | 
  **pW** | **string**|  | 
  **lt** | **int32**|  | 
  **pw2** | **string**|  | 
  **ver** | **int32**|  | 

### Return type

[**Login**](Login.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Logindata**
> LoginData Logindata(ctx, )


returns all login data

### Required Parameters
This endpoint does not need any parameter.

### Return type

[**LoginData**](LoginData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Loginform**
> LoginForm Loginform(ctx, optional)


returns all loginform

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***LoginApiLoginformOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a LoginApiLoginformOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **optional.Int32**|  | 
 **sid** | **optional.Int32**|  | 
 **pid** | **optional.Int32**|  | 
 **cn** | **optional.Int32**|  | 
 **sft** | **optional.Int32**|  | 
 **lASTNAME** | **optional.String**|  | 
 **cacheVer** | **optional.String**|  | 

### Return type

[**LoginForm**](LoginForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Prepareemloginform**
> PrepareEmLoginForm Prepareemloginform(ctx, optional)


returns all prepareemloginform

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***LoginApiPrepareemloginformOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a LoginApiPrepareemloginformOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cacheVer** | **optional.String**|  | 

### Return type

[**PrepareEmLoginForm**](PrepareEmLoginForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Prepareloginform**
> PrepareLoginForm Prepareloginform(ctx, optional)


returns all prepareloginform

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***LoginApiPrepareloginformOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a LoginApiPrepareloginformOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **optional.Int32**|  | 
 **sid** | **optional.Int32**|  | 
 **pid** | **optional.Int32**|  | 
 **cn** | **optional.Int32**|  | 
 **sft** | **optional.Int32**|  | 
 **lASTNAME** | **optional.String**|  | 
 **cacheVer** | **optional.String**|  | 

### Return type

[**PrepareLoginForm**](PrepareLoginForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

