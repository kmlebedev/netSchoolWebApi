# NetSchool.DiaryApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diaryAssignnDetails**](DiaryApi.md#diaryAssignnDetails) | **GET** /student/diary/assigns/{assignId} | 

<a name="diaryAssignnDetails"></a>
# **diaryAssignnDetails**
> DiaryAssignDetails diaryAssignnDetails(assignId, studentId)



returns assign information

### Example
```javascript
import {NetSchool} from 'net_school';
let defaultClient = NetSchool.ApiClient.instance;


let apiInstance = new NetSchool.DiaryApi();
let assignId = 56; // Number | 
let studentId = 56; // Number | 

apiInstance.diaryAssignnDetails(assignId, studentId, (error, data, response) => {
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
 **assignId** | **Number**|  | 
 **studentId** | **Number**|  | 

### Return type

[**DiaryAssignDetails**](DiaryAssignDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

