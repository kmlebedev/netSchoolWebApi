# NetSchool.LoginApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getauthdata**](LoginApi.md#getauthdata) | **POST** /auth/getdata | 
[**login**](LoginApi.md#login) | **POST** /login | 
[**logindata**](LoginApi.md#logindata) | **GET** /logindata | 
[**prepareemloginform**](LoginApi.md#prepareemloginform) | **GET** /prepareemloginform | 
[**prepareloginform**](LoginApi.md#prepareloginform) | **GET** /prepareloginform | 

<a name="getauthdata"></a>
# **getauthdata**
> GetAuthData getauthdata()



returns all login data

### Example
```javascript
import {NetSchool} from 'net_school';

let apiInstance = new NetSchool.LoginApi();
apiInstance.getauthdata((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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
```javascript
import {NetSchool} from 'net_school';

let apiInstance = new NetSchool.LoginApi();
let loginType = 56; // Number | 
let cid = 56; // Number | 
let sid = 56; // Number | 
let pid = 56; // Number | 
let cn = 56; // Number | 
let sft = 56; // Number | 
let scid = 56; // Number | 
let UN = "UN_example"; // String | 
let PW = "PW_example"; // String | 
let lt = 56; // Number | 
let pw2 = "pw2_example"; // String | 
let ver = 56; // Number | 

apiInstance.login(loginType, cid, sid, pid, cn, sft, scid, UN, PW, lt, pw2, ver, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loginType** | **Number**|  | 
 **cid** | **Number**|  | 
 **sid** | **Number**|  | 
 **pid** | **Number**|  | 
 **cn** | **Number**|  | 
 **sft** | **Number**|  | 
 **scid** | **Number**|  | 
 **UN** | **String**|  | 
 **PW** | **String**|  | 
 **lt** | **Number**|  | 
 **pw2** | **String**|  | 
 **ver** | **Number**|  | 

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
```javascript
import {NetSchool} from 'net_school';

let apiInstance = new NetSchool.LoginApi();
apiInstance.logindata((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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
> PrepareEmLoginForm prepareemloginform(opts)



returns all prepareemloginform

### Example
```javascript
import {NetSchool} from 'net_school';

let apiInstance = new NetSchool.LoginApi();
let opts = { 
  'cacheVer': "cacheVer_example" // String | 
};
apiInstance.prepareemloginform(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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
> PrepareLoginForm prepareloginform(opts)



returns all prepareloginform

### Example
```javascript
import {NetSchool} from 'net_school';

let apiInstance = new NetSchool.LoginApi();
let opts = { 
  'cacheVer': "cacheVer_example" // String | 
};
apiInstance.prepareloginform(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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

