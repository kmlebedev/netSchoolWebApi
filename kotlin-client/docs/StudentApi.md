# StudentApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/4.30.43656*

Method | HTTP request | Description
------------- | ------------- | -------------
[**studentDiary**](StudentApi.md#studentDiary) | **GET** /student/diary | 
[**studentDiaryInit**](StudentApi.md#studentDiaryInit) | **GET** /student/diary/init | 

<a name="studentDiary"></a>
# **studentDiary**
> Diary studentDiary(studentId, weekStart, weekEnd, withLaAssigns, withPastMandatory, yearId)



returns all assignments

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = StudentApi()
val studentId : kotlin.Int = 56 // kotlin.Int | 
val weekStart : java.time.LocalDate = 2013-10-20 // java.time.LocalDate | 
val weekEnd : java.time.LocalDate = 2013-10-20 // java.time.LocalDate | 
val withLaAssigns : kotlin.Boolean = true // kotlin.Boolean | 
val withPastMandatory : kotlin.Boolean = true // kotlin.Boolean | 
val yearId : kotlin.Int = 56 // kotlin.Int | 
try {
    val result : Diary = apiInstance.studentDiary(studentId, weekStart, weekEnd, withLaAssigns, withPastMandatory, yearId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling StudentApi#studentDiary")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling StudentApi#studentDiary")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studentId** | **kotlin.Int**|  |
 **weekStart** | **java.time.LocalDate**|  | [optional]
 **weekEnd** | **java.time.LocalDate**|  | [optional]
 **withLaAssigns** | **kotlin.Boolean**|  | [optional]
 **withPastMandatory** | **kotlin.Boolean**|  | [optional]
 **yearId** | **kotlin.Int**|  | [optional]

### Return type

[**Diary**](Diary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="studentDiaryInit"></a>
# **studentDiaryInit**
> StudentDiaryInit studentDiaryInit()



returns strudent diary init data

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = StudentApi()
try {
    val result : StudentDiaryInit = apiInstance.studentDiaryInit()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling StudentApi#studentDiaryInit")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling StudentApi#studentDiaryInit")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StudentDiaryInit**](StudentDiaryInit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

