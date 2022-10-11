# NetSchool.DiaryApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/4.30.43656*

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

