# StudentApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**studentDiary**](StudentApi.md#studentDiary) | **GET** /student/diary | 
[**studentDiaryInit**](StudentApi.md#studentDiaryInit) | **GET** /student/diary/init | 

<a name="studentDiary"></a>
# **studentDiary**
> Diary studentDiary(studentId, weekStart, weekEnd, withLaAssigns, withPastMandatory, yearId)



returns all assignments

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.StudentApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();


StudentApi apiInstance = new StudentApi();
Integer studentId = 56; // Integer | 
LocalDate weekStart = new LocalDate(); // LocalDate | 
LocalDate weekEnd = new LocalDate(); // LocalDate | 
Boolean withLaAssigns = true; // Boolean | 
Boolean withPastMandatory = true; // Boolean | 
Integer yearId = 56; // Integer | 
try {
    Diary result = apiInstance.studentDiary(studentId, weekStart, weekEnd, withLaAssigns, withPastMandatory, yearId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling StudentApi#studentDiary");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studentId** | **Integer**|  |
 **weekStart** | **LocalDate**|  | [optional]
 **weekEnd** | **LocalDate**|  | [optional]
 **withLaAssigns** | **Boolean**|  | [optional]
 **withPastMandatory** | **Boolean**|  | [optional]
 **yearId** | **Integer**|  | [optional]

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
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.StudentApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();


StudentApi apiInstance = new StudentApi();
try {
    StudentDiaryInit result = apiInstance.studentDiaryInit();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling StudentApi#studentDiaryInit");
    e.printStackTrace();
}
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

