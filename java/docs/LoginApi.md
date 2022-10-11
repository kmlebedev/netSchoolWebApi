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
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.LoginApi;


LoginApi apiInstance = new LoginApi();
try {
    LoginData result = apiInstance.logindata();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling LoginApi#logindata");
    e.printStackTrace();
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
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.LoginApi;


LoginApi apiInstance = new LoginApi();
String cacheVer = "cacheVer_example"; // String | 
try {
    PrepareEmLoginForm result = apiInstance.prepareemloginform(cacheVer);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling LoginApi#prepareemloginform");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cacheVer** | **String**|  | [optional]

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
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.LoginApi;


LoginApi apiInstance = new LoginApi();
String cacheVer = "cacheVer_example"; // String | 
try {
    PrepareLoginForm result = apiInstance.prepareloginform(cacheVer);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling LoginApi#prepareloginform");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cacheVer** | **String**|  | [optional]

### Return type

[**PrepareLoginForm**](PrepareLoginForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

