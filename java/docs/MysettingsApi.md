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
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.MysettingsApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();


MysettingsApi apiInstance = new MysettingsApi();
String at = "at_example"; // String | an authorization header
try {
    MySettings result = apiInstance.mysettings(at);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling MysettingsApi#mysettings");
    e.printStackTrace();
}
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

<a name="yearlist"></a>
# **yearlist**
> MySettingsYears yearlist(at)



returns all years

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.MysettingsApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();


MysettingsApi apiInstance = new MysettingsApi();
String at = "at_example"; // String | an authorization header
try {
    MySettingsYears result = apiInstance.yearlist(at);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling MysettingsApi#yearlist");
    e.printStackTrace();
}
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

