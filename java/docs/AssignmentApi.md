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
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.AssignmentApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();


AssignmentApi apiInstance = new AssignmentApi();
try {
    AssignmentTypes result = apiInstance.assignmentTypes();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling AssignmentApi#assignmentTypes");
    e.printStackTrace();
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

