# LoginApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/4.30.43656*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logindata**](LoginApi.md#logindata) | **GET** /logindata | 
[**prepareemloginform**](LoginApi.md#prepareemloginform) | **GET** /prepareemloginform | 
[**prepareloginform**](LoginApi.md#prepareloginform) | **GET** /prepareloginform | 

<a name="logindata"></a>
# **logindata**
> LoginData logindata()



returns all login data

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = LoginApi()
try {
    val result : LoginData = apiInstance.logindata()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling LoginApi#logindata")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling LoginApi#logindata")
    e.printStackTrace()
}
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

<a name="prepareemloginform"></a>
# **prepareemloginform**
> PrepareEmLoginForm prepareemloginform(cacheVer)



returns all prepareemloginform

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = LoginApi()
val cacheVer : kotlin.String = cacheVer_example // kotlin.String | 
try {
    val result : PrepareEmLoginForm = apiInstance.prepareemloginform(cacheVer)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling LoginApi#prepareemloginform")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling LoginApi#prepareemloginform")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cacheVer** | **kotlin.String**|  | [optional]

### Return type

[**PrepareEmLoginForm**](PrepareEmLoginForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="prepareloginform"></a>
# **prepareloginform**
> PrepareLoginForm prepareloginform(cacheVer)



returns all prepareloginform

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = LoginApi()
val cacheVer : kotlin.String = cacheVer_example // kotlin.String | 
try {
    val result : PrepareLoginForm = apiInstance.prepareloginform(cacheVer)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling LoginApi#prepareloginform")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling LoginApi#prepareloginform")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cacheVer** | **kotlin.String**|  | [optional]

### Return type

[**PrepareLoginForm**](PrepareLoginForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

