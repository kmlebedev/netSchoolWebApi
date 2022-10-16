# AssignmentApi

All URIs are relative to *https://virtserver.swaggerhub.com/LEBEDEVKM/NetSchool/5.10.63221*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignmentTypes**](AssignmentApi.md#assignmentTypes) | **GET** /grade/assignment/types | 

<a name="assignmentTypes"></a>
# **assignmentTypes**
> AssignmentTypes assignmentTypes()



returns all assignment types

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = AssignmentApi()
try {
    val result : AssignmentTypes = apiInstance.assignmentTypes()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AssignmentApi#assignmentTypes")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AssignmentApi#assignmentTypes")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AssignmentTypes**](AssignmentTypes.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

