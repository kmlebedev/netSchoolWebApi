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
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = LoginApi()
try {
    val result : GetAuthData = apiInstance.getauthdata()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling LoginApi#getauthdata")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling LoginApi#getauthdata")
    e.printStackTrace()
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
> Login login(loginType, cid, sid, pid, cn, sft, scid, uN, pW, lt, pw2, ver)



returns all login data

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = LoginApi()
val loginType : kotlin.Int = 56 // kotlin.Int | 
val cid : kotlin.Int = 56 // kotlin.Int | 
val sid : kotlin.Int = 56 // kotlin.Int | 
val pid : kotlin.Int = 56 // kotlin.Int | 
val cn : kotlin.Int = 56 // kotlin.Int | 
val sft : kotlin.Int = 56 // kotlin.Int | 
val scid : kotlin.Int = 56 // kotlin.Int | 
val uN : kotlin.String = uN_example // kotlin.String | 
val pW : kotlin.String = pW_example // kotlin.String | 
val lt : kotlin.Int = 56 // kotlin.Int | 
val pw2 : kotlin.String = pw2_example // kotlin.String | 
val ver : kotlin.Int = 56 // kotlin.Int | 
try {
    val result : Login = apiInstance.login(loginType, cid, sid, pid, cn, sft, scid, uN, pW, lt, pw2, ver)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling LoginApi#login")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling LoginApi#login")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loginType** | **kotlin.Int**|  |
 **cid** | **kotlin.Int**|  |
 **sid** | **kotlin.Int**|  |
 **pid** | **kotlin.Int**|  |
 **cn** | **kotlin.Int**|  |
 **sft** | **kotlin.Int**|  |
 **scid** | **kotlin.Int**|  |
 **uN** | **kotlin.String**|  |
 **pW** | **kotlin.String**|  |
 **lt** | **kotlin.Int**|  |
 **pw2** | **kotlin.String**|  |
 **ver** | **kotlin.Int**|  |

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

<a name="loginform"></a>
# **loginform**
> LoginForm loginform(cid, sid, pid, cn, sft, lASTNAME, cacheVer)



returns all loginform

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = LoginApi()
val cid : kotlin.Int = 56 // kotlin.Int | 
val sid : kotlin.Int = 56 // kotlin.Int | 
val pid : kotlin.Int = 56 // kotlin.Int | 
val cn : kotlin.Int = 56 // kotlin.Int | 
val sft : kotlin.Int = 56 // kotlin.Int | 
val lASTNAME : kotlin.String = lASTNAME_example // kotlin.String | 
val cacheVer : kotlin.String = cacheVer_example // kotlin.String | 
try {
    val result : LoginForm = apiInstance.loginform(cid, sid, pid, cn, sft, lASTNAME, cacheVer)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling LoginApi#loginform")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling LoginApi#loginform")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **kotlin.Int**|  | [optional]
 **sid** | **kotlin.Int**|  | [optional]
 **pid** | **kotlin.Int**|  | [optional]
 **cn** | **kotlin.Int**|  | [optional]
 **sft** | **kotlin.Int**|  | [optional]
 **lASTNAME** | **kotlin.String**|  | [optional]
 **cacheVer** | **kotlin.String**|  | [optional]

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
> PrepareLoginForm prepareloginform(cid, sid, pid, cn, sft, lASTNAME, cacheVer)



returns all prepareloginform

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = LoginApi()
val cid : kotlin.Int = 56 // kotlin.Int | 
val sid : kotlin.Int = 56 // kotlin.Int | 
val pid : kotlin.Int = 56 // kotlin.Int | 
val cn : kotlin.Int = 56 // kotlin.Int | 
val sft : kotlin.Int = 56 // kotlin.Int | 
val lASTNAME : kotlin.String = lASTNAME_example // kotlin.String | 
val cacheVer : kotlin.String = cacheVer_example // kotlin.String | 
try {
    val result : PrepareLoginForm = apiInstance.prepareloginform(cid, sid, pid, cn, sft, lASTNAME, cacheVer)
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
 **cid** | **kotlin.Int**|  | [optional]
 **sid** | **kotlin.Int**|  | [optional]
 **pid** | **kotlin.Int**|  | [optional]
 **cn** | **kotlin.Int**|  | [optional]
 **sft** | **kotlin.Int**|  | [optional]
 **lASTNAME** | **kotlin.String**|  | [optional]
 **cacheVer** | **kotlin.String**|  | [optional]

### Return type

[**PrepareLoginForm**](PrepareLoginForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

