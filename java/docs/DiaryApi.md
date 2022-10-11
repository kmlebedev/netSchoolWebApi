# DiaryApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/4.30.43656*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diaryAssignnDetails**](DiaryApi.md#diaryAssignnDetails) | **GET** /student/diary/assigns/{assignId} | 

<a name="diaryAssignnDetails"></a>
# **diaryAssignnDetails**
> DiaryAssignDetails diaryAssignnDetails(assignId, studentId)



returns assign information

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.DiaryApi;


DiaryApi apiInstance = new DiaryApi();
Integer assignId = 56; // Integer | 
Integer studentId = 56; // Integer | 
try {
    DiaryAssignDetails result = apiInstance.diaryAssignnDetails(assignId, studentId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling DiaryApi#diaryAssignnDetails");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignId** | **Integer**|  |
 **studentId** | **Integer**|  |

### Return type

[**DiaryAssignDetails**](DiaryAssignDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

