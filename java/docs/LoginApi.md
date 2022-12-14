# LoginApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getauthdata**](LoginApi.md#getauthdata) | **POST** /auth/getdata | 
[**login**](LoginApi.md#login) | **POST** /login | 
[**logindata**](LoginApi.md#logindata) | **GET** /logindata | 
[**loginform**](LoginApi.md#loginform) | **GET** /loginform | 
[**prepareemloginform**](LoginApi.md#prepareemloginform) | **GET** /prepareemloginform | 
[**prepareloginform**](LoginApi.md#prepareloginform) | **GET** /prepareloginform | 

<a name="getauthdata"></a>
# **getauthdata**
> GetAuthData getauthdata()



returns all login data

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.LoginApi;


LoginApi apiInstance = new LoginApi();
try {
    GetAuthData result = apiInstance.getauthdata();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling LoginApi#getauthdata");
    e.printStackTrace();
}
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

<a name="login"></a>
# **login**
> Login login(loginType, cid, sid, pid, cn, sft, scid, UN, PW, lt, pw2, ver)



returns all login data

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.LoginApi;


LoginApi apiInstance = new LoginApi();
Integer loginType = 56; // Integer | 
Integer cid = 56; // Integer | 
Integer sid = 56; // Integer | 
Integer pid = 56; // Integer | 
Integer cn = 56; // Integer | 
Integer sft = 56; // Integer | 
Integer scid = 56; // Integer | 
String UN = "UN_example"; // String | 
String PW = "PW_example"; // String | 
Integer lt = 56; // Integer | 
String pw2 = "pw2_example"; // String | 
Integer ver = 56; // Integer | 
try {
    Login result = apiInstance.login(loginType, cid, sid, pid, cn, sft, scid, UN, PW, lt, pw2, ver);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling LoginApi#login");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loginType** | **Integer**|  |
 **cid** | **Integer**|  |
 **sid** | **Integer**|  |
 **pid** | **Integer**|  |
 **cn** | **Integer**|  |
 **sft** | **Integer**|  |
 **scid** | **Integer**|  |
 **UN** | **String**|  |
 **PW** | **String**|  |
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

<a name="loginform"></a>
# **loginform**
> LoginForm loginform(cid, sid, pid, cn, sft, LASTNAME, cacheVer)



returns all loginform

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.LoginApi;


LoginApi apiInstance = new LoginApi();
Integer cid = 56; // Integer | 
Integer sid = 56; // Integer | 
Integer pid = 56; // Integer | 
Integer cn = 56; // Integer | 
Integer sft = 56; // Integer | 
String LASTNAME = "LASTNAME_example"; // String | 
String cacheVer = "cacheVer_example"; // String | 
try {
    LoginForm result = apiInstance.loginform(cid, sid, pid, cn, sft, LASTNAME, cacheVer);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling LoginApi#loginform");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **Integer**|  | [optional]
 **sid** | **Integer**|  | [optional]
 **pid** | **Integer**|  | [optional]
 **cn** | **Integer**|  | [optional]
 **sft** | **Integer**|  | [optional]
 **LASTNAME** | **String**|  | [optional]
 **cacheVer** | **String**|  | [optional]

### Return type

[**LoginForm**](LoginForm.md)

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
> PrepareLoginForm prepareloginform(cid, sid, pid, cn, sft, LASTNAME, cacheVer)



returns all prepareloginform

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.LoginApi;


LoginApi apiInstance = new LoginApi();
Integer cid = 56; // Integer | 
Integer sid = 56; // Integer | 
Integer pid = 56; // Integer | 
Integer cn = 56; // Integer | 
Integer sft = 56; // Integer | 
String LASTNAME = "LASTNAME_example"; // String | 
String cacheVer = "cacheVer_example"; // String | 
try {
    PrepareLoginForm result = apiInstance.prepareloginform(cid, sid, pid, cn, sft, LASTNAME, cacheVer);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling LoginApi#prepareloginform");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **Integer**|  | [optional]
 **sid** | **Integer**|  | [optional]
 **pid** | **Integer**|  | [optional]
 **cn** | **Integer**|  | [optional]
 **sft** | **Integer**|  | [optional]
 **LASTNAME** | **String**|  | [optional]
 **cacheVer** | **String**|  | [optional]

### Return type

[**PrepareLoginForm**](PrepareLoginForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

