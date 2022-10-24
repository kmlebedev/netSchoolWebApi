# MysettingsApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mysettings**](MysettingsApi.md#mysettings) | **GET** /mysettings | 
[**yearlist**](MysettingsApi.md#yearlist) | **GET** /mysettings/yearlist | 

<a name="mysettings"></a>
# **mysettings**
> MySettings mysettings(at)



returns my settings

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = MysettingsApi()
val at : kotlin.String = at_example // kotlin.String | an authorization header
try {
    val result : MySettings = apiInstance.mysettings(at)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MysettingsApi#mysettings")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MysettingsApi#mysettings")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **at** | **kotlin.String**| an authorization header |

### Return type

[**MySettings**](MySettings.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="yearlist"></a>
# **yearlist**
> MySettingsYears yearlist(at)



returns all years

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = MysettingsApi()
val at : kotlin.String = at_example // kotlin.String | an authorization header
try {
    val result : MySettingsYears = apiInstance.yearlist(at)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MysettingsApi#yearlist")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MysettingsApi#yearlist")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **at** | **kotlin.String**| an authorization header |

### Return type

[**MySettingsYears**](MySettingsYears.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

