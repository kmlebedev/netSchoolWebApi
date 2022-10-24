# NetSchool.MysettingsApi

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
```javascript
import {NetSchool} from 'net_school';
let defaultClient = NetSchool.ApiClient.instance;


let apiInstance = new NetSchool.MysettingsApi();
let at = "at_example"; // String | an authorization header

apiInstance.mysettings(at, (error, data, response) => {
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
```javascript
import {NetSchool} from 'net_school';
let defaultClient = NetSchool.ApiClient.instance;


let apiInstance = new NetSchool.MysettingsApi();
let at = "at_example"; // String | an authorization header

apiInstance.yearlist(at, (error, data, response) => {
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
 **at** | **String**| an authorization header | 

### Return type

[**MySettingsYears**](MySettingsYears.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

