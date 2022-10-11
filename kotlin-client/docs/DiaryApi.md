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
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = DiaryApi()
val assignId : kotlin.Int = 56 // kotlin.Int | 
val studentId : kotlin.Int = 56 // kotlin.Int | 
try {
    val result : DiaryAssignDetails = apiInstance.diaryAssignnDetails(assignId, studentId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DiaryApi#diaryAssignnDetails")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DiaryApi#diaryAssignnDetails")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignId** | **kotlin.Int**|  |
 **studentId** | **kotlin.Int**|  |

### Return type

[**DiaryAssignDetails**](DiaryAssignDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

