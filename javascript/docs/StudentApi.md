# NetSchool.StudentApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**studentDiary**](StudentApi.md#studentDiary) | **GET** /student/diary | 
[**studentDiaryInit**](StudentApi.md#studentDiaryInit) | **GET** /student/diary/init | 

<a name="studentDiary"></a>
# **studentDiary**
> Diary studentDiary(studentId, opts)



returns all assignments

### Example
```javascript
import {NetSchool} from 'net_school';
let defaultClient = NetSchool.ApiClient.instance;


let apiInstance = new NetSchool.StudentApi();
let studentId = 56; // Number | 
let opts = { 
  'weekStart': new Date("2013-10-20"), // Date | 
  'weekEnd': new Date("2013-10-20"), // Date | 
  'withLaAssigns': true, // Boolean | 
  'withPastMandatory': true, // Boolean | 
  'yearId': 56 // Number | 
};
apiInstance.studentDiary(studentId, opts, (error, data, response) => {
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
 **studentId** | **Number**|  | 
 **weekStart** | **Date**|  | [optional] 
 **weekEnd** | **Date**|  | [optional] 
 **withLaAssigns** | **Boolean**|  | [optional] 
 **withPastMandatory** | **Boolean**|  | [optional] 
 **yearId** | **Number**|  | [optional] 

### Return type

[**Diary**](Diary.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="studentDiaryInit"></a>
# **studentDiaryInit**
> StudentDiaryInit studentDiaryInit()



returns strudent diary init data

### Example
```javascript
import {NetSchool} from 'net_school';
let defaultClient = NetSchool.ApiClient.instance;


let apiInstance = new NetSchool.StudentApi();
apiInstance.studentDiaryInit((error, data, response) => {
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

[**StudentDiaryInit**](StudentDiaryInit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

